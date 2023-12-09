from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

class miVisitor(compiladoresVisitor):
    
    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Visitando arbol ")
        return self.visitChildren(ctx)
    
     # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("ENTRO AL VISIT DECLARACION")
        print("       ->Visitando declaracion " + str(ctx.getText()))
        tDato = ctx.getChild(3).getText()
        print(tDato)
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by compiladoresParser#definicion.
    def visitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        print("ENTRO EN LA DEFINICION")
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by compiladoresParser#lista_var.
    def visitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by compiladoresParser#expresion.
    def visitExpresion(self, ctx:compiladoresParser.ExpresionContext):
        return self.visitChildren(ctx)