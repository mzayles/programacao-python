# DESAFIO 009

""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final  do programa mostre:
	A média de idade do grupo
	Qual é o nome do homem mais velho
	Quantas mulheres tem menos de 20 anos """

media = 0
maior = 0
mulher = 0

for i in range(1, 5):
    nome = input(f"🔎 \033[1;34m{i}º Indivíduo:\033[0m digite seu nome: ").lower()
    idade = int(input(f"🔎 \033[1;34m{i}º Indivíduo:\033[0m digite sua idade: "))
    sexo = input(f"🔎 \033[1;34m{i}º Indivíduo:\033[0m digite seu sexo: ").lower()
    print()

    media = idade / i

    if sexo == 'masc':
        if idade > maior:
            nome_homem = nome
            maior = idade
    if sexo == 'fem':
        if idade < 20:
            mulher += 1

print(f"✅ A média de \033[1;34midade\033[0m dessas 4 pessoas é de {media:,.2f}.")
print(f"✅ O homem mais \033[1;34mvelho\033[0m se chama {nome_homem.capitalize()} e tem {maior} anos." if maior > 0 else "✅ Nenhum \033[1;34mhomem\033[0m cadastrado.") # operador ternário
print(f"✅ A quantidade de \033[1;34mmulheres\033[0m com menos de 20 anos é {mulher}." if mulher > 0 else "✅ Nenhuma \033[1;34mmulher\033[0m cadastrada.")

# VERSÃO 009.1

media = 0
idade_homem = 0
nome_homem = "Nenhum homem cadastrado"
mulher_menos_20 = 0

for i in range(1, 5):
    nome = input(f"Digite o {i}º nome: ")
    idade = int(input(f"Digite a {i}ª idade: "))
    sexo = input(f"Digite [F] ou [M] para o {i}º sexo: ").upper()
    print()
    media += idade
    if sexo == 'M' and idade > idade_homem:
        idade_homem = idade
        nome_homem = nome
    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1

print(f"\nMédia de idade grupo: {media/4:,.0f} anos")
print(f"Homem mais velho: {nome_homem}")
print(f"{mulher_menos_20} mulher(es) menos 20 anos" if mulher_menos_20 > 0 else "Nenhuma mulher cadastrada")