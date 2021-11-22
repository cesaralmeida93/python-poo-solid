from typing import Type

class Animal:

    def comer(self):
        print('O animal está Comendo')

    def dormir(self):
        print('O Animal está Dormindo')

    def andar(self):
        print('O animal está andando na jaula')

class Aves(Animal):

    def __init__(self):
        super().__init__()

    def cantar(self):
        print('A ave está cantando')

class Pinguim(Aves):

    def __init__(self):
        super().__init__()

    def escorregar(self):
        print('O Pinguim está escorregando no gelo')

class Pessoa:

    def observar(self, animal: Type[Animal]):
        animal.comer()

roberto = Pessoa()
pinguim = Pinguim()
roberto.observar(pinguim)