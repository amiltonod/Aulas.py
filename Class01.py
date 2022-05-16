produto = int(input('Valor do produto:R$'))
modo_pagamento = input('Pagamento á vista?: ')
if modo_pagamento == 'Sim' and 'sim':
    pagamento_avista = produto - (produto * 10 / 100)
    print('O valor do produto ficará {}.'.format(pagamento_avista))
else:
    pagamento_aprazo = produto + (produto * 8 / 100)
    print('O valor do produto ficará {}.'.format(pagamento_aprazo))
