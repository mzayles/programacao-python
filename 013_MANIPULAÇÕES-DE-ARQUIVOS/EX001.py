# DESAFIO 001

""" Crie um sistema de login que faça a leitura do arquivo login.txt que está na seguinte disposição:
root
1234
Leandro Toniati
Caso digite o login(root) e senha(1234) buscando as informações no arquivo, será apresentada
uma mensagem de boas vindas com o nome do usuário, caso contrário informe 'Usuário ou senha não conferem' """

import getpass
arq = 'login.txt'

with open(f"{caminho}/{arq}", 'r') as arquivo:
    texto = arquivo.readlines()

login = input("Login: ")
senha = getpass.getpass("Senha: ")

log = texto[0].strip('\n')
sen = texto[1].strip('\n')
usu = texto[2].strip('\n')

if login == log and senha == sen:
    print(f"Seja bem-vindo {usu}!")
else:
    print("Login ou senha inválidos...")

# VERSÃO 001.1

import getpass
arq = 'login.txt'

with open(f"{caminho}/{arq}", 'r') as arquivo:
    lista = arquivo.readlines()

tentativas = 1
verifica = True
while verifica:
    if tentativas > 3:
        print("Você excedeu o número de tentativas...")
        break
    login       = input("Login: ")
    senha       = getpass.getpass("Senha: ")
    usuario     = lista[0].strip('\n')
    senhaUser   = lista[1].strip('\n')
    nomeUser    = lista[2].strip('\n')
    if login == usuario and senha == senhaUser:
        print(f"\nSeja bem-vindo, {nomeUser}!")
        verifica = False
    else:
        print(f"Login ou Senha incorretos")
        print(f"Tentativa ({tentativas}/3)\n\n")
    tentativas += 1