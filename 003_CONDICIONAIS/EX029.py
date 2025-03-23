# DESAFIO 029

""" Faça um programa que leia três números e mostre qual é o
maior e qual é o menor. """

num1 = int(input("🔎 Digite o \033[1;34mprimeiro\033[0m valor inteiro: "))
num2 = int(input("🔎 Digite o \033[1;34msegundo\033[0m valor inteiro: "))
num3 = int(input("🔎 Digite o \033[1;34mterceiro\033[0m valor inteiro: "))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

print(f"\n\033[1;34mMaior\033[0m valor inteiro: {maior}.")
print(f"\033[1;34mMenor\033[0m valor inteiro: {menor}.")

# VERSÃO 029.1
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

print(f"Maior: {max(num1, num2, num3)}") # funçao max()
print(f"Menor: {min(num1, num2, num3)}") # funçao min()