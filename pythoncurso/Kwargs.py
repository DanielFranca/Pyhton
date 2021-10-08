"""
**Kwargs

Poderiamos chamar esse parâmetro de **Xis, mas por convenção chamamos de **Kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla
o kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.


# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f' A COR FAVORITA DE {pessoa.title()} É {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(daniel='navy')


def cumprimento_especial(**kwargs):
    if 'Daniel' in kwargs and kwargs ['Daniel'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Daniel!'
    elif 'Daniel' in kwargs:
        return f"{kwargs['Daniel']} Daniel!"
    return 'Não sei quem você é'

print(cumprimento_especial())
print(cumprimento_especial(Daniel='Python'))
print(cumprimento_especial(Daniel='Oi'))
print(cumprimento_especial(Daniel='especial'))


# Nas nossas funções, podemos ter:

- Parâmetros obrigatórios;
- *args
- Parâmetros default (Não obrigatórios);
- **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs ):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'carla', 9, 4, 3, java=False, python=True)
"""

# Entende por quê é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de parâmetros
# def mostra info(a, b, *args, instrutor='Daniel', **kwargs):
# return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parâmetros
def mostra_info(a, b, *args, instrutor='Daniel', **kwargs):
    return [a, b, args, instrutor, kwargs]

"""
a =1 
b =2
args =(3.)
instrutor = 'Daniel'
kwargs = ('sobrenome': 'França': 'cargo': 'Instrutor')

print(mostra_info(1, 2, 3, sobrenome='França', cargo='Instrutor'))


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'jones'}

print(mostra_nomes(**nomes))
"""

def soma_multiplos_numeros(a,b,c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
# OBS! OS NOMES DA CHAVE EM UM DICIONÁRIO DEVEM SER O MESMO DOS PARÂMETROS DA FUNÇÃO

#dicionario = dict(d=1, e=2, f=3) #Type Error

#soma_multiplos_numeros(**dicionario)

soma_multiplos_numeros(**dicionario, lang='Python')

