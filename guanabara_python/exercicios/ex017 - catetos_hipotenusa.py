'''Faça um programa que leia o comprimento do cateto adjacente de um 
triângulo retângulo, calcule e mostre o comprimento da hipotenusa'''

#co = float(input('Comprimento do cateto oposto? '))
#ca = float(input('Comprimento do cateto adjacente? '))

#hip = (co**2 + ca**2) ** (1/2)
#print('A hipotenusa irá medir {:.2f}, o cateto oposto {}, e o cateto adjacente {}'.format(hip, co, ca))

#Outra forma
import math

co1 = float(input('Comprimento do cateto oposto? '))
ca1 = float(input('Comprimento do cateto adjacente? '))

hi = math.hypot(co1, ca1)
print('A hipotenusa irá medir {:.2f}'.format(hi))