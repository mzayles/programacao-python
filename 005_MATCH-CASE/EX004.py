# DESAFIO 004

""" Implemente uma calculadora simples que realiza as operações de adição, subtração, multiplicação e divisão.
O usuário deve inserir dois números e, em seguida, selecionar a operação desejada (+, -, *, /).
Use o comando match case para realizar a operação correta e exibir o resultado. """

num1 = float(input("🔎 Digite o 1º número: "))
num2 = float(input("🔎 Digite o 2º número: "))

opcao = int(input("""
    \033[1;32m[1]\033[0m Adição
    \033[1;32m[2]\033[0m Subtração
    \033[1;32m[3]\033[0m Multiplicação
    \033[1;32m[4]\033[0m Divisão
\n"""))

match opcao:
    case _ if opcao == 1:
        print(f"✅ Adição: {num1 + num2}")
    case _ if opcao == 2:
        print(f"✅ Subtração: {num1 - num2}")
    case _ if opcao == 3:
        print(f"✅ Multiplicação: {num1 * num2}")
    case _ if opcao == 4:
        if num2 != 0:
            print(f"✅ Divisão: {num1 / num2}")
        else:
            print("Não pode ser divisível por 0! 🙄")
    case _:
        print("❌ Inválido!")