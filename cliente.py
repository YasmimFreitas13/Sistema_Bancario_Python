# A classe Cliente gerencia a relação com suas contas e endereço.
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    # O método 'realizar_transacao' delega a operação para o objeto 'transacao'.
    # Isso segue o princípio de polimorfismo, onde a mesma chamada de método
    # pode ter comportamentos diferentes (saque ou depósito).
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# A classe PessoaFisica herda de Cliente, adicionando informações de pessoa.
# Isso demonstra o conceito de herança, onde uma classe "filha" reutiliza
# a lógica da classe "pai" e adiciona a sua própria.
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)  # Chama o construtor da classe pai (Cliente)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf