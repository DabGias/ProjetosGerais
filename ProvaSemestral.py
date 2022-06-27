proCod = []
proNome = []
proSetor = []
proPreco = []
proQuant = []
proCodComprado = []
proNomeComprado = []
proPrecoComprado = []
proQuantComprado = []
consulta = 0

opc = int(input("""|--------- Menu de Opções ---------|
1 – Cadastrar produto
2 – Alterar produto
3 – Comprar produto
4 – Relatório de produtos cadastrados
5 – Relatório de produtos comprados
6 – Sair

Escolha uma opção: """))

while opc != 6:
    while opc < 1 or opc > 6:
        print("Opção inválida!!!")
        opc = int(input("""|--------- Menu de Opções ---------|
1 – Cadastrar produto
2 – Alterar produto
3 – Comprar produto
4 – Relatório de produtos cadastrados
5 – Relatório de produtos comprados
6 – Sair

Escolha uma opção: """))

    if opc == 1:
        print("|--------- Cadastrando Produto ---------|")
        senha = input("Senha: ")
        while senha != "RW@aDmin":
            print("Senha incorreta!!!")
            senha = input("Senha: ")

        cod = int(input("Qual o código do produto? "))
        while cod in proCod:
            print("Opção inválida!!!")
            print("O código deve ser único!")
            cod = int(input("Redigite o código do produto: "))
        proCod.append(cod)

        nome = input("Qual o nome do produto? ").upper().strip()
        proNome.append(nome)

        setor = input("Qual o setor do produto? ").upper().strip()
        while setor != "ACADEMIA E FITNESS" and setor != "BOX E ARTES MARCIAIS" and setor != "CICLISMO":
            print("Opção inválida!!!")
            print("As opções disponíveis para setor são: Academia e Fitness, Box e Artes Marciais e Ciclismo!")
            setor = input("Qual o setor do produto? ").upper().strip()
        proSetor.append(setor)

        preco = float(input("Qual o preço do produto? "))
        while preco <= 0:
            print("Opção inválida!!!")
            print("O preço deve ser maior que 0!")
            preco = float(input("Qual o preço do produto? "))
        proPreco.append(preco)

        quant = int(input("Qual a quantidade desse produto? "))
        while quant < 0:
            print("Opção inválida!!!")
            print("Quantidade não pode ser menor que 0!")
            quant = int(input("Qual a quantidade desse produto? "))
        proQuant.append(quant)

    if opc == 2:
        print("|--------- Alterando Produto ---------|")
        senha = input("Senha: ")
        while senha != "RW@aDmin":
            print("Senha incorreta!!!")
            senha = input("Senha: ")

        altCod = int(input("Qual o código do produto que gostaria de alterar? "))
        if altCod not in proCod:
            print("Opção inálida!!!")
            print("Código inexistente!")
        else:
            for i in range(len(proCod)):
                if proCod[i] == altCod:
                    consulta = i

            alt = int(input("O que gostaria de alterar no produto de código {}?(1 - Preço / 2 - Quantidade) "
                            .format(proCod[consulta])))
            while alt != 1 and alt != 2:
                print("Opção inválida!!!")
                alt = int(input("O que gostaria de alterar no produto de código {}?(1 - Preço / 2 - Quantidade) "
                                .format(proCod[consulta])))

            if alt == 1:
                novoPreco = float(input("Qual o novo preço do produto? "))
                while novoPreco <= 0:
                    print("Opção inválida!!!")
                    print("O preço deve ser maior que 0!")
                    novoPreco = float(input("Redigite o novo preço do produto: "))
                print("Mudando o preço do produto de nome '{}' e preço R${:.2f}"
                      .format(proNome[consulta].capitalize(), proPreco[consulta]), end=" ")
                proPreco[consulta] = novoPreco
                print("para o preço de R${:.2f}".format(proPreco[consulta]))

            if alt == 2:
                novaQuantidade = int(input("Qual a nova quantidade de produtos? "))
                while novaQuantidade < 0:
                    print("Opção inválida!!!")
                    print("A quantidade deve ser maior que 0!")
                    novaQuantidade = int(input("Redigite a nova quantidade de produtos: "))
                print("Mudando a quantidade de produto de nome '{}' e quantidade {}"
                      .format(proNome[consulta].capitalize(), proQuant[consulta]), end=" ")
                proQuant[consulta] = novaQuantidade
                print("para a quantidade de {}".format(proQuant[consulta]))

    if opc == 3:
        print("|--------- Comprando Produto ---------|")
        novaCompra = 1

        while novaCompra == 1:
            procuraProduto = input("Qual o nome do produto que deseja comprar? ").upper().strip()
            if procuraProduto not in proNome:
                print("Opção inálida!!!")
                print("Produto inexistente!")
            else:
                for i in range(len(proNome)):
                    if proNome[i] == procuraProduto:
                        print("Código: {} Nome: {}".format(proCod[i], proNome[i].capitalize()))

                codCompra = int(input("Digite o código do produto que deseja comprar: "))
                if codCompra not in proCod:
                    print("Opção inválida!!!")
                    print("Produto não cadastrado!")
                else:
                    proCodComprado.append(codCompra)

                    for i in range(len(proCod)):
                        if proCod[i] == codCompra:
                            consulta = i
                    proNomeComprado.append(proNome[consulta])
                    proPrecoComprado.append(proPreco[consulta])

                    if proQuant[consulta] == 0:
                        print("Esse produto não está disponível no estoque!")
                    else:
                        quantCompra = int(input("Qual a quantidade de produtos de nome '{}' e quantidade {} que deseja comprar? "
                                                .format(proNome[consulta].capitalize(), proQuant[consulta])))
                        proQuantComprado.append(quantCompra)

                        while quantCompra <= 0 or quantCompra > proQuant[consulta]:
                            print("Opção inválida!!!")
                            print("A quantidade a ser comprada deve ser maior que zero e menor que o número máximo!")
                            quantCompra = int(input("Redigite a quantidade de produtos de nome '{}' e quantidade {} que deseja comprar: "
                                                    .format(proNome[consulta].capitalize(), proQuant[consulta])))
                        proQuant[consulta] = proQuant[consulta] - quantCompra
                        print("PRODUTOS SUGERIDOS: ")
                        for i in range(len(proSetor)):
                            if proSetor[i] == proSetor[consulta]:
                                print(proNome[i])

                        novaCompra = int(input("Deseja realizar outra compra?(1 - Sim / 2 - Não) "))
                        while novaCompra != 1 and novaCompra != 2:
                            print("Opção inválida!!!")
                            novaCompra = int(input("Deseja realizar outra compra?(1 - Sim / 2 - Não) "))

    if opc == 4:
        print("|--------- Relatório de Produtos ---------|")
        for i in range(len(proCod)):
            print("{} -".format(proCod[i]), end=" ")
            print("{} -".format(proNome[i]), end=" ")
            print("{} -".format(proSetor[i]), end=" ")
            print("{:.2f} -".format(proPreco[i]), end=" ")
            print("{}".format(proQuant[i]))

    if opc == 5:
        print("|--------- Relatório de Compra ---------|")
        soma = 0
        for i in range(len(proCodComprado)):
            print("{} -".format(proCodComprado[i]), end=" ")
            print("{} -".format(proNomeComprado[i]), end=" ")
            print("{:.2f} -".format(proPrecoComprado[i]), end=" ")
            print("{} -".format(proQuantComprado[i]), end=" ")
            print("{}".format(proPrecoComprado[i] * proQuantComprado[i]))
            soma = soma + (proPrecoComprado[i] * proQuantComprado[i])
        print(soma)

    opc = int(input("""|--------- Menu de Opções ---------|
1 – Cadastrar produto
2 – Alterar produto
3 – Comprar produto
4 – Relatório de produtos cadastrados
5 – Relatório de produtos comprados
6 – Sair

Escolha uma opção: """))

print("Saindo do programa!")
