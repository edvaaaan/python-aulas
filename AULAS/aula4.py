# ORDEM DAS OPERAÇÕES: 1- () | 2- **, *, /, //, ** | 3- +, -

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A soma vale: {}'.format(n1 + n2))
print('A subtração vale: {}'.format(n1 - n2))
print('A multiplicação vale: {}'.format(n1 * n2))
print('A divisão vale: {}'.format(n1 / n2))
print('A divisão inteira vale: {}'.format(n1 // n2))
print('O resto da divisão vale: {}'.format(n1 % n2))
print('A potência vale: {}'.format(n1 ** n2))
print('A raiz quadrada vale: {}'.format(n1 ** (1/2)))

# ANTECESSOR E SUCESSOR 

num = int(input('Digete um número: '))
print('O antecessor de {} vale {} e o sucessor vale {}'.format(num, num - 1, num + 1))

# DOBRO, TRIPLO E RAIZ QUADRADA 

num = int(input('Digite um número: '))
print('O dobro de {} vale {}, o triplo {} e a raiz quadrada {}'.format(num, num * 2, num * 3, num * (1/2)))

# MEDIA DAS NOTAS 

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
soma = nota1 + nota2
print('A media do aluno foi {}'.format(soma/2))

# CONVERSOR DE MEDIDAS 

medida = int(input('Digite seu valor em metros: '))
print('O valor fale em centimetros {} e em milimetros {}'.format(medida * 100, medida * 1000))

# TABUADA

num = int(input('Digite um número: '))
print('{} vezes 1: {}'.format(num, num * 1))
print('{} vezes 2: {}'.format(num, num * 2))
print('{} vezes 3: {}'.format(num, num * 3))
print('{} vezes 4: {}'.format(num, num * 4))
print('{} vezes 5: {}'.format(num, num * 5))
print('{} vezes 6: {}'.format(num, num * 6))
print('{} vezes 7: {}'.format(num, num * 7))
print('{} vezes 8: {}'.format(num, num * 8))
print('{} vezes 9: {}'.format(num, num * 9))
print('{} vezes 10: {}'.format(num, num * 10))

# CONVERSOR DE MOEDAS 

valor = int(input('Digite seu valor em R$: '))
print('Seu valor em dólar vale: {}'.format(valor / 5.50))

# PINTANDO PAREDE 

altura = int(input('Qual a altura da parede: '))
largura = int(input('Qual a largura da parede: '))
print('Para a área de {} são necessarios {} litros de tinta'.format(altura * largura, (altura * largura)/2))

# 5% DESCONTO

valor = int(input('Digite o valor do produto: '))
print('O valor do produto com 5 porcento de desconto vale {}'.format(valor * 0.95))

# REAJUSTE SALARIAL  

salario = int(input('Digite seu salario atual: '))
print('O novo salario com 15 porcento de aumento vale {}'.format(salario + (salario * 15/100)))