# DESAFIO 022

""" Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.

Para salários superiores a R$ 1.250,00, calcule um aumento de
10%.

Para salários inferiores ou iguais, o aumento é de 15%. """

salario = float(input("Informe o salário do funcionário: R$ "))

if salario > 1250:
    print(f"\n\033[34mSalário atual:\033[0m R$ {salario:,.2f}.")
    print(f"\033[34mSalário com aumento de 10%:\033[0m R$ {salario + (salario * 0.1):,.2f}.")
elif salario <= 1250:
    print(f"\n\033[34mSalário atual:\033[0m R$ {salario:,.2f}.")
    print(f"\033[34mSalário com aumento de 15%:\033[0m R$ {salario + (salario * 0.15):,.2f}.")