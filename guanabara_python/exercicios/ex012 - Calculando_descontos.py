#faça um algoritmo que leia o preço de um produto e mostre seu novo preço , com 5% de desconto. 

preco = float(input('Digite o valor do produto adquirido: '))

desconto = (5/100) * preco
total = (preco - desconto)
print('O valor do produto é de R$ {}, e você tem um desconto de 5%, então seu total é de R$ {} '.format(preco, total))
