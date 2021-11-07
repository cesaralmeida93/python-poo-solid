# 10: Injeção de Dependência

- Injeção de dependência é uma relação de associação mais explícita
- As ações de um objeto começam a depender de outro objeto também
- Injeção de Dependência tras a i´deia de forte acoplamento, uma classe precisa obrigatóriamente que a outra classe exista
- Não é interessante que se tenha uma classe totalmente acoplada a outra, esse problema é resolvido usando interfaces e heranças

****
## python

```python
from typing import Type

class Casa:

    def __init__(self) -> None:
        self.__endereco = 'Rua dos Limoeiros'

    def acender_luzes(self) -> None:
        print('Estou Acendendo as Luzes')

    def get_endereco(self) -> str:
        return self.__endereco


class Pessoa:

    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__local = local
        self.__nome = nome

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)


casa_de_amigo = Casa()
ana = Pessoa('Ana', casa_de_amigo)

ana.entrar_no_local()
ana.apresentar_local()
```