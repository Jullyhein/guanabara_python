nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
separa = nome.split()
#o separa vai mostrar apenas o PRIMEIRO NOME, e mostrar quantas letras ele tem. 
print('Seu primeiro nome é {}, e tem  {} letras.'.format(separa[0], len(separa[0])))