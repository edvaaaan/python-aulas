# QUEBRANDO UM NÚMERO

import math

num = float(input('Digite um número: '))
print('A parte inteira de {} é {}'.format(num, math.floor(num)))

# CATETOS E HIPOTENUSA 

import math

cato = int(input('Digite o cateto oposto: '))
cata = int(input('Digite o cateto adjacente: '))
hip = math.sqrt((math.pow(cato, 2) + math.pow(cata, 2)))
print('A hipotenusa vale: {}'.format(hip))

# SENO, COSSENO E TANGENTE

import math

angulo = int(input('Digite um ângulo: '))
print('Seno: {}, cosseno: {} e tangente: {}'.format(math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))

# SORTEANDO UM ALUNO 

import random

aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('O aluno sorteado a apagar o quadro foi: {}'.format(random.choice(lista)))

# SORTEANDO A ORDEM DOS TRABALHOS

import random

aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem das apresentações será: {}'.format(lista))