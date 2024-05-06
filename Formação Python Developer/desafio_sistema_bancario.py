class SistemaBancario:
    def __init__(self):
        self.depositos = []
        self.saques = []
        self.saldo = 0
        self.saques_diarios = 3
        self.limite_saque = 500.00

    def deposito(self, valor):
        if valor > 0:
            self.depositos.append(valor)
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')

    def saque(self, valor):
        if self.saques_diarios > 0 and valor <= self.limite_saque and valor <= self.saldo:
            self.saques.append(valor)
            self.saldo -= valor
            self.saques_diarios -= 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif self.saques_diarios <= 0:
            print('Limite diário de saques atingido.')
        elif valor > self.limite_saque:
            print('Limite máximo de saque excedido.')
        else:
            print('Saldo insuficiente.')

    def extrato(self):
        if not self.depositos and not self.saques:
            return 'Não foram realizadas movimentações.'
        else:
            extrato = 'Extrato:\n'
            for deposito in self.depositos:
                extrato += f'Depósito: R$ {deposito:.2f}\n'
            for saque in self.saques:
                extrato += f'Saque: R$ {saque:.2f}\n'
            extrato += f'Saldo atual: R$ {self.saldo:.2f}'
            return extrato

# Utilização do sistema bancário com menu interativo
sistema = SistemaBancario()

while True:
    print("\nEscolha uma opção:")
    print("[d] Depósito")
    print("[s] Saque")
    print("[e] Extrato")
    print("[x] Sair")

    opcao = input(">> ").lower()

    if opcao == 'd':
        valor_deposito = float(input("Digite o valor do depósito: "))
        sistema.deposito(valor_deposito)
    elif opcao == 's':
        valor_saque = float(input("Digite o valor do saque: "))
        sistema.saque(valor_saque)
    elif opcao == 'e':
        print(sistema.extrato())
    elif opcao == 'x':
        break
    else:
        print("Opção inválida. Tente novamente.")