#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugadi o e a quantidade de dias 
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0,15 por km rodado. 
percorrido_km = float(input('Escreva quantos KMs foram percorridos: '))
qtd_dias = int(input('Nos informe o total de dias com carro alugado: '))

cal_dia = qtd_dias * 60
cal_km = percorrido_km * 0.15
total = cal_dia + cal_km

print('Agradecemos por nos procurar, sendo assim foram percorridos {} KM, e {} dias.\nEntão o aluguel ficou R$ {:.2f}.'.format(percorrido_km, qtd_dias, total))