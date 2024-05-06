'''Desafio
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.'''
# Lê o número de casos de teste
N = int(input())

# Loop para processar cada caso de teste
while N > 0:
    # Lê os valores de entrada e os divide em A e B
    v = input().split(" ")
    a = v[0].strip()  # Remove espaços em branco extras do valor de entrada A
    b = v[1].strip()  # Remove espaços em branco extras do valor de entrada B

    # Verifica se B é mais longo que A
    if len(b) > len(a):
        print("nao encaixa")  # Se B for mais longo que A, não pode encaixar
    # Verifica se os últimos dígitos de A correspondem a B
    elif a[-len(b):] == b:
        print("encaixa")  # Se os últimos dígitos de A correspondem a B, encaixa
    else:
        print("nao encaixa")  # Caso contrário, não encaixa

    N -= 1  # Passa para o próximo caso de teste