# DESAFIO 005

""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
coloque a lista em ordem sem usar o método sort().
No final mostre a lista ordenada na tela.
a, b = b, a """

# VERSÃO 005.1

n = []
for x in range(1, 6):
    num = int(input(f"Digite o {x}º número: "))
    n.append(num)

for i in range(len(n)):
    for j in range(len(n)):
        if n[i] < n[j]:
            n[i], n[j] = n[j], n[i]
            print(n)

print(f"\nNúmeros em ordem: {n}")