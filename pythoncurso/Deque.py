"""
Deque

Podemos dizer que o deque é uma lista de alta performance

"""

# Importa
from collections import deque

# Criando deque

deq = deque('daniel')

print(deq)

# Adicionando elementos no deque

deq.append('y')  # Adiciona no final

print(deq)

deq.append('l')  # Adiciona no começo da lista

print(deq)

# Remover elemento

print(deq.pop())  # Remove e retorna o último elemento

print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento

print(deq)




