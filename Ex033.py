# input's pedidos
from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# acabei usando listas apesar da aula ser de if e else, pois se mostrou mais eficiente.
numeros = [num1, num2, num3]
# começo do programa.
print('ANALISANDO...')
sleep(1)
print(f'O númmero maior dentre os demais é o {max(numeros)}')
print(f'O número menor dentre os demais é o {min(numeros)}')
