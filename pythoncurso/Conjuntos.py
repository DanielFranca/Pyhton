"""
Conjuntos

- Quando falamos de conjuntos em qualquer linguagem de programação estamos fazendo referência a teoria dos conjuntos da
matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves ()

Diferença entre Conjuntos e Mapas (Dicionários) em Pyhton:
    - Um dicionários tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

S = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(S)
print(type(S))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo
# Será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

S = {1, 2, 3, 4, 5, 5}
print(S)
print(type(S))

if 3 in S:
    print('Tem o 3')
else:
    print('Não tem o 3')



# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 18 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


# Assim como Todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

S = {1, 'b', True, 34.22, 44}
print(S)
print(type(S))

# Podemos iterar em um set normalmente
for valor in S:
    print(valor)

# Usos interesssantes com Sets

# Imagine que fizemos um formulário de cadastro de visistante em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas únicas , temos
# O que você faria? faria um loop na lista ?
# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
S = (1, 2, 3)

S.add(4)
S.add(4) # Duplicidade não gera erro. Simplesmente e não é adicionado
print(S)


# Adicionando elementos em um conjunto
S = (1, 2, 3)
print(S)

# Forma 1

S.remove(3) # Não é índice. Informando o valor a ser removido

print(S)

# OBS: Caso o valor não seja encontrado será gera o erro KEYerror. Nenhum valor é retornado

#Forma 2

S.discard(22)

print(S)

#OBS: Se o valor não for encontrado, nenhum erro é gerado
# Copiando um conjunto para outro...

S = {1, 2, 3}
print(S)

# Forma 1

novo = S.copy()
print(novo)

novo.add(4)

print(novo)
print(S)

# Forma 2 - Shallow Copy

novo = S

novo.add(4)

print(novo)
print(S)

# Podemos remover todos os itens de um conjunto

S.clear()
print(S)

# Métodos matemáticos de conjuntos

# Imagine que temos 2 conjuntos: Um contendo estudantes de curso PYTHON e um é contendo estudantes do curso de java

estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedra', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

# veja que alguns alunos que estudam python também estudam Java.
# Precismaos gerar um conjunto com nomes de estudantes únicos
# Forma 1 - utilizando Union

unicos2 = estudantes_python.union(estudantes_java)
print(unicos2)

# Forma 2 - Utilizando o caractere pipe
unico2 = estudantes_python | estudantes_java

print(unicos2)

# veja que alguns alunos que estudam python também estudam Java.
# Precismaos gerar um conjunto com nomes de estudantes únicos

# fORMA INTERSECTION

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#Forma 2- Utilizadno &

ambos2 = estudantes_python & estudantes_java
print(ambos2)




"""

# Métodos matemáticos de conjuntos

# Imagine que temos 2 conjuntos: Um contendo estudantes de curso PYTHON e um é contendo estudantes do curso de java

estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedra', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)






