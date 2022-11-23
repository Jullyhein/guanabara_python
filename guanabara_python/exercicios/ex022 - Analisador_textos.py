#Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúsculas.
#o nome com todas minúsculas.
#quantas letras ao todo(sem considerar espaços)
#
#quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
print('O seu nome em letras maiúsculas fica: {}'.format(nome.upper()))
print('O seu nome em letras minúsculas fica: {}'.format(nome.lower()))
print('Seu nome tem ao todo: {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#ou
separa = nome.split()
print('Seu primeiro nome é {}, e tem {} letras'.format(separa[0], len(separa[0])))



