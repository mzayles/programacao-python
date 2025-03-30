# DESAFIO 013: CONCATENAÇÃO

produto = input("Digite o nome do produto: ")
preco = 'R$ ' + input("Digite o preço do produto R$: ")

print()

print('\033[1;33;42m'," CARDÁPIO ".center(40, '#'),'\033[0m\n')
print(f"{'Pastel'.ljust(32, '.')}"f"{'R$ 6,50'.rjust(10, '.')}")
print(f"{'Coxinha'.ljust(32, '.')}"f"{'R$ 16,50'.rjust(10, '.')}")
print(f"{'Risoles de queijo'.ljust(32, '.')}"f"{'R$ 156,50'.rjust(10, '.')}")
print(f"{produto.ljust(32, '.')}"f"{preco.rjust(10, '.')}")