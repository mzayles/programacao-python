# DESAFIO 008

""" Solicite ao usuário o valor do salário atual, em seguida solicite o
percentual de aumento e imprima o valor do salário atualizado. """

salario_atual = float(input("Digite o seu salário atual: R$ "))
percentual = float(input("Digite o percentual de aumento: "))
salario_final = salario_atual + (salario_atual * (percentual / 100))

print(f"\n\033[1mSalário atualizado:\033[0m R$ {salario_final:,.2f}.")