# DESAFIO 017

""" A confederação Nacional de Natação precisa de uma programa
que leia o ano de nascimento de uma atleta e mostre sua
categoria, de acordo com a idade.

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 24 anos: SÊNIOR
Acima: MASTER """

ano_nasc = int(input("Digite o \033[1;32mano de nascimento\033[0m do atleta: "))
idade = 2025 - ano_nasc

if idade < 10:
    print("\033[1;34mCategoria:\033[0m MIRIM.")
elif idade < 15:
    print("\033[1;34mCategoria:\033[0m INFANTIL.")
elif idade < 20:
    print("\033[1;34mCategoria:\033[0m JUNIOR.")
elif idade < 25:
    print("\033[1;34mCategoria:\033[0m SÊNIOR.")
else:
    print("\033[1;34mCategoria:\033[0m MASTER.")