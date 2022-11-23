#desenvolva um programa que pergunte a distância de uma viagem em km, 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até
# 200km e R$0,45 para viagens mais longas. 
#condicional composta.
'''
distancia = float(input('Digite a distância da viagem: '))
if distancia <= 200:
    km = distancia * 0.50
    print('A tarifa cobrada pela distância {}KM, será de R$ {:.2f} pela sua viagem.'.format(distancia, km))
else:
    kms = distancia * 0.45
    print('A tarifa cobrada pela distância {}KM, será de R$ {:.2f}.'.format(distancia, kms))
'''

distancia = float(input('Qual é a KM de sua viagem?'))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('A tarifa cobrada pela distância {}KM, será de R$ {:.2f}.'.format(distancia, preco))