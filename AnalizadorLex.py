#Practica1 COMPILADORES 5CM2; Arreola Rojas Gustavo Adolfo; Ramirez Ayala Erandi
import os
import sys
from ASDR import *


lista_tokens=[]
def main():
    if len(sys.argv) > 2:
        print("Uso correcto: python Practica1.py nombre_archivo.txt")
        sys.exit(64)
    elif len(sys.argv) == 2:
        ejecutar_archivo(sys.argv[1])
    else:
        ejecutar_prompt()

def ejecutar_archivo(nombre_archivo):
    global lista_tokens
    if os.path.isfile(nombre_archivo):
        entrada = open(nombre_archivo)
        entrada = ''.join(entrada)
        tokens = list(entrada)
        b = tokens
        while len(b) > 0:
            # print(len(b))
            if str(b[0]) in simbolos_key or str(b[0]).isdigit() == True or str(b[0]).isalpha() == True or str(b[0]) == '\n' or str(b[0]) == ' ' or str(b[0]) == '"':
                aux = 0
                pass
            else:
                aux = 1
                print("Error léxico.")
                print("No se realizará el análisis sintáctico.")
                lista_tokens = []
                break
                if len(b) == 1:
                    # print("Hola")
                    break
                elif len(b) > 1:
                    # print(len(b))
                    b.pop(0)
                    # print(len(b))
                    # print(len(b))
                    pass
            if str(b[0]).isalpha() == True:
                b = automataRESIDEN(tokens)
            elif str(b[0]).isspace() == True:
                if len(b) == 1:
                    break
                else:
                    b.pop(0)
                    if str(b[0]).isalpha() == True:
                        b = automataRESIDEN(tokens)
            elif str(b[0]) == '"':
                b = automataCAD(tokens)
                # print(b)
                # elif str(b[0]).isspace()==False and str(b[0])
            elif str(b[0]).isdigit() == False and str(b[0]).isalpha() == False and aux == 0:
                if len(b) == 1:
                    b = automata1CARAC(tokens)
                else:
                    if (str(b[0]) == '/' and str(b[1]) == '/') or (str(b[0]) == '/' and str(b[1]) == '*'):
                        a, b = automataCOMEN(tokens)
                        if a == 0:
                            b = automata1CARAC(tokens)
                    else:
                        b = automata1CARAC(tokens)
            elif str(b[0]).isdigit() == True:
                b = automataNUM(tokens)
        if len(lista_tokens) > 0:
            nid = {'tipo': 'EOF', 'lexema': '', 'valor': 'null'}
            lista_tokens.append(nid)
            print("Tokens registrados:", lista_tokens)
            analizador = ASDR(lista_tokens)
            analizador.parse()

    else:
        print("El archivo no existe.")

def ejecutar_prompt():
    global lista_tokens
    while True:
        a = 1
        lista_tokens = []
        entrada = input(">>> ")
        tokens = list(entrada)
        b = tokens
        while len(b) > 0:
            # print(len(b))
            if str(b[0]) in simbolos_key or str(b[0]).isdigit() == True or str(b[0]).isalpha() == True or str(b[0]) == '\n' or str(b[0]) == ' ' or str(b[0]) == '"':
                aux = 0
                pass
            else:
                aux = 1
                print("Error léxico.")
                print("No se realizará el análisis sintáctico.")
                lista_tokens = []
                break
                if len(b) == 1:
                    # print("Hola")
                    break
                elif len(b) > 1:
                    # print(len(b))
                    b.pop(0)
                    # print(len(b))
                    # print(len(b))
                    pass
            if str(b[0]).isalpha() == True:
                b = automataRESIDEN(tokens)
            elif str(b[0]).isspace() == True:
                if len(b) == 1:
                    break
                else:
                    b.pop(0)
                    if str(b[0]).isalpha() == True:
                        b = automataRESIDEN(tokens)
            elif str(b[0]) == '"':
                b = automataCAD(tokens)
                # print(b)
                # elif str(b[0]).isspace()==False and str(b[0])
            elif str(b[0]).isdigit() == False and str(b[0]).isalpha() == False and aux == 0:
                if len(b) == 1:
                    b = automata1CARAC(tokens)
                else:
                    if (str(b[0]) == '/' and str(b[1]) == '/') or (str(b[0]) == '/' and str(b[1]) == '*'):
                        a, b = automataCOMEN(tokens)
                        if a == 0:
                            b = automata1CARAC(tokens)
                    else:
                        b = automata1CARAC(tokens)
            elif str(b[0]).isdigit() == True:
                b = automataNUM(tokens)


        if len(lista_tokens) > 0:
            nid = {'tipo': 'EOF', 'lexema': '', 'valor': 'null'}
            lista_tokens.append(nid)
            print("Tokens registrados:", lista_tokens)
            analizador = ASDR(lista_tokens)
            analizador.parse()
        
def automataNUM(lista):
    global lista_tokens
    state=0
    if '\n' in lista:
        pass
    else:
        lista.append("\n")
    tama = len(lista)
    #print(lista)
    for i in range(tama):
        if state==0:
            id=str(lista[i])
            #print(lista[i])
            if str(lista[i]).isnumeric()==True:
                state = 15
                #print("15")
                continue
        if state==15:
            #print(lista[i])
            id=id+str(lista[i])
            if str(lista[i]).isnumeric() == True:
                state = 15
                continue
            elif str(lista[i])=='.':
                state = 16
                continue
            elif str(lista[i])=='E':
                state=18
                continue
            #elif str(lista[i]).isalpha()==True:
            #    state=-1
            #    continue
            else:
                state=22
                #print(id)
                #print("Aceptación")
        if state==16:
            #print(lista[i])
            id = id + str(lista[i])
            if str(lista[i]).isnumeric() == True:
                state = 17
                continue
        if state==17:
            id = id + str(lista[i])
            if str(lista[i]).isnumeric() == True:
                state = 17
                continue
            elif str(lista[i])=='E':
                state=18
                continue
            #elif str(lista[i])=='.':
            #    state=-1
            #    continue
            else:
                state=23
                #print(id)
                #print("Aceptación")
        if state==18:
            id = id + str(lista[i])
            if str(lista[i])=='+' or str(lista[i])=='-':
                state=19
                continue
            elif str(lista[i]).isnumeric() == True:
                state=20
                continue
        if state==19:
            id = id + str(lista[i])
            if str(lista[i]).isnumeric() == True:
                state=20
                continue
        if state==20:
            id = id + str(lista[i])
            if str(lista[i]).isnumeric() == True:
                state=20
                continue
            #elif str(lista[i])=='.':
            #    state=-1
            #    continue
            else:
                state=21
                #print(id)
                #print("Aceptación")
        if state==-1:
            if str(lista[i]).isdigit()==True or str(lista[i])=='.' or str(lista[i])=='E' :
                id = id + str(lista[i])
                continue
            else:
                break
            #print("Error")

    if state==21 or state==22 or state==23:
        id = list(id)
        id.pop(-1)
        ite = len(id)
        for i in range(ite):
            lista.remove(id[i])
        if '.' in id:
            z = 0
        elif 'E' in id:
            z = 1
        else:
            z = 2
        id = ''.join(id)
        if z == 0:
            # y = ''.join(filter(lambda x: x.isdigit() or x in ['-', '+'], id))
            y = float(id)
        elif z == 1:
            y = ''.join(filter(lambda x: x.isdigit() or x in ['-', '+'], id))
            y = float(id)
        elif z == 2:
            y = int(id)
        print("<NUMBER " + str(id) + " " + str(y) + ">")
        nid = {'tipo': 'NUMBER', 'lexema': str(id), 'valor': y}
        lista_tokens.append(nid)
        return lista
    else:
        print("Número inválido.")
        #lista_tokens = []
        id = list(id)
        ite = len(id)
        for i in range(ite):
            lista.remove(id[i])
        return lista



def automataCOMEN(lista):
    global lista_tokens
    if '\n' in lista:
        pass
    else:
        lista.append("\n")
    tama=len(lista)
    #print(lista, tama)
    state=0
    for i in range(tama):
        if state==0:
            if lista[i]=='/':
                state=26
                id = str(lista[i])
                #print("26")
                continue
        if state==26:
            if lista[i]=='*':
                state=27
                #print("27")
                id = id + str(lista[i])
                continue
            elif lista[i]=='/':
                state=30
                id = id + str(lista[i])
                continue
            else:
                state=32
                return 0, lista
        if state==27:
            if lista[i]=='*':
                state=28
                id = id + str(lista[i])
                continue
            else:
                state=27
                #print("Estoy aqui")
                id = id + str(lista[i])
                continue
        if state==28:
            if lista[i]=='*':
                state=28
                id = id + str(lista[i])
                continue
            if lista[i]=='/':
                state=29
                id = id + str(lista[i])
                #print("Comentario multilinea")
            else:
                state=27
                id = id + str(lista[i])
                continue
        if state==30:
            if lista[i]=='\n':
                state=31
                id = id + str(lista[i])
                #print("Comentario unilinea")
            else:
                state=30
                id = id + str(lista[i])
                continue
    #print(state)
    if state==29 or state==31 or state==32:
        id = list(id)
        #print(id)
        ite = len(id)
        for i in range(ite):
            lista.remove(id[i])
        return 1, lista
    else:
        print("Error. Comentario multilínea sin cerrar.")
        print("No se realizará el análisis sintáctico.")
        lista_tokens = []
        id = list(id)
        # print(id)
        ite = len(id)
        for i in range(ite):
            lista.remove(id[i])
        return 1, lista

def automataM1CARAC(id, lista):
    tama=len(lista)
    for token in [id]:
        if token in simbolos_key:
            print("<" + simbolos[token] + " " + str(id) + " null>")
            nid = {'tipo': simbolos[token], 'lexema': str(id), 'valor': 'null'}
            lista_tokens.append(nid)
            id = list(id)
            ite = len(id)
            for i in range(ite):
                lista.remove(id[i])
            return lista
        else:
            return 0

def automata1CARAC(lista):
    tama=len(lista)
    state=0
    id=''
    aux=0
    cond=1
    c=0
    #print(lista)
    for i in range(tama):
        if state==0 and str(lista[i]).isdigit()==False and str(lista[i]).isalpha()==False:
            state=1
            id=id + str(lista[i])
            #print(id)
        if i>0 and state==1 and (str(lista[i]).isdigit()==False and str(lista[i]).isalpha()==False):
            state=2
            aux=0
            id = id + str(lista[i])
            aux=automataM1CARAC(id, lista)
            #print(aux)
            if aux!=0:
                return aux
            else:
                id=list(id)
                id.pop(-1)
                id=''.join(id)
                #print(id)
                c=1
                cond=0

        if i==tama-1:
            #id = id + str(lista[i])
            #print(id)
            for token in [id]:
                if token in simbolos_key:
                    print("<" + simbolos[token] + " " + str(id) + " null>")
                    nid = {'tipo': simbolos[token], 'lexema': str(id), 'valor': 'null'}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    #print(lista)
                    return lista
        if str(lista[i]).isalpha()==True:
            for token in [id]:
                if token in simbolos_key:
                    print("<" + simbolos[token] + " " + str(id) + " null>")
                    nid = {'tipo': simbolos[token], 'lexema': str(id), 'valor': 'null'}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                        #print(lista)
                    return lista
        if cond==0 and str(lista[i-c]).isalpha() == False:
            for token in [id]:
                if token in simbolos_key:
                    print("<" + simbolos[token] + " " + str(id) + " null>")
                    nid = {'tipo': simbolos[token], 'lexema': str(id), 'valor': 'null'}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                        #print(lista)
                    return lista

        

def automataCAD(lista):
    global lista_tokens
    tama=len(lista)
    state=0
    #print(lista)
    for i in range(tama):
        if i==tama-1 and state==0 and str(lista[i])=='"':
            print("Error. Cadena inválida.")
            print("No se realizará el análisis sintáctico.")
            lista_tokens = []
            id=list(lista)
            ite = len(lista)
            for i in range(ite):
                lista.remove(id[i])
                #print(lista)
            return lista
        elif state==0 and str(lista[i])=='"':
            id = str(lista[i])
            state=24
        if i>0 and state==24:
            id = id + str(lista[i])
            state=24
        if i>0 and state==24 and str(lista[i])=='"':
            prov=id.replace('"', '')
            print("<STRING " +id + " " + prov +">")
            nid={'tipo':'STRING', 'lexema': id, 'valor': prov}
            lista_tokens.append(nid)
            id=list(id)
            #print(id)
            ite = len(id)
            for i in range(ite):
                lista.remove(id[i])
                #print(lista)
            return lista
        elif i>0 and state==24 and str(lista[i])=='\n':
            print("Error. Cadena inválida.")
            print("No se realizará el análisis sintáctico.")
            lista_tokens = []
            id = list(lista)
            ite = len(lista)
            for i in range(ite):
                lista.remove(id[i])
                # print(lista)
            return lista
        if i==tama-1 and str(lista[i])!='"':
            print("Error. Cadena inválida.")
            print("No se realizará el análisis sintáctico.")
            lista_tokens = []
            id=list(id)
            ite = len(id)
            for i in range(ite):
                lista.remove(id[i])
                #print(lista)
            return lista
        i=i+1

def automataRESIDEN(lista):
    tama=len(lista)
    state=0
    #print(lista)
    for i in range(tama):
        if state==0 and (str(lista[i]).isalpha()==True):
            #print(lista[i])
            id = str(lista[i])
            state = 13

        if i>0 and state==13 and (str(lista[i]).isalpha()==True or str(lista[i]).isdigit()==True) :
            #print(lista[i])
            id = id + str(lista[i])

        if i>0 and state==13 and str(lista[i]).isalpha()==False and str(lista[i]).isdigit()==False:
            state=14
            id = id + str(lista[i])
            id=list(id)
            id.pop(-1)
            id=''.join(id)

            for token in [id]:
                if token in reservadas_key:
                    print("<" + reservadas[token] + " " + str(id) + " null>")
                    nid = {'tipo': reservadas[token], 'lexema': str(id), 'valor': 'null'}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    return lista
                else:
                    print("<IDENTIFIER " +id + " null>")
                    nid = {'tipo': 'IDENTIFIER', 'lexema': id, 'valor': 'null'}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    return lista

        if i==tama-1:
            for token in [id]:
                if token in reservadas_key:
                    print("<" + reservadas[token] + " " + str(id) + " null>")
                    nid = {'tipo': reservadas[token], 'lexema': str(id), 'valor': 'null'}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    return lista
                else:
                    print("<IDENTIFIER " + id + " null>")
                    nid = {'tipo': 'IDENTIFIER', 'lexema': id, 'valor': 'null'}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    return lista

        i = i + 1


simbolos = {'<': 'LESS', '<=': 'LESS_EQUAL', '>': 'GREATER', '>=': 'GREATER_EQUAL', '!': 'BANG', '!=': 'BANG_EQUAL',
            '=': 'EQUAL', '==': 'EQUAL_EQUAL', '+': 'PLUS', '-': 'MINUS', '*': 'STAR', '/': 'SLASH', '{': 'LEFT_BRACE',
            '}': 'RIGHT_BRACE', '(': 'LEFT_PAREN', ')': 'RIGHT_PAREN', ',': 'COMMA', '.': 'DOT', ';': 'SEMICOLON'}
simbolos_key = simbolos.keys()
reservadas = {'and': 'AND', 'else': 'ELSE', 'false': 'FALSE', 'for': 'FOR', 'fun': 'FUN', 'if': 'IF', 'null': 'NULL',
              'or': 'OR', 'print': 'PRINT', 'return': 'RETURN', 'true': 'TRUE', 'var': 'VAR', 'while': 'WHILE'}
reservadas_key = reservadas.keys()

main()
