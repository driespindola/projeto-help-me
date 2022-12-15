class Solicitacao():

    def __init__(self, tipo, descricao, gravidade):
        self.tipo = tipo
        self.descricao = descricao
        self.gravidade = gravidade
        self.tipo_solicitacao(self.tipo)
        self.descreva_solic(self.descricao, self.gravidade)

    def tipo_solicitacao(self, tipo):

        self.tipo = tipo

        self.tipo = int(input("Por favor digite um dos numeros a seguir referentes a sua solicitação"
                              "1 para TI, 2 para RH, 3 area de comercio,\n 4 Para a area de gerenciamento,"
                              "5 Para a area Fiscal, 6 Para a area de Marketing,"
                              "7 Para outro tipo de Solicitação:"))

        if (self.tipo == 1):
            self.tipo = "Area de TI"
            print("Bem vindo a area de TI")


        elif (self.tipo == 2):
            self.tipo = "Area de RH"
            print("Bem vindo a area de RH")

        elif (self.tipo == 3):
            self.tipo = "Setor Comerial"
            print("Bem vindo ao setor Comercial")


        elif (self.tipo == 4):
            self.tipo = "Area de Gerenciamento"
            print("Bem vindo a area de Gerenciamento")


        elif (self.tipo == 5):
            self.tipo = "Area Fiscal"
            print("Bem vindo a Area Fiscal")

        elif (self.tipo == 6):
            self.tipo = "Area de Marketing"
            print("Bem vindo a Area de Marketing")


        elif (self.tipo == 7):
            self.tipo = "Outra Area não especifica"
            print("sua solicitação não se referre a uma area especifica")


        else:
            print("Esse digito não corresponde a nenhuma Solicitação, por favor digite um numero valido")

            while (self.tipo != 1 or self.tipo != 2 or self.tipo != 3 or self.tipo != 4 or self.tipo != 5
                   or self.tipo != 6 or self.tipo != 7):
                self.tipo = int(input("Por favor digite um dos numeros a seguir referentes a sua solicitação"
                                      "1 para TI, 2 para RH, 3 area de comercio,\n4 Para a area de gerenciamento,"
                                      "5 Para a area Fiscal, 6 Para a area de Marketing,"
                                      "7 Para outro tipo de Solicitação:"))

        return self.tipo

    def descreva_solic(self, descricao, gravidade):
        self.descricao = descricao
        self.gravidade = gravidade

        self.descricao = str(input("Por favor descreva a natureza de sua solicitação:"))

        self.gravidade = int(input("Por favor indique o nivel de gravidade de sua solicitação\n"
                                   " 1 Pequena, 2 Moderada, 3 Consideravel, 4 Urgente, 5 Extrema Urgencia:"))

        if(self.gravidade == 1):
            self.gravidade = "Pequena Urgencia"

        if (self.gravidade == 2):
            self.gravidade = "Urgencia Moderada"

        if (self.gravidade == 3):
            self.gravidade = "Urgencia Consideravel"

        if (self.gravidade == 4):
            self.gravidade = "Urgente"

        if (self.gravidade == 5):
            self.gravidade = "Extrema Urgencia"

        return self.descricao
        return  self.gravidade