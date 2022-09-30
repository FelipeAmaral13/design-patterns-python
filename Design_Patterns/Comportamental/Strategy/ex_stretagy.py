from __future__ import annotations

class StringReprMixim:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__


class Order(StringReprMixim):

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value



class CalculateShipping(StringReprMixim):

    def calculate_default(self, order):
        return order.value * 0.05

    def calculate_express(self, order):
        return order.value * 0.1

    def execute_calculation(self, order, shipping):
        if shipping == 'Default':
            total = self.calculate_default(order)
        elif shipping == 'Express':
           total = self.calculate_express(order)
        print(total)



calculate_shipping = CalculateShipping()
order = Order(500)
calculate_shipping.execute_calculation(order, 'Default')