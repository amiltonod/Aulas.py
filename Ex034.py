sal = float(input('Digite o valor do salário:R$'))
if sal > 1250:
    mat = 10 / 100
    aum = (mat * sal) + sal
else:
    mat = 15 / 100
    aum = (mat * sal) + sal
print('O valor do aumento salárial ficou em {}R${}'.format('\033[0;34;40m', aum))
