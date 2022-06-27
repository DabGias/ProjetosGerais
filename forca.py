import random


def jogar():

    boas_vindas()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicia_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        tentativa = pede_tentativa()

        if tentativa in palavra_secreta:
            marca_chute_correto(palavra_secreta, tentativa, letras_acertadas)
        else:
            erros = erros + 1
            imagem_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_vitoria()
    else:
        imprime_derrota(palavra_secreta)
    print("Fim de jogo!")


def boas_vindas():

    print("********************************")
    print("***Bem-vindo ao jogo da forca***")
    print("********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicia_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pede_tentativa():
    tentativa = input("Qual letra deseja adivinhar? ")
    tentativa = tentativa.strip().upper()
    return tentativa


def marca_chute_correto(palavra_secreta, tentativa, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if tentativa == letra:
            letras_acertadas[index] = letra
        index = index + 1


def imprime_vitoria():
    print("Você ganhou!!!")


def imprime_derrota(palavra_secreta):
    print("Você perdeu.")
    print("A palavra era", palavra_secreta)


def imagem_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


if __name__ == "__main__":
    jogar()
