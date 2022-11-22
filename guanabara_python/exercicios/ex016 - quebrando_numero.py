# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

'''import math
real = float(input('Digite um valor: '))

print('O valor digitado foi {}, e sua porção inteira é {}'.format(real, math.trunc(real)))

#OUUUU

from math import trunc
real = float(input('Digite um valor: '))

print('O valor digitado foi {}, e sua porção inteira é {}'.format(real, trunc(real)))
'''
#OUUUUUU

num = float(input('Digite um valor: '))
print('O valor digitado foi {}, e seu valor inteiro é {}'.format(num, int(num)))