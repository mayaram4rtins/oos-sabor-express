from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):    
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @classmethod
    def lista_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")       

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            a1 = Avaliacao(cliente, nota)
            self._avaliacao.append(a1)
        
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'

        media = round(sum(avaliacao._nota for avaliacao in self._avaliacao)/len(self._avaliacao), 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for index, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                print(f'{index}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}')
            else:
                print(f'{index}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho} ')