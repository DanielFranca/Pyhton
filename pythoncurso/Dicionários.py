"""
Dicionários

Obs: Em algumas linguagens de programação, os dicionários Python são conhecidos como MAPAS

Dicionários são coleções do tiopo chave/valor

Dicionários são representados por chave {}.

Example:
print(type({})) = ira retornar dict

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chaves-valor'
    - Tanto chave quanto valor podem ser qualquer tipo de dado;
    - Podemos misturar tipos de dados

# Criação de dicionários

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'estados unidos', 'py': 'paraguai'}
print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'paraguai'}

# Acessando Elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

#OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

#Forma 2 - Acessando via Get - Recomendado

print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('ru', 'Não encontrado')

if pais:
    print('encontrei o pais {pais}')
else:
    print('não encontrei o pais')

# Caso o get não encontre o objeto com a chave informado será retornado o valor None e não será gerado KeyERROR

#Podemos definir um valor padrão para caso não encontremos o objeto com a chave informado.

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'paraguai'}

pais = paises.get('py', 'Não encontrado')

print(f'encontrei o pais {pais}')


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'paraguai'}

# Podemos verificar se determinada chave se encontra no dicionário

pais = paises.get('py', 'Não encontrado')

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado, inclusive (int, float, boolean, inclusive lista, tupla, dicionário, como
# de dicionários.

# Tuplas por exemplo são bastante interessante de utilizadas como chave de dicionários, pois as mesmas
# são imutáveis
localidades = {
    (35.6805, 396017): 'Escritório em Tóquio',
    (40.7128, 740060): 'Escritório em Nova Iorque',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}
print(localidades)
print(type(localidades))


# Adiconar elementos em um dicionário

receita = {'jan': 100, 'fev':120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'maio': 500}

receita.update(novo_dado) #receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

#Forma 1

receita['mai'] = 550
print(receita)

#Forma 2

receita.update({'maio': 600})
print(receita)

# Conclusão 1 = A forma de adicionar novos elementos ou atualizar dados no mesmo dicionário é a mesma.
# Conclusão 2 = Em dicionários. Não podemos ter chaves repetidas.



# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyERROR é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del  receita['fev']

print(receita)

# Se a chave já tiver sido apagada ou não existir será emitido um KeyError
# OBS: Neste caso o valor removido não é retornado.

"""

# imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos
"""
Carrinho de compras

    Produto 1:
        -nome;
        -quantidade;
        -preço;
    Produto2:
        -nome;
        -quantidade;
        -preço.
        


# 1 - Poderiamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 230.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual o índice de cada informação no produto.

# 2 - Poderiamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação no produto
# 3 - Poderiamos utlizar um Dicionário para isso? sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 230.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos do nosso carinho
# e em cada produto podemos ter a certeza sobre cada informação

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

d.clear()

print(d)

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Copiando um dicionário para outro

# Forma 1

novo = d.copy() # Deep Copy

print(novo)

novo['4'] = 4

print(d)
print(novo)

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Forma 2 #Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b',)

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

#O método fromkeys recebe dois parâmetros um interável e um valor.
#  Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)







