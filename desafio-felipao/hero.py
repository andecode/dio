"""Projeto Base: Escrevendo as Classes de Um Jogo
Escreva um programa em Python que crie uma classe genérica (class hero)  que represente um herói de uma aventura e que possua as seguintes propriedades:
- nome
- idade
- tipo (ex: guerreiro, mago, monge, ninja)

além disso, deve ter um método chamado atacar que deve atender os seguintes requisitos:
- exibir a mensagem: ("o {tipo} atacou usando {ataque}")
- aonde o {tipo} deve ser concatenado o tipo que está na propriedade da classe
- e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

- se mago -> no ataque exibir (usou magia)
- se guerreiro -> no ataque exibir (usou espada)
- se monje -> no ataque exibir (usou artes marciais)
- se ninja -> no ataque exibir (usou shuriken)

## Saída
Ao final deve se exibir uma mensagem:
print('O {tipo} atacou usando {ataque}"
ex: mago atacaou usando magia 
ex: guerreiro atacou usando espada

"""
class Hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'usou shuriken'
        else:
            ataque = 'usou um ataque genérico'

        print(f'O {self.tipo} atacou usando {ataque}')

heroi = Hero('Aragorn', 30, 'guerreiro')
heroi.atacar()

heroi2 = Hero('Gandalf', 1000, 'mago')
heroi2.atacar()

heroi3 = Hero('Bruce Lee', 35, 'monge')
heroi3.atacar()

heroi4 = Hero('Hanzo', 28, 'ninja')
heroi4.atacar()