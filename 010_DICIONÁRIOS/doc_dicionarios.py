# EXEMPLO 01

# diferente de tupla e lista
# pega um valor dentro de uma lista > JSON

almoco = {'comida': 'Lanche', 'bebida': 'Água', 'sobremesa': 'Pudim'}
print(type(almoco))
print(almoco)
print(almoco['sobremesa'])

# EXEMPLO 01 v2

almoco = {'comida': 'Lanche', 'bebida': 'Água', 'sobremesa': ['Pudim', 'Mousse']}
print(type(almoco))
print(almoco)

# da lista, você pode escolher qual deles você pode apresentar
print(almoco['sobremesa'][1])

# EXEMPLO 02 (JSON)

almoco = {
    'comida': 'Lanche',
    'bebida': 'Água',
    'sobremesa': 'Pudim'
    }

# tupla com todos os itens
print(almoco.items())

# EXEMPLO 03

# tupla com chaves
print(almoco.keys())

# EXEMPLO 04

# tupla com itens das chaves (somente valores)
print(almoco.values())

# EXEMPLO 05
print(almoco['comida'])

# EXEMPLO 06

# percorrer todo o dicionário
# para cada chave e valor em almoco.items, imprima a chave e o valor
for chave, valor in almoco.items():
    print(f"{chave:12} | {valor:>12}")

# EXEMPLO 07 (alterar valores do dicionário)

almoco['bebida'] = 'Suco de laranja'

for chave, valor in almoco.items():
    print(f"{chave:12} | {valor:>15}")

# EXEMPLO 08 (remover valores do dicionário)

# deleta a chave sobremesa
del almoco['sobremesa']

for chave, valor in almoco.items():
    print(f"{chave:12} | {valor:12}")

# EXEMPLO 08 (criar chave e valor para o dicionário)

almoco['sorvete'] = 'Chocolate'

for chave, valor in almoco.items():
    print(f"{chave:12} | {valor:12}")

# EXEMPLO 09

# dicionário lista
estado = {}
brasil = []

for c in range(2):
    estado['uf']    = input("Digite a unidade federativa: ")
    estado['sigla'] = input("Digite a sigla do estado: ")
    brasil.append(estado.copy()) # copy pega as duas informações e coloca na lista

print(brasil)
print(brasil[0]['sigla'])

# EXEMPLO 10

# abrindo a lista
# para cada estado em brasil