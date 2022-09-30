class Observer:
    """A classe Observer é inicializada com um objeto como argumento.
    O objeto nada mais é do que um Observável para acompanhar, ao qual está inscrito na criação."""

    def __init__(self, observable) -> None:
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("De ", args, kwargs, 'Para ', observable)


class Observable:
    """A classe Observable é inicializada com uma lista vazia para conter as instâncias do Observer.
    subscribe() -> adicionar um observador
    notify_observers() -> chamar a função notify() em cada observador
    unsubscribe() -> remover o observador da lista
    """

    def __init__(self) -> None:
        self._observers = []


    def subscribe(self, observer):
        self._observers.append(observer)


    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)


    def unsubscribe(self, observer):
        self._observers.remove(observer)


s1 = Observable()

ob1 = Observer(s1)
ob2 = Observer(s1)

s1.notify_observers('1st chamada', 'De observador')
s1.unsubscribe(ob2)

s1.notify_observers('2nd chamada', 'De observador')
