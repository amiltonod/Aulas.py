# input do valor do produto
val1 = float(input('Digite o valor do produto: R$'))
# calculo de porcentagens e declaração de váriaveis
vista_money_cheque = val1 - (10 / 100 * val1)
vista_card = val1 - (5 / 100 * val1)
x2 = val1 / 2
x3 = (val1 + (20 / 100 * val1)) / 3
# interface do usuario
print('[1] = Á VISTA DINHEIRO/CHEQUE -10% \n[2] = Á VISTA CARTÃO -5%')
print('[3] = Á PRAZO 2X S/CUSTO \n[4] = Á PRAZO 3X +20%')
forma_pag = int(input('Escolha a forma de pagamento: '))
# condições
if forma_pag == 1:
    print(f'O produto custá R${val1:.2f} o valor a ser pago com desconto de 10% fica R${vista_money_cheque:.2f}.')
elif forma_pag == 2:
    print(f'O produto custá R${val1:.2f} o valor a ser pago com desconto de 5% fica R${vista_card:.2f}.')
elif forma_pag == 3:
    print(f'O pruduto custá R${val1:.2f} o valor a ser pago a prazo em 2x R${x2:.2f}.')
elif forma_pag == 4:
    print(f'O produto custá R${val1:.2f} o valor a ser pago com juros de 20% fica 3x R${x3:.2f}.')
else:
    print(f'Valor do produto {val1:.2f}.')
    print('Escolha uma forma de pagamento válida.')
print('Agradecemos pela preferência, volte sempre!')
