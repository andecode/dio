'''Desafio de código - Verificação de Paridade
Descrição
Neste desafio, você deve escreva uma solução que receba um número inteiro como entrada e determine se ele é par ou ímpar. Dessa forma, a solução deve retornar uma string indicando Par se o número for par e Ímpar se o número for ímpar.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html

Entrada
A entrada do programa é um único número inteiro.

Saída
A saída do programa é uma string que será Par se o número for par e Ímpar se o número for ímpar.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
2	Par
5	Ímpar
6	Par
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.
'''
# Solicita ao usuário um número inteiro
numero = int(input())

# TODO: Verifique se o número é par ou ímpar e imprima o resultado:
if numero % 2 == 0:
  print("Par")
else:
  print("Ímpar")