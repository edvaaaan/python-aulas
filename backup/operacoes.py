# OPERAÇÕES BÁSICAS:
na = int(input('Digite o primeiro número: '))
nb = int(input('Digite o segundo número: '))

print('A soma de {} e {} é {}'.format(na, nb, na + nb))
print('A subtração de {} e {} é {}'.format(na, nb, na - nb))
print('A multiplicação de {} e {} é {}'.format(na, nb, na * nb))
print('A divisão de {} e {} é {:.2f}'.format(na, nb, na/nb))
print('O resto da divisão de {} e {} é {}'.format(na, nb, na%nb))

# ARÉA DO TRIÂNGULO
import math

a = int(input('Digite o tamanho: '))
b = int(input('Digite o tamanho: '))
c = int(input('Digite o tamanho: '))

peri = (a+b+c) / 2
area = math.sqrt(peri * (peri - a) * (peri - b) * (peri - c))

print('A área do triângulo é {:.2f}'.format(area))

# DESEMPENHO MOTOR
velocidade = int(input('Digite a velocidade do carro em km/h: '))
tempo = int(input('Digite o tempo da viagem em minutos: '))
consumo = int(input('Digite o consumo do carro em litros: '))

tempo_horas = tempo/60
distancia = velocidade * tempo_horas

print('O desempenho do motor é de {:.2f}'.format(distancia / consumo))

# PARCELANDO UMA TELEVISÃO 
valor = int(input('Digite o valor do produto que deseja comprar: '))
parcela = int(input('Digite a quantidade de vezes que você deseja parcelar: '))

if parcela == 1:
    juros = valor
    divisao = juros / parcela
    print('Você vai pagar 1 parcela de {} totalizando {}'.format(divisao, juros))
elif parcela == 2:
    juros = valor * 1.05
    divisao = juros / parcela
    print('Você vai pagar {} parcelas de {} totalizando {}'.format(parcela, divisao, juros))
elif parcela == 3:
    juros = valor * 1.10
    divisao = juros / parcela
    print('Você vai pagar {} parcelas de {} totalizando {}'.format(parcela, divisao, juros))
elif parcela == 4:
    juros = valor * 1.15
    divisao = juros / parcela
    print('Você vai pagar {} parcelas de {} totalizando {}'.format(parcela, divisao, juros))
elif parcela == 5:
    juros = valor * 1.20
    divisao = juros / parcela
    print('Você vai pagar {} parcelas de {} totalizando {}'.format(parcela, divisao, juros))
elif parcela == 6:
    juros = valor * 1.25
    divisao = juros / parcela
    print('Você vai pagar {} parcelas de {} totalizando {}'.format(parcela, divisao, juros))
elif parcela == 7:
    juros = valor * 1.30
    divisao = juros / parcela
    print('Você vai pagar {} parcelas de {} totalizando {}'.format(parcela, divisao, juros))
elif parcela == 8:
    juros = valor * 1.35
    divisao = juros / parcela
    print('Você vai pagar {} parcelas de {} totalizando {}'.format(parcela, divisao, juros))
elif parcela == 9:
    juros = valor * 1.40
    divisao = juros / parcela
    print('Você vai pagar {} parcelas de {} totalizando {}'.format(parcela, divisao, juros))
elif parcela == 10:
    juros = valor * 1.45
    divisao = juros / parcela
    print('Você vai pagar {} parcelas de {} totalizando {}'.format(parcela, divisao, juros))
else:
    print('Não podemos parcelar sua compra!')

# DISTÂNCIA ENTRE DOIS PONTOS

# XADREZ - OBI

# DOMINÓ - OBI