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
    esFuncion = False;

    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Visitando arbol")
        self.f = open("./output/CodigoIntermedio.txt", "w")
        self.visitChildren(ctx)
        print("Saliendo del arbol")
        self.f.write("label end")
        self.f.close()

    def visitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        # Si es una declaracion sin definicion
        if ctx.getChild(2).getText() != "":
            if ctx.getChild(2).getChild(1).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChildCount() == 4:
                self.visitCallFuncion(ctx.getChild(2).getChild(1).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0))
                self.f.write("pop " + ctx.getChild(1).getText() + "\n")
                return 
            
            self.visitDefinicion(ctx.getChild(2))
            self.f.write(ctx.getChild(1).getText() + " = " + self._temp.pop() + "\n")
        
        if ctx.getChild(3).getChildCount() != 0:
            self.visitLista_var(ctx.getChild(3))

    def visitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        if ctx.getChild(2).getChildCount() != 0:
            self.visitDefinicion(ctx.getChild(2))
            self.f.write(ctx.getChild(1).getText() + ' = ' + self._temp.pop() + '\n')
        
        if ctx.getChild(3).getChildCount() != 0:
            self.visitLista_var(ctx.getChild(3))

    def visitRetornar(self, ctx: compiladoresParser.RetornarContext):
        if self.esFuncion == False:
            self.f.write("jmp " + "end" + "\n")
            return
        if self.esFuncion == True:
            self.visitOpal(ctx.getChild(1))
            aux = self._temp.pop()
            self.f.write("push " + aux + "\n")

    def visitDefinicion(self, ctx: compiladoresParser.DefinicionContext):
        return self.visitOpal(ctx.getChild(1))

    def visitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        self.visitOpal(ctx.getChild(2))
        #verificar si es fun
        if ctx.getChild(2).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChildCount() == 4:
            self.visitCallFuncion(ctx.getChild(2).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0))
            self.f.write("pop " + ctx.getChild(0).getText() + "\n")
            return 
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
        self.visitTermino(ctx.getChild(0))
        
        if ctx.getChild(1).getText() != "":
            aux1 = self._temp.pop()
            self.visitExp(ctx.getChild(1))
            aux2 = self._temp.pop()
            temporal = self.getTemp.next_temporal()
            self.f.write(temporal + " = " + aux1 + " " + ctx.getChild(1).getChild(0).getText() + " " + aux2 + "\n")
            self._temp.append(temporal)

    def visitExp(self, ctx: compiladoresParser.ExpContext):
        self.visitTermino(ctx.getChild(1))
        
        if ctx.getChild(2).getText() != "":
            aux1 = self._temp.pop()
            self.visitExp(ctx.getChild(2))
            temporal = self.getTemp.next_temporal()
            aux2 = self._temp.pop()
            self.f.write(temporal + " = " + aux1 + " " + ctx.getChild(2).getChild(0).getText() + " " + aux2 + "\n")
            self._temp.append(temporal)

    def visitTermino(self, ctx: compiladoresParser.TerminoContext):
        self.visitFactor(ctx.getChild(0))

        #Verifico term (si hay alguna mul/div)
        if ctx.getChild(1).getText() != "":
            aux1 = self._temp.pop()
            self.visitTerm(ctx.getChild(1))
            aux2 = self._temp.pop()
            temporal = self.getTemp.next_temporal()
            self.f.write(temporal + " = " + aux1 + " " + ctx.getChild(1).getChild(0).getText() + " " + aux2 + "\n")
            self._temp.append(temporal)

    def visitTerm(self, ctx: compiladoresParser.TermContext):
        self.visitFactor(ctx.getChild(1))

        if ctx.getChild(2).getText() != "":
            self.visitTerm(ctx.getChild(2))

    def visitFactor(self, ctx: compiladoresParser.FactorContext):

        #verifico si es una llamada a una funcion
        if ctx.getChild(0).getChildCount() == 4:
            return

        if ctx.getChildCount() == 3:
            self.visitExpresionl(ctx.getChild(1))
            return
        if ctx.getChildCount() == 2:
            temporal = self.getTemp.next_temporal()
            self.f.write(temporal + " = " +  + ctx.getChild(0).getText() + " " + ctx.getChild(1).getText() + "\n")
            self._temp.append(temporal)
            return 
        if ctx.getChildCount() == 1:
            temporal = self.getTemp.next_temporal()
            self.f.write(temporal + " = " + ctx.getText() + "\n")
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

    def visitCallFuncion(self, ctx:compiladoresParser.CallFuncionContext):
        self.visitArgEnv(ctx.getChild(2))
        etiqueta = self.getEti.etiqueta_funcion(ctx.getChild(0).getText())
        self.f.write("push " + etiqueta[1] + "\n")
        self.f.write("jmp " + etiqueta[0] + "\n")
        self.f.write("label " + etiqueta[1] + "\n")
    
    def visitArgEnv(self, ctx: compiladoresParser.ArgEnvContext):
        argumentos = ctx.getText().split(",")

        for arg in argumentos:
            self.f.write("push " + arg + "\n")

    def visitDefFuncion(self, ctx:compiladoresParser.DefFuncionContext):
        if ctx.getChild(1).getText() == "main":
            self.visitBloque(ctx.getChild(5))
            return
        
        nombreFun = ctx.getChild(1).getText()
        et = self.getEti.funciones[nombreFun]
        
        self.f.write("label " + et[0] + "\n")
        self.esFuncion = True 
        list = Utilidades.getArgsFuncion(ctx.getText())
        for var in list:
            self.f.write("pop " + var.nombre + "\n")
        self.f.write("pop " + et[1] + "\n")
        self.visitBloque(ctx.getChild(5))
        self.f.write("jmp " + et[1] + "\n")
            
if __name__ == "__main__":
    pass
