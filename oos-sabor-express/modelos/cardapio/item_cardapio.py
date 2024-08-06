from abc import ABC, abstractmethod

'''
Herança consiste em compartilhamento de atributos e métodos de uma classe-pai por uma classe-filha.
Classe-pai ou classe base é a classe que concede as características.
Classe-filha ou classe derivada é a classe que herda as características.
A utilização da herança faz com que o programa flua de forma linear sem interações imprevisíveis.
Além disso, é válido frisar que a classe derivada é a implementação específica de um caso mais geral (classe base)
'''

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    '''
    Um método abstrato é um método declarado mas não é definido. Em vez disso, as subclasses que o implementam.
    Uma classe abstrata é projetada para ser especificamente usada como uma classe base.
    Dessa forma, a classe base não pode ser instanciada diretamente e pode conter métodos abstratos e concretos.
    '''
    
    @abstractmethod
    def aplicar_desconto(self):
        pass