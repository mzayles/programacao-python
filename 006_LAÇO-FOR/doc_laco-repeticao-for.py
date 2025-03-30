# EXEMPLO 01

# sempre acrescentar um número a mais > se lê de 1 até 5
# range(): intervalo
# se o intervalo não é especificado, range() começa pelo índice [0] > range(5)

for i in range(1, 6):
    print(i, end=' ') # muda o comportamento do print de vertical para horizontal

# EXEMPLO 02

# range(inicio, fim, salto)
# variável i: usada para contagem
# salto: pula de 2 em 2

for i in range(1, 10, 2):
    print(i, end=' ')

# EXEMPLO 03

# variável múltipla
inicio, fim, salto = 5, 0, -1

# contagem regressiva
for i in range(inicio, fim, salto):
    print(i, end=' ')

# EXEMPLO 04

for i in range(5):
    print(f"{i+1} | SENAI") # o i sozinho começaria em [0]

# EXEMPLO 05

texto = 'Python'

for letra in texto: # para cada X no Y, escreva X
    print(letra.upper(), end='   ')

# EXEMPLO 06

frase = ['PYTHON', 'É', 'FANTÁSTICO!']

for palavra in frase:
    print(palavra)

# EXEMPLO 07

lista = [1, 10, 20, 30, 40, 50]

# para cada numero na lista, se o numero for exatamente 30, pule-o e continue com o restante do array
# continue: pula a interação > volta pro começo do laço e ignora o restante da repetição

for numero in lista:
    if numero == 30:
        continue
    print(numero, end=' ')

# EXEMPLO 08

# break: finaliza o laço > transforma o laço de True para False
# para cada variável [i] no intervalo de 50 vezes, quando i for maior ou igual a 10, quebre o laço

for i in range(50):
    if i >= 10:
        break
    print(i+1, end=' ')

# EXEMPLO 09

for i in range(1, 11):
    print()
    for j in range(1, 11): # repete esse bloco 10 vezes, e depois volta para o laço de cima, que também se repete 10 vezes
        print(f"{i*j}".rjust(3), end=' ')

# EXEMPLO 10

for i in range(0, 11):
    print()
    for j in range(0, 11):
        print(f"{i+j}".rjust(3), end=' ')