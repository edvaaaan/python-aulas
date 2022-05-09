# TUPLA POR EXTENSO 

contagem = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
num = int(input('Digite um número de 0 a 10: '))

print('{} por expenso é {}'.format(num, contagem[num]))

# BRASILEIRÃO 

times = ('Vasco', 'Fluminense', 'Botafogo', 'Bahia', 'Atletico Mineiro', 'Flamengo', 'São Paulo', 'Cruzeiro', 'Corinthias', 'Santa Cruz')

print('Os primeiros colocados são: {}'.format(times[0:5]))
print('Os ultimos colocados são: {}'.format(times[-5:]))
print('A tabela em ordem alfabetica fica: {}'.format(sorted(times)))

# GERAR NUMEROS E COLOCAR NA TUPLA 
import random

gerador = random.randrange(10)

for c in range(5):
    print(gerador)