'''Desafio de código - Filtragem de Transações Acima de um Valor Específico
Descrição
Você está consumindo dados de uma API de uma instituição financeira que fornece uma lista de transações. Seu desafio é filtrar todas as transações que possuem um valor acima de um determinado limite.

Entrada
A entrada deve receber dois valores:
1. Um número decimal representando o valor limite.
2. Uma string contendo transações no seguinte formato: "ID:VALOR;ID:VALOR;..."

Saída
Deverá retornar uma lista de strings, onde cada string contém as informações das transações cujo valor é maior que o valor limite especificado.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
150.00
1:100.00;2:200.50;3:150.75	['2:200.5', '3:150.75']
300.00
4:500.00;5:600.00	['4:500.0', '5:600.0']
100.00
6:250.25;7:90.00;8:110.50	['6:250.25', '8:110.5']
'''
# Recebe o valor limite como entrada do usuário e converte para float
limite = float(input())
# Recebe a string de transações como entrada do usuário
transacoes = input()

# Define a função para filtrar transações acima do limite especificado
def filtrar_transacoes_acima_do_limite(limite, transacoes):
    if not transacoes:
        return []

    transacoes_filtradas = []
    lista_transacoes = transacoes.split(';')
    
    # Itera sobre cada transação na lista de transações
    for transacao in lista_transacoes:
        id_transacao, valor_str = transacao.split(':')
        valor = float(valor_str)
        
        # TODO: Compare o valor da transação com o limite e adiciona à lista filtrada se for maior
        if valor > limite:
            transacoes_filtradas.append(f"{id_transacao}:{valor}")
    return transacoes_filtradas
    
# Imprime as transações com valores acima do limite
print(filtrar_transacoes_acima_do_limite(limite, transacoes))