# DESAFIO 023

""" Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da passagem cobrando R$
0,50 por Km para viagens de até 200 Km e R$ 0,45 para
viagens mais longas. """

distancia = float(input("Informe a \033[4mdistância\033[0m (Km) da viagem: "))

if distancia <= 200:
    print(f"\033[34mPreço da viagem de {distancia:,.2f} Km:\033[0m R$ {distancia * 0.50:,.2f} 💸.")
else:
    print(f"\033[34mPreço da viagem de {distancia:,.2f} Km:\033[0m R$ {distancia * 0.45:,.2f} 💸.")