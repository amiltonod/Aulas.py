soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° número: '))
    if n %2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'Existem {cont} números pares, a soma de todos os números pares é {soma}.')
