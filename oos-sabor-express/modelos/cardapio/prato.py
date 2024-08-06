# Classes derivadas da classe ItemCardápio

from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    '''
    Um método que se molda diferente em diferentes classes é o que chamamos de polimorfismo
    '''
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)