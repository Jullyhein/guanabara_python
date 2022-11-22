#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informções possíveis sobre ele. 
n = input('Digite algo: ')

print('Olá, o valor digitado foi {}, então vamos tirar algumas dúvidas sobre ele.' .format(n))
print('O tipo do valor digitado é:', type(n))
print('Tem apenas espaços?', n.isspace())
print('Este valor é numérico?', n.isnumeric())
print('Este valor é um dígito?', n.isdigit())
print('É alfabético?'), n.isalpha()
print('Este valor é um decimal?', n.isdecimal())
print('Está capitalizada?', n.istitle())
print('Está maiúsculo?', n.isupper())
print('Está minúsculo?', n.islower())