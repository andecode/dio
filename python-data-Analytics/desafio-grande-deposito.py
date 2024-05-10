valor = float(input())

if valor > 0:
  #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
  print("Deposito realizado com sucesso!")
  print(f"Saldo atual: R$ {valor:.2f}")
# TODO: Imprimir a mensagem de encerrar o programa.
elif valor == 0:
  print("Encerrando o programa...")
# TODO: Imprimir a mensagem de valor inválido.
else:
  print("Valor invalido! Digite um valor maior que zero.")
  