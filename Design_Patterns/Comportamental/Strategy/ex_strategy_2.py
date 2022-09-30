class Orcamento:

    def __init__(self, valor) -> None:
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

class ISS:
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS:
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class Propina:
    def calcula(self, orcamento):
        return orcamento.valor * 0.15


class CalcaladoraImpostos:
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


calculador = CalcaladoraImpostos()
orcamento = Orcamento(500)
calculador.realiza_calculo(orcamento, ISS())
calculador.realiza_calculo(orcamento, ICMS())
calculador.realiza_calculo(orcamento, Propina())