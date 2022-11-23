#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

velocity = float(input('Digite a velocidade de um carro: '))
if velocity > 80:
    multa = (velocity - 80) * 7
    print('MULTADO.\nVocê excedeu o limite de velocidade que seria 80km.')
    print('Você foi multado, e o valor da multa ficaria R$ {:.2f}'.format(multa))
