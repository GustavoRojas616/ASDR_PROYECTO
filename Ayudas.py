class NodoAST:

  def __init__(self, tipo, valor):
    self.tipo = tipo
    self.valor = valor

  def __str__(self):
    return f"{self.tipo}({self.valor})"


def crear_ast(expresion):
  """Crea un AST para la expresión dada."""

  # Crear los nodos del AST
  nodo_suma = NodoAST("Sumar", ("x", "y"))
  nodo_x = NodoAST("Identificador", "x")
  nodo_y = NodoAST("Identificador", "y")

  # Conectar los nodos del AST
  nodo_suma.hijos = [nodo_x, nodo_y]

  # Devolver el AST
  return nodo_suma


expresion = "x + y"
ast_expresion = crear_ast(expresion)
print(ast_expresion)