# DESAFIO 001

""" Crie um programa para efetuar a leitura de um número inteiro e
apresentar o resultado do quadrado desse número """

num_inteiro = int(input("Digite um número: "))
print(f"O quadrado de {num_inteiro} é {num_inteiro ** 2}.")

# VERSÃO 001.1

numero_inteiro = int(input("Digite um número inteiro: "))
quadrado = numero_inteiro ** 2
print(quadrado)

# VERSÃO 001.2

numero_inteiro = int(input("Digite um número inteiro: "))
print(numero_inteiro ** 2)

# VERSÃO 001.3

print(int(input("Digite um número inteiro: ")) ** 2)

# VERSÃO 001.4

numero = int(input("Digite um número inteiro: ")) ** 2
print("O quadrado é:", numero)

# VERSÃO 001.5

numero_inteiro = int(input("Digite um número inteiro: "))
quadrado = numero_inteiro ** 2
print("\nO quadrado de {} é {}!".format(numero_inteiro, quadrado))

# VERSÃO 001.6

numero_inteiro = int(input("Digite um número inteiro: "))
quadrado = numero_inteiro ** 2
nome = 'Mariana'
print("\n%s diz que o quadrado de %d é %f!"%(nome, numero_inteiro, quadrado))

# %s: string;
# %d: número inteiro;
# %f:float.

# VERSÃO 001.7

numero_inteiro = int(input("Digite um número inteiro: "))
quadrado = numero_inteiro ** 2
nome = 'Mariana'

print(f"\n{nome} diz que o quadrado de {numero_inteiro} é {quadrado}!")