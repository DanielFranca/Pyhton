"""
Definindo Funções

    - Funções são pequenas partes de código que realizam tarefas específicas
    - Pode ou não receber entradas de dados e retornar uma saída de dados;
    - Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza varias tarefas dentro delas
é bom fazer uma verificação para que a função seja simplificada.
Já utlizamos várias funções desde que iniciamos o curso:
- Print()
- Len()
- Max()
- Count()
_ Muitas outras;


"""
"""

# Exemplo de utilização de funções:

#cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in do Python Print)

#print(cores)

#curso = 'Programação em python Essencial'

#print(curso)

#cores.append('roxo')

#print(cores)

#curso.append('Mais dados...') # AtributeError

#print(curso)

#cores.clear()
#print(cores)

#print(help(print))

# DRY - don´t repeat yourself - Não repita você mesmo/ Não repita seu código
"""
"""
Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> Sempre, com letras minúsculas, e se for nome composto, separado por underline (Snake Case)
parâmetros_de_entrada -> são opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_de_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos 
definindo uma função. Também abrimos o bloco do código com o já cohecido dois pontos: que é 
utilizado em Phyton para definir blocos.

"""

# Definindo a primeira função

#def diz_oi():
    #print('oi!')

"""
OBS: 

1 - Veja que, dentros das nosssas funções podemos utilizar outras funções:
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada
4 - Veja que essa função não retorna nada;
"""

# Utilizando funções:

# Chamada de execução
#diz_oi()

"""
Atenção:

Nunca esqueça de utilizar o parênteses ao executar uma função

Exemplo:

# ERRADO:
diz_oi

# CERTO:
diz_oi()

# ERRADO:
diz_oi ()

"""

# Exemplo 2

def cantar_parabens():
    print('parabéns pra você')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print('viva o aniversariante')

#0, 1, 2, 3, 4
#for n in range(5):
 #   cantar_parabens()

# Em PYthon podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável

canta = cantar_parabens

canta()
