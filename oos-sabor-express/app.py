from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

'''
O __pycache__ é uma forma mais simples do python interpretar aquele módulo que estamos importando.
Ou seja, é um diretório que o Python cria para armazenar os arquivos compilados em bytecode.
É uma forma que ele tem de interpretar de uma maneira muito mais simplesmente que o arquivo original
'''

r3 = Restaurante('Japa', 'Japonesa')

r3.alternar_estado()
r3.receber_avaliacao('Mayara', 4)
r3.receber_avaliacao('Lais', 3)

b1 = Bebida('Suco de Melancia', 5.00, '500 ml')
p1 = Prato('Pão', 2.00, 'Pão francês')

r3.adicionar_no_cardapio(p1)
r3.adicionar_no_cardapio(b1)

'''
A variável __name__ representa o nome do módulo que está sendo importado, no caso, restaurante.
Entretando, quando o módulo é executado por si só, ele é definido para __main__.
Para isso, coloca-se a condição __name__ == '__main__', logo, quando rodar o app.py,
A função main() será executada e apenas as instruções contidas nelas serão rodadas.
Caso isso não seja instruído ao python, ele rodaria todas as instruções do arquivo restaurante.py
'''

def main():
    r3.exibir_cardapio

if __name__ == '__main__':
    main()