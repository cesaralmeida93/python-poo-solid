# 5: Variáveis e Métodos de Classe

- Variável de Classe: Variável estática, são uma espécie de variável global
- Quando alterado o valor de uma ariável estática, ele é alterado no contexto geral da classe
- Esse contexto geral da classe é passado para o contexto de objeto dessa classe também
- `@classmethod` decorador que auxilia que o objeto entenda o contexto da classe
- `self` se referencia ao objeto, e `cls` se referencia a classe
 
## python

```python
class MinhaClasse:

    estatico = 'lhama'

    def __init__(self, estado):
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls):
        cls.estatico = 'Programador'

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.mudar_estatico()

obj1.print_estatico()
obj2.print_estatico()
```

```python
class Loja:

    tarifa = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self.__endereco)

    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa


loja_praia = Loja('Praia')
loja_centro = Loja('Centro')

loja_praia.apresentar_endereco()

print(loja_praia.vender())
print(loja_centro.vender())

loja_centro.alterar_tarifa(1.50)

print(loja_praia.vender())
print(loja_centro.vender())

print(loja_praia.tarifa)
```