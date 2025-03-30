# DESAFIO 003

""" Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. """

while True:
    num1 = float(input("✅ Digite o \033[1;34m1º\033[0m número: "))
    num2 = float(input("✅ Digite o \033[1;34m2º\033[0m número: "))

    opcao = int(input("""\nEscolha uma opção:
    \033[1;34m[1]\033[0m Somar
    \033[1;34m[2]\033[0m Multiplicar
    \033[1;34m[3]\033[0m Maior
    \033[1;34m[4]\033[0m Novos Números
    \033[1;34m[5]\033[0m Sair do programa"""))

    match opcao:
        case 1:
            print(f"\n💡 {num1} + {num2} = \033[1;32m{num1+num2}\033[0m\n")
        case 2:
            print(f"\n💡 {num1} x {num2} = \033[1;32m{num1*num2}\033[0m\n")
        case 3:
            print(f"\n💡 Maior entre {num1} e {num2} = \033[1;32m{max(num1, num2)}\033[0m\n")
        case 4:
            print("\n🔎 Escolha novos números: \n")
            continue
        case 5:
            print("\nSaindo...")
            break
        case _:
            print("\n\033[1;31mOpção inválida\033[0m\n")