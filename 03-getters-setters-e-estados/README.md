# 3: Getters/Setters e Estados

- è mais interessante utilizar métodos de modificação e retorno de estados(get/set), para manipular atributos privados

## python

```python
class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor
```