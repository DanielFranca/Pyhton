"""

Loop For

loop - Estrutura de repetição
For - Uma dessas estruturas

C OU JAVA

for(int 1 = 0: 1 < 10; i++){
    // execução do loop
}

Python


for item in interavel:
    //execução do loop


Utilizamos LOOPS para iterar sobre sequência ou sobre valores iteráveis

Exemplos de iteráveis:

String
   nome = 'Daniel França'

Lista
   lista = [1, 3, 5, 7, 9]

Rango
   numeros = rango(1, 18)


"""
""" 
nome = 'daniel frança varias coisas aleatorias'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar em uma lista

#Exemplo de for 1 iterando sobre uma STRING
for letra in nome:
    print(letra)

#Exemplo de for 2 iterando sobre uma LISTA

for numero in lista:
    print(numero)

#Exemplo de for 3 iterando sobre um RANGE
"""
"""
RANGE (valor_inicial, valor_final)

OBS: o valor final não é inclusive
1
2
3
4
5
6
7
8
9
10 - Não

Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)


for numero in range(1,10):
    print(numero)
    
for indice,letra in enumerate(nome):
    print(nome[indice])
    
for _, letra in enumerate(nome):
    print(letra)
    
OBS: QUANDO NÃO PRECISAMOS DE UM VALOR, PODEMOS DESCARTA-LO UTILIZANDO UNDERLINE (_)

nome = 'Daniel França'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

nome = 'daniel frança varias coisas aleatorias'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar em uma lista

nome = 'Daniel França'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input("quantas vezes esse laço deve"))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Daniel França'
for letra in nome:
    print(letra, end='')
    
Tabela de emojis unicode

"""
#ORIGINAL: U+1F60D
# Modificado: U0001F60D

for  _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)









