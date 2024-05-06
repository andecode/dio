'''Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções : criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)'''
class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    num_conta = 0  # Contador para gerar números de conta sequenciais

    def __init__(self, agencia, numero_conta, usuario):
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.usuario = usuario
        self.depositos = []
        self.saques = []
        self.saldo = 0
        self.saques_diarios = 3
        self.limite_saque = 500.00

    def deposito(self, saldo, valor, extrato):
        if valor > 0:
            self.depositos.append(valor)
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        return saldo, extrato

    def saque(self, *, saldo, valor, extrato, limite, numero_saques, limites_saques):
        if numero_saques > 0 and valor <= limite and valor <= saldo:
            self.saques.append(valor)
            saldo -= valor
            numero_saques -= 1
            extrato += f'Saque: R$ {valor:.2f}\n'
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif numero_saques <= 0:
            print('Limite diário de saques atingido.')
        elif valor > limite:
            print('Limite máximo de saque excedido.')
        else:
            print('Saldo insuficiente.')
        return saldo, extrato

    def extrato(self, saldo, *, extrato=''):
        if not self.depositos and not self.saques:
            return 'Não foram realizadas movimentações.'
        else:
            extrato = 'Extrato:\n'
            for deposito in self.depositos:
                extrato += f'Depósito: R$ {deposito:.2f}\n'
            for saque in self.saques:
                extrato += f'Saque: R$ {saque:.2f}\n'
            extrato += f'Saldo atual: R$ {saldo:.2f}'
            return extrato

def criar_usuario(usuarios):
    while True:
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário (logradouro, nro - bairro - cidade/estado): ")

        # Verifica se o CPF já está cadastrado
        if any(usuario.cpf == cpf for usuario in usuarios):
            print("CPF já cadastrado. Por favor, digite um CPF diferente.")
        else:
            usuarios.append(Usuario(nome, data_nascimento, cpf, endereco))
            print("Usuário cadastrado com sucesso.")
            break

def criar_conta_corrente(contas, usuarios):
    cpf = input("Digite o CPF do usuário para criar a conta corrente: ")
    usuario = next((user for user in usuarios if user.cpf == cpf), None)
    if usuario:
        ContaBancaria.num_conta += 1
        conta = ContaBancaria("0001", ContaBancaria.num_conta, usuario)  # Criar uma nova conta bancária associada ao usuário
        contas.append(conta)
        print(f"Conta corrente criada com sucesso para o usuário {usuario.nome}.")
    else:
        print("Usuário não encontrado.")

def listar_contas(contas):
    print("Lista de Contas Correntes:")
    for idx, conta in enumerate(contas, 1):
        print(f"{idx}. Titular: {conta.usuario.nome} - Agência: {conta.agencia} - Número: {conta.numero_conta} - Saldo: R$ {conta.saldo:.2f}")

# Utilização do sistema bancário com menu interativo
usuarios = []
contas = []

while True:
    print("\nEscolha uma opção:")
    print("[c] Criar Usuário")
    print("[n] Criar Conta Corrente")
    print("[d] Depósito")
    print("[s] Saque")
    print("[e] Extrato")
    print("[l] Listar Contas Correntes")
    print("[x] Sair")

    opcao = input(">> ").lower()

    if opcao == 'c':
        criar_usuario(usuarios)  # Criar um novo usuário
    elif opcao == 'n':
        criar_conta_corrente(contas, usuarios)  # Criar uma nova conta corrente
    elif opcao == 'd':
        if contas:
            depositar(contas[0])  # Realizar um depósito na primeira conta corrente (apenas para exemplo)
        else:
            print("Nenhuma conta corrente cadastrada.")
    elif opcao == 's':
        if contas:
            saldo, extrato = sacar(contas[0])  # Realizar um saque na primeira conta corrente (apenas para exemplo)
            contas[0].saldo = saldo
            contas[0].extrato += extrato
        else:
            print("Nenhuma conta corrente cadastrada.")
    elif opcao == 'e':
        if contas:
            visualizar_historico(contas[0])  # Visualizar o extrato da primeira conta corrente (apenas para exemplo)
        else:
            print("Nenhuma conta corrente cadastrada.")
    elif opcao == 'l':
        listar_contas(contas)  # Listar as contas correntes
    elif opcao ==
