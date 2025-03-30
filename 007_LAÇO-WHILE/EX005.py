# DESAFIO 005

""" Crie um programa que leia vários números inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores e qual foi o
maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores """

qtd = 0
soma = 0
maior = float('-inf') # cria um número negativo infinito
menor = float('inf') # cria um número positivo infinito

while True:
    n = input("Digite um número inteiro (S para sair): ").upper()

    if n.isdigit(): # o objeto [n] é um dígito
        n = int(n)
        qtd += 1
        soma += n
        maior = max(maior, n) # número digitado pelo cliente
        menor = min(menor, n)
    if n == 'S':
        break

print(f"\nA média dos valores é {soma / qtd:,.1f}")
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")