# 7: Associação de Classes

- Associação: Um objeto navega para a utilização de outro objeto
 
## python

```python
from typing import Type

class Interruptor:

    def __init__(self, comodo):
        self.__comodo = comodo

    def acender(self):
        print('acendendo {}'.format(self.__comodo))

    def apagar(self):
        print('apagando {}'.format(self.__comodo))


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('Fui dormir...')


lhama = Pessoa()
interruptor_quarto = Interruptor('quarto')
interruptor_cozinha = Interruptor('cozinha')

interruptor_quarto.acender()
lhama.acender_luz(interruptor_cozinha)
lhama.apagar_luz(interruptor_cozinha)
lhama.dormir()
```
