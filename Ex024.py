from time import sleep
cidade = str(input('Em qual ciadade você nasceu?: ')).strip().upper()
print('Analisando nome da cidade...')
sleep(2)
print('Sua cidade se chama {}'.format(cidade))
print('SANTO' in cidade)