# Classes derivadas da classe ItemCardápio

from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
    
    '''
    Um método que se molda diferente em diferentes classes é o que chamamos de polimorfismo
    '''
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)