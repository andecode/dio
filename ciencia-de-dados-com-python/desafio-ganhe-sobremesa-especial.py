# Recebendo o valor total do pedido como entrada do usuário
valorPedido = int(input())

# Criar as condições necessárias para impressão da saída conforme o enunciado.
# Verificando se o usuário tem direito a uma sobremesa grátis
if valorPedido >= 50.00:
    # Utilizando interpolação de strings para formatar a saída
    print("Parabens, você ganhou uma sobremesa gratis!")
else:
    # Utilizando interpolação de strings para formatar a saída
    print("Que pena, você nao ganhou nenhum brinde especial.")
