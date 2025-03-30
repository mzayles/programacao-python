# DESAFIO 006

""" Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma sequência de Fibonacci.
Exemplo:

0 –> 1 –> 1 –> 2 –> 3 –> 5 –> 8 """

anterior = 0
atual = 1
fibo = 0
i = 0

num = int(input("Digite uma quantidade para sequência Fibonacci: "))

while i < num:
    print(fibo, end = ' ')
    fibo = atual + anterior
    anterior = atual
    atual = fibo
    i += 1

# VERSÃO 006.1

anterior = 0
atual    = 1
fibo     = 0
i        = 1
seqFibo  = '0 1 '
numero   = int(input("Digite uma quantidade para sequência Fibonacci: "))

while i <= numero-2:
    fibo     = anterior+atual
    seqFibo += f'{fibo} '
    anterior = atual
    atual    = fibo
    i+=1

print(seqFibo)