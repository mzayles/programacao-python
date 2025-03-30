# DESAFIO 004

""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas. """

lista = []
par = []
impar = []

i = 1

while True:
    numero = int(input(f"🔎 Digite o {i}º número para \033[1;32mcadastrar\033[0m na lista (ou \033[1;33m0\033[0m para sair): "))

    if numero == 0:
        break
    if numero not in lista:
        lista.append(numero)
        i += 1
    else:
        print(f"\n💡 O {numero} já foi adicionado.")

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"\n✅ Lista \033[1;34mcompleta\033[0m: {lista}.")
print(f"✅ Lista com \033[1;34mvalores pares\033[0m: {par}.")
print(f"✅ Lista com \033[1;34mvalores ímpares\033[0m: {impar}.")

# VERSÃO 004.1

numeros = []
par = []
impar = []
while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    numeros.append(num)
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(numeros)
print(par)
print(impar)