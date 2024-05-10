"""Calculadora de partidas Rankeadas
Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador, depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do cálculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100 = Lendário
Se vitórias for maior ou igual a 101 = Imortal

Saída
Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de {saldo_de_viorias} e está no nível {nível}
"""

vitórias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel


saldo, nivel = calcular_nivel(vitórias, derrotas)

print(f"O Herói tem um saldo de {saldo} e está no nível {nivel}")