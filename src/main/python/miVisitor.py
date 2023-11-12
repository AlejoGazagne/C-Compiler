from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser
from Util.Utilidades import *
from Util.Temporales import *

class miVisitor(compiladoresVisitor):

    _temp = []
    getTemp = Temporales()

    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Visitando arbol")
        self.f = open("./output/CodigoIntermedio.txt", "w")
        self.visitChildren(ctx)
        print("Saliendo del arbol")
        self.f.close()

    def visitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        self.visitDefinicion(ctx.getChild(2))
        self.f.write(ctx.getChild(1).getText() + " = " + self._temp.pop())

    # Visit a parse tree produced by compiladoresParser#definicion.
    def visitDefinicion(self, ctx: compiladoresParser.DefinicionContext):
        return self.visitOpal(ctx.getChild(1))

    def visitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        self.visitOpal(ctx.getChild(2))
        self.f.write(ctx.getChild(0).getText() + " = " + self._temp.pop())

    def visitOpal(self, ctx: compiladoresParser.OpalContext):
        return self.visitExpresionl(ctx.getChild(0))
    
    def visitExpresionl(self, ctx: compiladoresParser.ExpresionContext):
        return self.visitTerminol(ctx.getChild(0))
    
    def visitExpl(self, ctx: compiladoresParser.ExplContext):
        return self.visitChildren(ctx)
    
    def visitTerminol(self, ctx: compiladoresParser.TerminolContext):
        self.visitExpresion(ctx.getChild(0))

    def visitExpresion(self, ctx: compiladoresParser.ExpresionContext):
        temporal = self.getTemp.next_temporal()
        self._temp.append(temporal)

        if ctx.getChild(1).getText() != '':
            self.f.write(temporal + " = " + self.visitTermino(ctx.getChild(0)) + " " + ctx.getChild(1).getChild(0).getText() + " " + self.visitExp(ctx.getChild(1)) + "\n")
        else: 
            self.f.write(temporal + " = " + self.visitTermino(ctx.getChild(0)) + "\n")
        return

    def visitExp(self, ctx: compiladoresParser.ExpContext):
        if ctx.getChild(2).getChildCount() == 0:
            return self.visitTermino(ctx.getChild(1))

        temporal = self.getTemp.next_temporal()
        self._temp.append(temporal)
        self.f.write(temporal + " = " + self.visitTermino(ctx.getChild(1)) + " " + ctx.getChild(2).getChild(0).getText() + " " + self.visitExp(ctx.getChild(2)) + "\n")

        return self._temp.pop()

    def visitTermino(self, ctx: compiladoresParser.TerminoContext):
        temporal = self.getTemp.next_temporal()
        self._temp.append(temporal)

        if ctx.getChild(0).getChildCount() == 3:
            self.visitExpresionl(ctx.getChild(0).getChild(1))
            self.f.write(temporal + " = " + self._temp.pop() + "\n")

        if ctx.getChild(0).getChildCount() == 2:
            self.f.write(temporal + " = " + ctx.getChild(0).getChild(0).getText() + ctx.getChild(0).getChild(1).getText() + "\n")

        if ctx.getChild(0).getChildCount() == 1:
            self.f.write(temporal + " = " + ctx.getChild(0).getChild(0).getText() + "\n")

        return self.visitTerm(ctx.getChild(1))

    def visitTerm(self, ctx: compiladoresParser.TermContext):
        if ctx.getChildCount() == 0:
            return self._temp.pop()

        temporal = self.getTemp.next_temporal()

        self.f.write(temporal + " = " + self._temp.pop() + " " + ctx.getChild(0).getText() + " " + self.visitFactor(ctx.getChild(1)) + "\n")

        self._temp.append(temporal)
        return self.visitTerm(ctx.getChild(2))

    def visitFactor(self, ctx: compiladoresParser.FactorContext):
        if ctx.getChildCount() == 3:
            self.visitExpresionl(ctx.getChild(1))
        if ctx.getChildCount() == 2:
            return ctx.getChild(0).getText() + ctx.getChild(1).getText()
        else:
            return ctx.getChild(0).getText()
        
if __name__ == "__main__":
    pass