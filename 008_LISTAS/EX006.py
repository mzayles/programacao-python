# DESAFIO 006

""" Dada a lista abaixo, contendo 3 vetores em cada um de seus elementos, itere por todos os seus elementos,
calculando a soma de todos os elementos presentes na lista.

lista_matrizes = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]
Resultado esperado: 378 """

# VERSÃO 006.1

lista_matrizes = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]

soma = 0
for matriz in lista_matrizes:
    for linha in matriz:
        for coluna in linha:
            soma += coluna
            print(coluna, end=' ')

print(f"\n\nSoma: {soma}")