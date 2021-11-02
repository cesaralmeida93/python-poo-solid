# 4: SOLID(S) - Responsabilidade Única

- SOLID é um acrônimo que cada letra significa um princípio diferente
- S de Single Responsability
- Um módulo deve ser responsável por um, e apenas um, ator
- Um módulo é apenas um conjunto coeso de funções e estruturas de dados

## python

```python
class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('acessando o banco de dados...')
        print('Cadastrar o usuário {}, Idade {}'.format(nome, idade))

    def __indicar_erro(self) -> None:
        print('dados inválidos!')
```