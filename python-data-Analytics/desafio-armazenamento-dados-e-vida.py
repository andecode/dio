# Desafio Armazenamento de Dados é Vida!
capacidade_atual, aumento_percentual = map(int, input().split())

# Calcula a nova capacidade total em teraflops
nova_capacidade = capacidade_atual * (1 + aumento_percentual / 100)

# Converte o resultado para um número inteiro
nova_capacidade_int = int(nova_capacidade)

# Imprime a nova capacidade
print(nova_capacidade_int)