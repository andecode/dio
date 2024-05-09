# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

#Verificar se a quantidade de passos é positiva
if quantidade_passos < 0:
  print("Número de passos inválido. Por favor, insira um número inteiro positivo.")
elif quantidade_passos == 0:
  print("Nenhum passo dado na floresta.")
else:
  #Simular os passos do explorador
  for i in range(1, quantidade_passos + 1):
    if i == 1:
      print(f"Explorador: {i} passo")
    else:
      print(f"Explorador: {i} passos")
