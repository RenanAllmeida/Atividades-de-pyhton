from itertools import permutations

def lin():
    print('=' * 30)

print('===Respotas da lista===')

#1

def soma(a, b = 2):
    return a + b

print(soma(3))

lin()

#2

def a(x):
    return x + 2
def b(x):
    return x * 3

print(b(a(1)))

lin()

#3

def pares(n):
    lista = []
    for i in range(n):
        if i % 2 == 0:
            lista.append(i)
    return lista

lin()

#4

def iniciais(nomes):
    lista = []
    for i in nomes:
        lista.append(i[0])
    return lista

nomes = ['Radja', 'Renan', 'Tiago', 'Lucas', 'Pedro']
print(iniciais(nomes))

lin()

#5

def soma_elementos(l1, l2):
    lista = []
    tamanho = min(len(l1), len(l2))
    for i in range(tamanho):
        lista.append(l1[i] + l2[i])
    return lista

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6]
print(soma_elementos(lista1, lista2))

lin()

#6

def intercalar(l1, l2):
    lista = []
    tamanho = min(len(l1), len(l2))
    for i in range(tamanho):
        lista.append(l1[i])
        lista.append(l2[i])
    lista.extend(l1[tamanho:])
    lista.extend(l2[tamanho:])
    return lista

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 7, 8]
print(intercalar(lista1, lista2))

lin()

#7 

def comuns(l1, l2):
    lista = []
    for i in l1:
        for j in l2:
            if i == j:
                lista.append(i)
    return lista

lista1 = [1, 1, 3, 2, 3, 4, 5, 6]
lista2 = [1, 7, 9, 10, 3, 6, 12]
print(comuns(lista1, lista2))

# ou tu faz assim:

def comuns2(l1, l2):
    lista = []
    for i in l1:
        if i in l2 and i not in lista:
            lista.append(i)
    return lista

lista1 = [1, 1, 3, 2, 3, 4, 5, 6]
lista2 = [1, 7, 9, 10, 3, 6, 12]
print(comuns2(lista1, lista2))

lin()

#8

def diferenca(l1, l2):
    lista = []
    for i in l1:
        if i not in l2 and i not in lista:
            lista.append(i)
    return lista

lista1 = [1, 1, 3, 2, 3, 4, 5, 6]
lista2 = [1, 7, 9, 10, 3, 6, 12]
print(diferenca(lista1, lista2))

lin()

#9

def comparar_tamanhos(l1, l2):
    if len(l1) > len(l2):
        print('A primeira lista é maior!')
    elif len(l1) == len(l2):
        print('As duas listas possuem a mesma quantidade de elementos!')
    else:
        print('A segunda lista é maior!')

lista1 = [1, 1, 3, 2, 3, 4, 5, 6]
lista2 = [1, 7, 9, 10, 3, 6, 12]
comparar_tamanhos(lista1, lista2)

lin()

#10

def ordenar_palavras(lista):
    lista.sort(key = len)
    return lista

lista = ["casa", "carro", "sol", "lua", "bicicleta", "barco", "rio"]
print(ordenar_palavras(lista))

lin()

#11

def todas_permutacoes(lista):
    return list(permutations(lista))

#12

usuarios = []

def validar_idade(idade):
    if idade >= 0 and idade <= 150:
        return True
    else:
        return False

def validar_nome(nome):
    if type(nome) != str:
        return False
    contador = 0
    for letra in nome:
        if letra != ' ':
            if (letra >= 'a' and letra <= 'z') or (letra >= 'A' and letra <= 'Z'):
                contador += 1
            else:
                return False
    if contador < 3:
        return False
    return True

def registrar_usuario(nome, idade):
    usuario = {}
    if validar_nome(nome):
        usuario['nome'] = nome
    else:
        return 'Nome inválido!'
    if validar_idade(idade):
        usuario['idade'] = idade
    else:
        return 'Idade inválida!'
    usuarios.append(usuario)
    return 'Usuario cadastrado com sucesso!'


def mostrar_usuarios():
    print('Usuarios cadastrados:')
    for usuario in (usuarios):
        print(f"Nome: {usuario['nome']}, idade: {usuario['idade']}")

def remover_usuario(nome, idade):
    for i, usuario in enumerate(usuarios):
        if usuario['nome'] == nome and usuario['idade'] == idade:
            del usuarios[i]
            return True
    return False


nome = 'Renan'
idade = 23
print(registrar_usuario(nome, idade))
mostrar_usuarios()
remover_usuario(nome, idade)
mostrar_usuarios()

lin()

#13
def ponto_mais_distante(lista_pontos):
    ponto_inicial = lista_pontos[0]
    maior_distancia = 0
    ponto_distante = 0
    for ponto in lista_pontos:
        d = distancia(ponto_inicial, ponto)
        if d > maior_distancia:
            maior_distancia = d
            ponto_distante = ponto
    return ponto_distante

lin()

#14

def inverter_string(string):
    if len(string) == 0:
        return ''
    return inverter_string(string[1:]) + string[0]

print(inverter_string('Renan'))

lin()

#15
def palindromo(texto):
    if len(texto) <= 1:
        return 'É palindromo'
    if texto[0] != texto[-1]:
        return 'Num é palindromo n'
    return palindromo(texto[1:-1])

texto = 'ioiooi'
print(palindromo(texto))

lin()

#16

def buscar(lista, valor, i = 0):
    if i == len(lista):
        return 'Não achei o valor informado'
    if lista[i] == valor:
        return f'achei o {valor} na posição {i + 1}'
    return buscar(lista, valor, i + 1)

lista = [0, 1, 2, 3, 4, 5, 6, 7]
print(buscar(lista, 9))

lin()

#17

def flatten(lista_aninhada):
    if len(lista_aninhada) == 0:
        return []
    primeiro = lista_aninhada[0]
    resto = lista_aninhada[1:]
    return primeiro + flatten(resto)

lista_de_listas = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    [True, False]
]

print(flatten(lista_de_listas))

lin()

#18

def multiplicar_listas(l1, l2, i = 0):
    tamanho = min(len(l1), len(l2))
    if i == tamanho:
        return []
    return [l1[i] * l2[i]] + multiplicar_listas(l1, l2, i + 1)

lista1 = [2, 3, 4]
lista2 = [2, 3, 5]
print(multiplicar_listas(lista1, lista2))