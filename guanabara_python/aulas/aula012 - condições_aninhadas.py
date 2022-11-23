nome = str(input('Digite seu nome: '))
if nome == 'Jullyen':
    print('Seu nome não é muito comum, mas é lindo!!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é muito popular no Brasil!')
else:
    print('Seu nome é normal'.format(nome))
print('Tenha um bom dia, {}'.format(nome))