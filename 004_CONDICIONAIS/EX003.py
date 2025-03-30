# DESAFIO 003

""" Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, exemplo:
    APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    SOCORRAM ME SUBI NO ONIBUS EM MARROCOS """

frase = input("Digite uma frase: ").lower().replace(' ', '')

if frase[::-1] == frase:
    print("A frase é um palíndromo 😵.")
else:
    print("A frase não é um palíndromo 🙄.")