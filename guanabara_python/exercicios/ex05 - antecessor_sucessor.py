#faça um programa que leia um numero inteiro e mostre na tela seu sucessor e antecessor.
num = (int(input('Digite um número inteiro: ')))

cont2 = num - (1)
cont = num + (1)

print('O número digitado foi: {}, e o antecessor do número digitado é {}, e o sucessor {}.'.format(num, cont2, cont))

#outro jeito para fazer.
#print('O número digitado foi: {}, e o antecessor do número digitado é {}, e o sucessor {}.'.format(num, (num-1), (num+1)))

#raiz quadrada dá para fazer de outra forma:
#pow(n, (1/2))