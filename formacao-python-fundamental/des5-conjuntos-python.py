'''Desafio de código - Explorando Conjuntos em Python
Descrição
Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.

Detalhamento:

Função elementos_comuns:
1. Crie a função que converte cada elemento das listas lista1 e lista2 para inteiro usando map(int, lista) antes de convertê-los em conjuntos (set) e encontrar a interseção entre eles. Isso garante que tratemos os elementos corretamente como números inteiros e não como strings.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/introduction.html#lists

Entrada
Duas listas de inteiros separados apenas por espaço, por exemplo: 1 2 3 4 e 3 4 5 6.

Saída
Uma lista com os elementos comuns, por exemplo: [3, 4]. Caso a entrada seja diferente do esperado, retorne: "Entrada inválida."

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
1 2 3 4
3 4 5 6	Elementos comuns às duas listas: [3, 4]
9 8 7 6 5
5 2 3 7	Elementos comuns às duas listas: [5, 7]
a b c d
a e i o u	Entrada inválida.
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.
'''
# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:
def elementos_comuns(lista1, lista2):
    
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2))

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")