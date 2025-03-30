# DESAFIO 003

""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou não na lista. """

lista = []

while True:
    numero = int(input("\n🔎 Digite um número para \033[1;34mcadastrar\033[0m na lista: "))
    lista.append(numero)

    usuario = input("⏩ Digite \033[1;32m[C]\033[0m para continuar ou digite \033[1;31m[P]\033[0m para parar: ").upper()

    if usuario == 'C':
        continue
    elif usuario == 'P':
        break
    else:
        print("💔 Digite algo válido.")

lista.sort()
lista.reverse()

print(f"\n✅ \033[1;34mQuantidade\033[0m de números digitados: \033[1;4m{len(lista)}\033[0m.")
print(f"✅ Lista de valores em \033[1;34mordem decrescente\033[0m: \033[1m{lista}\033[0m.")
print(f"✅ O valor 5 \033[1;32mestá\033[0m na lista." if 5 in lista else f"❎ \033[1;31mNão\033[0m existe número \033[1;34m5\033[0m na lista.")

# VERSÃO 003.1

numeros2 = []
i = 1
while True:
    numero2 = int(input(f"Digite o {i}º número (ou 0 para sair): "))
    if numero2 == 0:
        break
    if numero2 not in numeros2:
        numeros2.append(numero2)
        i+=1
    else:
        print(f"\033[31mNúmero ({numero2}) já cadastrado\033[0m")

print(f"\nForam cadastrados {len(numeros2)} números.")
numeros2.sort()
numeros2.reverse()
print(f"Lista decrescente: {numeros2}")
print("Tem 5 na lista." if 5 in numeros2 else "Não tem 5.")

# DESAFIO 003 versão 2

lista = []
i = 1

while True:
    numero = int(input(f"🔎 Digite o {i}º número para \033[1;34mcadastrar\033[0m na lista (\033[1mou 0 para sair\033[0m): "))

    if numero == 0:
        break

    lista.append(numero)
    i += 1

lista.sort()
lista.reverse()

print(f"\n✅ \033[1;34mQuantidade\033[0m de números digitados: \033[1;4m{len(lista)}\033[0m.")
print(f"✅ Lista de valores em \033[1;34mordem decrescente\033[0m: \033[1m{lista}\033[0m.")

if 5 in lista:
    print(f"✅ O valor \033[1;34m5\033[0m \033[1;32mestá\033[0m na lista.")
else:
    print(f"❎ \033[1;31mNão\033[0m existe número \033[1;34m5\033[0m na lista.")