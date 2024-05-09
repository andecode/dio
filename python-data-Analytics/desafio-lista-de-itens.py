# Lista para armazenar os itens
itens = []

# Solicita os itens ao usuário
for i in range(3):
    item = input()
    itens.append(item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")
    