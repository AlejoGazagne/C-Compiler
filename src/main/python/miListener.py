from antlr4 import *
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TS import TS
from ID import *
from Utilidades import *

class miListener(compiladoresListener):
    tablaDeSimbolos = TS()
    
    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comenzando la compilacion")
        print("-> Creo contexto general")
        self.tablaDeSimbolos.agregarContexto()
    
    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("-> Salgo del contexto general")
        print("Fin de la compilacion")
        
    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        #print("\tBloque con " + str(ctx.getChildCount()) + " hijos")
        print("Inicio bloque")
        self.tablaDeSimbolos.agregarContexto()

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        #print("\tBloque con " + str(ctx.getChildCount()) + " hijos")
        #print("\t--> " + ctx.getText())
        print("Fin del bloque")
    
    # Exit a parse tree produced by compiladoresParser#declaracion.
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
                print("No se agrego el identificador")
            else:
                self.tablaDeSimbolos.agregar(id)
                print("Se agrego un nuevo identificador")
                print(id.nombre)
        
    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        variables = ctx.getText()
        variables = variables.split(",")
        idVariables = [var.split("=")[0].strip() for var in variables]
        
        for var in idVariables:
            varCtx = self.tablaDeSimbolos.buscar(var)
            if varCtx:
                print("Ya esta declarado el identificador, y se realiza la asignacion")
                for id in varCtx.simbolos:
                    if id == var:
                        varCtx.simbolos[id].inicializado = True
            else: 
                print("No se encuentra delcarado el identificador, no se realiza la asignacion")
                
    # Exit a parse tree produced by compiladoresParser#prototipeFuncion.
    def exitPrototipeFuncion(self, ctx:compiladoresParser.PrototipeFuncionContext):
        tDato = str(ctx.getChild(0).getText())
        nombre = ctx.getText()[len(tDato):].split("(")[0].strip()
        argumentos = ctx.getText()[len(tDato):]
        listArgs = Utilidades.getArgsFuncion(argumentos)
                        
        id = Funcion(nombre, tDato, listArgs, False, False)
        
        if self.tablaDeSimbolos.buscarLocal(id.nombre):
            print("No se agrego un nuevo identificador")
        else:
            self.tablaDeSimbolos.agregar(id)
            print("Se agrego un nuevo identificador")
        
    
    # Exit a parse tree produced by compiladoresParser#callFuncion.
    def exitCallFuncion(self, ctx:compiladoresParser.CallFuncionContext):
        tDato = str(ctx.getChild(0).getText())
        nombreFuncion = ctx.getText()[len(tDato):].split("(")[0].strip()
        argumentos = ctx.getText()
        listArg = Utilidades.getArgsFuncion(argumentos)
        
        id = Funcion(nombreFuncion, tDato, listArg)
        
        ctxFuncion = self.tablaDeSimbolos.buscar(nombreFuncion)
        
        

        
        
        
    
