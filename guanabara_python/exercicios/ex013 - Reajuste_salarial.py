#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 
salario = float(input('Digite o valor do seu salário: '))

desconto = (15/100) * salario
total = (salario + desconto)
print('O valor digitado é de R$ {:.2f}, e você terá um aumento de R$ {:.2f}, então a partir do mês que vem você receberá um salário de R$ {:.2f}'.format(salario, desconto, total))
