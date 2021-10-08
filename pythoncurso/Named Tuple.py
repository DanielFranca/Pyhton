"""
Named Tuple

# Recap Tupla
tupla = {1, 2, 3}

print(tupla(1))

Named Tuple -> São Tupla, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.


"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='chow-chow', nome='Ray')

print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

# Forma 2

print(ray.idade)  # idade
print(ray.raca)   # raça
print(ray.nome)   # nome

