# DESAFIO 003

""" Crie um programa que peça ao usuário para inserir um número de 1 a 7,
onde cada número representa um dia da semana (1 para domingo, 2 para segunda-feira e assim por diante).
Use match case para imprimir o nome do dia da semana correspondente. """

numero = int(input("💡 Insira um número de 1 a 7 \033[1;32m(semana)\033[0m: "))

match numero:
    case _ if numero == 1:
        print("Domingo 🌞")
    case _ if numero == 2:
        print("Segunda-feira 🌞")
    case _ if numero == 3:
        print("Teça-feira 🌞")
    case _ if numero == 4:
        print("Quarta-feira 🌞")
    case _ if numero == 5:
        print("Quinta-feira 🌞")
    case _ if numero == 6:
        print("Sexta-feira 🌞")
    case _ if numero == 7:
        print("Sábado 🌞")
    case _:
        print("❌ Digite algo válido!")