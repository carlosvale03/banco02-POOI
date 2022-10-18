import abc

his_tributacao = list()

class Conta(abc.ABC):
    num_contas = 0
    def __init__(self, numero, saldo=0, hist_transacoes=0):
        self._num = numero
        self._saldo = saldo
        self._hitorico = hist_transacoes
        self._tipo = None

    @property
    def numero(self):
        return self._num

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def historico(self):
        return self._hitorico

    @property
    def tipo(self):
        return self._tipo

    @abc.abstractmethod
    def sacar(self, valor):
        '''Essa função abstrata está presente nas duas classes de conta.
        Elas iram retornar True se o valor for sacado ou False se o valor 
        informado for invalido.'''
        # pass

    @abc.abstractmethod
    def depositar(self, valor):
        '''Essa função abstrata está presente nas duas classes de conta.
        Elas iram retornar True se o valor for depositado ou False se o valor 
        informado for invalido.'''
        # pass




class ContaCorrente(Conta):
    def __init__(self, numero, saldo, hist_transacoes):
        super().__init__(numero, saldo, hist_transacoes)
        self._tipo = 'Conta corrente'
        # self.contador = 1
        Conta.num_contas += 1

    def tributar(self, valor_fixo=10, taxa=0.01):
        return valor_fixo + self._saldo * taxa

    def sacar(self, valor):
        if valor <= self._saldo and valor >= 0.01:
            self._saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        if valor >= 0.01:
            self._saldo += valor
            return True
        else:
            return False


class ContaPoupanca(Conta):
    def __init__(self, numero, saldo, hist_transacoes):
        super().__init__(numero, saldo, hist_transacoes)
        self._tipo = 'Conta poupança'
        Conta.num_contas += 1

    def sacar(self, valor):
        if valor <= self._saldo and valor >= 0.01:
            self._saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        if valor >= 0.1:
            self._saldo += valor
            return True
        else:
            return False