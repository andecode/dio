entrada = input("Digite o texto do tweet: ")

def verifica_tamanho_tweet(texto):
    if len(texto) > 140:
        print("MUTE")
    else:
        print("TWEET")

# Obtém a entrada do usuário


# Chama a função para verificar o tamanho e imprimir o resultado
verifica_tamanho_tweet(entrada)