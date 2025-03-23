# DESAFIO 031

""" Refaça o DESAFIO dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:

Equilátero: Todos os lados iguais
Isósceles: Dois lados iguais
Escaleno: Todos os lados diferentes """

a = float(input("✅ Digite o comprimento da \033[4mprimeira\033[0m reta: "))
b = float(input("✅ Digite o comprimento da \033[4msegunda\033[0m reta: "))
c = float(input("✅ Digite o comprimento da \033[4mterceira\033[0m reta: "))

if (a == b) and (a == c):
    print("\nTriângulo formado: 🔼 Equilátero.")
elif (a == b) or (a == c) or (b == a) or (b == c) or (c == a) or (c == b):
    print("\nTriângulo formado: 🔼 Isósceles.")
elif (a != b) and (a != c) and (b != a) and (b != c) and (c != a) and (c != b):
    print("\nTriângulo formado: 🔼 Escaleno.")