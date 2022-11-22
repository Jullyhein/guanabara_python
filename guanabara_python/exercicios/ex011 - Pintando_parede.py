#faça um programa que leia a largura e a altura de uma parede em 
# metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2m.

alt = float(input('Digite a altura de uma parede em metros: '))
larg = float(input('Digite a largura da mesma em metros: '))

area = larg * alt
tinta = area / 2
#total = tinta * 1000

print('A altura é {}, largura {}, A area informada é: {}m'.format(alt, larg, area))
print('Agradecemos por nos encaminhar as informações, você precisará de {} L de tinta para pintar a sua parede.'.format(tinta))
