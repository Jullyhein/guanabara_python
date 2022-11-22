#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considere US$ 1,00 = 3,27 REAIS.

#real = float(input('Digite um valor que tenha em sua carteira: R$ '))

#dolar = real / 5.30

#print('Você tem R$ {} reais, e pode comprar US$ {:.2f} dólares.' .format(real, dolar))

dolar = float(input('Digite um valor que tenha em sua carteira: US$ '))

real = dolar / 1.25
print('Você tem US$ {}, e poderia comprar R$ {:.2f} reais'.format(dolar, real))