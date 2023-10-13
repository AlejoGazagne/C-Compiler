// Generated from /home/alejo/Escritorio/Compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link compiladoresParser}.
 */
public interface compiladoresListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#log}.
	 * @param ctx the parse tree
	 */
	void enterLog(compiladoresParser.LogContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#log}.
	 * @param ctx the parse tree
	 */
	void exitLog(compiladoresParser.LogContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#tdato}.
	 * @param ctx the parse tree
	 */
	void enterTdato(compiladoresParser.TdatoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#tdato}.
	 * @param ctx the parse tree
	 */
	void exitTdato(compiladoresParser.TdatoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(compiladoresParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void enterInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void exitInstrucciones(compiladoresParser.InstruccionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitInstruccion(compiladoresParser.InstruccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(compiladoresParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#definicion}.
	 * @param ctx the parse tree
	 */
	void enterDefinicion(compiladoresParser.DefinicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#definicion}.
	 * @param ctx the parse tree
	 */
	void exitDefinicion(compiladoresParser.DefinicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(compiladoresParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(compiladoresParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#retornar}.
	 * @param ctx the parse tree
	 */
	void enterRetornar(compiladoresParser.RetornarContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#retornar}.
	 * @param ctx the parse tree
	 */
	void exitRetornar(compiladoresParser.RetornarContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#lista_var}.
	 * @param ctx the parse tree
	 */
	void enterLista_var(compiladoresParser.Lista_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#lista_var}.
	 * @param ctx the parse tree
	 */
	void exitLista_var(compiladoresParser.Lista_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stmt(compiladoresParser.While_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#while_stmt}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stmt(compiladoresParser.While_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void enterIf_stmt(compiladoresParser.If_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#if_stmt}.
	 * @param ctx the parse tree
	 */
	void exitIf_stmt(compiladoresParser.If_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#else_stmt}.
	 * @param ctx the parse tree
	 */
	void enterElse_stmt(compiladoresParser.Else_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#else_stmt}.
	 * @param ctx the parse tree
	 */
	void exitElse_stmt(compiladoresParser.Else_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void enterFor_stmt(compiladoresParser.For_stmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#for_stmt}.
	 * @param ctx the parse tree
	 */
	void exitFor_stmt(compiladoresParser.For_stmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#opar}.
	 * @param ctx the parse tree
	 */
	void enterOpar(compiladoresParser.OparContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#opar}.
	 * @param ctx the parse tree
	 */
	void exitOpar(compiladoresParser.OparContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(compiladoresParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(compiladoresParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(compiladoresParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(compiladoresParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(compiladoresParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(compiladoresParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(compiladoresParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(compiladoresParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(compiladoresParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(compiladoresParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#oplo}.
	 * @param ctx the parse tree
	 */
	void enterOplo(compiladoresParser.OploContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#oplo}.
	 * @param ctx the parse tree
	 */
	void exitOplo(compiladoresParser.OploContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#expresionLo}.
	 * @param ctx the parse tree
	 */
	void enterExpresionLo(compiladoresParser.ExpresionLoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#expresionLo}.
	 * @param ctx the parse tree
	 */
	void exitExpresionLo(compiladoresParser.ExpresionLoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#expLo}.
	 * @param ctx the parse tree
	 */
	void enterExpLo(compiladoresParser.ExpLoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#expLo}.
	 * @param ctx the parse tree
	 */
	void exitExpLo(compiladoresParser.ExpLoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#terminoLo}.
	 * @param ctx the parse tree
	 */
	void enterTerminoLo(compiladoresParser.TerminoLoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#terminoLo}.
	 * @param ctx the parse tree
	 */
	void exitTerminoLo(compiladoresParser.TerminoLoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#termLo}.
	 * @param ctx the parse tree
	 */
	void enterTermLo(compiladoresParser.TermLoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#termLo}.
	 * @param ctx the parse tree
	 */
	void exitTermLo(compiladoresParser.TermLoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#factorLo}.
	 * @param ctx the parse tree
	 */
	void enterFactorLo(compiladoresParser.FactorLoContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#factorLo}.
	 * @param ctx the parse tree
	 */
	void exitFactorLo(compiladoresParser.FactorLoContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#comp}.
	 * @param ctx the parse tree
	 */
	void enterComp(compiladoresParser.CompContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#comp}.
	 * @param ctx the parse tree
	 */
	void exitComp(compiladoresParser.CompContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#callFuncion}.
	 * @param ctx the parse tree
	 */
	void enterCallFuncion(compiladoresParser.CallFuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#callFuncion}.
	 * @param ctx the parse tree
	 */
	void exitCallFuncion(compiladoresParser.CallFuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link compiladoresParser#defFuncion}.
	 * @param ctx the parse tree
	 */
	void enterDefFuncion(compiladoresParser.DefFuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link compiladoresParser#defFuncion}.
	 * @param ctx the parse tree
	 */
	void exitDefFuncion(compiladoresParser.DefFuncionContext ctx);
}