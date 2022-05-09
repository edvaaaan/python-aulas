import random

tam = int(input('Quantos caracteres voce quer em sua senha: '))

caracteres = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
senha = ''

for r in range(tam):
    sorteio = random.choice(caracteres)
    senha = senha + sorteio
print(senha)