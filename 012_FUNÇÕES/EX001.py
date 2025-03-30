# DESAFIO 001

""" Crie uma função que calcule a soma de diversos números. """

def soma(*numeros):
    calculo = 0
    for numero in numeros:
        calculo += numero
    return calculo

print(soma(2, 85, 62))