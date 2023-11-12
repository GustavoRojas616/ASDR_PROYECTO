import sys
class TipoToken:
    #Tokens de un solo caracter
    LEFT_PAREN = 'LEFT_PAREN'
    RIGHT_PAREN = 'RIGHT_PAREN'
    LEFT_BRACE = 'LEFT_BRACE'
    RIGHT_BRACE = 'RIGHT_BRACE'
    COMMA = 'COMMA'
    DOT = 'DOT'
    MINUS = 'MINUS'
    PLUS = 'PLUS'
    SEMICOLON = 'SEMICOLON'
    SLASH = 'SLASH'
    STAR = 'STAR'

    #Tokens de uno o dos caracteres
    BANG = 'BANG'
    BANG_EQUAL = 'BANG_EQUAL'
    EQUAL = 'EQUAL'
    EQUAL_EQUAL = 'EQUAL_EQUAL'
    GREATER = 'GREATER'
    GREATER_EQUAL = 'GREATER_EQUAL'
    LESS = 'LESS'
    LESS_EQUAL = 'LESS_EQUAL'

    #Literales

    IDENTIFIER = 'IDENTIFIER'
    STRING = 'STRING'
    NUMBER = 'NUMBER'

    #Palabras clave
    AND = 'AND'
    ELSE = 'ELSE'
    FALSE = 'FALSE'
    FUN = 'FUN'
    FOR = 'FOR'
    IF = 'IF'
    NULL = 'NULL'
    OR = 'OR'
    PRINT = 'PRINT'
    RETURN = 'RETURN'
    TRUE = 'TRUE'
    VAR = 'VAR'
    WHILE = 'WHILE'

    EOF = 'EOF'

entrada = [{'tipo': 'VAR', 'lexema': 'var', 'valor': 'null'}, {'tipo': 'IDENTIFIER', 'lexema': 'nombre', 'valor': 'null'}, {'tipo': 'EQUAL', 'lexema': '=', 'valor': 'null'}, {'tipo': 'STRING', 'lexema': '"Nombre"', 'valor': 'Nombre'}, {'tipo': 'SEMICOLON', 'lexema': ';', 'valor': 'null'}, {'tipo': 'VAR', 'lexema': 'var', 'valor': 'null'}, {'tipo': 'IDENTIFIER', 'lexema': 'apellido1', 'valor': 'null'}, {'tipo': 'EQUAL', 'lexema': '=', 'valor': 'null'}, {'tipo': 'STRING', 'lexema': '"Apellido"', 'valor': 'Apellido'}, {'tipo': 'SEMICOLON', 'lexema': ';', 'valor': 'null'}, {'tipo': 'PRINT', 'lexema': 'print', 'valor': 'null'}, {'tipo': 'IDENTIFIER', 'lexema': 'nombre', 'valor': 'null'}, {'tipo': 'PLUS', 'lexema': '+', 'valor': 'null'}, {'tipo': 'STRING', 'lexema': '" "', 'valor': ' '}, {'tipo': 'PLUS', 'lexema': '+', 'valor': 'null'}, {'tipo': 'IDENTIFIER', 'lexema': 'apellido1', 'valor': 'null'}, {'tipo': 'SEMICOLON', 'lexema': ';', 'valor': 'null'}, {'tipo': 'EOF', 'lexema': '', 'valor': 'null'}]
class ASDR:

    def __init__(self, tokens):
        self.i = 0
        self.hayErrores = False
        self.tokens = tokens
        self.preanalisis = self.tokens[self.i]

    def parse(self):
        self.program()

        if self.preanalisis['tipo'] == TipoToken.EOF and not self.hayErrores:
            print("Consulta correcta.")
            return True
        else:
            print("Se encontraron errores.")
            return False

    # PROGRAM -> DECLARATION
    def program(self):
        self.declaration()

    #Declaraciones
    # DECLARATION -> FUN_DECL DECLARATION
    # DECLARATION -> VAR_DECL DECLARATION
    # DECLARATION -> STATEMENT DECLARATION
    # DECLARATION -> Ɛ
    def declaration(self):

        if self.preanalisis['tipo'] == TipoToken.FUN:
            self.fun_decl()
            self.declaration()

        elif self.preanalisis['tipo'] == TipoToken.VAR:
            self.var_decl()
            self.declaration()

        elif self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN or self.preanalisis['tipo'] == TipoToken.FOR or self.preanalisis['tipo'] == TipoToken.IF or self.preanalisis['tipo'] == TipoToken.PRINT or self.preanalisis['tipo'] == TipoToken.RETURN or self.preanalisis['tipo'] == TipoToken.WHILE or self.preanalisis['tipo'] == TipoToken.LEFT_BRACE:
            self.statement()
            self.declaration()

    # FUN_DECL -> fun FUNCTION
    def fun_decl(self):
        if self.preanalisis['tipo'] == TipoToken.FUN:
            self.coincidir(TipoToken.FUN)
            self.function()
        else:
            self.hayErrores = True
            print('Error. Se esperaba la palabra reservada fun')

    # VAR_DECL -> var id VAR_INIT;
    def var_decl(self):
        if self.preanalisis['tipo'] == TipoToken.VAR:
            self.coincidir(TipoToken.VAR)
            self.coincidir(TipoToken.IDENTIFIER) #Checar
            self.var_init()
            self.coincidir(TipoToken.SEMICOLON)
        else:
            self.hayErrores = True
            print("Error. Se esparaba la palabra reservada var")

    # VAR_INIT -> = EXPRESSION
    # VAR_INIT -> Ɛ
    def var_init(self):
        if self.preanalisis['tipo'] == TipoToken.EQUAL:
            self.coincidir(TipoToken.EQUAL)
            self.expression()

    #Sentencias
    # STATEMENT -> EXPR_STMT
    # STATEMENT -> FOR_STMT
    # STATEMENT -> IF_STMT
    # STATEMENT -> PRINT_STMT
    # STATEMENT -> RETURN_STMT
    # STATEMENT -> WHILE_STMT
    # STATEMENT -> BLOCK
    def statement(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.expr_stmt()
        elif self.preanalisis['tipo'] == TipoToken.FOR:
            self.for_stmt()
        elif self.preanalisis['tipo'] == TipoToken.IF:
            self.if_stmt()
        elif self.preanalisis['tipo'] == TipoToken.PRINT:
            self.print_stmt()
        elif self.preanalisis['tipo'] == TipoToken.RETURN:
            self.return_stmt()
        elif self.preanalisis['tipo'] == TipoToken.WHILE:
            self.while_stmt()
        elif self.preanalisis['tipo'] == TipoToken.LEFT_BRACE:
            self.block()
        else:
            self.hayErrores = True
            print('Error.')

    #EXPR_STMT -> EXPRESSION;
    def expr_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.expression()
            self.coincidir(TipoToken.SEMICOLON)
        else:
            self.hayErrores = True
            print("Error, se esperaba un expresion de estado")

    #FOR_STMT -> for(FOR_STMT_1 FOR_STMT_2 FOR_STMT_3)STATEMENT
    def for_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.FOR:
            self.coincidir(TipoToken.FOR)
            self.coincidir(TipoToken.LEFT_PAREN)
            self.for_stmt_1()
            self.for_stmt_2()
            self.for_stmt_3()
            self.coincidir(TipoToken.RIGHT_PAREN)
            self.statement()
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada for")

    #FOR_STMT_1 -> VAR_DECL
    # FOR_STMT_1 -> EXPR_STMT
    # FOR_STMT_1 -> ;
    def for_stmt_1(self):
        if self.preanalisis['tipo'] == TipoToken.VAR:
            self.var_decl()
        elif self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.expr_stmt()
        elif self.preanalisis['tipo'] == TipoToken.SEMICOLON:
            self.coincidir(TipoToken.SEMICOLON)
        else:
            self.hayErrores = True
            print("Error, se esparaba la palabra reservada var, declaracion de estado o punto y coma")

    #FOR_STMT_2 -> EXPRESSION;
    # FOR_STMT_2 -> ;
    def for_stmt_2(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.expression()
            self.coincidir(TipoToken.SEMICOLON)
        elif self.preanalisis['tipo'] == TipoToken.SEMICOLON:
            self.coincidir(TipoToken.SEMICOLON)
        else:
            self.hayErrores = True
            print("Error, se esperaba una declaracion de estado o un punto y coma.")

    #FOR_STMT_3 -> EXPRESSION
    #FOR_STMT_3 -> Ɛ
    def for_stmt_3(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.expression()

    #IF_STMT -> if (EXPRESSION) STATEMENT ELSE_STATEMENT
    def if_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.IF:
            self.coincidir(TipoToken.IF)
            self.coincidir(TipoToken.LEFT_PAREN)
            self.expression()
            self.coincidir(TipoToken.RIGHT_PAREN)
            self.statement()
            self.else_stmt()
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada if.")

    #ELSE_STATEMENT -> else STATEMENT
    #ELSE_STATEMENT -> Ɛ
    def else_statement(self):
        if self.preanalisis['tipo'] == TipoToken.ELSE:
            self.coincidir(TipoToken.ELSE)
            self.statement()

    #PRINT_STMT -> print EXPRESSION ;
    def print_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.PRINT:
            self.coincidir(TipoToken.PRINT)
            self.expression()
            self.coincidir(TipoToken.SEMICOLON)
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada print.")

    #RETURN_STMT -> return RETURN_EXP_OPC ;
    def return_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.RETURN:
            self.coincidir(TipoToken.RETURN)
            self.return_exp_opc()
            self.coincidir(TipoToken.SEMICOLON)
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada return.")

    #RETURN_EXP_OPC -> EXPRESSION
    #RETURN_EXP_OPC -> Ɛ
    def return_exp_opc(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.expression()

    #WHILE_STMT -> while (EXPRESSION) STATEMENT
    def while_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.WHILE:
            self.coincidir(TipoToken.WHILE)
            self.coincidir(TipoToken.LEFT_PAREN)
            self.expression()
            self.coincidir(TipoToken.RIGHT_PAREN)
            self.statement()
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada while.")

    #BLOCK -> {DECLARATION}
    def block(self):
        if self.preanalisis['tipo'] == TipoToken.LEFT_BRACE:
            self.coincidir(TipoToken.LEFT_BRACE)
            self.declaration()
            self.coincidir(TipoToken.RIGHT_BRACE)
        else:
            self.hayErrores = True
            print("Error, se esperaba el uso de las llaves.")

    #Expresiones
    #EXPRESSION -> ASSIGNMENT
    def expression(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.assignment()
        else:
            self.hayErrores = True
            print("Error, se esperaba una declaracion de estado, identificador o parentesis.")

    #ASSIGNMENT -> LOGIC_OR ASSIGNMENT_OPC
    def assignment(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.logic_or()
            self.assignment_opc()
        else:
            self.hayErrores = True
            print("Error.")

    #ASSIGNMENT_OPC -> = EXPRESSION
    #ASSIGNMENT_OPC -> Ɛ
    def assignment_opc(self):
        if self.preanalisis['tipo'] == TipoToken.EQUAL:
            self.coincidir(TipoToken.EQUAL)
            self.expression()

    #LOGIC_OR -> LOGIC_AND LOGIC_OR_2
    def logic_or(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.logic_and()
            self.logic_or_2()
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #LOGIC_OR_2 -> or LOGIC_AND LOGIC_OR_2
    #LOGIC_OR_2 -> Ɛ
    def logic_or_2(self):
        if self.preanalisis['tipo'] == TipoToken.OR:
            self.coincidir(TipoToken.OR)
            self.logic_and()
            self.logic_or_2()

    #LOGIC_AND -> EQUALITY LOGIC_AND_2
    def logic_and(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.equality()
            self.logic_and_2()
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #LOGIC_AND_2 -> and EQUALITY LOGIC_AND_2
    #LOGIC_AND_2 -> Ɛ
    def logic_and_2(self):
        if self.preanalisis['tipo'] == TipoToken.AND:
            self.coincidir(TipoToken.AND)
            self.equality()
            self.logic_and_2()

    #EQUALITY -> COMPARISON EQUALITY_2
    def equality(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.comparison()
            self.equality_2()
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #EQUALITY_2 -> != COMPARISON EQUALITY_2
    #EQUALITY_2 -> == COMPARISON EQUALITY_2
    #EQUALITY_2 -> Ɛ
    def equality_2(self):
        if self.preanalisis['tipo'] == TipoToken.BANG_EQUAL:
            self.coincidir(TipoToken.BANG_EQUAL)
            self.comparison()
            self.equality_2()
        elif self.preanalisis['tipo'] == TipoToken.EQUAL_EQUAL:
            self.coincidir(TipoToken.EQUAL_EQUAL)
            self.comparison()
            self.equality_2()

    #COMPARISON -> TERM COMPARISON_2
    def comparison(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.term()
            self.comparison_2()
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #COMPARISON_2 -> > TERM COMPARISON_2
    #COMPARISON_2 -> >= TERM COMPARISON_2
    #COMPARISON_2 -> < TERM COMPARISON_2
    #COMPARISON_2 -> <= TERM COMPARISON_2
    #COMPARISON_2 -> Ɛ
    def comparison_2(self):
        if self.preanalisis['tipo'] == TipoToken.GREATER:
            self.coincidir(TipoToken.GREATER)
            self.term()
            self.comparison_2()
        elif self.preanalisis['tipo'] == TipoToken.GREATER_EQUAL:
            self.coincidir(TipoToken.GREATER_EQUAL)
            self.term()
            self.comparison_2()
        elif self.preanalisis['tipo'] == TipoToken.LESS:
            self.coincidir(TipoToken.LESS)
            self.term()
            self.comparison_2()
        elif self.preanalisis['tipo'] == TipoToken.LESS_EQUAL:
            self.coincidir(TipoToken.LESS_EQUAL)
            self.term()
            self.comparison_2()

    #TERM -> FACTOR TERM_2
    def term(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.factor()
            self.term_2()
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #TERM_2 -> - FACTOR TERM_2
    #TERM_2 -> + FACTOR TERM_2
    #TERM_2 -> Ɛ
    def term_2(self):
        if self.preanalisis['tipo'] == TipoToken.MINUS:
            self.coincidir(TipoToken.MINUS)
            self.factor()
            self.term_2()
        elif self.preanalisis['tipo'] == TipoToken.PLUS:
            self.coincidir(TipoToken.PLUS)
            self.factor()
            self.term_2()

    #FACTOR -> UNARY FACTOR_2
    def factor(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.unary()
            self.factor_2()
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #FACTOR_2 -> / UNARY FACTOR_2
    #FACTOR_2 -> * UNARY FACTOR_2
    #FACTOR_2 -> Ɛ
    def factor_2(self):
        if self.preanalisis['tipo'] == TipoToken.SLASH:
            self.coincidir(TipoToken.SLASH)
            self.unary()
            self.factor_2()
        elif self.preanalisis['tipo'] == TipoToken.STAR:
            self.coincidir(TipoToken.STAR)
            self.unary()
            self.factor_2()

    #UNARY -> ! UNARY
    #UNARY -> - UNARY
    #UNARY -> CALL
    def unary(self):
        if self.preanalisis['tipo'] == TipoToken.BANG:
            self.coincidir(TipoToken.BANG)
            self.unary()
        elif self.preanalisis['tipo'] == TipoToken.MINUS:
            self.coincidir(TipoToken.MINUS)
            self.unary()
        elif self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.call()
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #CALL -> PRIMARY CALL_2
    def call(self):
        if self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.primary()
            self.call_2()
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #CALL_2 -> (ARGUMENTS_OPC) CALL_2
    #CALL_2 -> Ɛ
    def call_2(self):
        if self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.coincidir(TipoToken.LEFT_PAREN)
            self.arguments_opc()
            self.coincidir(TipoToken.RIGHT_PAREN)
            self.call_2()

    #PRIMARY -> true
    #PRIMARY -> false
    #PRIMARY -> null
    #PRIMARY -> number
    #PRIMARY -> string
    #PRIMARY -> id
    #PRIMARY -> (EXPRESSION)
    def primary(self):
        if self.preanalisis['tipo'] == TipoToken.TRUE:
            self.coincidir(TipoToken.TRUE)
        elif self.preanalisis['tipo'] == TipoToken.FALSE:
            self.coincidir(TipoToken.FALSE)
        elif self.preanalisis['tipo'] == TipoToken.NULL:
            self.coincidir(TipoToken.NULL)
        elif self.preanalisis['tipo'] == TipoToken.NUMBER:
            self.coincidir(TipoToken.NUMBER)
        elif self.preanalisis['tipo'] == TipoToken.STRING:
            self.coincidir(TipoToken.STRING)
        elif self.preanalisis['tipo'] == TipoToken.IDENTIFIER:
            self.coincidir(TipoToken.IDENTIFIER)
        elif self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.coincidir(TipoToken.LEFT_PAREN)
            self.expression()
            self.coincidir(TipoToken.RIGHT_PAREN)
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #Otras
    #FUNCTION -> id (PARAMETERS_OPC) BLOCK
    def function(self):
        if self.preanalisis['tipo'] == TipoToken.IDENTIFIER:
            self.coincidir(TipoToken.IDENTIFIER)
            self.coincidir(TipoToken.LEFT_PAREN)
            self.parameters_opc()
            self.coincidir(TipoToken.RIGHT_PAREN)
            self.block()
        else:
            self.hayErrores = True
            print("Error, se esperaba un identificador.")

    #FUNCTIONS -> FUN_DECL FUNCTIONS
    #FUNCTIONS -> Ɛ
    def functions(self):
        if self.preanalisis['tipo'] == TipoToken.FUN:
            self.fun_decl()
            self.functions()

    #PARAMETERS_OPC -> PARAMETERS
    #PARAMETERS_OPC -> Ɛ
    def parameters_opc(self):
        if self.preanalisis['tipo'] == TipoToken.IDENTIFIER:
            self.parameters()

    #PARAMETERS -> id PARAMETERS_2
    def parameters(self):
        if self.preanalisis['tipo'] == TipoToken.IDENTIFIER:
            self.coincidir(TipoToken.IDENTIFIER)
            self.parameters_2()
        else:
            self.hayErrores = True
            print("Error, se esperaba un identificador.")

    #PARAMETERS_2 -> , id PARAMETERS_2
    #PARAMETERS_2 -> Ɛ
    def parameters_2(self):
        if self.preanalisis['tipo'] == TipoToken.COMMA:
            self.coincidir(TipoToken.COMMA)
            self.coincidir(TipoToken.IDENTIFIER)
            self.parameters_2()

    #ARGUMENTS_OPC -> EXPRESSION ARGUMENTS
    #ARGUMENTS_OPC -> Ɛ
    def arguments_opc(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.expression()
            self.arguments()

    #ARGUMENTS -> , EXPRESSION ARGUMENTS
    #ARGUMENTS -> Ɛ
    def arguments(self):
        if self.preanalisis['tipo'] == TipoToken.COMMA:
            self.coincidir(TipoToken.COMMA)
            self.expression()
            self.arguments()

    def coincidir(self, t):
        if self.hayErrores:
            sys.exit()
        elif self.preanalisis['tipo'] == t:
            self.i = self.i + 1
            self.preanalisis = self.tokens[self.i]
        else:
            self.hayErrores = True
            print("ERROR")










analizador=ASDR(entrada)
analizador.parse()


