import Pyro4

class PPT_cliente_jogo:
    def __init__(self):
        self.game_server = Pyro4.Proxy("PYRONAME:PPT_jogo")

    def play(self, nome_jogador, escolha):
        return self.game_server.play(nome_jogador, escolha)

def main():
    client = PPT_cliente_jogo()

    while True:
        nome_jogador = input("Digite seu nome de jogador: ")
        escolha = input("Escolha (pedra, papel ou tesoura): ")
        result = client.play(nome_jogador, escolha)
        print(result)

if __name__ == "__main__":
    main()
