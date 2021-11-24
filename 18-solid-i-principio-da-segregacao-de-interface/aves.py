from interface import AveVoadora, AveQueNaoVoa

class Canario(AveVoadora):

    def comer(self):
        print('estou comendo!')

    def voar(self):
        print('estou voando!')

    def gritar(self):
        print('estou gritando!')

class Pinguim(AveQueNaoVoa):

    def comer(self):
        print('Estou comendo!')
        self.__acasalar()

    def gritar(self):
        print('Estou gritando!')

    def __acasalar(self):
        print('Agora vou acasalar....')