'''Desafio de código - Conversão de Dados de Temperatura
Descrição
Você está desenvolvendo um sistema de monitoramento de temperaturas para uma estação meteorológica. O seu script deve processar os dados brutos de temperaturas e converter esses dados de Celsius para Fahrenheit.

Para converter uma temperatura de Celsius para Fahrenheit, utiliza-se a fórmula matemática:

TF = (TC × 9/5) + 32

Onde:

TF representa a temperatura em graus Fahrenheit,
TC representa a temperatura em graus Celsius.

Entrada
A entrada deve receber uma string com valores numéricos separados por “,” (vírgula) representando as temperaturas em graus Celsius.

Saída
Deverá retornar uma lista de valores numéricos representando as temperaturas convertidas para Fahrenheit.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
0,10,20,30,40	[32.0, 50.0, 68.0, 86.0, 104.0]
-5,-15,5,15,25	[23.0, 5.0, 41.0, 59.0, 77.0]
12,25,30,18,5	[53.6, 77.0, 86.0, 64.4, 41.0]
'''
# Recebe a entrada do usuário como uma string e divide essa string nos caracteres ',' (vírgula),
temperaturas_celsius = input().split(',')

# função chamada converter_celsius_para_fahrenheit que recebe uma lista de strings
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    temperaturas_celsius = [float(temp) for temp in temperaturas_celsius]
    
    # TODO: Calcule as temperaturas em Fahrenheit para cada temperatura em Celsius convertida para float
    temperaturas_fahrenheit = []
    for temp_c in temperaturas_celsius:
      temp_f = (temp_c * 9/5) + 32
      temperaturas_fahrenheit.append(temp_f)
    
    return temperaturas_fahrenheit

# Imprime o resultado das temperaturas convertidas para Fahrenheit.
print(converter_celsius_para_fahrenheit(temperaturas_celsius))