# Generated from /home/alejo/Escritorio/Compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#log.
    def visitLog(self, ctx:compiladoresParser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tdato.
    def visitTdato(self, ctx:compiladoresParser.TdatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#definicion.
    def visitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#retornar.
    def visitRetornar(self, ctx:compiladoresParser.RetornarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_var.
    def visitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#while_stmt.
    def visitWhile_stmt(self, ctx:compiladoresParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#if_stmt.
    def visitIf_stmt(self, ctx:compiladoresParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#else_stmt.
    def visitElse_stmt(self, ctx:compiladoresParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#for_stmt.
    def visitFor_stmt(self, ctx:compiladoresParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opal.
    def visitOpal(self, ctx:compiladoresParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expresionl.
    def visitExpresionl(self, ctx:compiladoresParser.ExpresionlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expl.
    def visitExpl(self, ctx:compiladoresParser.ExplContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#terminol.
    def visitTerminol(self, ctx:compiladoresParser.TerminolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#terml.
    def visitTerml(self, ctx:compiladoresParser.TermlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expresion.
    def visitExpresion(self, ctx:compiladoresParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#exp.
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#termino.
    def visitTermino(self, ctx:compiladoresParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prototipeFuncion.
    def visitPrototipeFuncion(self, ctx:compiladoresParser.PrototipeFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#callFuncion.
    def visitCallFuncion(self, ctx:compiladoresParser.CallFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#defFuncion.
    def visitDefFuncion(self, ctx:compiladoresParser.DefFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#listaParEnv.
    def visitListaParEnv(self, ctx:compiladoresParser.ListaParEnvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parEnv.
    def visitParEnv(self, ctx:compiladoresParser.ParEnvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#listaParRec.
    def visitListaParRec(self, ctx:compiladoresParser.ListaParRecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parRec.
    def visitParRec(self, ctx:compiladoresParser.ParRecContext):
        return self.visitChildren(ctx)



del compiladoresParser