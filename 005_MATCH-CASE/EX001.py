# DESAFIO 001

""" Escreva um programa em Python que solicite ao usuário uma nota inteira entre 0 e 10.
Use o comando `match case` para classificar a nota de acordo com a tabela a seguir:

- 0-4: Nota Baixa
- 5-7: Nota Média
- 8-9: Nota Alta
- 10: Nota Excelente

Exiba a classificação correspondente. """

nota = int(input("Digite uma \033[1;4mnota\033[0m entre 0 e 10: "))

match nota:
    case 0 | 1 | 2 | 3 | 4:
        print("\033[1;31mNota baixa!")
    case 5 | 6 | 7:
        print("\033[1;33mNota média!")
    case 8 | 9:
        print("\033[1;34mNota alta!")
    case 10:
        print("\033[1;32mNota excelente!")
    case _:
        print("❌ Digite algo válido!")