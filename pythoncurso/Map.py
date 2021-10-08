"""
Map

Com map fazemos mapeamento de valores para função.

"""

import math

def area(r):
    """calcula a área de um círculo com raio 'r' """
    return math.pi * (r ** 2)

print(area(2))
print(area(5, 3))