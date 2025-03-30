# DESAFIO 007 BÔNUS

""" Dada a lista com 32 Times, faça o sorteio para outras duas listas (A e B).
Ao final, cada nova lista deve conter 16 times.
random.choice(times) """

# VERSÃO 007.1

import random
times=["Flamengo", "Palmeiras", "São Paulo", "Athletico-PR", "Atlético-MG" ,"Corinthians" ,"Fluminense", "Grêmio", "Fortaleza", "Internacional", "Bahia", "Botafogo", "Red Bull Bragantino", "Atlético-GO", "Ceará", "Cuiabá",
        'Goiás', 'Vasco', 'Juventude', 'Sport', 'CRB', 'Vitória', 'Criciúma', 'Sampaio Corrêa' ,'Operário-PR' ,'Botafogo-SP', 'Brusque', 'Ypiranga-RS', 'América-RN', 'Amazonas', 'Águia de Marabá', 'Sousa-PB']

timesA = []
timesB = []
for time in range(len(times)):
    sorteio = random.choice(times) # escolher
    if len(times) % 2 == 1:
        timesA.append(sorteio)
    else:
        timesB.append(sorteio)
    times.remove(sorteio)

print(timesA)
print(timesB)