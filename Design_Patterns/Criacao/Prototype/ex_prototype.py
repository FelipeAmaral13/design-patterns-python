from typing import List
from copy import deepcopy
from __future__ import annotations


class StringReprMixim:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__

class Times(StringReprMixim):

    def __init__(self, time:str) -> None:
        self.time = time
        

class Jogador(StringReprMixim):

    def __init__(self, firstname: str) -> None:
        self.firstname = firstname
        self.times: List[Times] = []

    def add_time(self, time: Times) -> None:
        self.times.append(time)
    
    def clone(self) -> Jogador:
        return deepcopy(self)


j1 = Jogador('iti')
j1.add_time('Cru')
print(j1)

j2 = j1.clone()
j2.firstname = 'utu'
j2.add_time('Fla')
j2.add_time('Flu')
print(j2)