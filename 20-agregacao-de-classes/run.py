from produtos import Produto
from carrinho import CarrinhoCompras

car = CarrinhoCompras()
monitor = Produto('Monitor', 1000)
cerveja = Produto('Cerveja', 5)
tv = Produto('TV', 1200)

car.adicionar_produto(monitor)
car.adicionar_produto(cerveja)
car.adicionar_produto(tv)

car.finalizar_compra()