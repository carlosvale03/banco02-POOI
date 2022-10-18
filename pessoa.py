import abc

class Pessoa(abc.ABC):
    def __init__(self, nome, cpf, dt_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._dt_nascimento = dt_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf

    @property
    def dt_nascimento(self):
        return self._dt_nascimento


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, dt_nascimento, salario):
        super().__init__(nome, cpf, dt_nascimento)
        self._salario = salario

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario


class Cliente(Pessoa):
    def __init__(self, nome, cpf, dt_nascimento, profissao):
        super().__init__(nome, cpf, dt_nascimento)
        self._profissao = profissao

    @property
    def profissao(self):
        return self._profissao
