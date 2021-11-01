# 2: Encapsulamento Privado

- Pilares da programação orientada a objetos: Encapsulamento, Polimorfismo, Herança (talvez abstração, mas não é um concenso)
- Encapsulamento: Relacionado a permissão de uso
- A classe cria o contexto, e o objeto ao ser instanciado está fora do contexto

## python
- modificador de acesso privado: não permite que o objeto tenha acesso ao atributo ou método privado, somente a classe

```python
class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def print_cpf(self):
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo', 32, '468464846465')
ronaldo.print_cpf()
print(ronaldo.__cpf) # retorna erro, não encontra o atributo privado
```

- a melhor maneira de utilizar métodos e atributos privado é encapsulando-os em métodos públicos

```python
class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):
        print('Estou Correndo')

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')

    def __apresentar_documento(self):
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo', 32, '468464846465')
ronaldo.beber('cerveja')
ronaldo.beber('coca-cola')
```