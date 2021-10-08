"""
PEP8 - Python enhancement Proposal

São propostas de melhorias para a linguagem python

zem of python
import this

A idéia do pep8 é que possamos escrever códigos de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;
class Calculadora
    pass

class CalculadoraCientifica
    pass

def soma();
    pass

def soma_dois();
    pass

Numero  =  4

Numero impar = 5

[3] - Utilize 4 espaços para identação! (Não usar tab)

if 'a' in 'banana';
    print('tem');

[4] - linhas em branco
- Separa funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

class Classe;
    pass

[5] -  Imports
- Imports devem ser sempre feitos em linhas separadas;

#Import Errado
imports sys, os

#imports Certo

 imports, sys, os
 imports os

#Não há problemas em utilizar;

from types imports StringType, ListType

#caso tenha muitos imports de um mesmo pacote, recomenda-se fazer;

from Type_import (
    StringType,
    ListType,
    SetType,
    OutroType,
)
# Importos devem ser colocados no topo do arquivos, logo depois de quaisquer comentários ou strings e
# antes de constantes ou variáveis globais.

[6] Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ], ( outro: 2] )

#Faça:

funcao(algo[1], (outro: 2)]

#Não faça:

algo [1]

#faça:

algo(1)

#Não faça;

dict ['chave'] = lista_(indice)

#Faça:

dict['chave'] - lista(indice)

#não faça:

 x                  =1
 y                  =3
 y                  =5

 #faça:

 x = 1
 y = 3
 varaiavel_longa = 5

[7] - termine sempre uma instrução com uma nova linha
"""



