from typing import Type
from interfaces.formas import FormasInterface

class Engenheiro:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterface]):
        perimetro = terreno.get_perimetro()
        print('{} mediu o perimetro: {} m'.format(self.nome, perimetro))

    def medir_area(self, terreno: Type[FormasInterface]):
        area = terreno.get_area()
        print('{} mediu a área: {} m²'.format(self.nome, area))