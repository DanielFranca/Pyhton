"""
Funções com Parâmetro (de entrada)

-  Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada mas não possuem saída;
- Possuem entrada e saída;

# Refatorando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(3))

ret = quadrado(6)
print(ret)

print(quadrado()) #TypeError



# Refatorando a função

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')

cantar_parabens('Geronimo')



# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# Em uma função quantos parâmetros forem necessários. Eles são separados por vírgula

# Exemplo

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Daniel'))
print(outra(5, 4, 'Python'))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

print(soma(2, 3, 4)) # TypeError passando argumentos e mais
print(soma(4)) # TypeErrror Passando argumentos a menos


# Nomeando parâmetros

def nome_completo(string1, string2):
    return f'Seu nome completo é {string1, string2}'

print(nome_completo('Daniel', 'França'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função:
# Argumentos são dados passados durante a execução de uma função:

# A ordem dos parâmetros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome='Daniel', sobrenome='França'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='França', nome='Daniel'))

"""

# Erro na utilização do return

def somar_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(somar_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(somar_impares(tupla))
