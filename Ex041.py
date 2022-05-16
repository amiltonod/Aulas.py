from datetime import date
nas = int(input('Digite a data do seu nascimento: '))
idade = date.today().year - nas
print(f'Idade {idade}')
if idade < 10:
    print('Sua categoria é a MIRIM.')
elif idade < 15:
    print('Sua categoria é a INFANTIL.')
elif idade < 20:
    print('Sua categoria é a JUNIOR.')
elif idade == 20:
    print('Sua categoria é a SENIOR.')
else:
    master = idade > 20
    print('Sua categoria é a MASTER.')
print('Boa competição!')

