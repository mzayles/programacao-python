# DESAFIO 026

""" Crie um programa que leia duas notas entre 0 a 10 de um aluno
e calcule sua média, mostrando uma mensagem no final, de
acordo com a média atingida.

Média abaixo de 5.0: REPROVADO
Média entre 5.0 a 6.9: RECUPERAÇÃO
Média igual ou superior a 7.0: APROVADO """

primeira_nota = float(input("Digite a nota da primeira prova: "))
segunda_nota = float(input("Digite a nota da segunda prova: "))
media = (primeira_nota + segunda_nota) / 2

if media >= 0 and media < 6:
    print(f"\nMÉDIA: {media} | \033[1;31mREPROVADO! 😥")
elif media >= 5 and media < 7: # redundante
    print(f"\nMÉDIA: {media} | \033[1;34mRECUPERAÇÃO! 😲")
else:
    print(f"\nMÉDIA: {media} | \033[1;32mAPROVADO! 😁")

# VERSÃO 026.1
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
media = (nota1+nota2)/2

if media < 5:
    print(f"Média: {media:,.2f} | REPROVADO")
elif media < 7:    # é óbvio que a nota já é maior ou igual a 5, pois o primeiro IF deu False.
    print(f"Média: {media:,.2f} | RECUPERAÇÃO")
else:
    print(f"Média: {media:,.2f} | APROVADO")