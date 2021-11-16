# TIPOS PRIMITIVOS
# INT, FLOAT, BOOL E STR

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma desses dois numeros vale {}'.format(s))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# DESCOBRINDO OS TIPOS 

var = input('Digite algo: ')
print('É numerico ?', var.isnumeric())
print('É alfabetico ?', var.isalpha())
print('É alfanumerico ?', var.isalnum())