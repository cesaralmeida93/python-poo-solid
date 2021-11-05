# 7: Associação de Classes

- Métodos estáticos possuem um contexo separado da classe e do objeto
- Classe e Objeto podem uilizar o método estático, mas o método estático não tem acesso aos atributos e métodos da classe ou do objeto
- Métodos estáticos são utilizados geralmente como um especificador 
- `@staticmethod`: decorador utilizado para demonstrar que determinado método é um método estático
 
## python

```python
class MinhaClasse:

    @staticmethod
    def metodo_estatico():
        print('Estou no meu método estático :D')


MinhaClasse.metodo_estatico()
```

```python
class Error:

    @staticmethod
    def error_500():
        print('Internal Server Error')

    @staticmethod
    def error_404():
        print('Not Found')


Error.error_500()
Error.error_404()

```
