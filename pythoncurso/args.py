""""
Entendendo o args*

- O *args é um parâmetro, como outro qualquer, isso significa que você poderá chamar de qualquer coisa, desde que comece
com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é *args

O parâmetro *args é utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde
já lembre-se que tuplas são imutáveis

# Exemplos

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros(4, 6, 9, 5))

# Entendendo o args

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(2, 3, 4, 5, 6))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Daniel' in args and 'França' in args:
        return "Bem vindo Daniel!"
    return 'Eu não permito você entrar'

print(verifica_info())
print(verifica_info(1, True, 'França', 'Daniel'))
print(verifica_info(1, 'França', 3.145))

"""

def soma_todos_numeros(*args):
    print(args)
    return sum(args)

#print(soma_todos_numeros())
#print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6,7]
# Desempacotador

print(soma_todos_numeros(*numeros))

#OBS: O asterisco serve para que informemos ao Python que estamos passando como
# argumento uma coleção de dados, dessa forma ele saberpa que precisará antes desempacotar estes dados.

