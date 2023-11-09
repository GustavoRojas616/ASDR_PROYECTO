simbolos = {'LESS': '<', 'LESS-EQUAL': '<=', 'GREATER': '>', 'GREATER_EQUAL': '>=', 'BANG': '!', 'BANG_EQUAL': '!=',
            'EQUAL': '=', 'EQUAL_EQUAL': '==', 'PLUS': '+', 'MINUS': '-', 'STAR': '*', 'SLASH': '/', 'LEFT_BRACE': '{',
            'RIGHT_BRACE': '}', 'LEFT_PAREN': '(', 'RIGHT_PAREN': ')', 'COMMA': ',', 'DOT': '.', 'SEMICOLON': ';'}
simbolos_values = simbolos.values()
reservadas = {'AND': 'and', 'ELSE': 'else', 'FALSE': 'false', 'FOR': 'for', 'FUN': 'fun', 'IF': 'if', 'NULL': 'null',
              'OR': 'or', 'PRINT': 'print', 'RETURN': 'return', 'TRUE': 'true', 'VAR': 'var', 'WHILE': 'while'}
reservadas_values = reservadas.values()

tokens=['var', 'nombre', '=', '"Nombre"', ';', 'var', 'apellido1', '=', '"Apellido"', ';', 'print', 'nombre', '+', '" "', '+', 'apellido1', ';']

preanalisis = 'perro55'
print(preanalisis.isalnum())



class ASDR:
    global tokens
    def __init__(self, tokens):
        self.i = 0
        self.hayErrores = False
        self.tokens = tokens
        self.preanalisis = self.tokens[self.i]

    def parse(self):
        self.program()

        if len(self.preanalisis) == len(tokens) and self.hayErrores==False:
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

        if self.preanalisis == reservadas.get('FUN'):
            self.fun_decl()
            self.declaration()

        elif self.preanalisis == reservadas.get('VAR'):
            self.var_decl()
            self.declaration()

        elif self.preanalisis == simbolos.get('BANG') or self.preanalisis == simbolos.get('MINUS') or self.preanalisis == reservadas.get('TRUE') or self.preanalisis == reservadas.get('FALSE') or self.preanalisis == reservadas.get('NULL') or self.preanalisis.isnumber() == True or self.preanalisis.isalnum() == True or (self.preanalisis not in simbolos_values and self.preanalisis not in reservadas_values) or self.preanalisis == simbolos.get('LEFT_PAREN') or self.preanalisis == reservadas.get('FOR') or self.preanalisis == reservadas.get('IF') or self.preanalisis == reservadas.get('PRINT') or self.preanalisis == reservadas.get('RETURN') or self.preanalisis == reservadas.get('WHILE') or self.preanalisis == simbolos.get('LEFT_BRACE'):
            self.statement()
            self.declaration()

    # FUN_DECL -> fun FUNCTION
    def fun_decl(self):
        if self.preanalisis == reservadas.get('FUN'):
            self.coincidir(reservadas.get('FUN'))
            self.function()
        else:
            self.hayErrores = True
            print('Error. Se esperaba la palabra reservada fun')

    # VAR_DECL -> var id VAR_INIT;
    def var_decl(self):
        if self.preanalisis == reservadas.get('VAR'):
            self.coincidir(reservadas.get('VAR'))
            self.coincidir() #Checar
            self.var_init()
            self.coincidir(simbolos.get('SEMICOLON'))
        else:
            self.hayErrores = True
            print("Error. Se esparaba la palabra reservada var")

    # VAR_INIT -> = EXPRESSION
    # VAR_INIT -> Ɛ
    def var_init(self):
        if self.preanalisis == simbolos.get('EQUAL'):
            self.coincidir(simbolos.get('EQUAL'))
            self.expression()

    # STATEMENT -> EXPR_STMT
    # STATEMENT -> FOR_STMT
    # STATEMENT -> IF_STMT
    # STATEMENT -> PRINT_STMT
    # STATEMENT -> RETURN_STMT
    # STATEMENT -> WHILE_STMT
    # STATEMENT -> BLOCK
    def statement(self):
        if self.preanalisis == simbolos.get('BANG') or self.preanalisis == simbolos.get('MINUS') or self.preanalisis == reservadas.get('TRUE') or self.preanalisis == reservadas.get('FALSE') or self.preanalisis == reservadas.get('NULL') or self.preanalisis.isnumber() == True or self.preanalisis.isalnum() == True or (self.preanalisis not in simbolos_values and self.preanalisis not in reservadas_values) or self.preanalisis == simbolos.get('LEFT_PAREN'):
            self.expr_stmt()
        elif self.preanalisis == reservadas.get('FOR'):
            self.for_stmt()
        elif self.preanalisis == reservadas.get('IF'):
            self.if_stmt()
        elif self.preanalisis == reservadas.get('PRINT'):
            self.print_stmt()
        elif self.preanalisis == reservadas.get('RETURN'):
            self.return_stmt()
        elif self.preanalisis == reservadas.get('WHILE'):
            self.while_stmt()
        elif self.preanalisis == simbolos.get('LEFT_BRACE'):
            self.block()
        else:
            self.hayErrores = True
            print('Error.')


