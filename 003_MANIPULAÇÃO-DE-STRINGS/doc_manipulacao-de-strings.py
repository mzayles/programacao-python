# FATIAMENTO DE STRINGS

texto = "Curso de Python"

# primeira posição de um objeto se inicia em 0, espaços contam como caracter.

print(texto[6])       # 7º caracterer
print(texto[9:15])    # 10º ao 15º caracterer
print(texto[9:15:2])  # 10º ao 15º caracterer de 2 em 2
print(texto[:5])      # até o 5º caracterer
print(texto[9:])      # 10º caracterer em diante
print(texto[::-1])    # inverter o texto
print(texto[-1])      # último caracterer

# ANÁLISE DE STRINGS

frase = "SENAI Ary Torres"

# tamanho da string
print(len(frase))

# contar caracteres
print(frase.count('r'))

# encontrar índice (retorna -1 se não encontrar)
print(frase.find('z'))

# encontrar índice (a partir da direita)
# índice que vem primeiro na direita
print(frase.rfind('r'))

# encontrar índice (gera erro se não encontrar)
print(frase.index('r'))

# vericar pertinência
# a palavra 'Ary' está na variável frase?
print('Ary' in frase)

# TRANSFORMAÇÃO DE STRINGS

# maiúscula
print(frase.upper())

# minúscula
print(frase.lower())

# primeira da frase em maiúscula
print(frase.capitalize())

# primeira letra de cada palavra em maiúscula
print(frase.title())

# TRANSFORMAÇÃO DE STRINGS

# substituir palavras
print(frase.replace('SENAI', 'ESCOLA'))
print(frase)
frase = frase.replace('SENAI', 'ESCOLA')
print(frase)

frase2 = "   oi    SENAI   Ary Torres oi  "

# retirada/limpeza das extremidades
# não é definitivo, no próximo print aparece a frase original
print(frase2.strip())
print(frase2.strip())

# limpar espaços antes e depois
# os espaços do meio não são retirados
frase2 = frase2.strip()

print(frase2.strip('oi'))

url = 'https://google.com/h'
print(url.rstrip('h'))

print(url.lstrip('https://'))

# JUNÇÃO E DIVISÃO DE STRINGS

texto = "SENAI Ary Torres"
# juntar caracteres com delimitador
print('.'.join(texto))

# dividir palavras em lista
print(texto.split())
print(texto.split()[0])   # primeira palavra
print(texto.split()[-1])  # última palavra
print(texto.split()[1])

lista = texto.split()
print(', '.join(lista))

# limpeza de string

novoTexto = "oi    SENAI   Ary   Torres   oi"

# limpeza das extremidades e transformação do texto em lista
novoTexto = novoTexto.strip('oi').split()
print(type(novoTexto))
print(' '.join(novoTexto))