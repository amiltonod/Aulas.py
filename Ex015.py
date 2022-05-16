km = float(input('Quantos Kms o carro andou?: '))
dias = int(input('Quantos dias o carro foi alugado?: '))
pagar = (km * 0.15) + (dias * 60)
print('O preço a pagar pelo uso do carro é R${:.2f}'.format(pagar))
