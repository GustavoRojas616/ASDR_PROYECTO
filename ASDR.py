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

entrada = [{'tipo': 'VAR', 'lexema': 'var', 'valor': 'null'}, {'tipo': 'IDENTIFIER', 'lexema': 'nombre', 'valor': 'null'}, {'tipo': 'EQUAL', 'lexema': '=', 'valor': 'null'}, {'tipo': 'STRING', 'lexema': '"Nombre"', 'valor': 'Nombre'}, {'tipo': 'SEMICOLON', 'lexema': ';', 'valor': 'null'}, {'tipo': 'VAR', 'lexema': 'var', 'valor': 'null'}, {'tipo': 'IDENTIFIER', 'lexema': 'apellido1', 'valor': 'null'}, {'tipo': 'EQUAL', 'lexema': '=', 'valor': 'null'}, {'tipo': 'STRING', 'lexema': '"Apellido"', 'valor': 'Apellido'}, {'tipo': 'SEMICOLON', 'lexema': ';', 'valor': 'null'}, {'tipo': 'PRINT', 'lexema': 'print', 'valor': 'null'}, {'tipo': 'IDENTIFIER', 'lexema': 'nombre', 'valor': 'null'}, {'tipo': 'PLUS', 'lexema': '+', 'valor': 'null'}, {'tipo': 'STRING', 'lexema': '" "', 'valor': ' '}, {'tipo': 'PLUS', 'lexema': '+', 'valor': 'null'}, {'tipo': 'IDENTIFIER', 'lexema': 'apellido1', 'valor': 'null'}, {'tipo': 'SEMICOLON', 'lexema': ';', 'valor': 'null'}]
class ASDR:

    def __init__(self, tokens):
        self.i = 10
        self.hayErrores = False
        self.tokens = tokens
        self.preanalisis = self.tokens[self.i]
        if self.preanalisis['tipo'] == TipoToken.PRINT:
            print(self.preanalisis)

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


analizador=ASDR(entrada)


