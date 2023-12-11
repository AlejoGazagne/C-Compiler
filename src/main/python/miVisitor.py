from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser
from Util.Utilidades import *
from Util.Temporales import *
from Util.Etiquetas import *

class miVisitor(compiladoresVisitor):

    _temp = []
    _eti = []
    getTemp = Temporales()
    getEti = Etiquetas()

    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Visitando arbol")
        self.f = open("./output/CodigoIntermedio.txt", "w")
        self.visitChildren(ctx)
        print("Saliendo del arbol")
        self.f.close()

    def visitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        # Si es una declaracion sin definicion
        if ctx.getChild(2).getText() != "":
            self.visitDefinicion(ctx.getChild(2))
            self.f.write(ctx.getChild(1).getText() + " = " + self._temp.pop() + "\n")

    def visitDefinicion(self, ctx: compiladoresParser.DefinicionContext):
        return self.visitOpal(ctx.getChild(1))

    def visitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        self.visitOpal(ctx.getChild(2))
        self.f.write(ctx.getChild(0).getText() + " = " + self._temp.pop() + "\n")

    def visitOpal(self, ctx: compiladoresParser.OpalContext):
        return self.visitExpresionl(ctx.getChild(0))
    
    def visitExpresionl(self, ctx: compiladoresParser.ExpresionContext):
        self.visitTerminol(ctx.getChild(0))

        if ctx.getChild(1).getChildCount() != 0:
            temporal = self.getTemp.next_temporal()
            self.visitExpl(ctx.getChild(1))
            tmp2 = self._temp.pop()
            tmp1 = self._temp.pop()
            self.f.write(temporal + " = " + tmp1 + " " + ctx.getChild(1).getChild(0).getText() + " " + tmp2 + "\n")
            self._temp.append(temporal)
    
    def visitExpl(self, ctx: compiladoresParser.ExplContext):
        self.visitTerminol(ctx.getChild(1))
    
    def visitTerminol(self, ctx: compiladoresParser.TerminolContext):
        # Es un if
        if ctx.getChildCount() == 4:
            temporal = self.getTemp.next_temporal()
            self.visitExpresion(ctx.getChild(0))
            self.visitExpresion(ctx.getChild(2))
            tmp2 = self._temp.pop()
            tmp1 = self._temp.pop()
            self.f.write(temporal + " = " + tmp1 + " " + ctx.getChild(1).getChild(0).getText() + " " + tmp2 + "\n")
            self._temp.append(temporal)

        if ctx.getChildCount() == 2:
            self.visitExpresion(ctx.getChild(0))

            if ctx.getChild(1).getText() != "":
                temporal = self.getTemp.next_temporal()
                self.visitTerml(ctx.getChild(1))
                tmp2 = self._temp.pop()
                tmp1 = self._temp.pop()
                self.f.write(temporal + " = " + tmp1 + " " + ctx.getChild(1).getChild(0).getText() + " " + tmp2 + "\n")
                self._temp.append(temporal)

    def visitExpresion(self, ctx: compiladoresParser.ExpresionContext):
        #self.visitTermino(ctx.getChild(0))
        temporal = self.getTemp.next_temporal()
        self._temp.append(temporal)

        if ctx.getChild(1).getText() != '':
            #temporal = self.getTemp.next_temporal()
            self.f.write(temporal + " = " + self.visitTermino(ctx.getChild(0)) + " " + ctx.getChild(1).getChild(0).getText() + " " + self.visitExp(ctx.getChild(1)) + "\n")
            #self._temp.append(temporal)
        else: 
            self.f.write(temporal + " = " + self.visitTermino(ctx.getChild(0)) + "\n")

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
            self._temp.pop()
            self.visitExpresionl(ctx.getChild(0).getChild(1))

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
    
    def visitTerml(self, ctx: compiladoresParser.TermlContext):
        self.visitExpresionl(ctx.getChild(1))

        if ctx.getChild(2).getText() != "":
            temporal = self.getTemp.next_temporal()
            self.f.write(temporal + " = " + self._temp.pop() + " " + ctx.getChild(2).getChild(0).getText() + " " + self.visitTerml(ctx.getChild(2)) + "\n")
            self._temp.append(temporal)

    def visitIf_stmt(self, ctx: compiladoresParser.If_stmtContext):
        if ctx.getChild(5) != None:
            self.visitOpal(ctx.getChild(2))
            et1 = self.getEti.next_etiqueta()
            et2 = self.getEti.next_etiqueta()
            self.f.write("ifn " + self._temp.pop() + " jmp " + et1 + "\n")
            self.visitInstruccion(ctx.getChild(4))
            self.f.write("jmp " + et2 + "\n")
            self.f.write("label " + et1 + "\n")
            self.visitElse_stmt(ctx.getChild(5))
            self.f.write("label " + et2 + "\n")
        else:
            self.visitOpal(ctx.getChild(2))
            et1 = self.getEti.next_etiqueta()
            self.f.write("ifn " + self._temp.pop() + " jmp " + et1 + "\n")
            self.visitInstruccion(ctx.getChild(4))
            self.f.write("label " + et1 + "\n")
    
    def visitElse_stmt(self, ctx: compiladoresParser.Else_stmtContext):
        self.visitBloque(ctx.getChild(1))

    def visitWhile_stmt(self, ctx: compiladoresParser.While_stmtContext):
        et1 = self.getEti.next_etiqueta()
        self.f.write("label " + et1 + "\n")
        self.visitOpal(ctx.getChild(2))
        et2 = self.getEti.next_etiqueta()
        self.f.write("ifn " + self._temp.pop() + " jmp " + et2 + "\n")
        self.visitInstruccion(ctx.getChild(4))
        self.f.write("jmp " + et1 + "\n")
        self.f.write("label " + et2 + "\n")
    
    def visitFor_stmt(self, ctx: compiladoresParser.For_stmtContext):
        self.visitAsignacion(ctx.getChild(2))
        et1 = self.getEti.next_etiqueta()
        self.f.write("label " + et1 + "\n")
        self.visitOpal(ctx.getChild(4))
        et2 = self.getEti.next_etiqueta()
        self.f.write("ifn " + self._temp.pop() + " jmp " + et2 + "\n")
        self.visitInstruccion(ctx.getChild(8))
        self.visitAsignacion(ctx.getChild(6))
        self.f.write("jmp " + et1 + "\n")
        self.f.write("label " + et2 + "\n")
        
if __name__ == "__main__":
    pass
#ARITMETICAS Y LOGICAS ANDANDO?