valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

#TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
preco_total_hamburgueres = valorHamburguer * quantidadeHamburguer
preco_total_bebidas = valorBebida * quantidadeBebida
preco_final_pedido = preco_total_hamburgueres + preco_total_bebidas

#TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
troco = valorPago - preco_final_pedido

#TODO: Imprimir a saída no formato especificado neste desafio.
print(f"O preço final do pedido é R$ {preco_final_pedido:.2f}. Seu troco é R$ {troco:.2f}.")
