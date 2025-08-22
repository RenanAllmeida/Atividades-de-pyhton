def lin():
    print('=' * 30)

#1
def fatorial(x):
    if x < 0:
        return ("numero invalido")
    fat = 1
    for i in range(x):
        fat *= i + 1
        print(fat)
    return fat

numero = -5
print(fatorial(numero))

lin()

#2
def fatorial_2 (N):
    if N == 1 or N == 0:
        return 1
    else:
        return N * fatorial_2(N - 1)

numero = 5
fat = fatorial_2(numero)
print(fat)

lin()

#3
def contagem_regressiva(n):
    if n == 0:
        print(n)
        return 0
    else:
        print(n, end = ', ')
    if n > 0:
        contagem_regressiva(n - 1)
    elif n < 0:
        contagem_regressiva(n + 1)

contagem_regressiva(-10)

lin()

#4
def contagem(n):
    if n <= 0:
        print('aqui parei')
        return 0
    novo_numero = int(input('esse n vale, joga outro aí: '))
    contagem(novo_numero)
    
numero = 0
contagem(numero)

lin()

#5
def apresentar(texto):
    print(f'Muito prazer, {texto}!')

nome = 'Renan'
apresentar(nome)

#6
def dobro(x):
    print(f'O dobro do seu numero é: {x + x}!')

numero = 10
dobro(numero)

lin()

#7
def repetir_msg(texto, n):
    while n != 0:
        print(texto)
        n -= 1

mensagem = 'unhe unhe'
repeticoes = 2
repetir_msg(mensagem, repeticoes)

lin()

#8
def tabuada(x):
    print(f'A tabuada de {x} de 1 a 10 é: ')
    i = 1
    while i <= 10:
        print(f'{x} x {i} = {x * i}')
        i += 1

numero = 3
tabuada(numero)

lin()

#9
def quadrado(x):
    return x * x

numero = 5
print(f'O quadrado de {numero} é {quadrado(numero)}')

lin()

#10
def area(L, C):
    area = L * C
    print('   CONTROLE DE TERRENOS   ')
    print('-' * 30)
    print('largura (m): '.upper(), L)
    print('comprimento (m): '.upper(), C)
    print(f'A área de um terreno de {L}x{C} é de {area}m².')

largura = float(4.5)
comprimento = float(8)
area(largura, comprimento)

lin()

#11
def media(list):
    valores = 0
    for num in list:
        valores += num
    media = valores / len(list)
    print(f'A média dos {len(list)} valores digitados é: {media:.2f}')

valores = [1, 2, 3, 4, 5]
media(valores)

lin()

#12
def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(eh_par(10))

lin()

#13

def soma_lista(lista):
    soma_lista = 0
    for x in lista:
        soma_lista += x
    return soma_lista

print(soma_lista(lista = [1, 2, 3, 4, 5]))

lin()

#14
def maior_valor(lista):
    maior = 0
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior

lista = [1, 2, 3, 4, 19, 5, 16]
print(f'O maior valor dessa lista é: {maior_valor(lista)}')

lin()

#15
def quantos_pares(lista):
    pares = 0
    for valor in lista:
        if valor % 2 == 0:
            pares += 1
    print(pares)

lista = []
for x in range(11):
    lista.append(x)
quantos_pares(lista)

lin()

#16
def negativos_para_0 (lista):
    nova_lista = []
    for valor in lista:
        if valor <= 0:
            nova_lista.append(0)
        else:
            nova_lista.append(valor)
    print(nova_lista)

lista = [-1, -2, -17, 0, 1, 2, 4]
negativos_para_0(lista)

lin()

#17
def multiplicar_lista(lista, n):
    resultados = []
    for valor in lista:
        resultados.append(valor * n)
    return resultados

lista = []
for x in range(1, 11):
    lista.append(x)
n = 3
print(lista)
print(multiplicar_lista(lista, n))

lin()

#18
def enumerar_lista(lista):
    for indice, x in enumerate(lista):
        print(f'{indice}:{x}')

lista = []
for x in range(4, 13):
    lista.append(x)
enumerar_lista(lista)

lin()

#19
def imprimir_invertido(lista):
    invertida = lista[::-1]
    print(invertida)

lista = ['Ana', 'Maria', 'Joana', 'Sofia', 'Radja']
imprimir_invertido(lista)

lin()

#20
def pares_recursao(lista, i = 0):
    if i == len(lista):
        return 0
    if lista[i] % 2 == 0:
        return 1 + pares_recursao(lista, i + 1)
    else:
        return pares_recursao(lista, i + 1)

lista = []
for x in range(1, 12):
    lista.append(x)
print(pares_recursao(lista))

lin()

#21
def maior_valor(lista, i = 0):
    if i == len(lista) - 1:
        return lista[i]
    maior = maior_valor(lista, i + 1)
    if lista[i] > maior:
        return lista[i]
    else:
        return maior
    
lista = [1, 10, 2, 8, 25, 3]
print(maior_valor(lista))

lin()

#22

def contar_repeticoes(lista, elemento, i = 0):
    if i == len(lista):
        return 0
    if lista[i] == elemento:
        return 1 + contar_repeticoes(lista, elemento, i + 1)
    else:
        return contar_repeticoes(lista, elemento, i + 1)
    
lista = [1, 1, 2, 4, 1, 5, 1, 2, 4, 6]
numero = 1
print(contar_repeticoes(lista, numero))

lin()

#23

def remover_negativos(lista, i = 0):
    if i == len(lista):
        return lista
    if lista[i] < 0:
        lista.pop(i)
        return remover_negativos(lista, i)
    else:
        return remover_negativos(lista, i + 1)
    
lista = [-1, -2, -3, 0, 1, 2, 3]
print(remover_negativos(lista))

lin()

#24

def inverter_lista(lista):
    if len(lista) == 0:
        return []
    return inverter_lista(lista[1:]) + [lista[0]]

lista = [10, 20, 34]
print(inverter_lista(lista))

lin()