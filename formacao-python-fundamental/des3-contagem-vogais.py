'''Desafio de código - Contagem de Vogais
Descrição
Neste desafio, implemente uma solução para completar a função conta_vogais que conta o número de vogais em uma string fornecida como entrada. Vogais são caracteres específicos sem acentuação, incluindo tanto letras minúsculas quanto maiúsculas (aeiouAEIOU).

Para resolver este desafio, siga os passos abaixo:

1. Defina um conjunto de vogais: Primeiramente, crie um conjunto contendo todas as vogais sem acentuação, incluindo tanto letras minúsculas quanto maiúsculas.

2. Inicialize um contador: Em seguida, crie uma variável para contar o número de vogais encontradas na string, começando com zero.

3. Itere pelos caracteres da string: Aqui percorremos cada caractere na string de entrada para verificar se é uma vogal.

4. Verifique se o caractere é uma vogal: Para cada caractere, verifique se ele está presente no conjunto de vogais definido no passo 1. Se o caractere for uma vogal, incremente o contador em 1.

5. Retorne o contador: Após percorrer todos os caracteres da string, retorne o valor do contador, que representa o número total de vogais na string.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements

Entrada
A função recebe como entrada uma única string contendo letras/palavras.

Saída
A função deve retornar um número inteiro que representa o total de vogais encontradas na string de entrada.
 

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
Python	O número de vogais na string 'Python' é: 1
Programação	O número de vogais na string 'Programação' é: 4
Função	O número de vogais na string 'Função' é: 2
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.
'''
def conta_vogais(texto):
    # TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = set('aeiouAEIOU')
    # TODO: Inicialize um contador para contar as vogais:
    contador = 0
    
    # Iteramos pelos caracteres da string
    for char in texto:
        # TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char in vogais:
          contador += 1
    
    return contador

# Solicitamos ao usuário que insira uma string
texto = input()

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")