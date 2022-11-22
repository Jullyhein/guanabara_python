#escreva um programa que leia um valor em metros e exiba convertivo cm e milimetros
m = int(input('Digite um valor em metros: '))

cm = m * 100
mm = m* 1000

print('Agradecemos por ter nos informado a metragem de {}, e a conversão em cm seria de {}cm, e a conversão em milímetros é de {}.'.format(m, cm, mm))