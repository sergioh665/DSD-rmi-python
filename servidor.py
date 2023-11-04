import Pyro4

@Pyro4.expose
class PPT_server_jogo:
    def __init__(self):
        self.players = {}
        self.results = []

    def play(self, nome_jogador, escolha):
        if nome_jogador not in self.players:
            self.players[nome_jogador] = escolha
        if len(self.players) == 2:
            result = self.determine_winner()
            self.results = []
            self.players = {}
            return result
        else:
            return "Aguardando a jogada do próximo jogador."

    def determine_winner(self):
        jogador1_nome, jogador2_nome = list(self.players.keys())
        jogador1_escolha = self.players[jogador1_nome]
        jogador2_escolha = self.players[jogador2_nome]

        if jogador1_escolha == jogador2_escolha:
            return "Empate entre os jogadores"
        elif (
            (jogador1_escolha == "pedra" and jogador2_escolha == "tesoura")
            or (jogador1_escolha == "tesoura" and jogador2_escolha == "papel")
            or (jogador1_escolha == "papel" and jogador2_escolha == "pedra")
        ):
            return f"{jogador1_nome} venceu a rodada"
        else:
            return f"{jogador2_nome} venceu a rodada"

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()

    game_server = PPT_server_jogo()
    uri = daemon.register(game_server)

    ns.register("PPT_jogo", uri)

    print("Servidor pronto para jogar Pedra, Papel e Tesoura.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
