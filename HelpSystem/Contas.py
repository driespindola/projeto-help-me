class Conta:
    def __init__(self):
        self.Defina_Nome()
        self.Defina_Senha()
        self.Defina_Area()




    def Defina_Nome(self):
        nome = str(input("Digite seu nome completo:"))
        if(len(nome)< 4 & len(nome)>= 20):
          if(len(nome) < 4):
            print("Nome invalido por não atender o requisito minimo de characteres")
            nome = str(input("Digite seu nome completo:"))
          elif(len(nome) >= 20):
            print("Nome invalido por ultrapasar o limite de characteres")
            nome = str(input("Digite seu nome completo:"))
        else:
            return nome



    def Defina_Senha(self):
        senha = str(input("Digite sua senha:"))
        if(len(senha) < 5):
            print("Senha invalida, a senha requer 5 um minimo caracteres nescessarios")
            senha = str(input("Digite sua senha:"))
        elif(len(senha)>20):
            print("Senha invalida, a senha ultrapasa o limiti de caracteres permitido")
        return senha



    def Defina_Area(self):
        codigo = int(input("Digite o Código de sua Area:"))
        if (codigo == 1000):
             print("area de TI")

        elif (codigo == 1001):
             print("area de RH")

        elif (codigo == 1002):
             print("area de Comércio")

        elif (codigo == 1003):
             print("area de Geranciamento")

        elif (codigo == 1004):
             print("area Fiscal")

        elif (codigo == 1005):
             print("area de Marketing")

        else:
            print("código invalido")
            if (codigo != 1000 or 1001 or 1002 or 1003 or 1004 or 1005):
                   codigo = int(input("Digite o Código de Sua area:"))

        return codigo
        return area
