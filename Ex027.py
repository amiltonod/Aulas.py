name = str(input('Digite seu nome completo: ')).strip()
m = name.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(m[0]))
# o -1 serve para mostrar a última string da lista
print('Seu último nome é {}'.format(m[-1]))
