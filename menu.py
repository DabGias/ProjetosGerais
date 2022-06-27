import adivinhação
import forca


def escolhe_jogo():
    print("********************************")
    print("******Bem-vindo ao menu*********")
    print("********************************")

    jogos = int(input("Selecione seu jogo: (1) Adivinhação e (2) Forca: "))
    if jogos == 1:
        print("Você selecionou: Adivinhação.")
        adivinhação.jogar()
    if jogos == 2:
        print("Você selecionou: Forca.")
        forca.jogar()


if __name__ == "__main__":
    escolhe_jogo()
