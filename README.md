# 🏦 Desafio DIO: Sistema Bancário POO

Este projeto foi desenvolvido como parte de um desafio proposto pelo bootcamp da **DIO + Suzano**, com o objetivo de criar um sistema bancário em **Python**. A implementação utiliza conceitos avançados de **Programação Orientada a Objetos (POO)** para estruturar o código de forma modular e escalável.

## 💻 Tecnologias e Ferramentas Utilizadas

- **Linguagem de Programação:** Python
- **Ambiente de Desenvolvimento (IDE):** Visual Studio Code (VS Code)
- **Controle de Versão:** Git e GitHub

## ✨ Funcionalidades

O sistema bancário implementa as seguintes operações:

- **Criar Usuário:** Cadastro de clientes do banco com CPF (único), nome, data de nascimento e endereço.
- **Criar Conta Corrente:** Associação de contas a clientes já cadastrados. Cada conta é um objeto com atributos e métodos próprios.
- **Listar Contas:** Exibe todas as contas criadas, detalhando agência, número da conta e titular.
- **Depósito:** Adiciona fundos a uma conta. As transações de depósito são tratadas como objetos, seguindo o padrão POO.
- **Saque:** Permite a retirada de dinheiro de uma conta, com um limite de 3 saques diários e um valor máximo de R$ 500 por saque. O sistema garante que a operação só seja realizada se houver saldo suficiente.
- **Extrato:** Exibe o histórico de todas as transações (depósitos e saques) realizadas na conta, mostrando o saldo atual.

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/YasmimFreitas13/Sistema_Bancario_Python.git](https://github.com/YasmimFreitas13/Sistema_Bancario_Python.git)

2. **Navegue até o diretório do projeto:**
   ```bash   
   cd Sistema_Bancario_Python

3. **Execute o script principal:**
   ```bash
   python main.py

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados os seguintes conceitos de POO:

- **Classes e Objetos:** Criação de classes como Cliente, ContaCorrente, Historico e Transacao para modelar o sistema bancário.

- **Encapsulamento:** Utilização de atributos privados (_saldo, _historico) e propriedades (@property) para proteger os dados e controlar o acesso a eles.

- **Herança:** A classe PessoaFisica herda de Cliente, e ContaCorrente herda de Conta, reutilizando e estendendo a lógica de suas classes-base.

- **Polimorfismo:** Implementação de uma interface Transacao e classes Deposito e Saque que a implementam, permitindo que a mesma chamada de método (realizar_transacao) execute comportamentos diferentes.

- **Estrutura Modular:** Organização do código em múltiplos arquivos (cliente.py, conta.py, transacao.py), tornando o projeto mais limpo, fácil de manter e escalável.

## 👩‍💻 Desenvolvido por

Yasmim Freitas Coimbra