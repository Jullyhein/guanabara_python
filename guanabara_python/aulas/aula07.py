#operadores aritméticos. 
#n = 5 + 3 * 2 
#print(n)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1/n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a multiplicação {}, a divisão {:.2f}'.format(s, m, d), end = ' ')
print('O resto {}, e a exponenciação {}'.format(di, e))