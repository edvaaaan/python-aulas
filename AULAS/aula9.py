# ADIVINHE O NUMERO 
import random

np = random.randrange(5)
nv = int(input('Digite um número entre 0 e 5: '))

if nv == np:
    print('Você ganhou!')
else:
    print("Você perdeu!")

# MULTANDO OS CARROS
v = int(input('Digite a velocidade do seu carro: '))
m = (v - 80) * 7
if v > 80:
    print('Você foi multado, o valor da multa é {} reais'.format(m))
else:
    print('Tudo OK!')

# IMPAR OU PAR
n = int(input('Digite um número: '))
if n%2 == 0:
    print('Seu número é par!')
else: 
    print('Seu número é ímpar!')

# VIAGEM
km = int(input('Digite a distancia em km de sua viagem: '))
pabd = float(km * 0.50)
pacd = float(km * 0.45)

if km > 200:
    print('O preço da sua viagem é de {} reais'.format(pacd))
else:
    print('O preço da sua viagem é de {} reais'.format(pabd))

# MAIOR E MENOR 
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O número é {} o maior'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O número é {} o maior'.format(n2))
else:
    print('O número é {} o maior'.format(n3))

if n1 < n2 and n1 < n3:
    print('O número é {} o menor'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O número é {} o menor'.format(n2))
else:
    print('O número é {} o menor'.format(n3))

# AUMENTO DE SALARIO
salario = int(input('Digite seu salario atual: '))

if salario > 1250:
    print('Seu aumento deve ser de {:.2f}'.format(salario * 1.1))
else:
    print('Seu aumento deve ser de {:.2f}'.format(salario * 1.15))