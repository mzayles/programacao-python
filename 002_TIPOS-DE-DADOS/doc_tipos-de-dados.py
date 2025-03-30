# TIPOS NUMÉRICOS (int | float)

x = 10       # inteiro
y = -1       # inteiro negativo
z = -5.29    # decimal negativo (número americano)
pi = 3.1415  # decimal

print(x)
print(y)
print(z)
print(pi)

# TIPO CARACTERES | STRINGS (str)

nome = 'Mariana'
escola = "SENAI Ary Torres"

print(nome)
print(escola)

print() # quebra de linha
print(escola)
print('\n', escola) # quebra de linha com escape
print('\n', escola[0])

# index(0, 1, 2, 3, 4, 5)

# TIPOS LÓGICOS (bool)

continuar = True
parar = False
casado = True

print(continuar)
print(parar)
print(casado)

# IDENTIFICAR TIPOS PRIMITIVOS (texto, número e lógico)

print(type(x))
print(type(pi))
print(type(nome))
print(type(casado))

# DECLARAÇÃO DE VARIÁVEIS

texto1 = '2'
texto2 = str(2)
numero1 = 3
numero2 = int(3)
decimal1 = float(3)
decimal2 = 3.0
logico = bool(False)

print(texto1)
print(texto2)
print(numero1)
print(numero2)
print(decimal1)
print(decimal2)
print(logico)

# camelCase: funções e classes | snake_case
# constantes: letra maiúscula

# ANÁLISE DE STRINGS (str)

n = '5t'

print(n.isnumeric())   # numérico - apenas strings
print(n.isalpha())     # alfabético
print(n.isalnum())     # alfanumérico
print(n.isupper())     # maiúscula
print(n.islower())     # minúscula
print(n.istitle())     # primeira maiúscula
print(n.isdecimal())   # numérico
print(n.isspace())     # espaço

# EXEMPLO ANÁLISE DE STRINGS

num = input("Digite um número ")
if num.isnumeric():
    num = int(num)
else:
    print("Não é número!")

print(type(num))

# ENTRADA DE DADOS (INPUT)

numeroInteiro = int(input("Digite um número inteiro: "))
print(numeroInteiro)

numeroDecimal = float(input("\nDigite um número decimal: ")) # separador de decimal: . (não vírgula)
print(numeroDecimal)

valorLogico = bool(input("\nDigite algo: ")) # verificar se a pessoa digitou algo
print(valorLogico)

# não há necessidade declarar str() para o input()
texto = str(input("\nDigite um valor alfanumérico:\n"))
print(texto)

# CONSTANTES

PI = 3.1415
GRAVIDADE = 9.81

print("\nValor de PI:", PI, "\n\n\n")
print("\nValor de gravidade:", GRAVIDADE)

# CORES

"""
\033[ESTILO;FONTE;FUNDOm TEXTO \033[0m
\033[m    \033[0m

|033[m: colocar cor
\033[0m: break

Estilos: 0 nenhum | 1 negrito | 3 itálico | 4 sublinhado
"""

print("\033[3;36m HELLO, WORLD")
print("\033[0;32m HELLO, MARIANA\n")

print("\033[1;33;45m   TEXTO   \033[0m")

# cores de fonte
print("\033[30m CINZA")
print("\033[31m VERMELHO")
print("\033[32m VERDE")
print("\033[33m AMARELO")
print("\033[34m CIAN")
print("\033[35m MAGENTA")
print("\033[36m AZUL")
print("\033[37m BRANCO")

# cores de fundo
print("\033[40m CINZA")
print("\033[41m VERMELHO")
print("\033[42m VERDE")
print("\033[43m AMARELO")
print("\033[44m CIAN")
print("\033[45m MAGENTA")
print("\033[46m AZUL")
print("\033[47m BRANCO")

print("\033[1;33;45m\033[2m\033[3m\033[4m   TEXTO   \033[0m")

# COLUNAS COM PREENCHIMENTO E ALINHAMENTO

print(" CENTRALIZADO ".center(30, '-'))
print(" DIREITA".rjust(30, '-'))
print("ESQUERDA ".ljust(30, '-'))

# ALINHAMENTO PARA F STRINGS

print(f"| {'Unidade':>20} | {'5':^20} |") # alinhar esquerda
print(f"| {'Unidade':^20} | {'5':^20} |") # alinhar centro
print(f"| {'Unidade':<20} | {'5':^20} |\n\n") # alinhar direita

print(f"| {'Nome':^15} | {'Mariana':^9} |")
print(f"| {'Idade':^15} | {'17':^9} |")
print(f"| {'Altura':^15} | {'161cm':^9} |")

# MULTIPLICAÇÃO DE STRINGS

sus = '#'
estrela = '*'

print(sus*2, estrela*10, sus*2)
print('='*16)