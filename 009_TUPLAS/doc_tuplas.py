# TUPLAS

# imutável, mais perfomática
# entre parênteses

linguagens = ('Assembly', 'JAVA', 'Python', 'C#')
print(linguagens)

linguagens2 = 'Assembly', 'JAVA', 'Python', 'C#'
print(linguagens2)
print(type(linguagens2))

# ACESSOS PARA TUPLAS

lanches = ('Hamburger', 'Pastel', 'Coxinha', 'Pizza')

print(lanches[0])   # primeiro item
print(lanches[-1])  # ultimo item
print(lanches[1:3]) # dois itens
print(lanches[1:])  # a partir do segundo
print(lanches[:2])  # até o segundo
print(lanches[:])   # todos

# GERA ERRO (TUPLA É IMUTÁVEL)

lanches = ('Hamburger', 'Pastel', 'Coxinha', 'Pizza')
lanches[0] = 'Hotdog'

# PERCORRER UMA TUPLA

lanches = ('Hamburger', 'Pastel', 'Coxinha', 'Pizza')

for lanche in lanches:
    print(lanche)

# PERCORRER UMA TUPLA POR ÍNDICE

lanches = ('Hamburger', 'Pastel', 'Coxinha', 'Pizza')

for i in range(len(lanches)):
    print(lanches[i])

# PERCORRER UMA TUPLA POR ÍNDICE

lanches = ('Hamburger', 'Pastel', 'Coxinha', 'Pizza')

# atribuição dupla de variáveis (variável númerica)
for posicao, lanche in enumerate(lanches):
    print(f"{posicao+1} | {lanche}")

# CONVERTER LISTA EM TUPLA

# criação de uma lista vazia que recebe 5 números inteiros
lista = list()
lista = [1, 2, 3, 4, 5]

# tupla recebeu um metódo que converte a lista para tupla > tuple()
tupla = tuple(lista)
print(tupla)

# MÉTODO SORTED

lanches = ('Hamburger', 'Pastel', 'Coxinha', 'Pizza')

# ordenar a tupla em ordem crescente por meio do método sorted()
# sem tuple() ele vira uma lista
ordenar = sorted(lanches)
print(type(ordenar))

ordenar = tuple(sorted(lanches))
print(ordenar)
print(type(ordenar))

# MÉTODO DEL

# limpar da memória
lanches = ('Hamburger', 'Pastel', 'Coxinha', 'Pizza')
del(lanches)
print(lanches)

# CONCATENAR TUPLAS

lanches = ('Hamburger', 'Pastel', 'Coxinha', 'Pizza')
doces = ('Pudim', 'Bolo', 'Sorvete')

unificada = lanches + doces

print(unificada)