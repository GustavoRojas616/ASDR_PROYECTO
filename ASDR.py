#Entrega lunes en la noche
import sys

class ExprAssign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"ExprAssign({self.name}{self.value})"

class ExprBinary:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"ExprBinary({self.left}{self.operator}{self.right})"

class ExprCallFunction:
    def __init__(self, callee, arguments):
        self.callee = callee
        self.arguments = arguments

    def __str__(self):
        return f"ExprCallFunction({self.callee}{self.arguments})"

#class Expression:  (abstract class (?))
#    def __init__(self):
#        pass

class ExprGet:
    def __init__(self, object, name):
        self.object = object
        self.name = name

    def __str__(self):
        return f"ExprGet({self.object}{self.name})"
class ExprGrouping:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"ExprGrouping({self.expression})"

class ExprLiteral:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ExprLiteral({self.value})"

class ExprLogical:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"ExprLogical({self.left}{self.operator}{self.right})"
class ExprSet:
    def __init__(self, object, name, value):
        self.object = object
        self.name = name
        self.value = value

    def __str__(self):
        return f"ExprSet({self.object}{self.name}{self.value})"
class ExprSuper:
    def __init__(self, method):
        self.method = method

    def __str__(self):
        return f"ExprSuper({self.method})"
class ExprThis:
    def __init__(self):
        pass

class ExprUnary:
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"ExprUnary({self.operator}{self.right})"
class ExprVariable:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"ExprVariable({self.name})"
#class Statement:  (abstract class (?))
#    def __init__(self):
#        pass

class StmtBlock:
    def __init__(self, statements):
        self.statements = statements

    def __str__(self):
        return f"StmtBlock({self.statements})"

#class StmtClass:
#    def __init__(self, name, superclass, methods):
#        self.name = name
#        self.superclass = superclass
#        self.methods = methods

class StmtExpression:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"StmtExpression({self.expression})"

class StmtFunction:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    def __str__(self):
        return f"StmtFunction({self.name}{self.params}{self.body})"
class StmtIf:
    def __init__(self, condition, thenBranch, elseBranch):
        self.condition = condition
        self.thenBranch = thenBranch
        self.elseBranch = elseBranch

    def __str__(self):
        return f"StmtIf({self.condition}{self.thenBranch}{self.elseBranch})"

class StmtLoop:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __str__(self):
        return f"StmtLoop({self.condition}{self.body})"
class StmtPrint:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"StmtPrint({self.expression})"

class StmtReturn:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"StmtReturn({self.value})"
class StmtVar:
    def __init__(self, name, initializer):
        self.name = name
        self.initializer = initializer

    def __str__(self):
        return f"StmtVar({self.name}{self.initializer})"
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
        statements = []
        value = self.declaration(statements)
        for i in value:
            print(f'Aqui {i}')

    #Declaraciones
    # DECLARATION -> FUN_DECL DECLARATION
    # DECLARATION -> VAR_DECL DECLARATION
    # DECLARATION -> STATEMENT DECLARATION
    # DECLARATION -> Ɛ
    def declaration(self, statements):

        if self.preanalisis['tipo'] == TipoToken.FUN:
            fundcl = self.fun_decl()
            statements.append(fundcl)
            self.declaration(statements)
            #return fundcl

        elif self.preanalisis['tipo'] == TipoToken.VAR:
            vardcl = self.var_decl()
            statements.append(vardcl)
            self.declaration(statements)
            #return vardcl

        elif self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN or self.preanalisis['tipo'] == TipoToken.FOR or self.preanalisis['tipo'] == TipoToken.IF or self.preanalisis['tipo'] == TipoToken.PRINT or self.preanalisis['tipo'] == TipoToken.RETURN or self.preanalisis['tipo'] == TipoToken.WHILE or self.preanalisis['tipo'] == TipoToken.LEFT_BRACE:
            stmt = self.statement()
            statements.append(stmt)
            self.declaration(statements)
            print(f'masarriba {stmt}')
            #return stmt
        return statements

    # FUN_DECL -> fun FUNCTION
    def fun_decl(self):
        if self.preanalisis['tipo'] == TipoToken.FUN:
            self.coincidir(TipoToken.FUN)
            fun = self.function()
            return fun
        else:
            self.hayErrores = True
            print('Error. Se esperaba la palabra reservada fun')

    # VAR_DECL -> var id VAR_INIT;
    def var_decl(self):
        if self.preanalisis['tipo'] == TipoToken.VAR:
            self.coincidir(TipoToken.VAR)
            self.coincidir(TipoToken.IDENTIFIER) #Checar
            name = self.previous()
            initializer = self.var_init()
            print(name)
            self.coincidir(TipoToken.SEMICOLON)
            pc = self.previous()
            stmtv = StmtVar(name['lexema'], str(initializer))
            print(stmtv)
            return stmtv
        else:
            self.hayErrores = True
            print("Error. Se esparaba la palabra reservada var")

    # VAR_INIT -> = EXPRESSION
    # VAR_INIT -> Ɛ
    def var_init(self):
        if self.preanalisis['tipo'] == TipoToken.EQUAL:
            self.coincidir(TipoToken.EQUAL)
            initializer = self.expression()
            return initializer

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
            return self.expr_stmt()
        elif self.preanalisis['tipo'] == TipoToken.FOR:
            return self.for_stmt()
        elif self.preanalisis['tipo'] == TipoToken.IF:
            return self.if_stmt()
        elif self.preanalisis['tipo'] == TipoToken.PRINT:
            return self.print_stmt()
        elif self.preanalisis['tipo'] == TipoToken.RETURN:
            value = self.return_stmt()
            print(f'Soy return {value}')
            return value
        elif self.preanalisis['tipo'] == TipoToken.WHILE:
            return self.while_stmt()
        elif self.preanalisis['tipo'] == TipoToken.LEFT_BRACE:
            return self.block()
        else:
            self.hayErrores = True
            print('Error.')

    #EXPR_STMT -> EXPRESSION;
    def expr_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expression = self.expression()
            self.coincidir(TipoToken.SEMICOLON)
            return StmtExpression(expression)
        else:
            self.hayErrores = True
            print("Error, se esperaba un expresion de estado")

    #FOR_STMT -> for(FOR_STMT_1 FOR_STMT_2 FOR_STMT_3)STATEMENT
    def for_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.FOR:
            self.coincidir(TipoToken.FOR)
            self.coincidir(TipoToken.LEFT_PAREN)
            condition = self.for_stmt_1()
            condition2 = self.for_stmt_2()
            condition3 = self.for_stmt_3()
            cond = str(condition) + str(condition2) + str(condition3)
            print(cond)
            self.coincidir(TipoToken.RIGHT_PAREN)
            body = self.statement()
            stmtl = StmtLoop(cond, body)
            print(stmtl)
            return stmtl
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada for")

    #FOR_STMT_1 -> VAR_DECL
    # FOR_STMT_1 -> EXPR_STMT
    # FOR_STMT_1 -> ;
    def for_stmt_1(self):
        if self.preanalisis['tipo'] == TipoToken.VAR:
            return self.var_decl()
        elif self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            return self.expr_stmt()
        elif self.preanalisis['tipo'] == TipoToken.SEMICOLON:
            self.coincidir(TipoToken.SEMICOLON)
            pc = self.previous()
            return pc['lexema']
        else:
            self.hayErrores = True
            print("Error, se esparaba la palabra reservada var, declaracion de estado o punto y coma")

    #FOR_STMT_2 -> EXPRESSION;
    # FOR_STMT_2 -> ;
    def for_stmt_2(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            exp = self.expression()
            self.coincidir(TipoToken.SEMICOLON)
            pc = self.previous()
            return str(exp)
        elif self.preanalisis['tipo'] == TipoToken.SEMICOLON:
            self.coincidir(TipoToken.SEMICOLON)
            pc = self.previous()
            return pc
        else:
            self.hayErrores = True
            print("Error, se esperaba una declaracion de estado o un punto y coma.")

    #FOR_STMT_3 -> EXPRESSION
    #FOR_STMT_3 -> Ɛ
    def for_stmt_3(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            return self.expression()

    #IF_STMT -> if (EXPRESSION) STATEMENT ELSE_STATEMENT
    def if_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.IF:
            self.coincidir(TipoToken.IF)
            self.coincidir(TipoToken.LEFT_PAREN)
            condition = self.expression()
            print(f'Llegaste {condition}')
            self.coincidir(TipoToken.RIGHT_PAREN)
            thenBranch = self.statement()
            elseBranch = self.else_stmt()
            stmtif = StmtIf(condition, thenBranch, elseBranch)
            print(stmtif)
            return stmtif
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada if.")

    #ELSE_STATEMENT -> else STATEMENT
    #ELSE_STATEMENT -> Ɛ
    def else_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.ELSE:
            self.coincidir(TipoToken.ELSE)
            elseBranch = self.statement()
            return elseBranch
        #return

    #PRINT_STMT -> print EXPRESSION ;
    def print_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.PRINT:
            self.coincidir(TipoToken.PRINT)
            expression = self.expression()
            self.coincidir(TipoToken.SEMICOLON)
            pc = self.previous()
            stmtp = StmtPrint(str(expression))
            print(stmtp)
            return stmtp
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada print.")

    #RETURN_STMT -> return RETURN_EXP_OPC ;
    def return_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.RETURN:
            self.coincidir(TipoToken.RETURN)
            value = self.return_exp_opc()
            print(f'return_stmt {value}')
            self.coincidir(TipoToken.SEMICOLON)
            return StmtReturn(value)
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada return.")

    #RETURN_EXP_OPC -> EXPRESSION
    #RETURN_EXP_OPC -> Ɛ
    def return_exp_opc(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            value = self.expression()
            return value

    #WHILE_STMT -> while (EXPRESSION) STATEMENT
    def while_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.WHILE:
            self.coincidir(TipoToken.WHILE)
            self.coincidir(TipoToken.LEFT_PAREN)
            condition = self.expression()
            self.coincidir(TipoToken.RIGHT_PAREN)
            body = self.statement()
            stmtl = StmtLoop(condition, body)
            return stmtl
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada while.")

    #BLOCK -> {DECLARATION}
    def block(self):
        if self.preanalisis['tipo'] == TipoToken.LEFT_BRACE:
            self.coincidir(TipoToken.LEFT_BRACE)
            statementsb = []
            stmtb = StmtBlock(self.declaration(statementsb))
            print(f'Soy un block {statementsb}')
            self.coincidir(TipoToken.RIGHT_BRACE)
            return stmtb
        else:
            self.hayErrores = True
            print("Error, se esperaba el uso de las llaves.")

    #Expresiones
    #EXPRESSION -> ASSIGNMENT
    def expression(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            valor = self.assignment()
            print(f'expression {valor}')
            return valor
        else:
            self.hayErrores = True
            print("Error, se esperaba una declaracion de estado, identificador o parentesis.")

    #ASSIGNMENT -> LOGIC_OR ASSIGNMENT_OPC
    def assignment(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            name = self.logic_or()
            name = self.assignment_opc(name)
            print(f'assignment {name}')
            return name
        else:
            self.hayErrores = True
            print("Error.")

    #ASSIGNMENT_OPC -> = EXPRESSION
    #ASSIGNMENT_OPC -> Ɛ
    def assignment_opc(self, name):
        if self.preanalisis['tipo'] == TipoToken.EQUAL:
            self.coincidir(TipoToken.EQUAL)
            value = self.expression()
            exprAss = ExprAssign(name, value)
            return exprAss
        return name

    #LOGIC_OR -> LOGIC_AND LOGIC_OR_2
    def logic_or(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expr = self.logic_and()
            expr = self.logic_or_2(expr)
            print(f'logic_or {expr}')
            return expr
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #LOGIC_OR_2 -> or LOGIC_AND LOGIC_OR_2
    #LOGIC_OR_2 -> Ɛ
    def logic_or_2(self, expr):
        if self.preanalisis['tipo'] == TipoToken.OR:
            self.coincidir(TipoToken.OR)
            operador = self.previous()
            expr2 = self.logic_and()
            expl = ExprLogical(expr, operador['lexema'], expr2)
            return self.logic_or_2(expl)
        return expr

    #LOGIC_AND -> EQUALITY LOGIC_AND_2
    def logic_and(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expr = self.equality()
            expr = self.logic_and_2(expr)
            print(f'logic_and {expr}')
            return expr
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #LOGIC_AND_2 -> and EQUALITY LOGIC_AND_2
    #LOGIC_AND_2 -> Ɛ
    def logic_and_2(self, expr):
        if self.preanalisis['tipo'] == TipoToken.AND:
            self.coincidir(TipoToken.AND)
            operador = self.previous()
            expr2 = self.equality()
            expl = ExprLogical(expr, operador['lexema'], expr2)
            return self.logic_and_2(expl)
        return expr

    #EQUALITY -> COMPARISON EQUALITY_2
    def equality(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expr = self.comparison()
            expr = self.equality_2(expr)
            print(f'equality {expr}')
            return expr
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #EQUALITY_2 -> != COMPARISON EQUALITY_2
    #EQUALITY_2 -> == COMPARISON EQUALITY_2
    #EQUALITY_2 -> Ɛ
    def equality_2(self, expr):
        if self.preanalisis['tipo'] == TipoToken.BANG_EQUAL:
            self.coincidir(TipoToken.BANG_EQUAL)
            operador = self.previous()
            expr2 = self.comparison()
            expb = ExprBinary(expr, operador['lexema'], expr2)
            return self.equality_2(expb)
        elif self.preanalisis['tipo'] == TipoToken.EQUAL_EQUAL:
            self.coincidir(TipoToken.EQUAL_EQUAL)
            operador = self.previous()
            expr2 = self.comparison()
            expb = ExprBinary(expr, operador['lexema'], expr2)
            return self.equality_2(expb)
        return expr

    #COMPARISON -> TERM COMPARISON_2
    def comparison(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expr = self.term()
            expr = self.comparison_2(expr)
            print(f'comparison {expr}')
            return expr
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #COMPARISON_2 -> > TERM COMPARISON_2
    #COMPARISON_2 -> >= TERM COMPARISON_2
    #COMPARISON_2 -> < TERM COMPARISON_2
    #COMPARISON_2 -> <= TERM COMPARISON_2
    #COMPARISON_2 -> Ɛ
    def comparison_2(self, expr):
        if self.preanalisis['tipo'] == TipoToken.GREATER:
            self.coincidir(TipoToken.GREATER)
            operador = self.previous()
            expr2 = self.term()
            expb = ExprBinary(expr, operador['lexema'], expr2)
            return self.comparison_2(expb)
        elif self.preanalisis['tipo'] == TipoToken.GREATER_EQUAL:
            self.coincidir(TipoToken.GREATER_EQUAL)
            operador = self.previous()
            expr2 = self.term()
            expb = ExprBinary(expr, operador['lexema'], expr2)
            return self.comparison_2(expb)
        elif self.preanalisis['tipo'] == TipoToken.LESS:
            self.coincidir(TipoToken.LESS)
            operador = self.previous()
            expr2 = self.term()
            expb = ExprBinary(expr, operador['lexema'], expr2)
            return self.comparison_2(expb)
        elif self.preanalisis['tipo'] == TipoToken.LESS_EQUAL:
            self.coincidir(TipoToken.LESS_EQUAL)
            operador = self.previous()
            expr2 = self.term()
            expb =ExprBinary(expr, operador['lexema'], expr2)
            return self.comparison_2(expb)
        return expr

    #TERM -> FACTOR TERM_2
    def term(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expr = self.factor()
            expr = self.term_2(expr)
            print(f'term {expr}')
            return expr
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #TERM_2 -> - FACTOR TERM_2
    #TERM_2 -> + FACTOR TERM_2
    #TERM_2 -> Ɛ
    def term_2(self, expr):
        if self.preanalisis['tipo'] == TipoToken.MINUS:
            self.coincidir(TipoToken.MINUS)
            operador = self.previous()
            expr2 = self.factor()
            expb = ExprBinary(expr, operador['lexema'], expr2)
            return self.term_2(expb)
        elif self.preanalisis['tipo'] == TipoToken.PLUS:
            self.coincidir(TipoToken.PLUS)
            operador = self.previous()
            expr2 = self.factor()
            expb = ExprBinary(expr, operador['lexema'], expr2)
            return self.term_2(expb)
        return expr

    #FACTOR -> UNARY FACTOR_2
    def factor(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expr = self.unary()
            expr = self.factor_2(expr)
            print(f'factor {expr}')
            return expr
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #FACTOR_2 -> / UNARY FACTOR_2
    #FACTOR_2 -> * UNARY FACTOR_2
    #FACTOR_2 -> Ɛ
    def factor_2(self, expr):
        if self.preanalisis['tipo'] == TipoToken.SLASH:
            self.coincidir(TipoToken.SLASH)
            operador = self.previous()
            expr2 = self.unary()
            expb = ExprBinary(expr, operador['lexema'], expr2)
            return self.factor_2(expb)
        elif self.preanalisis['tipo'] == TipoToken.STAR:
            self.coincidir(TipoToken.STAR)
            operador = self.previous()
            expr2 = self.unary()
            expb = ExprBinary(expr, operador['lexema'], expr2)
            return self.factor_2(expb)
        return expr

    #UNARY -> ! UNARY
    #UNARY -> - UNARY
    #UNARY -> CALL
    def unary(self):
        if self.preanalisis['tipo'] == TipoToken.BANG:
            self.coincidir(TipoToken.BANG)
            operador = self.previous()
            expr = self.unary()
            return ExprUnary(operador['lexema'], expr)
        elif self.preanalisis['tipo'] == TipoToken.MINUS:
            self.coincidir(TipoToken.MINUS)
            operador = self.previous()
            expr = self.unary()
            return ExprUnary(operador['lexema'], expr)
        elif self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            return self.call()
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #CALL -> PRIMARY CALL_2
    def call(self):
        if self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expr = self.primary()
            expr = self.call_2(expr)
            print(f'call {expr}')
            return expr
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #CALL_2 -> (ARGUMENTS_OPC) CALL_2
    #CALL_2 -> Ɛ
    def call_2(self, expr):
        arguments = []
        if self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.coincidir(TipoToken.LEFT_PAREN)
            lstArguments = self.arguments_opc(arguments)
            self.coincidir(TipoToken.RIGHT_PAREN)
            ecf = ExprCallFunction(expr, lstArguments)
            return self.call_2(ecf)
        return expr


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
            return ExprLiteral(True)
        elif self.preanalisis['tipo'] == TipoToken.FALSE:
            self.coincidir(TipoToken.FALSE)
            return ExprLiteral(False)
        elif self.preanalisis['tipo'] == TipoToken.NULL:
            self.coincidir(TipoToken.NULL)
            return ExprLiteral(None)
        elif self.preanalisis['tipo'] == TipoToken.NUMBER:
            self.coincidir(TipoToken.NUMBER)
            numero = self.previous()
            #print(numero['valor'])
            return ExprLiteral(numero['valor'])
        elif self.preanalisis['tipo'] == TipoToken.STRING:
            self.coincidir(TipoToken.STRING)
            string = self.previous()
            #print(string['valor'])
            return ExprLiteral(string['valor'])
        elif self.preanalisis['tipo'] == TipoToken.IDENTIFIER:
            self.coincidir(TipoToken.IDENTIFIER)
            id = self.previous()
            #print(id['lexema'])
            return ExprVariable(id['lexema'])
        elif self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            self.coincidir(TipoToken.LEFT_PAREN)
            expr = self.expression()
            self.coincidir(TipoToken.RIGHT_PAREN)
            return ExprGrouping(expr)
        else:
            self.hayErrores = True
            print("Error, se esperaba una expresion de estado.")

    #Otras
    #FUNCTION -> id (PARAMETERS_OPC) BLOCK
    def function(self):
        if self.preanalisis['tipo'] == TipoToken.IDENTIFIER:
            self.coincidir(TipoToken.IDENTIFIER)
            id = self.previous()
            self.coincidir(TipoToken.LEFT_PAREN)
            parameters = []
            param = self.parameters_opc(parameters)
            #parameters.append(param)
            for i in parameters:
                print(f'Elementos param {i}')
            self.coincidir(TipoToken.RIGHT_PAREN)
            print(self.preanalisis['tipo'])
            body = self.block()
            print(body)
            stmtf = StmtFunction(id['lexema'], param, body)
            return stmtf
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
    def parameters_opc(self, parameters):
        if self.preanalisis['tipo'] == TipoToken.IDENTIFIER:
            return self.parameters(parameters)
        return parameters

    #PARAMETERS -> id PARAMETERS_2
    def parameters(self, parameters):
        if self.preanalisis['tipo'] == TipoToken.IDENTIFIER:
            self.coincidir(TipoToken.IDENTIFIER)
            id = self.previous()
            parameters.append(id['lexema'])
            parameters.extend(self.parameters_2())
        else:
            self.hayErrores = True
            print("Error, se esperaba un identificador.")

        return parameters

    #PARAMETERS_2 -> , id PARAMETERS_2
    #PARAMETERS_2 -> Ɛ
    def parameters_2(self):
        aux = []
        if self.preanalisis['tipo'] == TipoToken.COMMA:
            self.coincidir(TipoToken.COMMA)
            self.coincidir(TipoToken.IDENTIFIER)
            id2 = self.previous()
            aux.append(id2['lexema'])
            aux.extend(self.parameters_2())
            return aux

        return aux


    #ARGUMENTS_OPC -> EXPRESSION ARGUMENTS
    #ARGUMENTS_OPC -> Ɛ
    def arguments_opc(self, arguments):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expr = self.expression()
            arguments.append(expr)
            arguments.extend(self.arguments())
            return arguments
        return arguments

    #ARGUMENTS -> , EXPRESSION ARGUMENTS
    #ARGUMENTS -> Ɛ
    def arguments(self):
        aux = []
        if self.preanalisis['tipo'] == TipoToken.COMMA:
            self.coincidir(TipoToken.COMMA)
            expr = self.expression()
            aux.append(expr)
            aux.extend(self.arguments())
            return aux
        return aux

    def coincidir(self, t):
        if self.hayErrores:
            sys.exit()
        elif self.preanalisis['tipo'] == t:
            self.i = self.i + 1
            self.preanalisis = self.tokens[self.i]
        else:
            self.hayErrores = True
            print("Error.")

    def previous(self):
        j = self.i - 1
        last = self.tokens[j]

        return last










