# transacao.py
from abc import ABC, abstractmethod

# A classe Transacao é uma classe abstrata, ou seja, não pode ser instanciada.
# Ela serve como um contrato (interface) para todas as transações futuras.
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# A classe Saque implementa a interface Transacao.
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    # O método registrar delega a operação de sacar para a conta.
    # Em seguida, registra a transação no histórico da conta, se for bem-sucedida.
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# A classe Deposito também implementa a interface Transacao.
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    # O método registrar delega a operação de depositar para a conta.
    # Em seguida, registra a transação no histórico da conta, se for bem-sucedida.
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)