#faça um algoritmo que faça a conversão de temperaturas. 

cel = float(input('Informe a temperatura em C°: '))

conversao = ((cel * 9) /5) + 32

print('Agradecemos por nos informar que a temperatura local é de {}°C, e convertendo para Fareheit fica {}°F'.format(cel, conversao))