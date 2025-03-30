# DESAFIO 004

""" Faça com que o programa anterior possa cadastrar uma quantidade de alunos escolhida pelo usuário.
No final apresente as informações tabuladas. """

alunos = list()
dicionario = dict()
quantidade = int(input("Digite quantos alunos quer cadastrar: "))

for i in range(quantidade):
    nome = input(f"Digite o {i+1}º nome: ")
    media = float(input(f"Digite a {i+1}ª média: "))
    if media < 5:
        situacao = 'Reprovado'
    elif media < 7:
        situacao = 'Exame'
    else:
        situacao = 'Aprovado'
    dicionario['nome']=nome
    dicionario['media']=media
    dicionario['situacao']=situacao
    alunos.append(dicionario.copy())

print()
print(f"\033[0;95m{'ALUNOS'.center(15)} {'MÉDIA'.center(5)} {'SITUAÇÃO'.center(11)}\033[0m")
for j in range(len(alunos)):
    print(f"\033[0;30;47m {alunos[j]['nome']:<15} {alunos[j]['media']:^5} {alunos[j]['situacao']:^11} ")