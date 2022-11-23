
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) /2
print('Sua média foi de {}.'.format(m))
if m >=6.0:
    print('Sua média foi boa, Parabéns!')
else:
    print('Sua média foi ruim, Estude mais !')

#simplificado
print('Parabéns pela sua média' if m >=6.0 else 'Estude mais!!!!')
