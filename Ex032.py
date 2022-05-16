from _datetime import date
ano = int(input('Digite o ano que quer analisar: . Se quer analisar o ano atual digite 0.\n'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO.')
