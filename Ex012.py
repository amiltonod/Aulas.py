valor = float(input('Digite o valor do produto: R$ '))
p = (valor * 5) / 100
print('O valor do produto é {} com o desconto ficou {:.2f}.'.format(valor, valor - p))
