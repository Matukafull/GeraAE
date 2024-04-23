class Unidade:
    unidade = []
    def __init__(self, unidade, diretoria):
        self._unidade= unidade
        self._diretoria= diretoria
        Unidade.unidade.append()

    def listar_diretoria ():
        print("1. Guariroba")
        print("2. MT 1")
        print("3. MT 2")
        print("4. Governador Valadares")

    def listar_unidadeG():
        print("Unidade escolhida: Guariroba")

    def listar_unidadeMT1():
        print ("Sinop")
        print ("Sorriso")
        print ("Santa Carmem")
        print ("Marcelandia")
        print ("Claudia")
        print ("União do Sul")
        print ("Novo Progresso")
        print ("Peixoto de Azevedo")
        print ("Matupá")
        print ("Guarantã")
        print ("Carlinda")

    def listar_unidadeMT2():
        print ("Primavera do Leste")
        print ("Barra do Garças")
        print ("Pedra Preta")
        print ("Porto Espiridião")
        print ("Jauru")
        print ("Poconé")
        print ("Jangada")
        print ("Confresa")
        print ("São José")
        print ("Diamantino")
        print ("Nortelândia")
        print ("Campo Verde")
        print ("Paranatinga")

    def listar_unidadeGV():
        print("Unidade escolhida: GovernadorValadares")





@classmethod
def escolher_unidades(cls):
    unidade = input('Digite a opção ')