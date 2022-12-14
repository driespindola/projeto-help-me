class Solicitacao:

    def __init__(self, tipo,descricao, solic):
        self.tipo = tipo
        self.descricao = descricao
        self.tipo_solicitacao(self.tipo)
        self.descreva_solic(self.descricao)


    def registrar(self,registro):
        registro = 0
        self.registro = registro
        self.registro = self.registro +1
        return  self.registro

    def tipo_solicitacao(self,tipo):

        self.tipo = tipo

        print("por favor insira a area de sua solicitcão")
        self.tipo = int(input("Por favor digite um dos numeros a seguir referentes a sua solicitação"
                              "1 para TI, 2 para RH, 3 area de comercio,\n4 Para a area de gerenciamento,"
                              "5 Para a area Fiscal, 6 Para a area de Marketing,"
                              "7 Para outro tipo de Solicitação:"))

        if(self.tipo == 1):
            print("Bem vindo a area de TI")


        elif(self.tipo == 2):
            print("Bem vindo a area de RH")

        elif(self.tipo == 3):
            print("Bem vindo ao setor comercial")


        elif(self.tipo == 4):
            print("Bem vindo a area de gerenciamento")


        elif(self.tipo == 5):
            print("Bem vindo a area fiscal")

        elif(self.tipo == 6):
            print("Bem vindo a area de Marketing")

        elif(self.tipo == 7):
            print("sua solicitação não se referre a uma area especifica")


        else:
            print("Esse digito não corresponde a nenhuma Solicitação, por favor digite um numero valido")
            while(self.tipo != 1 or self.tipo != 2 or self.tipo != 3 or self.tipo != 4 or self.tipo != 5
                  or self.tipo != 6 or self.tipo != 7):
                      self.tipo = int(input("Por favor digite um dos numeros a seguir referentes a sua solicitação"
                                            "1 para TI, 2 para RH, 3 area de comercio,\n4 Para a area de gerenciamento,"
                                            "5 Para a area Fiscal, 6 Para a area de Marketing,"
                                            "7 Para outro tipo de Solicitação:"))

        return self.tipo


    def descreva_solic(self, descricao):
        self.descricao = descricao
        self.descricao = str(input("Por favor descreva a natureza de sua solicitação:"))

        return self.descricao