from abc import ABC, abstractmethod

class Observer(ABC):
    """A classe Observer é inicializada com um objeto como argumento.
    O objeto nada mais é do que um Observável para acompanhar, ao qual está inscrito na criação."""

    @abstractmethod
    def update(self, subject) -> None: pass


class Observable:

    """A classe Observable é inicializada com uma lista vazia para conter as instâncias do Observer.
    attach() -> adicionar um observador
    notify() -> notifica a atualizacao de cada observador
    detach() -> remover o observador da lista
    """

    _observers_list = list()

    def __init__(self) -> None:
        pass

    def attach(self, observer) -> None:
        print(f'{observer.name} added')
        self._observers_list.append(observer)
        self.notify()
        

    def detach(self, observer) -> None:
        print(f'{observer.name} removed')
        self._observers_list.remove(observer)
        self.notify()


    def notify(self) -> None:
        print('Notifying ...')
        for obs in self._observers_list:
            obs.update()



class Item1(Observer):

    
    def __init__(self, name) -> None:
        self.name = name

    def update(self) -> None:
        print(self.name)


ob1 = Observable()
item1 = Item1('item1')
ob1.attach(item1)

item2 = Item1('item2')
ob1.attach(item2)

ob1.notify()

ob1.detach(item1)

