class Jogador:
    def __init__(self, nome, numero_camisa):
        self.__nome = nome
        self.__numero_camisa = numero_camisa
        # O método __init__ é um construtor que é chamado quando um objeto é instanciado a partir da classe Jogador.
        # Ele recebe parâmetros nome e numero_camisa e atribui esses valores aos atributos correspondentes do objeto.
        # Os atributos são definidos com dois underscores "__" na frente, indicando que são atributos privados.

    def get_nome(self):
        return self.__nome
        # O método get_nome retorna o valor do atributo privado __nome.

    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        # O método set_nome recebe um novo_nome como parâmetro e atualiza o atributo privado __nome com o novo valor.

    def get_numero_camisa(self):
        return self.__numero_camisa
        # O método get_numero_camisa retorna o valor do atributo privado __numero_camisa.

    def set_numero_camisa(self, novo_numero_camisa):
        self.__numero_camisa = novo_numero_camisa
        # O método set_numero_camisa recebe um novo_numero_camisa como parâmetro e atualiza o atributo privado __numero_camisa com o novo valor.

jogador = Jogador("Garrincha", 7)
# Cria uma instância da classe Jogador, passando os valores correspondentes para nome e numero_camisa.

print(jogador.get_nome())               # Saída: "Garrincha"
# Chama o método get_nome para obter o nome do jogador e imprime o resultado.

print(jogador.get_numero_camisa())      # Saída: 7
# Chama o método get_numero_camisa para obter o número da camisa do jogador e imprime o resultado.

jogador.set_nome("Nilton Santos")
# Chama o método set_nome para atualizar o nome do jogador.

jogador.set_numero_camisa(6)
# Chama o método set_numero_camisa para atualizar o número da camisa do jogador.

print(jogador.get_nome())               # Saída: "Nilton Santos"
# Chama o método get_nome para obter o novo nome do jogador e imprime o resultado.

print(jogador.get_numero_camisa())      # Saída: 6
# Chama o método get_numero_camisa para obter o novo número da camisa do jogador e imprime o resultado.
