from models import Insersor, Repositorio, insersor

class RepositorioFaker(Repositorio):
    def __init__(self):
        super().__init__()

    def select(self, name: int) -> None:
        return None

repo = RepositorioFaker()
insersor = Insersor(repo)

data = insersor.inserir_dado('Lhama', 26)
print(data)