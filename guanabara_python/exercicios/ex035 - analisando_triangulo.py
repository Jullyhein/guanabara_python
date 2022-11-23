#Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo. 
from time import sleep
t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro seguimento'))
print('-'*20)
print('Analisando ...')
sleep(2)
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 +t2:
    print('Os segmentos podem formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo.')
