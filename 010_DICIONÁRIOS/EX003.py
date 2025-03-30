# DESAFIO 003

""" Faça  um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
(Abaixo de 5: Reprovado | entre 5 e 6,9: Exame | 7: acima Aprovado)
No final mostre o conteúdo da estrutura na tela. """

dicionario = {}
nome = input("Digite o nome: ")
media = float(input("Digite a média: "))
if media < 5:
    situacao = 'Reprovado'
elif media < 7:
    situacao = 'Exame'
else:
    situacao = 'Aprovado'

dicionario['nome'] = nome
dicionario['media'] = media
dicionario['situacao'] = situacao

print(dicionario)