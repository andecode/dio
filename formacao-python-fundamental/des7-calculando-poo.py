'''Desafio de código - Calculando com POO
Descrição
O desafio consiste em implementar uma classe Calculadora que utilize os princípios da Programação Orientada a Objetos (POO). A classe deve conter um método para realizar a operação de soma entre dois números inteiros, encapsulando assim a lógica matemática da adição.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/classes.html

Entrada
A entrada será composta por dois números inteiros fornecidos pelo usuário.

Saída
A saída esperada é o resultado da soma dos dois números inteiros fornecidos como entrada.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
5
5	10
8
8	16
20
10	30
'''
# TODO: Crie uma classe e método para realizar a soma:
class Calculadora:
    def soma(self, a, b):
        return a + b

num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)