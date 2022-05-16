numero = int(input('Digite um numero: '))
# dividindo e a % serve para colocar o resto da divisão fazendo assim que com que o código saia corretamente
# primeira vez que uso o %(resto) para fazer um código, muito proveitoso até agora!
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
# prints sem segredo usando o format e a váriavel.
print('Analisando o número {}.'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
