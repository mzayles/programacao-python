# ESTRUTURAS CONDICIONAIS

""" OPERADORES RELACIONAIS (OU DE COMPARAÇÃO)

>  MAIOR
<  MENOR
>= MAIOR OU IGUAL
<= MENOR OU IGUAL
== IGUAL
!= DIFERENTE """
 
# OPERADORES LÓGICOS

""" and | or | not | in | not in """

# BLOCO IF

x = 7

if x > 5:
    print("É maior que 5.")
    if x < 8:
        print("Também é menor que 8.")
if x == 10:
    print("X vale 10")

# BLOCO IF E ELSE

y = 10

if y != 8:
    print("É diferente de 8!")
else:
    print("É igual a 8!")

# BLOCO IF, ELIF E ELSE

z = 15

if z <= 10:
    print("Frio")
elif z <= 20:
    print("Morno")
elif z <= 30:
    print("Quente")
else:
    print("Muito quente")

# BLOCO COM AND

n = 15

if n >= 10 and n <= 20:
    print("N está entre 10 e 20.")
else:
    print("N não está entre 10 e 20.")

# BLOCO COM OR

casado = True
filhos = False

if casado or filhos:
    print("Corre!!!")
else:
    print("Livre para casar...")

# BLOCO COM IN

escola = "SENAI Ary Torres"

if 'Ary' in escola:
    print("Tem Ary no nome!")
else:
    print("Não tem Ary no nome!")

# BLOCO COM IN

escola = "SENAI Ary Torres"

if 'Ary' not in escola:
    print("Não tem Ary no nome!")
else:
    print("Tem Ary no nome!")

# NÃO UTILIZAR ESSA ESTRUTURA!!!

a = 3
b = 2
c = 1

if a > b > c:
    print("A é maior.")

# TRABALHAR COM EMOJIS

print("Where'd all the time go... 🌱")