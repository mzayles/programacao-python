# ESCOPO DE VARIÁVEIS

# VARIÁVEL LOCAL (função sem argumento e sem retorno)

def funcaoLocal():
    variavelLocal = 10
    print(variavelLocal)

funcaoLocal()
# variável dentro de uma função só vale dentro da função
# print(variavelLocal) # gera erro

# VARIÁVEL GLOBAL (Função sem argumento e sem retorno)

variavelGlobal = 5

def funcaoGlobal():
    # pode ser lida dentro de sub programas
    global variavelGlobal
    variavelGlobal += 1
    print(variavelGlobal)

print(variavelGlobal)
funcaoGlobal()
print(variavelGlobal)
funcaoGlobal()

# FUNÇÃO SEM ARGUMENTO

def saudacao():
    print("Olá, mundo!")
saudacao()

# FUNÇÃO COM PARÂMETRO

def soma(x, y):
    resultado = x + y
    print(resultado)

soma(4, 3)

# FUNÇÃO COM PARÂMETRO E RETORNO

def soma(x, y):
    resultado = x + y
    return resultado

print(soma(4, 3) - soma(1, 1))

# FUNÇÃO COM PARÂMETRO, RETORNO E VALOR PADRÃO

# se nínguem passar os parâmetros, ele utliiza o valor padrão
def divisao(x = 10, y = 1):
    resultado = x / y
    return resultado

print(divisao())

# EMPACOTAMENTO DE DADOS

# múltipla, não sabe quantos valores virão
# vou trasnformar em lista todos os números que vierem
def mult(*numeros):
    calculo = 1
    for i in numeros:
        calculo *= i
    return calculo

print(mult(2, 3, 2))