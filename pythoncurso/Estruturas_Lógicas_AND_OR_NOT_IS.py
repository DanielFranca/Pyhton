""""
Estruturas Lógicas: AND (E), OR (OU), NOT (NÃO), IS (É)

Operadores unários:
  - not

Operados binários:
  - and, or, is


  Regras de Funcionamento:

Para o "And", ambos os valores precisam ser True

ativo = True
logado = True

if ativo and logado:
    print("Bem Vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, visualize a caixa de entrada de seu e-mail")





Para o "OR", um ou outro valor deve ser True

ativo = True
logado = False

if ativo or logado:
    print("Bem Vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, visualize a caixa de entrada de seu e-mail")




Para o "Not", o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True

ativo = False
logado = False

if not ativo:
    print("Você precisa ativar sua conta. Por favor, visualize a caixa de entrada de seu e-mail")
else:
    print("Bem-Vindo usuário")


Para o "IS", o valor é comparado com o segundo.

"""
ativo = True
logado = False

if ativo:
    print("Bem vindo usuário")
else:
    print("Você precisa ativar sua conta. Por favor, visualize a caixa de entrada de seu e-mail")
# is ativo false?
print(ativo is True)

