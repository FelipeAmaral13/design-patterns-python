from __future__ import annotations
from abc  import ABC, abstractmethod

class Order:

    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self): return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStrategy(ABC):

    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TweentyPercent(DiscountStrategy):

    def calculate(self, value: float) -> float:
        return value - (value * 0.2)



order = Order(1000, TweentyPercent())
order.total_with_discount