class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
        # O método __init__ é um construtor que é chamado quando um objeto é instanciado a partir da classe Jogador.
        # Ele recebe parâmetros nome e posicao e atribui esses valores aos atributos correspondentes do objeto.

    def imprimir(self):
        print(f"Nome: {self.nome}")
        print(f"Posição: {self.posicao}")
        # O método imprimir imprime as informações do jogador, nome e posição.

class Garrincha(Jogador):
    def __init__(self, nome, posicao, apelido):
        super().__init__(nome, posicao)
        self.apelido = apelido
        # A classe Garrincha herda da classe Jogador e adiciona um novo atributo, apelido.
        # O método __init__ da classe Garrincha chama o método __init__ da classe Jogador usando super().
        # Isso garante que os atributos nome e posicao sejam inicializados corretamente pela classe pai.

    def imprimir(self):
        super().imprimir()
        print(f"Apelido: {self.apelido}")
        # O método imprimir da classe Garrincha chama o método imprimir da classe Jogador usando super().
        # Em seguida, imprime o apelido do jogador.

garrincha = Garrincha("Manuel Francisco dos Santos", "Ponta Direita", "Anjo das Pernas Tortas")
garrincha.imprimir()
# Cria uma instância da classe Garrincha, passando os valores correspondentes para nome, posição e apelido.
# Em seguida, chama o método imprimir, que exibe todas as informações do jogador Garrincha, incluindo o apelido.
