# EX 001 

num = []
pares = []
impares = []
aux = 0

for c in range(7):
    num.append(int(input('Digite um número: ')))

for c in range(7):
    if num[aux] % 2 == 0:
        pares.append(num[aux])
    else:
        impares.append(num[aux])
    aux += 1

print(pares)
print(impares)

# EX 002 
import random

jogo = []
jogos = []

numdejogos = int(input('Quantos jogos você quer fazer: '))

for a in range(numdejogos):
    for b in range(0, 6):
        num = random.randint(0, 60)

        if num not in jogo:
            jogo.append(num)
        
    jogos.append(jogo[:])
    jogo.clear()

print(jogos)