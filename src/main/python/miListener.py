from antlr4 import *
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TS import TS
from ID import *
from Util.Utilidades import *
import re

class miListener(compiladoresListener):
    contextos = open("./output/TablaDeSimbolos.txt", "w")
    errores = open("./output/Errores.txt", "w")
    tablaDeSimbolos = TS()
    listaArgumentos = []
    error = False
    
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comenzando la compilacion")
        print("-> Creo contexto general")
    
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("-> Salgo del contexto general")
        print("Fin de la compilacion")
        ctx = self.tablaDeSimbolos.getContextos()
        # Contexto global
        self.contextos.write('\tContexto global\n')

        for var in ctx[-1].simbolos.values():
            if var.__class__ == Variable:
                self.contextos.write('\t\t' + var.tDato + '\t' + var.nombre + '\t')
                if var.inicializado:
                    self.contextos.write('inicializada\t')
                else:
                    self.contextos.write('no inicializada\t')
                if var._accedido:
                    self.contextos.write('accedida\n')
                else:
                    self.contextos.write('no accedida\n')
            else:
                self.contextos.write('\t\t' + var.tDato + '\t' + var.nombre + '\t')

                if var.inicializado:
                    self.contextos.write('inicializada\t')
                else:
                    self.contextos.write('no inicializada\t')
                if var._accedido:
                    self.contextos.write('accedida\n')
                else:
                    self.contextos.write('no accedida\n')

                self.contextos.write('\t\tArgumentos de la funcion: \n')

                for arg in var.args:
                    self.contextos.write('\t\t\t' + arg.tDato + '\t' + arg.nombre + '\t')
                    if arg.inicializado:
                        self.contextos.write('inicializada\t')
                    else:
                        self.contextos.write('no inicializada\t')
                    if arg._accedido:
                        self.contextos.write('accedida\n')
                    else:
                        self.contextos.write('no accedida\n')
        
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        #print("\tBloque con " + str(ctx.getChildCount()) + " hijos")
        print("Inicio bloque")
        self.tablaDeSimbolos.agregarContexto()
        if ctx.parentCtx.getChild(0).getText() != "int":
            if ctx.parentCtx.getChild(0).getText() != "double":
                return
            
        for var in self.listaArgumentos:
            self.tablaDeSimbolos.agregar(var)
        self.listaArgumentos.clear()

    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        print("Fin del bloque")

        ctxs = self.tablaDeSimbolos.getContextos()

        if ctx.parentCtx != None:
            # print(str(ctx[-1]))
            self.contextos.write('\tContexto de la funcion: ' + str(ctx.parentCtx.getChild(1)) + '\n')

            for var in ctxs[-1].simbolos.values():

                self.contextos.write('\t\t' + var.tDato + '\t' + var.nombre + '\t')
                if var.inicializado:
                    self.contextos.write('inicializada\t')
                else:
                    self.contextos.write('no inicializada\t')
                if var._accedido:
                    self.contextos.write('accedida\n')
                else:
                    self.contextos.write('no accedida\n')
        
        self.tablaDeSimbolos.borrarContexto()
    
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        tDato = str(ctx.getChild(0).getText())
        variables = ctx.getText()[len(tDato):]
        variables = variables.split(",")
        idVariables = [var.split("=")[0].strip() for var in variables]
        
        for var in range(len(variables)):
            # if idVariables[var].replace('.', '', 1).isdigit():
            #     print("No se puede declarar el valor: " + idVariables[var])
            #     self.error = True

            id = Variable(idVariables[var], tDato)
            if variables[var].find("="):
                id.inicializado = True
            if self.tablaDeSimbolos.buscarLocal(id.nombre):
                print("No se declaro el identificador: " + id.nombre)
                pass
            else:
                self.tablaDeSimbolos.agregar(id)
                print("Se declaro un nuevo identificador: " + id.nombre)
                #print(id.nombre)
        
    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        #las asignaciones son individuales por que se rompen en las funciones
        variable = ctx.getText()
        idVariable = variable.split("=")[0].strip()

        idFuncion = variable.split("=")[1].split("(")[0].strip()
        ctxFun = self.tablaDeSimbolos.buscarGlobal(idFuncion)

        if ctxFun:
            varCtx = self.tablaDeSimbolos.buscar(idVariable)
            if varCtx:
                print("Se encuentra la variable '" + idVariable + "' para la asignacion")
                for id in varCtx.simbolos:
                    if id == idVariable:
                        tDatoVar = varCtx.simbolos[id].tDato

                for id in ctxFun.simbolos:
                    if id == idFuncion:
                        tDatoFun = ctxFun.simbolos[id].tDato
                        
                if tDatoFun == tDatoVar:
                    print("El tipo de dato de la variable coincide con el tipo de dato de retorno de la funcion")
                else:
                    self.errores.write("Los tipos de datos de la variable y retorno de la funcion no coinciden")
                    self.error = True
            else:
                self.error.write("No se encuentra la variable " + idVariable + " para la asignacion")
                self.error = True

        else:
            varCtx = self.tablaDeSimbolos.buscar(idVariable)
            if varCtx:
                print("Ya esta declarado el identificador '" + idVariable + "', y se realiza la asignacion")
                for id in varCtx.simbolos:
                    if id == idVariable:
                        varCtx.simbolos[id].inicializado = True
                        
            else: 
                self.error.write("No se encuentra delcarado el identificador " + idVariable + ", no se realiza la asignacion")
                self.error = True
                #cortar ejecucion
                
    def exitPrototipeFuncion(self, ctx:compiladoresParser.PrototipeFuncionContext):
        tDato = str(ctx.getChild(0).getText())
        nombre = ctx.getText()[len(tDato):].split("(")[0].strip()
        listArgs = Utilidades.getArgsFuncion(ctx.getText()[len(tDato):])
        
        id = Funcion(nombre, tDato, listArgs)
        
        if self.tablaDeSimbolos.buscarLocal(id.nombre):
            self.error.write("No se agrego un nuevo identificador PARA EL PROTOTIPO: " + id.nombre)
            self.error = True
            pass
        else:
            id.inicializado = True
            self.tablaDeSimbolos.agregar(id)
            print("Se agrego un nuevo identificador PARA EL PROTOTIPO: " + id.nombre)
        
    def exitCallFuncion(self, ctx:compiladoresParser.CallFuncionContext):
        #print("Call Funcion")
        nombreFuncion = ctx.getChild(0).getText()
        ls = re.split(r'[+/*,-]', ctx.getText().split("(")[1].split(")")[0])

        ctxFuncion = self.tablaDeSimbolos.buscar(nombreFuncion)

        if ctxFuncion == None:
            self.error.write("No encuentro el prototipo de la funcion")
            self.error = True
            return 
            
        print("Encontre el prototipo de la funcion: " + nombreFuncion)

        for id in ls:
            if id.replace('.', '', 1).isdigit():
                print("Se envia una numero")
            else:
                ctxPar = self.tablaDeSimbolos.buscar(id)
                if ctxPar == None:
                    self.error.write("No se encontro el parametro para la funcion: " + id)
                    self.error = True
                else:
                    print("Se encontro el parametro para la funcion: " + id)
                
    def exitDefFuncion(self, ctx:compiladoresParser.DefFuncionContext):
        #print("DEFINICION FUNCION")
        tDato = str(ctx.getChild(0).getText())
        nombreFun = ctx.getText()[len(tDato):].split("(")[0].strip()
        if nombreFun == "main":
            return
        
        listArgs = Utilidades.getArgsFuncion(ctx.getText()[len(tDato):])
        for i in listArgs:
            self.listaArgumentos.append(i)
        self.listaArgumentos = listArgs

        ctxFun = self.tablaDeSimbolos.buscarGlobal(nombreFun)

        if ctxFun:
            print("Se encontro el nombre de la funcion: " + nombreFun)

            for clave, valor in ctxFun.simbolos.items():
                if clave == nombreFun:
                    idFun = valor
            if idFun.tDato != tDato:
                self.error.write("El tipo de dato de retorno no coincide con el prototipo")
                self.error = True
                return
            
            print("El tipo de dato de retorno coincide con el prototipo")
            for i in range(len(listArgs)):
                if listArgs[i].tDato != ctxFun.simbolos[nombreFun].args[i].tDato:
                    self.error.write("Los tipos de datos no coinciden con el prototipo")
                    self.error = True
                    break
                print("Los tipos de datos coinciden con el prototipo")
        else: 
            print("No se encontro el nombre pero se agrega: " + nombreFun)
            #no esta contenido
            id = Funcion(nombreFun, tDato, listArgs)
            if self.tablaDeSimbolos.buscarLocal(id.nombre):
                print("No se agrego un nuevo identificador PARA EL PROTOTIPO: " + nombreFun)
                pass
            else:
                self.tablaDeSimbolos.agregar(id)
                print("Se agrego un nuevo identificador PARA EL PROTOTIPO: " + id.nombre)
        
        #agrego los argumentos de la fun al contexto
        for i in listArgs:
            self.tablaDeSimbolos.agregar(i)

    def exitFactor(self, ctx: compiladoresParser.FactorContext):
        if ctx.getChild(0).getChildCount() != 0:
            return

        if ctx.getChildCount() == 3:
            return
        
        nombre = ctx.getText()
        if not nombre.replace('.', '', 1).isdigit():
            ctxVar = self.tablaDeSimbolos.buscar(nombre)
            if ctxVar == None:
                self.errores.write("La variable '" + nombre + "' no se encuentra definida")
                self.error = True
            else:
                for var in ctxVar.simbolos.items():
                    if ctx.getChildCount() == 2:
                        if var[1].nombre == ctx.getChild(1).getText():
                            var[1].setAccedido
                            self.tablaDeSimbolos.actualizar(var[1])
                    else:
                        if var[1].nombre == ctx.getChild(0).getText():
                            var[1]._accedido = True
                            self.tablaDeSimbolos.actualizar(var[1])
        
    def exitArgRec(self, ctx: compiladoresParser.ArgRecContext):
        if ctx.getChildCount() != 0:
            nombre = ctx.getChild(1).getText()
            tDato = ctx.getChild(0).getText()
            id = Variable(nombre, tDato)
            id.inicializado = True
            self.listaArgumentos.append(id)
    
    def exitListaArgRec(self, ctx: compiladoresParser.ListaArgRecContext):
        if ctx.getChildCount() != 0:
            nombre = ctx.getChild(2).getText()
            tDato = ctx.getChild(1).getText()
            id = Variable(nombre, tDato)
            id.inicializado = True
            self.listaArgumentos.append(id)