# OPÇÃO ÚNICA

operacao = input("""
ESCOLHA UMA OPÇÃO:

[1] Opção 1
[2] Opção 2
[3] Opção 3
""")

match operacao: # corresponda com operação...
    case '1': # caso operação seja X, faça Y
        print("Opção 1 foi escolhida...")
    case '2':
        print("Opção 2 foi escolhida...")
    case '3':
        print("Opção 3 foi escolhida...")
    case _: # _: else
        print("Opção inválida...")

# OPÇÃO MULTIPLA

operacao = input("""
ESCOLHA UMA OPÇÃO:

[1] Opção 1
[2] Opção 2
[3] Opção 3
""")

match operacao: # várias opçoes para representar uma operação
    case '1' | '2': # caso seja X ou Y, faça Z -- funciona como OR
        print("Opção 1 ou 2 escolhida...")
    case '3':
        print("Opção 3 foi escolhida...")
    case _:
        print("Opção inválida...")

# OPÇÃO MÚLTIPLA COM CASE _ IF

numero = int(input("Digite um número: "))

match numero:
    case 1 | 3 | 5 | 7 | 9:
        print("É ímpar entre 0 e 10")
    case _ if numero < 0: # caso o número seja menor que 0, escreva...
        print("É negativo")
    case _: # se não...
        print("Um número qualquer...")

# CABEÇALHO

print("""
_______________________________________________________

🌷🌱\033[1m  WHERE'D ALL THE TIME GO, STARTING TO FLY \033[0m 🌷🌱
_______________________________________________________
""")