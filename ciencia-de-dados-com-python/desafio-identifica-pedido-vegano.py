numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input().strip().lower() == 's'

    #TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.
    tipo = "Vegano" if ehVegano else "Nao-vegano"

    print(f"Pedido {i}: {prato} ({tipo}) - {calorias} calorias")
    