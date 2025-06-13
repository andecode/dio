'''Desafio de código - Conhecendo Tuplas em Python
Descrição
Desenvolva uma função em Python que recebe uma tupla de números inteiros e retorna a soma de todos os elementos dessa tupla. A função deve ser capaz de lidar com tuplas de qualquer tamanho, contanto que todos os elementos sejam números inteiros. O objetivo é praticar a manipulação de tuplas e a utilização de funções em Python.

Explicação de Resolução:

1. Converta cada string na "lista_strings" em um número inteiro utilizando a função "int()".
2. Use a função "map()" para aplicar a função "int()" a cada elemento da "lista_strings".
3. Armazene o resultado em uma variável chamada "elementos".

Documentação Oficial:
https://docs.python.org/pt-br/3/library/stdtypes.html#tuple

Entrada
A entrada para o seu programa será uma única linha de texto contendo vários números inteiros separados por espaços. Esses números devem ser lidos e convertidos para uma tupla de inteiros.

Saída
A saída do seu programa deve ser a soma de todos os números inteiros presentes na tupla. O resultado deve ser exibido de forma clara e amigável, seguindo o formato especificado. Aqui estão os passos detalhados para a saída:

1. Calcule a soma de todos os elementos da tupla.

2. Exiba a soma do valor calculado no formato: A soma dos elementos da tupla é: <soma>

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
2 5 6 7 9	A soma dos elementos da tupla é: 29
9 8 7 6 5	A soma dos elementos da tupla é: 35
50 50 50 50	A soma dos elementos da tupla é: 200
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.
'''
# No "TODO", abaixo: Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:

def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()
# No "TODO", abaixo: Defina tupla para receber os números inteiros:
    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")