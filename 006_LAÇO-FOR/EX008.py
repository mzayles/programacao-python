# DESAFIO 008

""" Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. """

maior = 0
menor = 0

for idade in range(1, 8):
    ano_nasc = int(input(f"🔎 Digite o \033[1;34m{idade}º ano de nascimento\033[0m: "))

    if ano_nasc <= 2007:
        maior += 1
    if ano_nasc > 2007:
        menor += 1

print(f"\nA quantidade de pessoas que \033[1;31mnão atingiram a maioridade\033[0m é {menor}.")
print(f"A quantidade de pessoas já são \033[1;32mmaiores de idade\033[0m é {maior}.")

# VERSÃO 008.1

maior = 0
menor = 0
ano_atual = 2025

for i in range(1, 8):
    idade = ano_atual-int(input(f"Digite o {i}º ano de nascimento: "))
    if idade >= 18:
        maior+=1
    else:
        menor+=1

print(f"\nMaior de idade: {maior}")
print(f"Menor de idade: {menor}")