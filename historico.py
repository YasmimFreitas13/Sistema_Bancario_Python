# A classe Historico armazena as transações de uma conta em uma lista.
# Isso torna mais fácil buscar, filtrar e exibir transações.
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    # Adiciona a transação ao histórico, salvando o tipo e o valor.
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Obtém o nome da classe (Saque, Deposito)
                "valor": transacao.valor,
            }
        )