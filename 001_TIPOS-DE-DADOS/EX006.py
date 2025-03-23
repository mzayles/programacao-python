# DESAFIO 006

""" Dado a nota das provas P1, P2 e P3, calcular a média (aritmética) das notas do aluno. """

prova1 = float(input("Digite a nota da 1º prova: "))
prova2 = float(input("Digite a nota da 2º prova: "))
prova3 = float(input("Digite a nota da 3º prova: "))

print(f"\n✅ A sua média é de \033[1;34m{(prova1 + prova2 + prova3) / 3:,.1f}\033[0m.")