"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas ás nossas list comprehension

"""

# Exemplos

#1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# refatorar

# Qualquer número par módulo de 2 é 0 e 0 em python é false. not false = true
pares = [numero for numero in numeros if not numero % 2]

# Qualquer numero ímpar  módulo de 2 é 1, e 1 em python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)
