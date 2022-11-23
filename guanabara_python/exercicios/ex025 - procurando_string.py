#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SILVA"

nome = str(input('Qual seu nome completo: ')).strip()

print('Seu nome tem Silva? {}'.format('Silva' in nome))

nome = str(input('Escreva seu nome: '))
print('Nome digitado tem Santos? {}'.format('Santos' in nome))