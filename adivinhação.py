import random


def jogar():
    print("********************************")
    print("Bem-vindo ao jogo de adivinhação")
    print("********************************")

    rodada = 1
    numero_de_tentativas = 0
    total_de_tentativas = 0
    pontos = 1000
    dificuldade = int(input("Selecione a dificuldade (Fácil = 1, Médio = 2 e Difícil = 3): "))

    if dificuldade == 1:
        numero_de_tentativas = 20
        total_de_tentativas = 20
        print("Você selecionou: Fácil.")
    if dificuldade == 2:
        numero_de_tentativas = 10
        total_de_tentativas = 10
        print("Você selecionou: Médio.")
    if dificuldade == 3:
        numero_de_tentativas = 5
        total_de_tentativas = 5
        print("Você selecionou: Difícil.")
    numero_secreto = random.randrange(1, 101)
    while numero_de_tentativas > 0:
        print("Rodada", rodada, "de", total_de_tentativas)
        tentativa = input("Digite um número de 1 a 100: ")
        print("Você digitou", tentativa)
        numero = int(tentativa)
        acertou = numero == numero_secreto
        maior = numero > numero_secreto
        menor = numero < numero_secreto
        pontos_perdidos = abs(numero - numero_secreto)
        if acertou:
            print("Você acertou!")
            print("Você alcançou a pontuação de", pontos)
            numero_de_tentativas = 0
        else:
            if maior:
                print("Você errou, seu chute foi maior que o número secreto.")
            if menor:
                print("Você errou, seu chute foi menor que o número secreto.")
            if numero < 1 or numero > 100:
                print("Você digitou um número fora dos limites apresentados.")
        numero_de_tentativas = numero_de_tentativas - 1
        rodada = rodada + 1
        pontos = pontos - pontos_perdidos

    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()
