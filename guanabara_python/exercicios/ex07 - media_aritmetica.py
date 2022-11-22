#desenvolva um programa que leia as duas notas de um aluno, e calcule e mostre a média.
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2)/2

print('A sua média é de: {:.2f}'.format(media))