# CRIAR LISTA VAZIA

# indíce se inicia em [0]
# declarar uma lista vazia para alimentá-la no meio do código

lista1 = []
lista2 = list()

print(type(lista1))
print(type(lista2))

# MANIPULAÇÃO DE LISTAS

bancos = ['Banco do Brasil', 'CEF', 'Santander']
print(bancos)
print(bancos[1])

# substituir item na lista
bancos[1] = 'Itaú' # na posição 1, recebe 'Itaú', deletando CEF
print(bancos)

# substituir último item na lista
bancos[-1] = 'C6' # na última posição, recebe 'C6', deletando Santander
print(bancos)

# agregar itens a lista
bancos = bancos + ['Safra'] # bancos recebe mais um índice
print(bancos)

# agregar itens a lista (operador de atribuição)
bancos += ['Bradesco', 'Nubank']
print(bancos)

# MÉTODOS PARA LISTAS

lista = [4, 5, 3, 5]
print(lista)

# adicionar itens a lista
lista.append(2)
print(lista)

# adicionar valor no índice específico
lista.insert(2, -3)
print(lista)

# contar valores
print(lista.count(5))

# verificar tamanho da lista
# quantidade de objetos
print(len(lista))

# obter índice do item da lista
# o primeiro 5 tá em que posição da lista
print(lista.index(5))

# reverter itens da lista
# trabalha em conjunto com sort()
# não atribuir a uma variável
lista.reverse()
print(lista)

# ordenar a lista
# na própria linha, sem atribuição
# não atribuir a uma variável
lista.sort()
print(lista)

# remover item através do valor
# remove somente o primeiro 5 que aparecer
# usar o FOR para remover todos os 5 que aparecer
lista.remove(5)
print(lista)

# remover último item da lista (recebe valor removido)
removeu = lista.pop()
print(removeu)
print(lista)

# remover intervalo ou índice
# item 1 até 3, mas não pega o último número escrito > índice 1 e 2
del lista[1:3]
print(lista)

# limpar lista
# não atribuir a uma variável
lista.clear()
print(lista)

# LISTA DENTRO DE LISTA

compras = [10.2, 3.35, 16.3, ['Tomate', 'Cebola', 'Pimentão']]
print(compras)
print(compras[3])

print(len(compras))

# acumulando índices para acessar um objeto específico
print(compras[3][1])

# EXEMPLO 01

print(f"O {compras[3][0].lower()} custa R$ {compras[0]:,.2f}. 🍅")
print(f"A {compras[3][1].lower()} custa R$ {compras[1]:,.2f}. 🧅")
print(f"O {compras[3][2].lower()} custa R$ {compras[2]:,.2f}. 🥒")
print(f"\n\033[1;32mValor total:\033[0m R$ {compras[0] + compras[1] + compras[2]} 💸.")

# PERCORRRER UMA LISTA

roupas = ['Camiseta', 'Bermuda', 'Calça', 'Meia']
for peca in roupas:
    print(peca)

# PERCORRRER UMA LISTA COM ÍNDICE

roupas = ['Camiseta', 'Bermuda', 'Calça', 'Meia']
for i, peca in enumerate(roupas): # i recebe enumerador, peca recebe roupa > trazer informação e índice
    print(i+1, peca)

# PERCORRRER UMA LISTA ATRAVÉS DO ÍNDICE

roupas = ['Camiseta', 'Bermuda', 'Calça', 'Meia']
for i in range(len(roupas)): # para cada i no intervalo de 4 vezes em roupas
    print(i+1, roupas[i]) # 0 vira 1 > percorre os índices de roupas

# VERIFICAR SE UMA LISTA POSSUI ITENS

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letra = input("Digite a letra: ").lower()

if letra in letras:
    print("\033[32mEstá")
else:
    print("\033[31mNão está")

# VERIFICAR SE UMA LISTA NÃO POSSUI ITENS

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letra = input("Digite a letra: ").lower()

if letra not in letras:
    print("\033[31mNão está")
else:
    print("\033[32mEstá")