import os

class Inicio:
    gerar = []

    def __init__(self, matricula,codeOS,parecer_OS):
        self.matricula = matricula
        self.codeOS= codeOS
        self.parecer_OS= parecer_OS
        Gerar.gerar.append(self)
        pass

def exibir_nome_aplicação():
    print(25*'-')
    print(""" 𝘨𝘦𝘳𝘢𝘈𝘌 """)
    print(25*'-')
    pass

def menuprincipal():
    print('1. Gerar OS')
    print('2. Cancelar OS')
    print('3. Encerrar OS no retorno')
    ##print('4. Gerar produtividade')
    print('4. Sair')

def voltarMenuPrincipal():
    print ('Aperte enter para voltar ao menu principal: ')
    menuprincipal()

def opcaoinvalida():
    os.system('cls')
    print ('Ops! Parece que você digitou uma opção que não é válida. Vamos tentar novamente\n')
    input('Tecle enter para voltar ao menu principal: ')
    main()

def gerando_os():
    os.system('cls')
    print ('Legal! Vamos gerar sua OS ')
    pass

def encerrando_os():
    os.system('cls')
    print('Certo. Vamos encerrar esse serviço: ')
    pass

def cancelando_os():
    os.system('cls')
    print ('Ok. Vamos cancelar essa OS: ')
    pass

def sair_do_app():
    os.system('cls')
    print('Volte logo!!')

def choicer():
        menuprincipal()
        numchoice = (input('Escolha uma das opções acima: '))
        try:
            choice = int(numchoice)
            if choice == 1:
                        gerando_os()
            elif choice == 2:
                        cancelando_os()                
            elif choice == 3: 
                        encerrando_os()  
            elif choice == 4:
                        sair_do_app()                    
            else:
                opcaoinvalida()
        except:
              opcaoinvalida()

    
     



def main ():
    os.system('cls')
    exibir_nome_aplicação()
    choicer()



if __name__ == '__main__':
    main()