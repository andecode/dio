'''Desafio
Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de diretórios.
Após concluir a modelagem de classes e a criação dos métodos. Atualizar os métodos que tratam as opções do menu para funcionaram com as classes modeladas.'''
import textwrap

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Conta:
    def __init__(self, agencia, numero_conta, titular):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito:\tR$ {valor:.2f}\n')
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def sacar(self, valor, limite_saque):
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False
        
        if valor > limite_saque:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False
        
        if self.numero_saques >= 3:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        self.saldo -= valor
        self.extrato.append(f'Saque:\t\tR$ {valor:.2f}\n')
        self.numero_saques += 1
        return True

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta.extrato else ''.join(conta.extrato))
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_usuario():
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append(Usuario(nome, cpf, data_nascimento, endereco))
    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        numero_conta = len(contas) + 1
        conta = Conta("0001", numero_conta, usuario)
        contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas():
    for conta in contas:
        linha = f"""\
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero_conta}
            Titular:\t{conta.titular.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


usuarios = []
