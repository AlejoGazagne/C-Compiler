// Generated from /home/alejo/Escritorio/Compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class compiladoresParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		EQ=1, PA=2, PC=3, LLA=4, LLC=5, PYC=6, COMA=7, MAS=8, MENOS=9, MOD=10, 
		MUL=11, DIV=12, LT=13, GT=14, LE=15, GE=16, EQQ=17, NEQ=18, AND=19, ORR=20, 
		NUMERO=21, INT=22, DOUBLE=23, WHILE=24, IF=25, ELSE=26, FOR=27, RETURN=28, 
		ID=29, WS=30, OTRO=31;
	public static final int
		RULE_log = 0, RULE_tdato = 1, RULE_programa = 2, RULE_instrucciones = 3, 
		RULE_instruccion = 4, RULE_declaracion = 5, RULE_definicion = 6, RULE_asignacion = 7, 
		RULE_bloque = 8, RULE_retornar = 9, RULE_lista_var = 10, RULE_while_stmt = 11, 
		RULE_if_stmt = 12, RULE_else_stmt = 13, RULE_for_stmt = 14, RULE_opar = 15, 
		RULE_expresion = 16, RULE_exp = 17, RULE_termino = 18, RULE_term = 19, 
		RULE_factor = 20, RULE_oplo = 21, RULE_expresionLo = 22, RULE_expLo = 23, 
		RULE_terminoLo = 24, RULE_termLo = 25, RULE_factorLo = 26, RULE_comp = 27, 
		RULE_prototipeFuncion = 28, RULE_callFuncion = 29, RULE_defFuncion = 30, 
		RULE_listaParEnv = 31, RULE_parEnv = 32, RULE_listaParRec = 33, RULE_parRec = 34;
	private static String[] makeRuleNames() {
		return new String[] {
			"log", "tdato", "programa", "instrucciones", "instruccion", "declaracion", 
			"definicion", "asignacion", "bloque", "retornar", "lista_var", "while_stmt", 
			"if_stmt", "else_stmt", "for_stmt", "opar", "expresion", "exp", "termino", 
			"term", "factor", "oplo", "expresionLo", "expLo", "terminoLo", "termLo", 
			"factorLo", "comp", "prototipeFuncion", "callFuncion", "defFuncion", 
			"listaParEnv", "parEnv", "listaParRec", "parRec"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'('", "')'", "'{'", "'}'", "';'", "','", "'+'", "'-'", 
			"'%'", "'*'", "'/'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", 
			"'||'", null, "'int'", "'double'", "'while'", "'if'", "'else'", "'for'", 
			"'return'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "EQ", "PA", "PC", "LLA", "LLC", "PYC", "COMA", "MAS", "MENOS", 
			"MOD", "MUL", "DIV", "LT", "GT", "LE", "GE", "EQQ", "NEQ", "AND", "ORR", 
			"NUMERO", "INT", "DOUBLE", "WHILE", "IF", "ELSE", "FOR", "RETURN", "ID", 
			"WS", "OTRO"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "compiladores.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public compiladoresParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogContext extends ParserRuleContext {
		public TerminalNode LT() { return getToken(compiladoresParser.LT, 0); }
		public TerminalNode GT() { return getToken(compiladoresParser.GT, 0); }
		public TerminalNode LE() { return getToken(compiladoresParser.LE, 0); }
		public TerminalNode GE() { return getToken(compiladoresParser.GE, 0); }
		public TerminalNode EQQ() { return getToken(compiladoresParser.EQQ, 0); }
		public TerminalNode NEQ() { return getToken(compiladoresParser.NEQ, 0); }
		public LogContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_log; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLog(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLog(this);
		}
	}

	public final LogContext log() throws RecognitionException {
		LogContext _localctx = new LogContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_log);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 516096L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TdatoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(compiladoresParser.INT, 0); }
		public TerminalNode DOUBLE() { return getToken(compiladoresParser.DOUBLE, 0); }
		public TdatoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tdato; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTdato(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTdato(this);
		}
	}

	public final TdatoContext tdato() throws RecognitionException {
		TdatoContext _localctx = new TdatoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_tdato);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==DOUBLE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode EOF() { return getToken(compiladoresParser.EOF, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			instrucciones();
			setState(75);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionesContext extends ParserRuleContext {
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public InstruccionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instrucciones; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterInstrucciones(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitInstrucciones(this);
		}
	}

	public final InstruccionesContext instrucciones() throws RecognitionException {
		InstruccionesContext _localctx = new InstruccionesContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_instrucciones);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LLA:
			case INT:
			case DOUBLE:
			case WHILE:
			case IF:
			case FOR:
			case RETURN:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				instruccion();
				setState(78);
				instrucciones();
				}
				break;
			case EOF:
			case LLC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionContext extends ParserRuleContext {
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladoresParser.PYC, 0); }
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public RetornarContext retornar() {
			return getRuleContext(RetornarContext.class,0);
		}
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public DefFuncionContext defFuncion() {
			return getRuleContext(DefFuncionContext.class,0);
		}
		public CallFuncionContext callFuncion() {
			return getRuleContext(CallFuncionContext.class,0);
		}
		public PrototipeFuncionContext prototipeFuncion() {
			return getRuleContext(PrototipeFuncionContext.class,0);
		}
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public InstruccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterInstruccion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitInstruccion(this);
		}
	}

	public final InstruccionContext instruccion() throws RecognitionException {
		InstruccionContext _localctx = new InstruccionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_instruccion);
		try {
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				declaracion();
				setState(84);
				match(PYC);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(86);
				asignacion();
				setState(87);
				match(PYC);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(89);
				retornar();
				setState(90);
				match(PYC);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(92);
				if_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(93);
				for_stmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(94);
				while_stmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(95);
				defFuncion();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(96);
				callFuncion();
				setState(97);
				match(PYC);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(99);
				prototipeFuncion();
				setState(100);
				match(PYC);
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(102);
				bloque();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public DefinicionContext definicion() {
			return getRuleContext(DefinicionContext.class,0);
		}
		public Lista_varContext lista_var() {
			return getRuleContext(Lista_varContext.class,0);
		}
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterDeclaracion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitDeclaracion(this);
		}
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_declaracion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			tdato();
			setState(106);
			match(ID);
			setState(107);
			definicion();
			setState(108);
			lista_var();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefinicionContext extends ParserRuleContext {
		public TerminalNode EQ() { return getToken(compiladoresParser.EQ, 0); }
		public OparContext opar() {
			return getRuleContext(OparContext.class,0);
		}
		public DefinicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definicion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterDefinicion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitDefinicion(this);
		}
	}

	public final DefinicionContext definicion() throws RecognitionException {
		DefinicionContext _localctx = new DefinicionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_definicion);
		try {
			setState(113);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EQ:
				enterOuterAlt(_localctx, 1);
				{
				setState(110);
				match(EQ);
				setState(111);
				opar();
				}
				break;
			case PYC:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode EQ() { return getToken(compiladoresParser.EQ, 0); }
		public OploContext oplo() {
			return getRuleContext(OploContext.class,0);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(ID);
			setState(116);
			match(EQ);
			setState(117);
			oplo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode LLA() { return getToken(compiladoresParser.LLA, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLC() { return getToken(compiladoresParser.LLC, 0); }
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterBloque(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitBloque(this);
		}
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_bloque);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(LLA);
			setState(120);
			instrucciones();
			setState(121);
			match(LLC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RetornarContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(compiladoresParser.RETURN, 0); }
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode NUMERO() { return getToken(compiladoresParser.NUMERO, 0); }
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public RetornarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_retornar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterRetornar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitRetornar(this);
		}
	}

	public final RetornarContext retornar() throws RecognitionException {
		RetornarContext _localctx = new RetornarContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_retornar);
		try {
			setState(131);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(123);
				match(RETURN);
				setState(124);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(125);
				match(RETURN);
				setState(126);
				match(NUMERO);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(127);
				match(RETURN);
				setState(128);
				asignacion();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(129);
				match(RETURN);
				setState(130);
				declaracion();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_varContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladoresParser.COMA, 0); }
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public DefinicionContext definicion() {
			return getRuleContext(DefinicionContext.class,0);
		}
		public Lista_varContext lista_var() {
			return getRuleContext(Lista_varContext.class,0);
		}
		public Lista_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLista_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLista_var(this);
		}
	}

	public final Lista_varContext lista_var() throws RecognitionException {
		Lista_varContext _localctx = new Lista_varContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_lista_var);
		try {
			setState(139);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				match(COMA);
				setState(134);
				match(ID);
				setState(135);
				definicion();
				setState(136);
				lista_var();
				}
				break;
			case PYC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class While_stmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(compiladoresParser.WHILE, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public OploContext oplo() {
			return getRuleContext(OploContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterWhile_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitWhile_stmt(this);
		}
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			match(WHILE);
			setState(142);
			match(PA);
			setState(143);
			oplo();
			setState(144);
			match(PC);
			setState(145);
			instruccion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_stmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(compiladoresParser.IF, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public OploContext oplo() {
			return getRuleContext(OploContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public Else_stmtContext else_stmt() {
			return getRuleContext(Else_stmtContext.class,0);
		}
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIf_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIf_stmt(this);
		}
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_if_stmt);
		try {
			setState(160);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(147);
				match(IF);
				setState(148);
				match(PA);
				setState(149);
				oplo();
				setState(150);
				match(PC);
				setState(151);
				instruccion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(153);
				match(IF);
				setState(154);
				match(PA);
				setState(155);
				oplo();
				setState(156);
				match(PC);
				setState(157);
				instruccion();
				setState(158);
				else_stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Else_stmtContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(compiladoresParser.ELSE, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public Else_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterElse_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitElse_stmt(this);
		}
	}

	public final Else_stmtContext else_stmt() throws RecognitionException {
		Else_stmtContext _localctx = new Else_stmtContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_else_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			match(ELSE);
			setState(163);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_stmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(compiladoresParser.FOR, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public List<AsignacionContext> asignacion() {
			return getRuleContexts(AsignacionContext.class);
		}
		public AsignacionContext asignacion(int i) {
			return getRuleContext(AsignacionContext.class,i);
		}
		public List<TerminalNode> PYC() { return getTokens(compiladoresParser.PYC); }
		public TerminalNode PYC(int i) {
			return getToken(compiladoresParser.PYC, i);
		}
		public OploContext oplo() {
			return getRuleContext(OploContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterFor_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitFor_stmt(this);
		}
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			match(FOR);
			setState(166);
			match(PA);
			setState(167);
			asignacion();
			setState(168);
			match(PYC);
			setState(169);
			oplo();
			setState(170);
			match(PYC);
			setState(171);
			asignacion();
			setState(172);
			match(PC);
			setState(173);
			instruccion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OparContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public OparContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterOpar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitOpar(this);
		}
	}

	public final OparContext opar() throws RecognitionException {
		OparContext _localctx = new OparContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_opar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			expresion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterExpresion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitExpresion(this);
		}
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_expresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			termino();
			setState(178);
			exp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public TerminalNode MAS() { return getToken(compiladoresParser.MAS, 0); }
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode MENOS() { return getToken(compiladoresParser.MENOS, 0); }
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_exp);
		try {
			setState(189);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(180);
				match(MAS);
				setState(181);
				termino();
				setState(182);
				exp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(184);
				match(MENOS);
				setState(185);
				termino();
				setState(186);
				exp();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTermino(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTermino(this);
		}
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_termino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			factor();
			setState(192);
			term();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public TerminalNode MUL() { return getToken(compiladoresParser.MUL, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminalNode DIV() { return getToken(compiladoresParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(compiladoresParser.MOD, 0); }
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_term);
		try {
			setState(207);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(194);
				match(MUL);
				setState(195);
				factor();
				setState(196);
				term();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(198);
				match(DIV);
				setState(199);
				factor();
				setState(200);
				term();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(202);
				match(MOD);
				setState(203);
				factor();
				setState(204);
				term();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode NUMERO() { return getToken(compiladoresParser.NUMERO, 0); }
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode MENOS() { return getToken(compiladoresParser.MENOS, 0); }
		public CallFuncionContext callFuncion() {
			return getRuleContext(CallFuncionContext.class,0);
		}
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_factor);
		try {
			setState(220);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(209);
				match(NUMERO);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(210);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(211);
				match(MENOS);
				setState(212);
				match(NUMERO);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(213);
				match(MENOS);
				setState(214);
				match(ID);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(215);
				callFuncion();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(216);
				match(PA);
				setState(217);
				expresion();
				setState(218);
				match(PC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OploContext extends ParserRuleContext {
		public ExpresionLoContext expresionLo() {
			return getRuleContext(ExpresionLoContext.class,0);
		}
		public OploContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_oplo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterOplo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitOplo(this);
		}
	}

	public final OploContext oplo() throws RecognitionException {
		OploContext _localctx = new OploContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_oplo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			expresionLo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionLoContext extends ParserRuleContext {
		public TerminoLoContext terminoLo() {
			return getRuleContext(TerminoLoContext.class,0);
		}
		public ExpLoContext expLo() {
			return getRuleContext(ExpLoContext.class,0);
		}
		public ExpresionLoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresionLo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterExpresionLo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitExpresionLo(this);
		}
	}

	public final ExpresionLoContext expresionLo() throws RecognitionException {
		ExpresionLoContext _localctx = new ExpresionLoContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_expresionLo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			terminoLo();
			setState(225);
			expLo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpLoContext extends ParserRuleContext {
		public TerminalNode ORR() { return getToken(compiladoresParser.ORR, 0); }
		public TerminoLoContext terminoLo() {
			return getRuleContext(TerminoLoContext.class,0);
		}
		public ExpLoContext expLo() {
			return getRuleContext(ExpLoContext.class,0);
		}
		public ExpLoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expLo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterExpLo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitExpLo(this);
		}
	}

	public final ExpLoContext expLo() throws RecognitionException {
		ExpLoContext _localctx = new ExpLoContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_expLo);
		try {
			setState(232);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ORR:
				enterOuterAlt(_localctx, 1);
				{
				setState(227);
				match(ORR);
				setState(228);
				terminoLo();
				setState(229);
				expLo();
				}
				break;
			case PC:
			case PYC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoLoContext extends ParserRuleContext {
		public FactorLoContext factorLo() {
			return getRuleContext(FactorLoContext.class,0);
		}
		public TermLoContext termLo() {
			return getRuleContext(TermLoContext.class,0);
		}
		public TerminoLoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terminoLo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTerminoLo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTerminoLo(this);
		}
	}

	public final TerminoLoContext terminoLo() throws RecognitionException {
		TerminoLoContext _localctx = new TerminoLoContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_terminoLo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			factorLo();
			setState(235);
			termLo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermLoContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(compiladoresParser.AND, 0); }
		public FactorLoContext factorLo() {
			return getRuleContext(FactorLoContext.class,0);
		}
		public TermLoContext termLo() {
			return getRuleContext(TermLoContext.class,0);
		}
		public TermLoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termLo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTermLo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTermLo(this);
		}
	}

	public final TermLoContext termLo() throws RecognitionException {
		TermLoContext _localctx = new TermLoContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_termLo);
		try {
			setState(242);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AND:
				enterOuterAlt(_localctx, 1);
				{
				setState(237);
				match(AND);
				setState(238);
				factorLo();
				setState(239);
				termLo();
				}
				break;
			case PC:
			case PYC:
			case ORR:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorLoContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public CompContext comp() {
			return getRuleContext(CompContext.class,0);
		}
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ExpresionLoContext expresionLo() {
			return getRuleContext(ExpresionLoContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public FactorLoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factorLo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterFactorLo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitFactorLo(this);
		}
	}

	public final FactorLoContext factorLo() throws RecognitionException {
		FactorLoContext _localctx = new FactorLoContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_factorLo);
		try {
			setState(250);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(244);
				factor();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(245);
				comp(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(246);
				match(PA);
				setState(247);
				expresionLo();
				setState(248);
				match(PC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompContext extends ParserRuleContext {
		public List<OparContext> opar() {
			return getRuleContexts(OparContext.class);
		}
		public OparContext opar(int i) {
			return getRuleContext(OparContext.class,i);
		}
		public LogContext log() {
			return getRuleContext(LogContext.class,0);
		}
		public List<CompContext> comp() {
			return getRuleContexts(CompContext.class);
		}
		public CompContext comp(int i) {
			return getRuleContext(CompContext.class,i);
		}
		public CompContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterComp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitComp(this);
		}
	}

	public final CompContext comp() throws RecognitionException {
		return comp(0);
	}

	private CompContext comp(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CompContext _localctx = new CompContext(_ctx, _parentState);
		CompContext _prevctx = _localctx;
		int _startState = 54;
		enterRecursionRule(_localctx, 54, RULE_comp, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(253);
			opar();
			setState(254);
			log();
			setState(255);
			opar();
			}
			_ctx.stop = _input.LT(-1);
			setState(263);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CompContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_comp);
					setState(257);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(258);
					log();
					setState(259);
					comp(2);
					}
					} 
				}
				setState(265);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrototipeFuncionContext extends ParserRuleContext {
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ParRecContext parRec() {
			return getRuleContext(ParRecContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public PrototipeFuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prototipeFuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterPrototipeFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitPrototipeFuncion(this);
		}
	}

	public final PrototipeFuncionContext prototipeFuncion() throws RecognitionException {
		PrototipeFuncionContext _localctx = new PrototipeFuncionContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_prototipeFuncion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(266);
			tdato();
			setState(267);
			match(ID);
			setState(268);
			match(PA);
			setState(269);
			parRec();
			setState(270);
			match(PC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CallFuncionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ParEnvContext parEnv() {
			return getRuleContext(ParEnvContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public CallFuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callFuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterCallFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitCallFuncion(this);
		}
	}

	public final CallFuncionContext callFuncion() throws RecognitionException {
		CallFuncionContext _localctx = new CallFuncionContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_callFuncion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(ID);
			setState(273);
			match(PA);
			setState(274);
			parEnv();
			setState(275);
			match(PC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefFuncionContext extends ParserRuleContext {
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ParRecContext parRec() {
			return getRuleContext(ParRecContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public DefFuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defFuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterDefFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitDefFuncion(this);
		}
	}

	public final DefFuncionContext defFuncion() throws RecognitionException {
		DefFuncionContext _localctx = new DefFuncionContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_defFuncion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			tdato();
			setState(278);
			match(ID);
			setState(279);
			match(PA);
			setState(280);
			parRec();
			setState(281);
			match(PC);
			setState(282);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListaParEnvContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladoresParser.COMA, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public ListaParEnvContext listaParEnv() {
			return getRuleContext(ListaParEnvContext.class,0);
		}
		public ListaParEnvContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaParEnv; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterListaParEnv(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitListaParEnv(this);
		}
	}

	public final ListaParEnvContext listaParEnv() throws RecognitionException {
		ListaParEnvContext _localctx = new ListaParEnvContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_listaParEnv);
		try {
			setState(289);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(284);
				match(COMA);
				setState(285);
				expresion();
				setState(286);
				listaParEnv();
				}
				break;
			case PC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParEnvContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public ListaParEnvContext listaParEnv() {
			return getRuleContext(ListaParEnvContext.class,0);
		}
		public ParEnvContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parEnv; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterParEnv(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitParEnv(this);
		}
	}

	public final ParEnvContext parEnv() throws RecognitionException {
		ParEnvContext _localctx = new ParEnvContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_parEnv);
		try {
			setState(295);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PA:
			case MENOS:
			case NUMERO:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(291);
				expresion();
				setState(292);
				listaParEnv();
				}
				break;
			case PC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListaParRecContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladoresParser.COMA, 0); }
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public ListaParRecContext listaParRec() {
			return getRuleContext(ListaParRecContext.class,0);
		}
		public ListaParRecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaParRec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterListaParRec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitListaParRec(this);
		}
	}

	public final ListaParRecContext listaParRec() throws RecognitionException {
		ListaParRecContext _localctx = new ListaParRecContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_listaParRec);
		try {
			setState(303);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(297);
				match(COMA);
				setState(298);
				tdato();
				setState(299);
				match(ID);
				setState(300);
				listaParRec();
				}
				break;
			case PC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParRecContext extends ParserRuleContext {
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public ListaParRecContext listaParRec() {
			return getRuleContext(ListaParRecContext.class,0);
		}
		public ParRecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parRec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterParRec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitParRec(this);
		}
	}

	public final ParRecContext parRec() throws RecognitionException {
		ParRecContext _localctx = new ParRecContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_parRec);
		try {
			setState(310);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case DOUBLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(305);
				tdato();
				setState(306);
				match(ID);
				setState(307);
				listaParRec();
				}
				break;
			case PC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 27:
			return comp_sempred((CompContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean comp_sempred(CompContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001f\u0139\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007"+
		"\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007"+
		"\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007"+
		"\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007"+
		"\"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003"+
		"R\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004h\b\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0003\u0006r\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t\u0084\b\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0003\n\u008c\b\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0003\f\u00a1\b\f\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00be\b\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00d0\b\u0013\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u00dd"+
		"\b\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u00e9"+
		"\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0003\u0019\u00f3\b\u0019\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u00fb"+
		"\b\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0005\u001b\u0106\b\u001b\n"+
		"\u001b\f\u001b\u0109\t\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0003\u001f\u0122\b\u001f\u0001 \u0001 \u0001 \u0001"+
		" \u0003 \u0128\b \u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0003!\u0130"+
		"\b!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0003\"\u0137\b\"\u0001\""+
		"\u0000\u00016#\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BD\u0000\u0002\u0001\u0000\r"+
		"\u0012\u0001\u0000\u0016\u0017\u0138\u0000F\u0001\u0000\u0000\u0000\u0002"+
		"H\u0001\u0000\u0000\u0000\u0004J\u0001\u0000\u0000\u0000\u0006Q\u0001"+
		"\u0000\u0000\u0000\bg\u0001\u0000\u0000\u0000\ni\u0001\u0000\u0000\u0000"+
		"\fq\u0001\u0000\u0000\u0000\u000es\u0001\u0000\u0000\u0000\u0010w\u0001"+
		"\u0000\u0000\u0000\u0012\u0083\u0001\u0000\u0000\u0000\u0014\u008b\u0001"+
		"\u0000\u0000\u0000\u0016\u008d\u0001\u0000\u0000\u0000\u0018\u00a0\u0001"+
		"\u0000\u0000\u0000\u001a\u00a2\u0001\u0000\u0000\u0000\u001c\u00a5\u0001"+
		"\u0000\u0000\u0000\u001e\u00af\u0001\u0000\u0000\u0000 \u00b1\u0001\u0000"+
		"\u0000\u0000\"\u00bd\u0001\u0000\u0000\u0000$\u00bf\u0001\u0000\u0000"+
		"\u0000&\u00cf\u0001\u0000\u0000\u0000(\u00dc\u0001\u0000\u0000\u0000*"+
		"\u00de\u0001\u0000\u0000\u0000,\u00e0\u0001\u0000\u0000\u0000.\u00e8\u0001"+
		"\u0000\u0000\u00000\u00ea\u0001\u0000\u0000\u00002\u00f2\u0001\u0000\u0000"+
		"\u00004\u00fa\u0001\u0000\u0000\u00006\u00fc\u0001\u0000\u0000\u00008"+
		"\u010a\u0001\u0000\u0000\u0000:\u0110\u0001\u0000\u0000\u0000<\u0115\u0001"+
		"\u0000\u0000\u0000>\u0121\u0001\u0000\u0000\u0000@\u0127\u0001\u0000\u0000"+
		"\u0000B\u012f\u0001\u0000\u0000\u0000D\u0136\u0001\u0000\u0000\u0000F"+
		"G\u0007\u0000\u0000\u0000G\u0001\u0001\u0000\u0000\u0000HI\u0007\u0001"+
		"\u0000\u0000I\u0003\u0001\u0000\u0000\u0000JK\u0003\u0006\u0003\u0000"+
		"KL\u0005\u0000\u0000\u0001L\u0005\u0001\u0000\u0000\u0000MN\u0003\b\u0004"+
		"\u0000NO\u0003\u0006\u0003\u0000OR\u0001\u0000\u0000\u0000PR\u0001\u0000"+
		"\u0000\u0000QM\u0001\u0000\u0000\u0000QP\u0001\u0000\u0000\u0000R\u0007"+
		"\u0001\u0000\u0000\u0000ST\u0003\n\u0005\u0000TU\u0005\u0006\u0000\u0000"+
		"Uh\u0001\u0000\u0000\u0000VW\u0003\u000e\u0007\u0000WX\u0005\u0006\u0000"+
		"\u0000Xh\u0001\u0000\u0000\u0000YZ\u0003\u0012\t\u0000Z[\u0005\u0006\u0000"+
		"\u0000[h\u0001\u0000\u0000\u0000\\h\u0003\u0018\f\u0000]h\u0003\u001c"+
		"\u000e\u0000^h\u0003\u0016\u000b\u0000_h\u0003<\u001e\u0000`a\u0003:\u001d"+
		"\u0000ab\u0005\u0006\u0000\u0000bh\u0001\u0000\u0000\u0000cd\u00038\u001c"+
		"\u0000de\u0005\u0006\u0000\u0000eh\u0001\u0000\u0000\u0000fh\u0003\u0010"+
		"\b\u0000gS\u0001\u0000\u0000\u0000gV\u0001\u0000\u0000\u0000gY\u0001\u0000"+
		"\u0000\u0000g\\\u0001\u0000\u0000\u0000g]\u0001\u0000\u0000\u0000g^\u0001"+
		"\u0000\u0000\u0000g_\u0001\u0000\u0000\u0000g`\u0001\u0000\u0000\u0000"+
		"gc\u0001\u0000\u0000\u0000gf\u0001\u0000\u0000\u0000h\t\u0001\u0000\u0000"+
		"\u0000ij\u0003\u0002\u0001\u0000jk\u0005\u001d\u0000\u0000kl\u0003\f\u0006"+
		"\u0000lm\u0003\u0014\n\u0000m\u000b\u0001\u0000\u0000\u0000no\u0005\u0001"+
		"\u0000\u0000or\u0003\u001e\u000f\u0000pr\u0001\u0000\u0000\u0000qn\u0001"+
		"\u0000\u0000\u0000qp\u0001\u0000\u0000\u0000r\r\u0001\u0000\u0000\u0000"+
		"st\u0005\u001d\u0000\u0000tu\u0005\u0001\u0000\u0000uv\u0003*\u0015\u0000"+
		"v\u000f\u0001\u0000\u0000\u0000wx\u0005\u0004\u0000\u0000xy\u0003\u0006"+
		"\u0003\u0000yz\u0005\u0005\u0000\u0000z\u0011\u0001\u0000\u0000\u0000"+
		"{|\u0005\u001c\u0000\u0000|\u0084\u0005\u001d\u0000\u0000}~\u0005\u001c"+
		"\u0000\u0000~\u0084\u0005\u0015\u0000\u0000\u007f\u0080\u0005\u001c\u0000"+
		"\u0000\u0080\u0084\u0003\u000e\u0007\u0000\u0081\u0082\u0005\u001c\u0000"+
		"\u0000\u0082\u0084\u0003\n\u0005\u0000\u0083{\u0001\u0000\u0000\u0000"+
		"\u0083}\u0001\u0000\u0000\u0000\u0083\u007f\u0001\u0000\u0000\u0000\u0083"+
		"\u0081\u0001\u0000\u0000\u0000\u0084\u0013\u0001\u0000\u0000\u0000\u0085"+
		"\u0086\u0005\u0007\u0000\u0000\u0086\u0087\u0005\u001d\u0000\u0000\u0087"+
		"\u0088\u0003\f\u0006\u0000\u0088\u0089\u0003\u0014\n\u0000\u0089\u008c"+
		"\u0001\u0000\u0000\u0000\u008a\u008c\u0001\u0000\u0000\u0000\u008b\u0085"+
		"\u0001\u0000\u0000\u0000\u008b\u008a\u0001\u0000\u0000\u0000\u008c\u0015"+
		"\u0001\u0000\u0000\u0000\u008d\u008e\u0005\u0018\u0000\u0000\u008e\u008f"+
		"\u0005\u0002\u0000\u0000\u008f\u0090\u0003*\u0015\u0000\u0090\u0091\u0005"+
		"\u0003\u0000\u0000\u0091\u0092\u0003\b\u0004\u0000\u0092\u0017\u0001\u0000"+
		"\u0000\u0000\u0093\u0094\u0005\u0019\u0000\u0000\u0094\u0095\u0005\u0002"+
		"\u0000\u0000\u0095\u0096\u0003*\u0015\u0000\u0096\u0097\u0005\u0003\u0000"+
		"\u0000\u0097\u0098\u0003\b\u0004\u0000\u0098\u00a1\u0001\u0000\u0000\u0000"+
		"\u0099\u009a\u0005\u0019\u0000\u0000\u009a\u009b\u0005\u0002\u0000\u0000"+
		"\u009b\u009c\u0003*\u0015\u0000\u009c\u009d\u0005\u0003\u0000\u0000\u009d"+
		"\u009e\u0003\b\u0004\u0000\u009e\u009f\u0003\u001a\r\u0000\u009f\u00a1"+
		"\u0001\u0000\u0000\u0000\u00a0\u0093\u0001\u0000\u0000\u0000\u00a0\u0099"+
		"\u0001\u0000\u0000\u0000\u00a1\u0019\u0001\u0000\u0000\u0000\u00a2\u00a3"+
		"\u0005\u001a\u0000\u0000\u00a3\u00a4\u0003\u0010\b\u0000\u00a4\u001b\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a6\u0005\u001b\u0000\u0000\u00a6\u00a7\u0005"+
		"\u0002\u0000\u0000\u00a7\u00a8\u0003\u000e\u0007\u0000\u00a8\u00a9\u0005"+
		"\u0006\u0000\u0000\u00a9\u00aa\u0003*\u0015\u0000\u00aa\u00ab\u0005\u0006"+
		"\u0000\u0000\u00ab\u00ac\u0003\u000e\u0007\u0000\u00ac\u00ad\u0005\u0003"+
		"\u0000\u0000\u00ad\u00ae\u0003\b\u0004\u0000\u00ae\u001d\u0001\u0000\u0000"+
		"\u0000\u00af\u00b0\u0003 \u0010\u0000\u00b0\u001f\u0001\u0000\u0000\u0000"+
		"\u00b1\u00b2\u0003$\u0012\u0000\u00b2\u00b3\u0003\"\u0011\u0000\u00b3"+
		"!\u0001\u0000\u0000\u0000\u00b4\u00b5\u0005\b\u0000\u0000\u00b5\u00b6"+
		"\u0003$\u0012\u0000\u00b6\u00b7\u0003\"\u0011\u0000\u00b7\u00be\u0001"+
		"\u0000\u0000\u0000\u00b8\u00b9\u0005\t\u0000\u0000\u00b9\u00ba\u0003$"+
		"\u0012\u0000\u00ba\u00bb\u0003\"\u0011\u0000\u00bb\u00be\u0001\u0000\u0000"+
		"\u0000\u00bc\u00be\u0001\u0000\u0000\u0000\u00bd\u00b4\u0001\u0000\u0000"+
		"\u0000\u00bd\u00b8\u0001\u0000\u0000\u0000\u00bd\u00bc\u0001\u0000\u0000"+
		"\u0000\u00be#\u0001\u0000\u0000\u0000\u00bf\u00c0\u0003(\u0014\u0000\u00c0"+
		"\u00c1\u0003&\u0013\u0000\u00c1%\u0001\u0000\u0000\u0000\u00c2\u00c3\u0005"+
		"\u000b\u0000\u0000\u00c3\u00c4\u0003(\u0014\u0000\u00c4\u00c5\u0003&\u0013"+
		"\u0000\u00c5\u00d0\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005\f\u0000\u0000"+
		"\u00c7\u00c8\u0003(\u0014\u0000\u00c8\u00c9\u0003&\u0013\u0000\u00c9\u00d0"+
		"\u0001\u0000\u0000\u0000\u00ca\u00cb\u0005\n\u0000\u0000\u00cb\u00cc\u0003"+
		"(\u0014\u0000\u00cc\u00cd\u0003&\u0013\u0000\u00cd\u00d0\u0001\u0000\u0000"+
		"\u0000\u00ce\u00d0\u0001\u0000\u0000\u0000\u00cf\u00c2\u0001\u0000\u0000"+
		"\u0000\u00cf\u00c6\u0001\u0000\u0000\u0000\u00cf\u00ca\u0001\u0000\u0000"+
		"\u0000\u00cf\u00ce\u0001\u0000\u0000\u0000\u00d0\'\u0001\u0000\u0000\u0000"+
		"\u00d1\u00dd\u0005\u0015\u0000\u0000\u00d2\u00dd\u0005\u001d\u0000\u0000"+
		"\u00d3\u00d4\u0005\t\u0000\u0000\u00d4\u00dd\u0005\u0015\u0000\u0000\u00d5"+
		"\u00d6\u0005\t\u0000\u0000\u00d6\u00dd\u0005\u001d\u0000\u0000\u00d7\u00dd"+
		"\u0003:\u001d\u0000\u00d8\u00d9\u0005\u0002\u0000\u0000\u00d9\u00da\u0003"+
		" \u0010\u0000\u00da\u00db\u0005\u0003\u0000\u0000\u00db\u00dd\u0001\u0000"+
		"\u0000\u0000\u00dc\u00d1\u0001\u0000\u0000\u0000\u00dc\u00d2\u0001\u0000"+
		"\u0000\u0000\u00dc\u00d3\u0001\u0000\u0000\u0000\u00dc\u00d5\u0001\u0000"+
		"\u0000\u0000\u00dc\u00d7\u0001\u0000\u0000\u0000\u00dc\u00d8\u0001\u0000"+
		"\u0000\u0000\u00dd)\u0001\u0000\u0000\u0000\u00de\u00df\u0003,\u0016\u0000"+
		"\u00df+\u0001\u0000\u0000\u0000\u00e0\u00e1\u00030\u0018\u0000\u00e1\u00e2"+
		"\u0003.\u0017\u0000\u00e2-\u0001\u0000\u0000\u0000\u00e3\u00e4\u0005\u0014"+
		"\u0000\u0000\u00e4\u00e5\u00030\u0018\u0000\u00e5\u00e6\u0003.\u0017\u0000"+
		"\u00e6\u00e9\u0001\u0000\u0000\u0000\u00e7\u00e9\u0001\u0000\u0000\u0000"+
		"\u00e8\u00e3\u0001\u0000\u0000\u0000\u00e8\u00e7\u0001\u0000\u0000\u0000"+
		"\u00e9/\u0001\u0000\u0000\u0000\u00ea\u00eb\u00034\u001a\u0000\u00eb\u00ec"+
		"\u00032\u0019\u0000\u00ec1\u0001\u0000\u0000\u0000\u00ed\u00ee\u0005\u0013"+
		"\u0000\u0000\u00ee\u00ef\u00034\u001a\u0000\u00ef\u00f0\u00032\u0019\u0000"+
		"\u00f0\u00f3\u0001\u0000\u0000\u0000\u00f1\u00f3\u0001\u0000\u0000\u0000"+
		"\u00f2\u00ed\u0001\u0000\u0000\u0000\u00f2\u00f1\u0001\u0000\u0000\u0000"+
		"\u00f33\u0001\u0000\u0000\u0000\u00f4\u00fb\u0003(\u0014\u0000\u00f5\u00fb"+
		"\u00036\u001b\u0000\u00f6\u00f7\u0005\u0002\u0000\u0000\u00f7\u00f8\u0003"+
		",\u0016\u0000\u00f8\u00f9\u0005\u0003\u0000\u0000\u00f9\u00fb\u0001\u0000"+
		"\u0000\u0000\u00fa\u00f4\u0001\u0000\u0000\u0000\u00fa\u00f5\u0001\u0000"+
		"\u0000\u0000\u00fa\u00f6\u0001\u0000\u0000\u0000\u00fb5\u0001\u0000\u0000"+
		"\u0000\u00fc\u00fd\u0006\u001b\uffff\uffff\u0000\u00fd\u00fe\u0003\u001e"+
		"\u000f\u0000\u00fe\u00ff\u0003\u0000\u0000\u0000\u00ff\u0100\u0003\u001e"+
		"\u000f\u0000\u0100\u0107\u0001\u0000\u0000\u0000\u0101\u0102\n\u0001\u0000"+
		"\u0000\u0102\u0103\u0003\u0000\u0000\u0000\u0103\u0104\u00036\u001b\u0002"+
		"\u0104\u0106\u0001\u0000\u0000\u0000\u0105\u0101\u0001\u0000\u0000\u0000"+
		"\u0106\u0109\u0001\u0000\u0000\u0000\u0107\u0105\u0001\u0000\u0000\u0000"+
		"\u0107\u0108\u0001\u0000\u0000\u0000\u01087\u0001\u0000\u0000\u0000\u0109"+
		"\u0107\u0001\u0000\u0000\u0000\u010a\u010b\u0003\u0002\u0001\u0000\u010b"+
		"\u010c\u0005\u001d\u0000\u0000\u010c\u010d\u0005\u0002\u0000\u0000\u010d"+
		"\u010e\u0003D\"\u0000\u010e\u010f\u0005\u0003\u0000\u0000\u010f9\u0001"+
		"\u0000\u0000\u0000\u0110\u0111\u0005\u001d\u0000\u0000\u0111\u0112\u0005"+
		"\u0002\u0000\u0000\u0112\u0113\u0003@ \u0000\u0113\u0114\u0005\u0003\u0000"+
		"\u0000\u0114;\u0001\u0000\u0000\u0000\u0115\u0116\u0003\u0002\u0001\u0000"+
		"\u0116\u0117\u0005\u001d\u0000\u0000\u0117\u0118\u0005\u0002\u0000\u0000"+
		"\u0118\u0119\u0003D\"\u0000\u0119\u011a\u0005\u0003\u0000\u0000\u011a"+
		"\u011b\u0003\u0010\b\u0000\u011b=\u0001\u0000\u0000\u0000\u011c\u011d"+
		"\u0005\u0007\u0000\u0000\u011d\u011e\u0003 \u0010\u0000\u011e\u011f\u0003"+
		">\u001f\u0000\u011f\u0122\u0001\u0000\u0000\u0000\u0120\u0122\u0001\u0000"+
		"\u0000\u0000\u0121\u011c\u0001\u0000\u0000\u0000\u0121\u0120\u0001\u0000"+
		"\u0000\u0000\u0122?\u0001\u0000\u0000\u0000\u0123\u0124\u0003 \u0010\u0000"+
		"\u0124\u0125\u0003>\u001f\u0000\u0125\u0128\u0001\u0000\u0000\u0000\u0126"+
		"\u0128\u0001\u0000\u0000\u0000\u0127\u0123\u0001\u0000\u0000\u0000\u0127"+
		"\u0126\u0001\u0000\u0000\u0000\u0128A\u0001\u0000\u0000\u0000\u0129\u012a"+
		"\u0005\u0007\u0000\u0000\u012a\u012b\u0003\u0002\u0001\u0000\u012b\u012c"+
		"\u0005\u001d\u0000\u0000\u012c\u012d\u0003B!\u0000\u012d\u0130\u0001\u0000"+
		"\u0000\u0000\u012e\u0130\u0001\u0000\u0000\u0000\u012f\u0129\u0001\u0000"+
		"\u0000\u0000\u012f\u012e\u0001\u0000\u0000\u0000\u0130C\u0001\u0000\u0000"+
		"\u0000\u0131\u0132\u0003\u0002\u0001\u0000\u0132\u0133\u0005\u001d\u0000"+
		"\u0000\u0133\u0134\u0003B!\u0000\u0134\u0137\u0001\u0000\u0000\u0000\u0135"+
		"\u0137\u0001\u0000\u0000\u0000\u0136\u0131\u0001\u0000\u0000\u0000\u0136"+
		"\u0135\u0001\u0000\u0000\u0000\u0137E\u0001\u0000\u0000\u0000\u0011Qg"+
		"q\u0083\u008b\u00a0\u00bd\u00cf\u00dc\u00e8\u00f2\u00fa\u0107\u0121\u0127"+
		"\u012f\u0136";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}