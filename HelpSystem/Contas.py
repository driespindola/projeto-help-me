class Conta:
    def __init__(self, nome, senha, codigo):
        self.nome = nome
        self.senha = senha
        self.codigo = codigo
        self.Defina_Nome(self.nome)
        self.Defina_Senha(self.senha)
        self.Defina_Area(self.codigo)



    def Defina_Nome(self, nome):
        self.nome = nome
        self.nome = str(input("Digite seu nome completo:"))

        if(len(self.nome)<4 or len(self.nome) > 20):
           while(len(self.nome) <4 or len(self.nome)> 20):
               if(len(self.nome) == 0):
                   print("Nome não pode estar em branco")
                   self.nome = str(input("Digite seu nome completo:"))
               elif (len(self.nome) < 4):
                   print("Nome invalido, o Nome não pode ter menos do que o minimo de 4 caracteres")
                   self.nome = str(input("Digite seu nome completo:"))
               elif (len(self.nome) > 20):
                   print("Nome invalido, o Nome não pode passar do limite de caracteres")
                   self.nome = str(input("Digite seu nome completo:"))
        else:
            return self.nome


    def Defina_Senha(self, senha):
        self.senha = senha
        self.senha = str(input("Digite sua senha:"))

        if(len(self.senha) < 6 or len(self.senha) > 9):
            while(len(self.senha) < 6 or len(self.senha) > 9):
                if(len(self.senha) == 0):
                    print("Senha invalida, você não ter uma senha vazia")
                    self.senha = str(input("Digite sua senha:"))
                elif(len(self.senha) < 6):
                    print("Senha invalida, a senha requer 5 um minimo caracteres nescessarios")
                    self.senha = str(input("Digite sua senha:"))
                elif(len(self.senha) > 9):
                    print("Senha invalida, a senha ultrapasa o limiti de caracteres permitido")
                    self.senha = str(input("Digite sua senha:"))
        else:
            return senha


    def Defina_Area(self,codigo):
        self.codigo = codigo
        self.codigo = str(input("Digite o Código de sua Area:"))

        if not(self.codigo =="1000" or self.codigo =="1001" or self.codigo =="1002" or
               self.codigo == "1003" or self.codigo == "1004" or self.codigo == "1005"):
            while not(self.codigo in codigo):
                print("código invalido")
                self.codigo = str(input("Digite o Código de Sua area:"))

                if (self.codigo == "1000"):
                    print("Bem vindo a area de TI")
                    break

                if (self.codigo == "1001"):
                    print("Bem vindo a area de RH")
                    break

                if (self.codigo == "1002"):
                    print("Bem vindo a area de Comércio")
                    break

                if (self.codigo == "1003"):
                    print("Bem vindo a area de Geranciamento")
                    break

                if (self.codigo == "1004"):
                    print("Bem vindo a area Fiscal")
                    break

                if (self.codigo == "1005"):
                    print("Bem vindo a area de Marketing")
                    break

        elif (self.codigo == "1000"):
            print("Bem vindo a area de TI")

        elif (self.codigo == "1001"):
            print("Bem vindo a area de RH")

        elif (self.codigo == "1002"):
            print("Bem vindo a area de Comércio")

        elif (self.codigo == "1003"):
            print("Bem vindo a area de Geranciamento")

        elif (self.codigo == "1004"):
            print("Bem vindo a area Fiscal")

        elif (self.codigo == "1005"):
            print("Bem vindo a area de Marketing")

        return self.codigo