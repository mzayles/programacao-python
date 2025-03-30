# DESAFIO 012

""" Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
Condições Necessárias:

a + b > c
a + c > b
b + c > a """

a = float(input("✅ Digite o comprimento da \033[4mprimeira\033[0m reta: "))
b = float(input("✅ Digite o comprimento da \033[4msegunda\033[0m reta: "))
c = float(input("✅ Digite o comprimento da \033[4mterceira\033[0m reta: "))

if (a + b) > c and (a + c) > b and (b + c) > a: # todas as sentenças precisam ser verdadeiras
    print("\nÉ \033[32mpossível\033[0m formar um triângulo!")
else:
    print("\n\033[31mNão é possível\033[0m formar um triângulo!")