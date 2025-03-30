# DESAFIO 018

""" Desenvolva uma lógica que leia o peso e a altura de uma
pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:

Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
Entre 25 e 30: Sobrepeso
Entre 30 e 40: Obesidade
Acima de 40: Obesidade Mórbida """

peso = float(input("Informe seu \033[1;34mpeso\033[0m: "))
altura = float(input("Informe sua \033[1;34maltura\033[0m: "))
imc = peso / (altura ** 2)

print(f"\n🔎 IMC: {imc}")

if imc < 18.5:
    print(f"💡 Abaixo do peso.")
elif imc < 26:
    print("💡 Peso ideal.")
elif imc >= 25 and imc <= 30:
    print(f"💡 Sobrepeso.")
elif imc >= 30 and imc <= 40:
    print(f"💡 Obesidade.")
elif imc > 40:
    print(f"💡 Obesidade mórbida.")