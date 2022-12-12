class Solicitacao:

    def __init__(self):
        self.definir_tipo()


    def definir_tipo(self):
        print("por favor insira o tipo de sua solicitcão")
        tipo = int(input("1 Solocitação para o TI,2 Solocitação para o RH,3 Solocitação de comercio,"
                         "4 Solocitação para a area de gerenciamento, 5 Solocitação para area fiscal,"
                         "6 Solocitação para a area de Marketing, 7 Outro tipo de Solocitação:"))
        if(tipo == 1):
            print("Bem vindo a area de TI, por favor nos informe a natureza de sua solicitação")
        if (tipo == 2):
            print("Bem vindo a area de RH, por favor nos informe a natureza de sua solicitação")
        if (tipo == 3):
            print("Bem vindo ao setor comercial, por favor nos informe a natureza de sua solicitação")
        if (tipo == 4):
            print("Bem vindo a area de gerenciamento, por favor nos informe a natureza de sua solicitação")
        if (tipo == 5):
            print("Bem vindo a area fiscal por favor nos informe a natureza de sua solicitação")
        if (tipo == 6):
            print("Bem vindo a area de Marketing por favor nos informe a natureza de sua solicitação")
        if (tipo == 7):
            print("por favor nos informe a natureza de sua solicitação")