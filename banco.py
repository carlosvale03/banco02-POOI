class Banco:
    def __init__(self):
        self._funcionario = dict()
        self._cliente = dict()
        self._conta_corrente = dict()
        self._conta_poupanca = dict()
        self._seguro = dict()
        self._historico = dict()

    @property
    def funcionarios(self):
        return self._funcionario

    @funcionarios.setter
    def funcionarios(self, funcionario):
        self._funcionario = funcionario

    @property
    def cliente(self):
        return self._cliente

    @property
    def conta_corrente(self):
        return self._conta_corrente

    @conta_corrente.setter
    def conta_corrente(self, conta):
        self._conta_corrente = conta

    @property
    def conta_poupanca(self):
        return self._conta_poupanca

    @property
    def seguro(self):
        return self._seguro

    @seguro.setter
    def seguro(self, seguro):
        self._seguro = seguro
    
    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, historico):
        self._historico = historico

    def identifica_contas(self, cpf):
        if cpf in self.conta_corrente and cpf in self.conta_poupanca:
            return 2
        elif cpf in self.conta_poupanca:
            return 'poupanca'
        elif cpf in self.conta_corrente:
            return 'corrente'
        else:
            return 0