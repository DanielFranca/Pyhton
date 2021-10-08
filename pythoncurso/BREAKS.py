"""
SAINDO DE LOOPS COM BREAKS

Funciona da mesma forma da linguagem C ou Java
Usamos Breaks para sair de loops de maneira forçada ou projetada

"""
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print("Sai do loop")

# Exemplo 2

while True:
    comando = input("digite 'sair' para sair: ")
    if comando ++ 'sair':
        break
