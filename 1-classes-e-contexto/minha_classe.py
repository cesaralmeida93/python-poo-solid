class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal Avancado')

    def voltar_canal(self):
        print('Voltar o canal')

    def escolher_canal(self, canal):
        print('Alterado para o canal: {}'.format(canal))


controle_sala = ControleRemoto('samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

controle_quarto = ControleRemoto('LG', 'quarto')
print(controle_quarto.comodo)
print(controle_quarto.televisao)
controle_quarto.avancar_canal()
controle_quarto.escolher_canal(45)