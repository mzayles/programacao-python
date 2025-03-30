# DESAFIO 011

""" Construir um cardápio utilizando colunas e autopreenchimento. """

print(f"\033[33;42m", " CARDÁPIO ".center(40, '#'), "\033[0m")
print("\nPastel".ljust(35, '.'), "R$ 6,50")
print("Coxinha".ljust(34, '.'), "R$ 5,50")
print("Risoles de queijo".ljust(34, '.'), "R$ 7,50")

# VERSÃO 011.1

print('\033[1;33;42m'," CARDÁPIO ".center(40, '#'),'\033[0m\n')
print(f"{'Pastel'.ljust(32, '.')}"f"{'R$ 6,50'.rjust(10, '.')}") # '': o programa entende que é uma string normal, caso contrário, as "" encerraria a f string.
print(f"{'Coxinha'.ljust(32, '.')}"f"{'R$ 16,50'.rjust(10, '.')}")
print(f"{'Risoles de queijo'.ljust(32, '.')}"f"{'R$ 156,50'.rjust(10, '.')}")