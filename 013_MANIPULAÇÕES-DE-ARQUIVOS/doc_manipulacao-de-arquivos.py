# CONECTAR E SINCRONIZAR PASTA DO GOOGLE DRIVE

from google.colab import drive
drive.mount('/content/drive')

caminho = '/content/drive/MyDrive/Colab Notebooks/25032501/arquivos'

# EXEMPLO 01 (w write)

arq = 'dados.txt'

with open(f"{caminho}/{arq}", 'w') as arquivo:
    arquivo.write("Mariana Alves de Souza")

# EXEMPLO 02

arq = 'dadosOrcamento.txt'

with open(f"{caminho}/{arq}", 'w') as arquivo:
    arquivo.write("""São Paulo, 12 de setembro de 2024

Segue valor do orçamento solicitado:

100 Peças X: R$ 200,00
200 Peças Y: R$ 150,00
Total: R$ 350,00

Atenciosamente,
Mariana""")

# EXEMPLO 03

arq = 'dadosAnimais.txt'

with open(f"{caminho}/{arq}", 'w') as arquivo:
    arquivo.write('Cachorro\n')
    arquivo.write('Gato\n')
    arquivo.write('Passarinho\n')

# EXEMPLO 04
import random

arq = 'dadosNumeros.txt'

with open(f"{caminho}/{arq}", 'w') as arquivo:
    for i in range(6):
        numero = random.randint(1, 60)
        n = str(numero)+'\n'
        arquivo.write(n)

# EXEMPLO 05 (a append)

arq = 'dadosAnimais.txt'

with open(f"{caminho}/{arq}", 'a') as arquivo:
    arquivo.write('Girafa\n')
    arquivo.write('Cavalo\n')
    arquivo.write('Leão\n')

# EXEMPLO 06

animais = ['Jacaré', 'Onça', 'Papagaio', 'Camelo', 'Anta']

arq = 'dadosAnimais.txt'

with open(f"{caminho}/{arq}", 'a') as arquivo:
    for animal in animais:
        arquivo.write(f'{animal}\n')

# EXEMPLO 07 (r read)

arq = 'dadosOrcamento.txt'

with open(f"{caminho}/{arq}", 'r') as arquivo:
    print(arquivo.read())

# EXEMPLO 08

arq = 'dadosOrcamento.txt'

with open(f"{caminho}/{arq}", 'r') as arquivo:
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())

# EXEMPLO 09

arq = 'dadosOrcamento.txt'

with open(f"{caminho}/{arq}", 'r') as arquivo:
    texto = arquivo.readline()
    print(texto[0:20])

# EXEMPLO 10

arq = 'dadosOrcamento.txt'

with open(f"{caminho}/{arq}", 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip('\n'))