class Nodo:
    def __init__(self, valor=None, hijos=None):
        self.valor = valor
        self.hijos = hijos if hijos is not None else []

def construir_ast(entrada):
    tokens = entrada.split()
    indice = 0

    def expresion():
        nonlocal indice
        nodo_termino = termino()
        nodos_adicionales = []

        while indice < len(tokens) and tokens[indice] in {'+', '-'}:
            operador = tokens[indice]
            indice += 1
            nodo_siguiente_termino = termino()
            nodos_adicionales.append(Nodo(operador, [nodo_termino, nodo_siguiente_termino]))

        return Nodo('expresion', [nodo_termino] + nodos_adicionales)

    def termino():
        nonlocal indice
        nodo_factor = factor()
        nodos_adicionales = []

        while indice < len(tokens) and tokens[indice] in {'*', '/'}:
            operador = tokens[indice]
            indice += 1
            nodo_siguiente_factor = factor()
            nodos_adicionales.append(Nodo(operador, [nodo_factor, nodo_siguiente_factor]))

        return Nodo('termino', [nodo_factor] + nodos_adicionales)

    def factor():
        nonlocal indice

        if tokens[indice].isdigit():
            nodo = Nodo('entero', [Nodo(tokens[indice])])
            indice += 1
            return nodo
        elif tokens[indice] == '(':
            indice += 1
            nodo_expresion = expresion()
            if tokens[indice] == ')':
                indice += 1
                return Nodo('factor', [Nodo('('), nodo_expresion, Nodo(')')])
            else:
                raise SyntaxError('Se esperaba ")"')
        else:
            raise SyntaxError('Factor no reconocido')

    return expresion()

# Ejemplo de uso
entrada = "3 + 5 * (2 - 8)"
ast = construir_ast(entrada)

# Función para imprimir el AST de manera más legible
def imprimir_ast(nodo, indent=0):
    print("  " * indent + str(nodo.valor))
    for hijo in nodo.hijos:
        imprimir_ast(hijo, indent + 1)

print("AST:")
imprimir_ast(ast)