# EXEMPLO 01

i = 1

# enquanto 1 for menor ou igual a 10, faça X
# incrementar 1 na variável de contador para que não vire um loop infinito
while i <= 10:
    print(i, end=' ')
    i += 1

# EXEMPLO 02

i = 10

# contagem regressiva
# enquanto 10 for maior ou igual a 1
# decremente 1 na variável contador

while i >= 1:
    print(i, end=' ')
    i -= 1

# EXEMPLO 03

i = 0

while i < 5:
    i += 1
    if i == 3:
        print("Pulando a iteração 3")
        continue
    print(i)
else:
    print("Fim do loop.")

# EXEMPLO 04

# laço infinito
# enquanto verdadeiro
while True:
    r = input("Digite (S) para sair ou (C) para continuar\n")
    if r.upper() == 'S':
        print("Saindo do loop...")
        break
    print("\nContinuando...\n")

# EXEMPLO 05

while True:
    r = input("Digite (S) para sair ou (C) para continuar\n").upper()
    if r != 'S' and r != 'C':
        print("\nDeixa de besteira, só vale S e C! 👶")
        continue
    if r == 'S':
        print("Saindo do loop...")
        break
    print("\nContinuando...\n")

# EXEMPLO 06

from google.colab import output
import time

while True:
    time.sleep(3) # 3 segundos com a mensagem na tela
    output.clear()

    r = input("Digite (S) para sair ou (C) para continuar\n").upper()
    if r != 'S' and r != 'C':
        print("\nDeixa de besteira, só vale S e C! 👶")
        continue
    if r == 'S':
        print("Saindo do loop...")
        break
    print("\nContinuando...\n")

# MÉTODOS max E min

print(max(20, 4, 89, 2))
print(min(20, 4, 89, 2))

# CONCATENAÇÃO

escola = 'SENAI'
print(escola + 'Ary Torres')

# EXERCÍCIO CONCATENAÇÃO

nome1 = 'Mariana'
nome2 = 'Alves'
nome3 = 'de'
nome4 = 'Souza'
nome_completo = nome1 + ' ' + nome2+ ' ' + nome3+ ' ' + nome4

print(nome_completo)