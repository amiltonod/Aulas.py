from time import sleep
nom = str(input('Qual seu nome completo?: ')).strip().upper()
print('Seu nome tem Silva?')
print('ANALISANDO...')
sleep(1)
print('SILVA' in nom)
