# EXEMPLO WHILE

#capacidade = int(input('Digite a capacidade do busão: '))
#aux = 0

#while capacidade > 0:
#    pessoas = int(input('Quantas pessoas vão entrar ou sair: '))
#    aux += pessoas

#    if aux == 0:
#        print('VAZIO')
#    elif aux > 0 and aux < capacidade:
#        print('AINDA CABE')
#    elif aux == capacidade:
#        print('LOTADO')
#    elif aux == capacidade * 2:
#        print('HORA DE PARTIR')
#        break
#    else:
#        print('DEU MERDA')

# EXEMPLO FOR

#capacidade = int(input('Digite a capacidade do busão: '))
#no_busao = 0

#for aux in range(no_busao, capacidade * 2):
#    pessoas = int(input('Quantas pessoas vão entrar ou sair: '))
#    no_busao += pessoas

#    if no_busao == 0:
#        print('VAZIO')
#    elif no_busao > 0 and no_busao < capacidade:
#        print('AINDA CABE')
#    elif no_busao == capacidade:
#        print('LOTADO')
#    elif no_busao == capacidade * 2:
#        print('HORA DE PARTIR')
#        break
#    else:
#        print('DEU MERDA')