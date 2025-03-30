# DESAFIO 004

""" Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o 999). """

qtd = 0
soma = 0

# usuário que para o programa
while True:
    numero = int(input("⏩ Digite qualquer \033[1;32mnúmero inteiro\033[0m: "))

    if numero == 999:
        print("\n💨 Programa encerrado.")
        break
    else:
        qtd += 1
        soma += numero

print(f"\n✅ \033[1;34mQuantidade\033[0m de números digitados: {qtd}")
print(f"✅ \033[1;34mSoma\033[0m entre os números digitados: {soma}")