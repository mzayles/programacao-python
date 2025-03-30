# DESAFIO 003

""" Desenvolva um programa que leia quatro números inteiros pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares. """

# usuário alimenta a tupla
tp = tuple(int(input(f"Digite o {x + 1}º número: ")) for x in range(4))

# operador ternário
print(f"\nO 9 foi digitado {tp.count(9)} vez(es)" if tp.count(9) > 0 else "\nNão há 9")

# index() dá erro se não acha o que estamos procurando
print(f"O 3 foi encontrado na {tp.index(3) + 1}ª posição" if 3 in tp else "\nNão há 3")
print("Números pares:", end=' ')

for i in range(len(tp)):
    if tp[i] % 2 == 0:
        print(tp[i], end=' ')