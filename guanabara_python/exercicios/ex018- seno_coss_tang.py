#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''from math import sin, cos

angulo = float(input('Digite um ângulo que você deseja: '))

print('O ângulo de {}, tem o SENO de {}'.format(angulo, sin(angulo)))
print('O ângulo de {}, tem o SENO de {}'.format(angulo, cos(angulo)))
#print('O ângulo de {}, tem o SENO de {}'.format(angulo, sin(angulo)))'''

#tem que converter primeiro em radianos e em seguida calcular o que foi pedido

import math
angulo1= float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo1))

print('O ângulo digitado foi {}, e o SENO é de: {:.2f}'.format(angulo1, seno))
cosseno = math.cos(math.radians(angulo1))
print('O ângulo digitado foi {}, e o COSSENO é de: {:.2f}'.format(angulo1, cosseno))
tangente  = math.tan(math.radians(angulo1))
print('O ângulo digitado foi {}, e a TANGENTE é de: {:.2f}'.format(angulo1, tangente))