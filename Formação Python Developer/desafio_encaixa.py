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