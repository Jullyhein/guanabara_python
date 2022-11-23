#faça um programa que leia o nome completo de uma pessoa, e mostre em seguida o primeiro e o último nome separadamente.
#ex: Ana Maria de Souza Primeiro = Ana último = Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
