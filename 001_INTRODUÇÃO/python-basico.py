print("Hello, world!")
print("Mariana Alves")

""" Algorítmo Lanche

Passo 01: Crie uma lista de igredientes.
Passo 02: Separe pão, alface, queijo, peito de peru e tomate.
Passo 03: Pegue duas fatias de pão e coloque sob a mesa.
Passo 04: Coloque uma fatia lado a lado.
Passo 05: Lave o tomate e corte em três rodelas.
Passo 06: Lave três alfaces.
Passo 07: Corte uma fatia de peito de peru.
Passo 08: Coloque o alface em cima da pimeira fatia de pão.
Passo 09: Coloque o peito de peru em cima do alface.
Passo 10: Coloque queijo em cima do peito de peru.
Passo 11: Coloque os tomates em cima do queijo.
Passo 12: Pegue a a segunda fatia e coloque em cima dos tomates.
Passo 13: Coloque o sanduíche em um prato.
Passo 14: Deguste o lanche.

# Abstração Lógica: Cafeteira

Componente 01: Botões liga/desliga - serve para ligar e desligar a máquina.Componente 02: Copo para a água - local onde a água vai ferver.
Componente 03: Tampa com furos - vaporizador da água fervente.
Componente 04: Copo de igredientes - local para colocar o café e açucar.
Componente 05: Coador - local onde o café vai ser coado.
Componente 06: Copo para o café - local onde o café vai sair pronto para consumo.

# Lógica de programação: Barril

Passo 01: 1 litro do barril B para o barril A.
Passo 02: 3 litros do barril C para o barril A.

Assim, o barril A e B terá 4 litros cada e o barril C ficará vazio.
"""

# DESAFIO TROCA DE VARIÁVEIS

a = 5
b = 2
c = 0

c = a
a = b
b = c

print(a)
print(b)

# TROCA SIMULTÂNEA DE VARIÁVEIS

a = 5
b = 2
c = 0

a, b = b, a

print(a)
print(b)

# EXEMPLO 01: OPERADOR LÓGICO AND

nota = 7
frequencia = 72

if nota > 6 and frequencia >= 75:
    print('Aprovado')
else:
    print('Reprovado')

# EXEMPLO 02: EXERCÍCIO LÓGICO IDADE

idade = int(input("Digite sua idade: ")) # operador INT() e INPUT()

if idade >= 18:
    print("Pode votar")
else:
    print("Não pode votar")

# EXEMPLO DIAGRAMA: EXERCÍCIO DE MÉDIA

nota1 = 0
nota2 = 0
media = 0

nota1 = float(input("Digite a 1ª nota: ")) # operador FLOAT()
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2) / 2 # aritmética

if media >= 5:
    print('Aprovado')
else:
    print('Reprovado')

# EXEMPLO TESTE DE MESA (TABELA POWERPOINT)

x = 2
y = 3
z = x * y + y

print(z)

# OPERADORES ARITMÉTICOS

a = 10
b = 3

print(a +  b)     # 13      (adição)
print(a -  b)     # 7       (subtração)
print(a *  b)     # 30      (multiplicação)
print(a /  b)     # 3.3333  (divisão)
print(a // b)     # 3       (divisão inteira)
print(a %  b)     # 1       (módulo/resto da divisão)
print(a ** b)     # 1000    (exponenciação)
print(a ** (1/b)) # 2.14    (radiciação)

# OPERADORES RELACIONAIS OU DE COMPARAÇÃO

a = 10
b = 3

print(a == b)  # False  igual
print(a != b)  # True   diferente
print(a >  b)  # True   maior
print(a <  b)  # False  menor
print(a >= b)  # True   maior ou igual "usado como a partir de"
print(a <= b)  # False  menor ou igual "usado como a partir de"

# OPERADORES LÓGICOS

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# EXEMPLO OPERADORES LÓGICOS

nota = 5
falta = 25

if nota >= 5 and falta <= 25:
    print('Aprovado')
else:
    print('Reprovado')

# OPERADORES DE ATRIBUIÇÃO

a = 10
a += 2  # a = a + 2
print(a) # 12

b = 10
b -= 2  # b = b - 2
print(b) # 8

c = 10
c *= c  # c = c * c
print(c) # 100

d = 10
d /= 2 # d = d / 2
print(d) # 5.0

d = 10
d **= 2 # d = d ** 2
print(d) # 100

d = 10
d //= 2
print(d)

d = 10
d %= 2
print(d) # 5.0

# EXPRESSÕES

"""
1) PARÊNTESES
2) POTÊNCIA E RAIZ
3) MULTIPLICAÇÃO E DIVISÃO
4) ADIÇÃO E SUBTRAÇÃO
"""

print(2+2*5**2)
print((2+2)*5**2)
print(((2+2)*5)**2) # ordem: soma, multiplicação e potência.

# REFATORAÇÃO: melhorar o código sem alterar seu comportamento externo.

# ORIGINAL
a = 10
b = 20
c = a + b

print('Original', c)

# REFATORADO
def soma(x, y): # FUNÇÃO DEF(argumento1, argumento2)
    return x + y

print('Refatorado', soma(45, 48))