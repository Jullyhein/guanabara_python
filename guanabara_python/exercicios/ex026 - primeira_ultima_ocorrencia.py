#Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "a"
#em que posição ela aparece na primeira vez em que posicao ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('Seu nome tem ao todo: {}'.format (frase.count('A')))
print('A primeira letra A apareceu na posição: {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição: {}.'.format(frase.rfind('A')+1))

