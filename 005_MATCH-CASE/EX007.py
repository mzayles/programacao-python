# VERSÃO 007.1

letra = input("Digite uma letra: ").lower()

if len(letra) == 1: # verificar se o usuário digitou um número ou mais
    match letra:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print("\n\033[32mÉ uma vogal")
        case _ if letra.isalpha():
            print("\n\033[32mÉ uma consoante")
        case _:
            print("\n\033[31mNão é uma vogal")
else:
    print("Digite apenas uma letra...")