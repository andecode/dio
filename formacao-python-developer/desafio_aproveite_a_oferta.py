'''Desafio
Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia você comprar 
refrigerantes e levar os cascos vazios no dia seguinte, ela troca cada conjunto de K garrafas 
vazias  por uma garrafa cheia. Um cliente quer aproveitar ao máximo essa oferta e por isso 
comprou várias garrafas no primeiro dia da promoção. Agora ele quer saber quantas garrafas 
terá ao final do segundo dia da promoção, se usá-la ao máximo.

Faça um programa para calcular isso.

Entrada
A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos 
de teste. Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),  
respectivamente o número de refrigerantes comprados e o número de garrafas vazias 
para ganhar uma cheia.

Saída
Para cada caso de teste imprima o número de garrafas que o cliente terá no segundo dia, 
se aproveitar ao máximo a oferta.
'''
T = int(input()) #Lendo o número de casos de teste

while T > 0: #Loop while que executa T vezes
  T -= 1 #Decrementa T a cada iteração do loop
  N, K = input().split()
  N = int(N)
  K = int(K)
  '''Divide o número de garrafas vazias pelo número de cascos necessários para trocar por uma garrafa cheia
     Calcula o resto da divisão de N por K para contar as garrafas que não podem ser trocadas por uma cheia
     Soma o resultado das duas operações para obter o total'''
  total = int(int(N % K) + int(N /K))
    
  print(total)
