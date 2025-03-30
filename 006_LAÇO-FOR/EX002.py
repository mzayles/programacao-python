# DESAFIO 002

""" Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontram no intervalo de 1 até 500. """

soma = 0

for i in range(3, 500, 3):
    if i % 2 == 0:
        continue
    soma += i # operador de atribuição

print(f"💡 A \033[4msoma\033[0m dos números ímpares que são múltiplos de 3 no intervalo de 1 até 500 é \033[1;32m{soma}\033[0m.")