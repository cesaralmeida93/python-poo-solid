class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):
        print('Estou Correndo')

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')

    def __apresentar_documento(self):
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo', 32, '468464846465')
ronaldo.beber('cerveja')
ronaldo.beber('coca-cola')
