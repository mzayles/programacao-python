# DESAFIO 006

""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão. """

primeiro_termo = int(input("Digite o \033[1;32mprimeiro termo\033[0m: "))
razao = int(input("Digite a \033[1;32mrazão\033[0m da PA: "))

print()

for i in range(1, 11):
    termo = primeiro_termo + (i - 1) * razao # a = an + (n -1)r
    print(f"🔎 O {i}º termo é: {termo}")

# VERSÃO 006.1

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))

for i in range(9):
    if i == 0:
        print(termo, end=' ')
    termo += razao
    print(termo, end=' ')