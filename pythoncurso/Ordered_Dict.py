"""
Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {c}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

OrderedDict -> é um dicionário, que nos garante a ordem de inserção dos elementos



# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

"""

# Entendendo a diferença entre dict e ordered dict

# Dicionários Comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 2}

print(dict1 == dict2)  # True -> Já que a ordem dos elementos não importa para o dicionário

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False -> já que a ordem dos elementos importa para o OrderedDict




