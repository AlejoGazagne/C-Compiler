from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

class miVisitor(compiladoresVisitor):
    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Visitando arbol ")
        return None
    
     # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("       ->Visitando declaracion " + str(ctx.getText()))
        return self.visitLista_var(ctx)
    
    # Visit a parse tree produced by compiladoresParser#lista_var.
    def visitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        print("   -> visitando delcaracion " + ctx.getText())
        return self.visitChildren(ctx)