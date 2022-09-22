# --Estudo de Design Patterns - Simple TimeFactory
#  Nesse estudo o cliente vai requistar a uma Factory a criação das classes

from abc import ABC, abstractmethod
import random

class Jogador(ABC):

    @abstractmethod
    def jogador(self) -> None: pass

    @abstractmethod
    def camisa_jogador(self) -> None: pass


class JogadorBasquete(Jogador):
    
    def jogador(self) -> None:
        print('Este é um jogador de Basquete')

    def camisa_jogador(self) -> None:
        numero_camisa = random.randint(1, 100)
        print(f'O jogador de {JogadorBasquete.__name__} possui a camisa {numero_camisa}')


class JogadorFutebol(Jogador):
    
    def jogador(self) -> None:
        print('Este é um jogador de Futebol')

    def camisa_jogador(self) -> None:
        numero_camisa = random.randint(1, 100)
        print(f'O jogador de {JogadorFutebol.__name__} possui a camisa {numero_camisa}')


class TimeFactory:
    @staticmethod
    def get_time(tipo: str) -> Jogador:
        if tipo == 'basquete':
            return JogadorBasquete()
        if tipo == 'futebol':
            return JogadorFutebol()

        assert 0, 'Sem referencia de tipo de Jogador'
    

