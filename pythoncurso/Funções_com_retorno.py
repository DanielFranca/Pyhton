"""

Funções com  retorno


numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Em pyhton, quando uma função não retorna nenhum valor, o retorno é NONE

Exemplo de função com retorno

def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()

print(f'Retorno {ret}')

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra
reservada return

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()

print(f'Retorno {ret}')

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de sua função
Podemos passar a execução da função para outras funções



def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7()}')



# Refatorando a primeira função

def diz_oi():
    return 'oi'

alguem = 'Pedro'

print(diz_oi())
print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return

1- Ela finaliza a função, ela sai da execução da função;
2- Podemos ter, em uma função, diferentes returns:
3- Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores;


# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função
def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'oi'
    print('Estou sendo executado após o retorno')


print(diz_oi())


# Exemplo 2 - Podemos ter, em uma função, diferentes returns:

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())


# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5

#num1, num2, num3, num4 = outra_funcao()

#print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))


# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randônico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())

"""

# Erros comuns na utilização do retorno, que na verdade não é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 5
    if numero %2 != 0:
        return True
    else:
        return False

print(eh_impar())