# FINANCIANDO UMA CASA 

#p = int(input('Qual o preço da casa que voce deseja comprar ? '))
#s = int(input('Qual o seu salario ? '))
#a = int(input('Em quantos anos voce pretende pagar essa casa ? '))

#f = p / a * 12
#pf = s * 30 / 100

#if f > pf:
#    print('Você não pode financiar a casa')
#else:
#    print('Você pode financiar e vai ter que pagar {} reais mensalmente'.format(f))

# QUAL O MAIOR VALOR

pv = int(input('Digite o primeiro valor: '))
sv = int(input('Digite o segundo valor: '))

if pv > sv:
    print('O primeiro valor é o maior')
elif sv > pv:
    print('O segundo valor é o maior')
else:
    print('Não existe valor maior')

# ALISTAMENTO

idade = int(input('Digite sua idade: '))

if idade == 18:
    print('Esta na idade de você se alistar!')
elif idade > 18:
    print('Já passou {} ano de você se alistar!'.format(idade - 18))
else:
    print('Você ainda não esta na idade, mas daqui a {} anos de você deve se alistar!'.format(18 - idade))

# MEDIA DE NOTAS 

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

if media < 5:
    print('REPROVADO')
elif 5 < media and media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

# CATEGORIA 

data = int(input('Digite seu ano de nascimento: '))
idade = 2022 - data

if idade <= 9: 
    print('MIRIM')
elif 9 < idade and idade <= 14:
    print('INFANTIL')
elif 14 < idade and idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')

# QUAL O TIPO DE TRIANGULO 

la = int(input('Digite o tamanho do primeiro lado: '))
lb = int(input('Digite o tamanho do segundo lado: '))
lc = int(input('Digite o tamanho do terceiro lado: '))

if la == lb and la == lc:
    print('O seu triângulo é equilátero')
elif la == lb or la == lc or lb == lc:
    print('O seu triângulo é isóceles')
else:
    print('Seu triângulo é escaleno')

# IMC
#import math

#altura = float(input('Digite sua altura em metros: '))
#peso = float(input('Digite seu peso em kilos: '))

#imc = math.pow(altura, 2) / peso
#print('Seu IMC é {}'.format(imc))

# 

# PEDRA, PAPEL E TESOURO
import random 

print('Pedra = R, Papel = P, Tesoura = S')
jogador = str(input('Digite sua opção: '))

lista = ['R', 'P', 'S']
maquina = random.choice(lista)
print('A maquina escolheu: {}'.format(maquina))

if jogador == 'R' and maquina == 'S':
    print('Você venceu!')
elif jogador == 'P' and maquina == 'R':
    print('Você venceu!')
elif jogador == 'S' and maquina == 'P':
    print('Você venceu!')
elif jogador == 'R' and maquina == 'P':
    print('Você perdeu!')
elif jogador == 'P' and maquina == 'S':
    print('Você venceu!')
elif jogador == 'S' and maquina == 'R':
    print('Você venceu!')
else:
    print('Empate!')