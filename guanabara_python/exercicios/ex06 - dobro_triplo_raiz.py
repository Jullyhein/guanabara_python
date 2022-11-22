#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. 

num = int(input('Digite um número: '))

dob = num ** (2)
trip = num ** (3) 
raiz = num**(1//2)

print('Agradecemos pelo número. \nO valor digitado foi {},\nO dobro do valor é: {},\nO triplo: {},\nE a raíz quadrada é {}'.format(num, dob, trip, raiz))

#outro jeito
#print('Agradecemos pelo número. \nO valor digitado foi {},\nO dobro do valor é: {},\nO triplo: {},\nE a raíz quadrada é {}'.format(num, (num**2), (num**3), (num**(1/2))))