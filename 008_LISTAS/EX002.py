# DESAFIO 002

""" Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final serão exibidos
todos os valores únicos digitados, em ordem crescente. """

lista = []

while True:
    numero = int(input("\n🔎 Digite um número para \033[1;32mcadastrar\033[0m na lista: "))

    if numero not in lista:
        lista.append(numero)
    else:
        print("💡 Esse número já foi adicionado.\n")

    usuario = input("⏩ Digite \033[1;34m[C]\033[0m para continuar ou digite \033[1;34m[P]\033[0m para parar: ").upper()

    if usuario == 'C':
        continue
    elif usuario == 'P':
        break
    else:
        print("💔 Digite algo válido.")

lista.sort()
print(f"\n✅ Valores \033[1;32múnicos\033[0m digitados: \033[1;34m{lista}\033[0m.")

# VERSÃO 002.1

numeros2 = []
i = 1
while True:
    numero2 = int(input(f"Digite o {i}º número (ou 0 para sair): "))
    if numero2 == 0:
        break
    if numero2 in lista:
        continue
    numeros2.append(numero2)
    i+=1

numeros2.sort()
print(numeros2)

# VERSÃO 002.2

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

numeros2.sort()

for i in numeros2:
    print(i, end=' ')