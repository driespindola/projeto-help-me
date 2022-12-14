class Solicitacao:

    def __init__(self, tipo):
        self.tipo = tipo
        self.definir_tipo(tipo)


    def definir_tipo(self,tipo):
        self.tipo = tipo
        print("por favor insira o tipo de sua solicitcão")
        self.tipo = int(input("1 Solocitação para o TI,2 Solocitação para o RH,3 Solocitação de comercio,"
                         "4 Solocitação para a area de gerenciamento, 5 Solocitação para area fiscal,"
                         "6 Solocitação para a area de Marketing, 7 Outro tipo de Solocitação:"))
        if(self.tipo == 1):
            print("Bem vindo a area de TI, por favor nos informe a natureza de sua solicitação")
        elif (self.tipo == 2):
            print("Bem vindo a area de RH, por favor nos informe a natureza de sua solicitação")
        elif (self.tipo == 3):
            print("Bem vindo ao setor comercial, por favor nos informe a natureza de sua solicitação")
        elif (self.tipo == 4):
            print("Bem vindo a area de gerenciamento, por favor nos informe a natureza de sua solicitação")
        elif (self.tipo == 5):
            print("Bem vindo a area fiscal por favor nos informe a natureza de sua solicitação")
        elif (self.tipo == 6):
            print("Bem vindo a area de Marketing por favor nos informe a natureza de sua solicitação")
        elif (self.tipo == 7):
            print("por favor nos informe a natureza de sua solicitação")
        else:
            print("Esse digito não corresponde a nenhuma Solicitação, por favor digite um numeto valido")
            while(self.tipo != 1 or self.tipo != 2 or self.tipo != 3 or self.tipo != 4 or self.tipo != 5
                  or self.tipo != 6 or self.tipo != 7):
                      self.tipo = int(input("1 Solocitação para o TI,2 Solocitação para o RH,3 Solocitação de comercio,"
                                       "4 Solocitação para a area de gerenciamento, 5 Solocitação para area fiscal,"
                                       "6 Solocitação para a area de Marketing, 7 Outro tipo de Solocitação:"))