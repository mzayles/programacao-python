# DESAFIO 002

""" Refaça o DESAFIO 01 considerando notas decimais. """

nota = float(input("Digite uma \033[1;4mnota inteira\033[0m entre 0 e 10: "))

match nota:
    case _ if nota < 0:
        print("Nota inválida!")
    case _ if nota < 5:
        print(f"\nNota: {nota}")
        print("\033[1;31mNota baixa!")
    case _ if nota < 8:
        print(f"\nNota: {nota}")
        print("\033[1;33mNota média!")
    case _ if nota < 10:
        print(f"\nNota: {nota}")
        print("\033[1;34mNota alta!")
    case 10:
        print(f"\nNota: {nota}")
        print("\033[1;32mNota excelente!")
    case _:
        print("❌ Digite algo válido!")

# VERSÃO 002.1

nota = float(input("Digite a nota para obter a classificação: "))

match nota:
    case _ if nota < 0:
        print(f"\nNota inválida")
    case _ if nota <= 4:
        print(f"\nNota Baixa: {nota}")
    case _ if nota <= 7:
        print(f"\nNota Média: {nota}")
    case _ if nota <= 9:
        print(f"\nNota Alta: {nota}")
    case _ if nota <= 10:
        print(f"\nNota Excelente: {nota}")
    case _:
        print(f"\nNota inválida")