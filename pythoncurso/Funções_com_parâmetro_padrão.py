"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Daniel França')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero

print(quadrado(3))
print(quadrado()) #TypeError



def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3)) #2 * 2 * 2 = 8
print(exponencial(3, 2)) #3 *3 -9

print(exponencial(3)) #Por padrão eleva ao quadrado
print(exponencial(3, 5))# Eleva a potência informada pelo usuário

# OBS
# Se o usuário passar somente 1 parâmetro. este será atribuido ao parâmetro número, e será calculado o quadrado deste
# número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido número e o segundo ao parâmetro potência. Então será
calculada a potência



# OBS: Em funções Python, os parâmetros em valores default padrão DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) #TypeError
print(soma()) #TypeError




# Exemplo mais complexo

def mostra_informacao(nome='Daniel', analista=False):
    if nome == 'Daniel' and analista:
        return 'Bem-Vindo Analista Daniel'
    elif nome == 'Daniel':
        return 'Eu pensei que voce era analista'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(analista=True))
print(mostra_informacao('Pessoal do Git'))



# Por quê utlizar parâmetros com valor default?

- Nos permite ser mais flexiveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;


# Quais tipos de dados podemos usar para valores default para parâmetros

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc:

def soma(num1, num2):
    return num1 + num2
def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))



# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

Instrutor = 'Daniel' # Variável Global

def diz_oi():
    instrutor = 'Python'
    return f'oi {instrutor}'

print(diz_oi())

#OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência


def diz_oi():
    aluno = 'Daniel' # Variável local
    return f'Olá {aluno}'

print(diz_oi())

print(aluno) #NameError

# Atenção com varpaveis globais (Se puder evitarm evite!)

total = 0

def incrementa():
    total = total + 1
    return total

print(incrementa())



# Atenção com varpaveis globais (Se puder evitarm evite!)

total = 0

def incrementa():
    global total  # Avisando que queremos utilizar a variável global

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""

# podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 10

    def dentro():
        nonlocal contador

        contador = contador + 2
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

