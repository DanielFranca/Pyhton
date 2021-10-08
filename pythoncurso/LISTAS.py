"""
lISTAS

Listas em python funciona como vetores/matrizes em outras linguagens, com a diferença de serem dinâmico e também de
podermos colocar qualquer tipo de dado

linguagens C/JAVA: ARRAYS
  - POSSUEM TAMANHO E TIPO DE DADO FIXO;
  OU SEJA, NESTAS LINGUAGENS SE VOCÊ CRIAR UM ARRAY DE TIPO INT E COM TAMANHO 5,
  ESTE ARRAY SERÁ SEMPRE DO TIPO INTEIRO E PODERÁ TER SEMPRE NO MÁXIMO 5 VALORES.

 JÁ EM PYTHON

- DINÂMICO: NÃO POSSUI TAMANHO FIXO; OU SEJA, podemos criar a lista e simplesmente ir adicionando elementos:
- Qualquer tipo de dado: não possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

# import list1 as list1

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 37]

lista2 = ['D', 'a', 'n', 'i', 'e', 'l', '', 'F', 'r', 'a', 'n', 'ç', 'a']

lista3 = []

lista4 = list(range(11))

lista5 = list('Daniel França')




"""
""" 

# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'encontrei o {num}')
else:
    print(f'Não encontrei o {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrência de um valor em uma lista
print(lista1.count(11))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar valores ou elementos em listas, utilizamos a função APPEN


print(lista1)
lista1.append(42)
print(lista1)

#OBS: Com append, nós só conseguimos adicionar 1 elemento por vez

# lista1.append(12, 34, 56) #ERRO

lista1.append([8, 3, 11]) #coloca a lista como elemento único
print(lista1)

if [8, 3, 1] in lista1:
    print('encontramos a lista')
else:
    print('não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional á lista
print(lista1)

Podemos inserir um novo elemento na lista indicando a posição do índice
# OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista 

lista1.insert[2, 'Novo Valor']
print(lista1)

#Podemos facilmente juntar duas listas

lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

#Podemos facilmente inverter uma lista

#lista1.reverse()
#lista2.reverse()

print(lista1) #Forma1
print(lista2)

print(lista1(::-1)) #Forma2 com string
print(lista2(::-2))

#Ambos imprimem a mesma coisa

#Copiar uma lista

lista6 = lista2.copy()
print(lista6)

#Podemos contar quantos elementos existem dentro da lista 
print((len(lista5)))

#Podemos remover um elemento pelo índice
# OBS: Os elementos a direita deste índice serão deslocados para a esquerda
#Se não houver elemento no índice informado teremos o erro indexerror
lista5.pop(2)
print(lista5)

#Podemos remover todos os elementos (zerar a lista)

print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova =  [1, 2, 3]
print(nova) 
nova = nova * 3
print(nova)

#Podemos converter uma string para uma lista
#Exemplo1

curso =  'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: por padrão o split separa ps elementos da listas pelo espaço entre elas

#Exemplo 2

curso = 'programação.em.python:, Essencial'
print(curso)
curso = curso.split(',')
print(curso)

#Convertendo uma lista em uma string

lista6 = ['programa', 'em', 'python', 'essencial']
print(lista6)

#Abaixo estamos falando: Pega a lista, coloca espaço entre cada elemento e transforma em uma string
curso = ' '. join(lista6)
print(curso)

#Abaixo estamos falando: Pega a lista, coloca espaço entre cada elemento e transforma em uma string
curso = '$'. join(lista6)
print(curso)

#Podemos realmente colocar qualquer tipo de dado em uma lisra, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]
print(lista6)
print(type(lista6))

#Iterando sobre listas

#Exemplo 1 Utilizando for

for elemento in lista1:
    print(elemento)

#Exemplo 2 Utilizando for

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

#Exemplo 3 - Utilizando While

carrinho = []
produto = ''

while produto != 'sair':
    print("adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
    
#Utilizando variavel em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

#Utilizando variavel em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5


# Fazemos acesso aos documentos de forma indexada

#           0         1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pensar na lista como um circulo, onde
# o final de um elemento está ligado ao início da lista.
print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
#print(cores[-5]) erro, pois não existe índice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
    
# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)
    
# LISTAS ACEITAM VALORES REPETIDOS
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)


# Outros métodos úteis

#Encontrar um índice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

# Em qual índice esta o valor 67
print(numeros.indice(6))

# Em qual índice da lista está o valor 97
print(numeros.index(9))

# print(numeros.index(19)) # Gera valueError

# OBS: Caso não tenha este elemento na lista, será apresentado erro

# OBS: Retorna o índice do primeiro elemento encontrado
print(numeros.indice(5)) # Retorna o índice do primeiro valor encontrado

# Podemos fazer busca dentro de um range, ou seja, qual índice começar e começar a buscar
print(numero.index[5, 1]) # buscando a partir do indice 1
print(numero.index[5, 2]) # buscando a partir do indice 2
print(numero.index[5, 3]) # buscando a partir do indice 3
print(numero.index[5, 4]) # buscando a partir do indice 4
#OBS: Caso não tenha este elemento na lista, será apresentado erro

# Podemos fazer busca dentro de um range, inicio/fim
print(numero.index(8, 3, 6)) #  Buscar o índice do valor 8, entre os índices 3 a 6

 Revisão de string

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

#TRABALHANDO COM SLICE DE LISTA COM O PARÂMETRO 'INICIO'

lista = [1, 2, 3, 4]

print(lista[::1]) # Iniciando no indice e pegando todos os elementos restantes

#TRABALHANDO COM SLICE DE LISTA COM O PARÂMETRO 'fim'

print(lista[:2]) # Começa em 8, pega até o índice 2 - 1

print(lista[:4]) # Começa em 8, pega até o indice 4 - 1

print(lista[1:3]) # Começa em 1, pega até o indice 3 - 1

# Trabalhando com Slice de lista com o parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2

print(lista[::2]) # Começa em 8, vai até, de 2 em 2


# Invertendo valores em uma lista

nomes = ['Daniel', 'França']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Daniel', 'França']

nomes.reverse()
print(nomes)

# Soma, Valor máximo, Valor mínimo, tamanho de uma lista

# Se os valores forem todos inteiros ou reais.

lista =  [1, 2, 3, 4, 5, 6]

print(sum(lista)) #soma
print(max(lista)) #máximo valor
print(min(lista)) #mínimo valor
print(len(lista)) #tamanho da lista

# Transforma uma lista em tupla

lista =  [1, 2, 3, 4, 5, 6,]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#Desempacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

#OBS: Se tivermos mais elementos para desempacotar do que variáveis para receber os valores, teremos valueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

#Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiando os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# E é chamado de Deep Copy (cópia profunda)

#Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista #cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

#Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista
#mas após realizae modificação de uma das listas, essa modificação se refletiu em ambas as listas.
#Isso em python é chamado de Shallow Copy.

"""




