# 1: Classes e Encapsulamento

- Classe é uma abstração de algum elemento natural que possue ações e características
- Exemplo: Uma classe pessoa possui características(altura, cor dos olhos) e ações(andar, comer)
- Características são atributos, e ações são métodos

## python
- self sempre se referencia a classe em que ele está identado

```python
class MinhaClasse:

    def meu_metodo(self):
        print('Estou no método')
```

- método construtor: função que define regras para instanciar um objeto da classe

```python
class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo
```

