soma = 0
cont = 0
for c in range(1, 501, 2):
    if c %3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'O total de números múltiplos por 3 é {cont} e o total da soma entre eles é {soma}')
