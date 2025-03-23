# DESAFIO 010

""" Imprima uma árvore de Natal como no exemplo utilizando a multiplicação
de Strings.
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
         ***
         ***
         *** """

estrela = '*'
espaco = ' '

print(f"{espaco * 8} {estrela}")
print(f"{espaco * 7} {estrela * 3}")
print(f"{espaco * 6} {estrela * 5}")
print(f"{espaco * 5} {estrela * 7}")
print(f"{espaco * 4} {estrela * 9}")
print(f"{espaco * 3} {estrela * 11}")
print(f"{espaco * 2} {estrela * 13}")
print(f"{espaco * 1} {estrela * 15}")
print(f"{espaco * -1} {estrela * 17}")
print(f"{espaco * 7} {estrela * 3}")
print(f"{espaco * 7} {estrela * 3}")
print(f"{espaco * 7} {estrela * 3}")

print(f"\n\033[32m{espaco * 8} {estrela}")
print(f"{espaco * 7} {estrela * 3}")
print(f"{espaco * 6} {estrela * 5}")
print(f"{espaco * 5} {estrela * 7}")
print(f"{espaco * 4} {estrela * 9}")
print(f"{espaco * 3} {estrela * 11}")
print(f"{espaco * 2} {estrela * 13}")
print(f"{espaco * 1} {estrela * 15}")
print(f"{espaco * -1} {estrela * 17}\033[0m")
print(f"\033[31m{espaco * 7} {estrela * 3}")
print(f"{espaco * 7} {estrela * 3}")
print(f"{espaco * 7} {estrela * 3}")

print(f"\n{espaco * 8}\033[32m\033[42m{estrela}\033[0m")
print(f"{espaco * 7}\033[32m\033[42m{estrela * 3}\033[0m")
print(f"{espaco * 6}\033[32m\033[42m{estrela * 5}\033[0m")
print(f"{espaco * 5}\033[32m\033[42m{estrela * 7}\033[0m")
print(f"{espaco * 4}\033[32m\033[42m{estrela * 9}\033[0m")
print(f"{espaco * 3}\033[32m\033[42m{estrela * 11}\033[0m")
print(f"{espaco * 2}\033[32m\033[42m{estrela * 13}\033[0m")
print(f"{espaco * 1}\033[32m\033[42m{estrela * 15}\033[0m")
print(f"{espaco * -1}\033[32m\033[42m{estrela * 17}\033[0m")
print(f"{espaco * 7}\033[31m\033[41m{estrela * 3}\033[0m")
print(f"{espaco * 7}\033[31m\033[41m{estrela * 3}\033[0m")
print(f"{espaco * 7}\033[31m\033[41m{estrela * 3}\033[0m")