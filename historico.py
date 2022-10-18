import datetime

class Historico:
    def __init__(self, cpf=0):
        self._data_criacao = datetime.datetime.now()
        self._transacoes = list()
        self._cpf = cpf

    @property
    def data_criacao(self):
        return self._data_criacao

    @property
    def transacoes(self):
        return self._transacoes

    @property
    def cpf(self):
        return self._cpf

    def add_transacoes(self, t):
        self._transacoes.append(t)

    def imprime(self):
        print(f'Data de criação da conta: {self._data_criacao}')
        for i in self._transacoes:
            print(i)