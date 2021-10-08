"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis Globais
  - Variáveis Globais são reconhecidas, ou seja, seu escopo compreende, Todo o progresso.

2 - Variáveis Locais:
    Vriáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo Java:
Int numero = 42;
"""

numero = 42 #Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Daniel'
print(numero)
print(type(numero))

nao_existe = 'oi'
print(nao_existe)

numero = 42
novo = 0

if numero > 10   #Escopo Local, a variável novo está delcarada localmente dentro do bloco if, portanto, é local
    novo = numero + 10
    print(novo)

print(novo)



