# ceil -> pra cima, floor-> pra baixo, pow -> potencia, sqrt -> raiz quadrada, fatorial -> fatorial 
# import biblioteca | from biblioteca import função

import math 

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {}'.format(num, raiz))

# {:.Xf} -> arredondar 

import random

num = random.random()
print('O número gerado é {}'.format(num))
numint = random.randint(1, 10)
print('O número gerado é {}'.format(numint))