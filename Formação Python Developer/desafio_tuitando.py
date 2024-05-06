'''DESAFIO
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

Entrada
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

Saída
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".'''

entrada = input("Digite o texto do tweet: ")

def verifica_tamanho_tweet(texto):
    if len(texto) > 140:
        print("MUTE")
    else:
        print("TWEET")

# Obtém a entrada do usuário


# Chama a função para verificar o tamanho e imprimir o resultado
verifica_tamanho_tweet(entrada)