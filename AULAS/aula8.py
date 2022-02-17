# NOME COMPLETO
import string

nome = str(input('Digite seu nome completo: '))
print('Seu nome em caixa alta é {}'.format(nome.upper()))
print('Seu nome em caixa baixa é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro tem {} letras'.format(nome.find(' ')))

# DIGITOS DE UM NUMERO
import string

numero = str(input('Digite um número: '))
print('Milhar: {}'.format(numero[0]))
print('Centena: {}'.format(numero[1]))
print('Dezena: {}'.format(numero[2]))
print('Unidade: {}'.format(numero[3]))

# COMEÇA OU NÃO COM SANTO
import string

cidade = str(input('Digite o nome de uma cidade: '))
if 'santo' in cidade:
    print('Tem sim')
else:
    print('Não tem')

# TEM SILVA
import string

nome = str(input('Digite seu nome completo: '))
if 'silva' in nome:
    print('Tem sim')
else:
    print('Não tem')

# LETRAS A
import string

palavra = str(input('Digite uma palavra qualquer: ')).upper()
print('A letra "A" aparece {} vezes'.format(palavra.count('A')))
print('A primeira vez ela aparece na posição {}'.format(palavra.find('A') + 1))
print('A ultima vez ela aparece na posição {}'.format(palavra.rfind('A') + 1))