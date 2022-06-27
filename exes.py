listJanela = []

for j in range(0, 24):
    listJanela.append(0)

listCorredor = []

for c in range(0, 24):
    listCorredor.append(0)

count = 0

print("=" * 40)
resp = int(input("""1 - Vender Passagem;
2 - Carcelar compra;
3 - Mostrar mapa de ocupação;
4 - Sair.

Escolha sua opção: """))

while resp != 4:
    while resp < 1 or resp > 4:
        print("{}Opção indisponível!!!{}".format('\033[31m', '\033[0;0m'))
        print("=" * 40)
        resp = int(input("""1 - Vender Passagem;
2 - Carcelar compra;
3 - Mostrar mapa de ocupação;
4 - Sair.

Escolha sua opção: """))

    for element in listJanela:
        if element == 1:
            count += 1

    for element in listCorredor:
        if element == 1:
            count += 1

    if resp == 1:
        if count < 48:
            print("=" * 40)
            fileira = int(input("Você deseja sentar em que fileira? (1 - Janela / 2 - Corredor) "))

            if fileira == 1:
                lugarJanela = int(input("Que lugar gostaria de sentar na fileira da janela? (0 ao 23) "))

                while lugarJanela > 23 or lugarJanela < 0:
                    print("{}Opção indisponível!!!{}".format('\033[31m', '\033[0;0m'))
                    lugarJanela = int(input("Que lugar gostaria de sentar na fileira da janela? (0 ao 23) "))

                if listJanela[lugarJanela] == 0:
                    print("{}Venda do acento {} realizada com sucesso!{}".format('\033[32m', lugarJanela, '\033[0;0m'))
                    listJanela[lugarJanela] = 1

                else:
                    while listJanela[lugarJanela] == 1:
                        print("{}Poltrona {} está ocupada!{}".format('\033[31m', lugarJanela, '\033[0;0m'))
                        lugarJanela = int(
                            input("Escolha outro lugar que gostaria de sentar na fileira da janela (0 ao 23): "))

                    print("{}Venda realizada com sucesso!{}".format('\033[32m', '\033[0;0m'))
                    listJanela[lugarJanela] = 1

            if fileira == 2:
                lugarCorredor = int(input("Que lugar gostaria de sentar na fileira do corredor? (0 ao 23) "))

                while lugarCorredor > 23 or lugarCorredor < 0:
                    print("{}Opção indisponível!!!{}".format('\033[31m', '\033[0;0m'))
                    lugarCorredor = int(input("Que lugar gostaria de sentar na fileira do corredor? (0 ao 23) "))

                if listCorredor[lugarCorredor] == 0:
                    print("{}Venda do acento {} realizada com sucesso!{}".format('\033[32m', lugarCorredor, '\033[0;0m'))
                    listCorredor[lugarCorredor] = 1

                else:
                    while listCorredor[lugarCorredor] == 1:
                        print("{}Poltrona {} está ocupada!{}".format('\033[31m', lugarCorredor, '\033[0;0m'))
                        lugarJanela = int(
                            input("Escolha outro lugar que gostaria de sentar na fileira do corredor (0 ao 23): "))

                    print("{}Venda realizada com sucesso!{}".format('\033[32m', '\033[0;0m'))
                    listCorredor[lugarCorredor] = 1
        else:
            print("{}Opção indisponível!!!{}".format('\033[31m', '\033[0;0m'))

    if resp == 2:
        if count > 0:
            print("=" * 40)
            fileira = int(input("Você deseja cancelar o acento em que fileira? (1 - Janela / 2 - Corredor) "))

            if fileira == 1:
                lugarJanela = int(input("Que acento gostaria de cancelar na fileira da janela? (0 ao 23) "))

                while lugarJanela > 23 or lugarJanela < 0:
                    print("{}Opção indisponível!!!{}".format('\033[31m', '\033[0;0m'))
                    lugarJanela = int(input("Que acento gostaria de cancelar na fileira da janela? (0 ao 23) "))

                if listJanela[lugarJanela] == 1:
                    print("{}Venda do acento {} cancelada com sucesso!{}".format('\033[32m', lugarJanela, '\033[0;0m'))
                    count -= 1
                    listJanela[lugarJanela] = 0

                else:
                    while listJanela[lugarJanela] == 0:
                        print("{}Poltrona {} não foi comprada!{}".format('\033[31m', lugarJanela, '\033[0;0m'))
                        lugarJanela = int(
                            input("Escolha outro lugar que gostaria de cancelar na fileira da janela (0 ao 23): "))

                    print("{}Cancelamento do acento {} realizada com sucesso!{}".format('\033[32m', lugarJanela, '\033[0;0m'))
                    count -= 1
                    listJanela[lugarJanela] = 0

            if fileira == 2:
                lugarCorredor = int(input("Que acento gostaria de cancelar na fileira da janela? (0 ao 23) "))

                while lugarCorredor > 23 or lugarCorredor < 0:
                    print("{}Opção indisponível!!!{}".format('\033[31m', '\033[0;0m'))
                    lugarCorredor = int(input("Que acento gostaria de cancelar na fileira da janela? (0 ao 23) "))

                if listCorredor[lugarCorredor] == 1:
                    print("{}Venda do acento {} cancelada com sucesso!{}".format('\033[32m', lugarCorredor, '\033[0;0m'))
                    count -= 1
                    listCorredor[lugarCorredor] = 0

                else:
                    while listCorredor[lugarCorredor] == 0:
                        print("{}Poltrona {} não foi comprada!{}".format('\033[31m', lugarCorredor, '\033[0;0m'))
                        lugarCorredor = int(
                            input("Escolha outro lugar que gostaria de cancelar na fileira da janela (0 ao 23): "))

                    print("{}Cancelamento do acento {} realizada com sucesso!{}".format('\033[32m', lugarCorredor, '\033[0;0m'))
                    count -= 1
                    listCorredor[lugarCorredor] = 0
        else:
            print("{}Opção indisponível!!!{}".format('\033[31m', '\033[0;0m'))

    if resp == 3:
        print("{}Fileira da janela: {}".format('\033[33m', '\033[0;0m'))
        for i in range(0, 24):
            if listJanela[i] == 1:
                print("Acento {} -> {}Ocupado{}".format(i, '\033[31m', '\033[0;0m'))
            else:
                print("Acento {} -> {}Livre{}".format(i, '\033[32m', '\033[0;0m'))

        print("{}Fileira do corredor: {}".format('\033[33m', '\033[0;0m'))
        for i in range(0, 24):
            if listCorredor[i] == 1:
                print("Acento {} -> {}Ocupado{}".format(i, '\033[31m', '\033[0;0m'))
            else:
                print("Acento {} -> {}Livre{}".format(i, '\033[32m', '\033[0;0m'))

    print("=" * 40)
    resp = int(input("""1 - Vender Passagem;
2 - Carcelar compra;
3 - Mostrar mapa de ocupação;
4 - Sair.

Escolha sua opção: """))

print("Saindo da aplicação...")
