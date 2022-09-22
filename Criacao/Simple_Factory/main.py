from Design_Patterns.Simple_Factory.jogador import TimeFactory
import random


if __name__ == "__main__":

    jogadores_disponiveis = ['basquete', 'futebol']

    for i in range(10):
        _jogador = TimeFactory.get_time(random.choice(jogadores_disponiveis))
        _jogador.jogador()
        _jogador.camisa_jogador()