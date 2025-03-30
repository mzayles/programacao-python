# DESAFIO 004

""" Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artificio, indo de 10 até 0, com uma pausa
de 1 segundo entre eles.
Utilizar a Biblioteca TIME | time.sleep(segundos) """

from google.colab import output
import time

print("✅ Preparando contagem regressiva para \033[1;34mfogos de artifício\033[0m: \n")
for i in range(10, -1, -1):
    print(i)
    segundos = time.sleep(1)
    output.clear() # limpeza

print("🔥🔥 \033[1;41m ESTOURO DE FOGOS! \033[0m 🔥🔥")

# VERSÃO 004.1

from google.colab import output
import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
    output.clear()

print(" 🎆 FELIZ ANO NOVO!!! 🍾 ".center(50, '#'))