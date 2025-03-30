# EXEMPLO 01

try:
    numerador   = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    razao = numerador/denominador
except Exception as erro:
    print(f"Erro encontrado: {erro}")
    print(f"Erro encontrado: {erro.__class__}")
else:
    print(razao)

# EXEMPLO 02

try:
    # código que pode gerar erro
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except(ValueError, TypeError):
    # trata erros mencionados acima
    print("Digite um número válido")
except(ZeroDivisionError):
    # trata erro mencionado acima
    print("Não é possível dividir por zero")
else:
    # executa se não houver erro
    # apenas saída dos dados
    print(f"\nResultado: {resultado}")
finally:
    # sempre executa
    print("\nEncerrando o programa...")

# EXEMPLO 03

try:
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    media = (nota1+nota2)/2
except: # qualquer erro, ele sempre vai mostrar a mesma frase
    print("Deu ruim")
else:
    if media < 5:
        print(f"\nMédia: {media:,.1f}")
        print("Resultado: REPROVADO")
    elif media < 7:
        print(f"\nMédia: {media:,.1f}")
        print("Resultado: RECUPERAÇÃO")
    else:
        print(f"\nMédia: {media:,.1f}")
        print("Resultado: APROVADO")

# EXEMPLO 04

import time
from google.colab import output

while True:
    try:
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        media = (nota1+nota2)/2
    except:
        output.clear()
        print("Deu ruim")
        time.sleep(3)
        print()
        continue
    else:
        if media < 5:
            print(f"\nMédia: {media:,.1f}")
            print("Resultado: REPROVADO")
        elif media < 7:
            print(f"\nMédia: {media:,.1f}")
            print("Resultado: RECUPERAÇÃO")
        else:
            print(f"\nMédia: {media:,.1f}")
            print("Resultado: APROVADO")
        break