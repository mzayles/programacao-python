# CRAPS GAME

import random
import time
from google.colab import output

dado = 0
alvo = 0
tentativa = 0

def jogar():
    global dado, alvo, tentativa

    nome = input("🚀 Bem-vindo(a) ao jogo de sorte \033[1mCraps\033[0m, jogador! Antes de iniciarmos, informe seu \033[1;4mnome\033[0m: ")

    print(f"\nÓtimo \033[1m{nome.capitalize()}\033[0m! No Craps, você lançará um dado que varia entre \033[1m2 e 12\033[0m. \n📜 Agora, preste atenção nas \033[1mregras\033[0m:")
    print("""\n    🏆 Se tirar \033[1m7 ou 11\033[0m na primeira jogada, você \033[1mganha\033[0m!
    💀 Se tirar \033[1m2, 3 ou 12\033[0m, você \033[1mperde\033[0m.
    🎯 Se tirar \033[1m4, 5, 6, 8, 9 ou 10\033[0m, esse será seu \033[1mnúmero-alvo\033[0m e seu objetivo é tirá-lo novamente para \033[1mvencer\033[0m.
    ⚔️ Caso tire o número \033[1m7\033[0m como \033[1malvo\033[0m, você \033[1mperde\033[0m.""")
    time.sleep(1)
    print(f"\n\033[1mBoa sorte no jogo, {nome.capitalize()}! Vamos começar.\033[0m")
    time.sleep(1)

    def lancarDados():
        global dado

        while True:
            usuario = input("""\n    💚🎲 \033[1m[L]\033[0m Lançar dados | 🏡 \033[1m[S]\033[0m Sair do jogo\n\n""").upper()

            if usuario == 'L':
                dado = random.randint(2, 12)

                print("🎲 Lançando dados", end="")
                time.sleep(0.5)
                print('.', end="")
                time.sleep(0.5)
                print('.', end="")
                time.sleep(0.5)
                print('.\n', end="")

                print(f"\nNúmero lançado no dado: {dado}")
                return True
            elif usuario == 'S':
                print(f"👋 Obrigado(a) por jogar o Craps, \033[1m{nome.capitalize()}\033[0m. Até mais!")
                return False
    if not lancarDados():
        return

    def jogarNovamente():
            while True:
                opcao = input("\nDeseja jogar novamente? ✅ [S] Sim ou ❎ [N] Não: ").upper()

                if opcao != 'S' and opcao != 'N':
                    print("💔 \033[1mDigite algo válido! Somente [S] ou [N]\033[0m.")
                    continue
                if opcao == 'N':
                    print(f"👋 Obrigado(a) por jogar o Craps, \033[1m{nome.capitalize()}\033[0m. Até mais!")
                    break
                output.clear()
                jogar()
                break

    def dados():
        global alvo, tentativa

        while True:
            if dado == 7 or dado == 11:
                print("\033[1mParabéns! Você ganhou.\033[0m")
                jogarNovamente()
                break
            elif dado == 2 or dado == 3 or dado == 12:
                print("💔 \033[1mCraps! Você perdeu.\033[0m")
                jogarNovamente()
                break
            elif dado == 4 or dado == 5 or dado == 6 or dado == 8 or dado == 9 or dado == 10:
                alvo = dado
                time.sleep(0.5)
                print(f"\n🎯 Opa! Você achou o seu \033[1mnúmero-alvo: {alvo}\033[0m. Agora o seu objetivo é encontrá-lo novamente ao lançar os dados.\n"
                      "\033[1mMas lembre-se, o número 7\033[0m agora é o seu \033[1minimigo\033[0m. ⚔️\n")
                time.sleep(3)
                print(f"\033[1m    ----------- Ranking de Troféus 🎖️ -----------\033[0m\n")
                time.sleep(1)
                print("""    🏆 \033[1mMenos de 3 tentativas:\033[0m Lenda do Crap
    🥇 \033[1mMenos de 5 tentativas:\033[0m Mestre dos Dados
    🥈 \033[1mMenos de 10 tentativas:\033[0m Jogador Experiente
    🥉 \033[1m\033[0m10 ou mais tentativas:\033[0m Aprendiz do Crap""")
                time.sleep(1)

                while True:
                    if not lancarDados():
                        return

                    if dado == alvo:
                        tentativa += 1

                        if tentativa < 4:
                            time.sleep(1)
                            print(f"\n🎉 \033[1mParabéns! Você ganhou.\033[0m \nAchou o seu número-alvo \033[1m[{alvo}]\033[0m em {tentativa} tentativas." if tentativa != 1
                                    else f"\n🎉 \033[1mParabéns! Você ganhou.\033[0m \nAchou o seu número-alvo \033[1m[{alvo}]\033[0m de primeira.")
                            print("\033[1mTroféu:\033[0m 🏆 Lenda do Crap")
                            jogarNovamente()
                        elif tentativa < 7:
                            time.sleep(1)
                            print(f"\n🎉 \033[1mParabéns! Você ganhou.\033[0m \nAchou o seu número-alvo \033[1m[{alvo}]\033[0m em {tentativa} tentativas.")
                            print("\033[1mTroféu:\033[0m 🥇 Mestre dos Dados")
                            jogarNovamente()
                        elif tentativa < 11:
                            time.sleep(1)
                            print(f"\n🎉 \033[1mParabéns! Você ganhou.\033[0m \nAchou o seu número-alvo \033[1m[{alvo}]\033[0m em {tentativa} tentativas.")
                            print("\033[1mTroféu:\033[0m 🥈 Jogador Experient")
                            jogarNovamente()
                        elif tentativa > 10:
                            time.sleep(1)
                            print(f"\n🎉 \033[1mParabéns! Você ganhou.\033[0m \nAchou o seu número-alvo \033[1m[{alvo}]\033[0m em {tentativa} tentativas.")
                            print("\033[1mTroféu:\033[0m 🥉 Aprendiz do Crap")
                            jogarNovamente()
                        break
                    elif dado == 7:
                        time.sleep(1)
                        print("💔 \033[1mCraps! Você perdeu.\033[0m")
                        jogarNovamente()
                        break
                    else:
                        tentativa += 1
                        print("🔄 Errou. Continuando", end="")
                        time.sleep(0.5)
                        print('.', end="")
                        time.sleep(0.5)
                        print('.', end="")
                        time.sleep(0.5)
                        print('.\n', end="")
                break
    dados()
jogar()