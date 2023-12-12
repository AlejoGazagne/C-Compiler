from antlr4 import *
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TS import TS
from ID import *
from Util.Utilidades import *

class miListener(compiladoresListener):
    tablaDeSimbolos = TS()
    
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comenzando la compilacion")
        print("-> Creo contexto general")
    
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("-> Salgo del contexto general")
        print("Fin de la compilacion")
        
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        #print("\tBloque con " + str(ctx.getChildCount()) + " hijos")
        print("Inicio bloque")
        self.tablaDeSimbolos.agregarContexto()

    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        #print("\tBloque con " + str(ctx.getChildCount()) + " hijos")
        #print("\t--> " + ctx.getText())
        print("Fin del bloque")
        pass
    
    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        tDato = str(ctx.getChild(0).getText())
        variables = ctx.getText()[len(tDato):]
        variables = variables.split(",")
        idVariables = [var.split("=")[0].strip() for var in variables]
        
        for var in range(len(variables)):
            id = Variable(idVariables[var], tDato)
            if variables[var].find("="):
                id.inicializado = True
            if self.tablaDeSimbolos.buscarLocal(id.nombre):
                print("No se declaro el identificador")
                pass
            else:
                self.tablaDeSimbolos.agregar(id)
                print("Se declaro un nuevo identificador")
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
                print("Se encuentra la variable para la asignacion")
                for id in varCtx.simbolos:
                    if id == idVariable:
                        tDatoVar = varCtx.simbolos[id].tDato

                for id in ctxFun.simbolos:
                    if id == idFuncion:
                        tDatoFun = ctxFun.simbolos[id].tDato
                        
                if tDatoFun == tDatoVar:
                    print("El tipo de dato de la variable coincide con el tipo de dato de la funcion")
                else:
                    print("Los tipos de datos de la variable y la funcion no coinciden")
            else:
                print("No se encuentra la variable para la asignacion")

        else:
            varCtx = self.tablaDeSimbolos.buscar(idVariable)
            if varCtx:
                print("Ya esta declarado el identificador, y se realiza la asignacion")
                for id in varCtx.simbolos:
                    if id == idVariable:
                        varCtx.simbolos[id].inicializado = True
                        
            else: 
                print("No se encuentra delcarado el identificador, no se realiza la asignacion")
                #cortar ejecucion
        
                
    def exitPrototipeFuncion(self, ctx:compiladoresParser.PrototipeFuncionContext):
        tDato = str(ctx.getChild(0).getText())
        nombre = ctx.getText()[len(tDato):].split("(")[0].strip()
        argumentos = ctx.getText()[len(tDato):]
        listArgs = Utilidades.getArgsFuncion(ctx.getText()[len(tDato):])

        for arg in argumentos:
            if arg[:3] == "int":
                nombreVar = arg[3:]
                tDatoVar = "int"
                listArgs.append(Variable(nombreVar, tDatoVar))
            elif arg[:6] == "double":
                nombreVar = arg[6:]
                tDatoVar = "double"
                listArgs.append(Variable(nombreVar, tDatoVar))
            elif arg == "":
                print("lista de argumentos vacia")
        
        id = Funcion(nombre, tDato, listArgs)
        
        if self.tablaDeSimbolos.buscarLocal(id.nombre):
            print("No se agrego un nuevo identificador PARA EL PROTOTIPO")
            pass
        else:
            self.tablaDeSimbolos.agregar(id)
            print("Se agrego un nuevo identificador PARA EL PROTOTIPO")
        
    def exitCallFuncion(self, ctx:compiladoresParser.CallFuncionContext):
        #print("Call Funcion")
        nombreFuncion = ctx.getChild(0).getText()
        listaPar = ctx.getText().split("(")[1].split(")")[0].split(",")
        
        ctxFuncion = self.tablaDeSimbolos.buscar(nombreFuncion)

        if ctxFuncion == None:
            print("No encuentro el prototipo de la funcion")
            
            return 
            
        print("Encontre el prototipo de la funcion")
        for clave, valor in ctxFuncion.simbolos.items():
            if clave == nombreFuncion:
                idFuncion = valor
        
        contador = 1
        for id in listaPar:
            ctxPar = self.tablaDeSimbolos.buscar(id)
            if ctxPar == None:
                print("No se encontro el parametro para la funcion")
                return 
            print("Se encontro el parametro para la funcion")
            for clave, valor in ctxPar.simbolos.items():
                if clave == id:
                    idPar = valor
            if idPar.tDato != idFuncion.tDato:
                print("El tipo de dato no coincide con el prototipo de la funcion")
                return 
            contador += 1
                
    def exitDefFuncion(self, ctx:compiladoresParser.DefFuncionContext):
        #print("DEFINICION FUNCION")
        tDato = str(ctx.getChild(0).getText())
        nombreFun = ctx.getText()[len(tDato):].split("(")[0].strip()
        if nombreFun == "main":
            return
        listArgs = Utilidades.getArgsFuncion(ctx.getText()[len(tDato):])

        ctxFun = self.tablaDeSimbolos.buscarGlobal(nombreFun)

        if ctxFun:
            print("Se encontro el nombre de la funcion")

            for clave, valor in ctxFun.simbolos.items():
                if clave == nombreFun:
                    idFun = valor
            if idFun.tDato != tDato:
                print("El tipo de dato de retorno no coincide con el prototipo")
                return
            
            print("El tipo de dato de retorno coincide con el prototipo")
            for i in range(len(listArgs)):
                if listArgs[i].tDato != ctxFun.simbolos[nombreFun].args[i].tDato:
                    print("Los tipos de datos no coinciden con el prototipo")
                    break
                print("Los tipos de datos coinciden con el prototipo")
        else: 
            print("No se encontro el nombre pero se agrega")
            #no esta contenido
            id = Funcion(nombreFun, tDato, listArgs)
            if self.tablaDeSimbolos.buscarLocal(id.nombre):
                print("No se agrego un nuevo identificador PARA EL PROTOTIPO")
                pass
            else:
                self.tablaDeSimbolos.agregar(id)
                print("Se agrego un nuevo identificador PARA EL PROTOTIPO")
        
        #agrego los argumentos de la fun al contexto
        for i in listArgs:
            self.tablaDeSimbolos.agregar(i)