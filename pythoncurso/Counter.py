"""
Módulo Collections - Counter (Contador)

Collection -> High perfomance Container DataType

Counter -> Recebe um literável como parâmetro e cria um objeto do tipo colecction COUNTER que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parãmetro e como valor a qauntidade
de ocorrências desse elemento.

from collections import Counter

# Exemplo 2

# Podemos utilizar qualquer iterável, aqui usamos uma lista

lista = [1, 1, 1, 22, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter

res = Counter(lista)

print(type(res))

print(res)

# Counter ({1: 5, 3: 5, 2: 3, 4: 3, 5: 3, 45: 2, 66: 2, 22: 1, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade ocorrências.

Exemplo 2

from collections import Counter

print(Counter('Daniel França'))


"""

from collections import Counter

# Exemplo 3

texto = """ No Brasil, o dia da árvore é comemorado em 21 de setembro, às vésperas da entrada da primavera. No Norte e 
Nordeste do país as árvores costumam ser homenageadas também na última semana de março, época do início do período das 
chuvas naquela região. A árvore é o símbolo maior da natureza. Plantar, cuidar, proteger e defender as árvores significa
valorizar todo o verde que ainda existe no planeta. A defesa de florestas como a da Amazônia, por exemplo, está se 
tornando uma questão de sobrevivência para nossa espécie, devido aos inúmeros problemas ambientais que nós mesmos 
criamos na Terra.... - Veja mais em https://educacao.uol.com.br/datas-comemorativas/0921---dia-da-arvore.htm?cmpid=copi
aecola """

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

