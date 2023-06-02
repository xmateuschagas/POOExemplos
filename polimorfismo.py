class Jogador:
    def marcar_gol(self):
        pass
        # Este é um método vazio que serve como um esqueleto para os métodos nas subclasses.

class Garrincha(Jogador):
    def marcar_gol(self):
        return "Garrincha marcou um gol!"
        # Implementação do método marcar_gol na classe Garrincha. Retorna uma string informando que Garrincha marcou um gol.

class NiltonSantos(Jogador):
    def marcar_gol(self):
        return "Nilton Santos marcou um gol!"
        # Implementação do método marcar_gol na classe NiltonSantos. Retorna uma string informando que Nilton Santos marcou um gol.

def comemorar_gol(jogador):
    print(jogador.marcar_gol())
    # Função que recebe um objeto do tipo Jogador (ou uma de suas subclasses) como parâmetro.
    # Chama o método marcar_gol do objeto jogador e imprime a mensagem de comemoração do gol.

garrincha = Garrincha()
nilton_santos = NiltonSantos()

comemorar_gol(garrincha)       # Saída: "Garrincha marcou um gol!"
comemorar_gol(nilton_santos)   # Saída: "Nilton Santos marcou um gol!"
