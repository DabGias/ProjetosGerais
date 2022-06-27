print("Bem-vindo ao app do challenge!!!")
print("-" * 40)
print("{}Cadastro{}".format('\033[33m', '\033[0;0m'))
nomeCadastro = input("Digite seu nome: ").upper().strip()
senhaCadastro = input("Digite sua senha: ").strip()

while len(senhaCadastro) < 9:
    print("{}⚠{} {}Senha inválida!!! A senha deve ter mais de 8 caractéres!{} {}⚠{}"
          .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
    senhaCadastro = input("Reescreva sua senha: ").strip()

senhaConfirm = input("Confirme sua senha: ").strip()

while senhaConfirm != senhaCadastro:
    print("{}⚠{} {}A senha digitada é diferente da original!{} {}⚠{}"
          .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
    senhaConfirm = input("Confirme sua senha novamente: ").strip()
print("{}Sua senha de {} digitos foi confirmada!{}".format('\033[32m', len(senhaConfirm), '\033[0;0m'))

print("-" * 40)
print("{}Login{}".format('\033[33m', '\033[0;0m'))
nomeLogin = input("Digite o seu nome: ").upper().strip()

while nomeLogin != nomeCadastro:
    print("-" * 40)
    print("{}⚠{} {}Nome incorreto!!!{} {}⚠{}"
          .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
    nomeLogin = input("Digite o seu nome: ").upper()
    print("-" * 40)

senhaLogin = input("Digite sua senha: ")

while senhaLogin != senhaCadastro:
    print("-" * 40)
    print("{}⚠{} {}Senha incorreta!!!{} {}⚠{}"
          .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
    senhaLogin = input("Digite sua senha: ")
    print("-" * 40)

print("{}Acesso garantido!{}".format('\033[32m', '\033[0;0m'))

funcs = int(input("""App do challenge:
----------------------------------------
1 - Auto-análise;
2 - Feedback.
----------------------------------------
3 - Sair.

Escolha uma opção: """))

while funcs != 3:
    while funcs < 1 or funcs > 3:
        print("-" * 40)
        print("{}⚠{} {}Opção inválida!!!{} {}⚠{}"
              .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
        print("-" * 40)
        funcs = int(input("""App do challenge:
----------------------------------------
1 - Auto-análise;
2 - Feedback.
----------------------------------------
3 - Sair.

Escolha uma opção: """))

    if funcs == 1:
        print("-" * 40)
        print("{}Auto-análise{}".format('\033[33m', '\033[0;0m'))
        print("{} faça sua auto-análise, com notas de 1-5: ".format(nomeLogin.title()))

        python = int(input("Python: "))
        while python < 1 or python > 5:
            print("{}⚠{} {}Nota inválida, a nota digitada deve ser entre 1 e 5!{} {}⚠{}"
                  .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
            python = int(input("Python: "))

        sql = int(input("SQL: "))
        while sql < 1 or sql > 5:
            print("{}⚠{} {}Nota inválida, a nota digitada deve ser entre 1 e 5!{} {}⚠{}"
                  .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
            sql = int(input("SQL: "))

        java = int(input("Java: "))
        while java < 1 or java > 5:
            print("{}⚠{} {}Nota inválida, a nota digitada deve ser entre 1 e 5!{} {}⚠{}"
                  .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
            java = int(input("Java: "))

        web = int(input("Dev. Web (HTML/CSS/JavaScript): "))
        while web < 1 or web > 5:
            print("{}⚠{} {}Nota inválida, a nota digitada deve ser entre 1 e 5!{} {}⚠{}"
                  .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
            web = int(input("Dev. Web (HTML/CSS/JavaScript): "))

        chatbot = int(input("ChatBot: "))
        while chatbot < 1 or chatbot > 5:
            print("{}⚠{} {}Nota inválida, a nota digitada deve ser entre 1 e 5!{} {}⚠{}"
                  .format('\033[33m', '\033[0;0m', '\033[31m', '\033[0;0m', '\033[33m', '\033[0;0m'))
            chatbot = int(input("ChatBot: "))

        print("A sua média é de: {}{}{}".format('\033[32m', (python + sql + java + web + chatbot) / 5, '\033[0;0m'))

    if funcs == 2:
        print("{}Feedback{}".format('\033[33m', '\033[0;0m'))
        print("""Feedback da sua situação em relação a vaga concorrida: 
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur est inventore quia a impedit corporis accusamus 
iste exercitationem delectus, quisquam dicta repellat cumque, illo recusandae voluptatem, quasi accusantium tenetur 
nesciunt. Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia, ipsa eum architecto ducimus quidem labore 
exercitationem atque corporis consequatur veritatis quisquam minima animi dolorem quo distinctio laborum earum harum.""")
        print("-" * 40)

    funcs = int(input("""App do challenge:
----------------------------------------
1 - Auto-análise;
2 - Feedback.
----------------------------------------
3 - Sair.

Escolha uma opção: """))

print("Você saiu da aplicação!")
