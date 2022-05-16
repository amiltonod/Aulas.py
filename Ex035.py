print('\033[1;32m+--+' * 8)
print('\033[1;31;40m!___\033[mAnalisador de triângulos\033[1;31;40m___!')
print('\033[1;32m+--+\033[m' * 8)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento'))
if a < b + c and b < a + c and c < a + b:
    print('O segmento acima pode formar um triângulo')
else:
    print('O segmento acima não pode formar um triângulo')
