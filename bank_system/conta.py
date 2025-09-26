from bank_system.cliente import Cliente
from bank_system.historico import Historico

# A classe Conta armazena atributos e métodos da conta bancária.
# Isso demonstra o encapsulamento, pois o saldo e outros atributos
# só podem ser acessados através dos métodos da classe.
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    # Este é um método de classe (@classmethod). Ele cria uma nova instância de Conta
    # e é uma forma alternativa de criar objetos, sem a necessidade de chamar o __init__ diretamente.
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # Propriedades (`@property`) são usadas para acessar atributos privados de forma controlada,
    # como se fossem atributos públicos.
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

# A classe ContaCorrente herda de Conta.
# O método 'sacar' é reescrito (polimorfismo) para adicionar novas regras de negócio.
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        # A lógica para contar saques agora é responsabilidade da própria classe.
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            # Chama o método 'sacar' da classe pai (Conta).
            # Isso evita a duplicação de código.
            return super().sacar(valor)

        return False

    # O método __str__ é usado para definir a representação em string do objeto,
    # tornando a função de listar contas mais limpa.
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """