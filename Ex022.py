nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome todo em maiúsculo {}'.format(nome.upper()))
print('Seu nome todo em minúsculo {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} ele tem {} letras'.format(separa[0], len(separa[0])))


