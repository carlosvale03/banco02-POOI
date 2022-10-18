class Seguro:
    def __init__(self, valor_mensal, valor_total):
        self._valor_mensal = valor_mensal
        self._valor_total = valor_total

    @property
    def valor_mensal(self):
        return self._valor_mensal

    @valor_mensal.setter
    def valor_mensal(self, v_mensal):
        self._valor_mensal = v_mensal

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, v_total):
        self._valor_total = v_total


    def tributar(self, valor_fixo=10, taxa=0.02):
        return valor_fixo + self._valor_mensal * taxa