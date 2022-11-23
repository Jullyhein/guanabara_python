#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário 
# tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuario venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
print('-'*40)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5')
print('-'*40)
jogador = int(input('Em que número eu pensei? '))
print('PENSANDO ...')
sleep(3)
if jogador == computador:
    print('Parabéns, você me venceu!!!')
else:
    print('GANHEEEEEEI, Pensei no número {}, e não no {}'. format(computador, jogador))
