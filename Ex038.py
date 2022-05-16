# dando as váriaveis
nmr1 = int(input('Digite o primeiro número inteiro: '))
nmr2 = int(input('Digite o segundo número inteiro: '))
# condições com todas as váriavies possiveis empate maior e menor
if nmr1 > nmr2:
    print(f'O primeiro valor {nmr1} é maior que o segundo valor {nmr2}.')
elif nmr2 > nmr1:
    print(f'O segundo valor {nmr2} é maior que o primeiro valor {nmr1}.')
else:
    print('Não existe valor maior os dois são iguais.')
