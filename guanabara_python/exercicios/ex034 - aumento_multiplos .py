#Escreva um programa que pergunte o salário do funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250,00, calcule um aumento de 10%. 
# Para inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite seu salário. R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario +(salario * 10 /100)
print('Quem ganhava R$ {:.2f}, passa a ganhar R$ {:.2f}.'.format(salario, novo))