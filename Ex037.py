# nesse ponto é feito o cabeçalho do programa
nmr = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
# aqui é feita a escolha de opções
opc = int(input('Escolha uma opção: '))
# no python é dada a conversão sem precisar abrir variáveis no caso foi usado
# bin para binário, oct para octal e hex para hexadecimal.
if opc == 1:
    print(f'Dado o número inteiro {nmr} a conversão BINÁRIA é \033[1;31;40m{bin(nmr)[2:]}\033[m')
elif opc == 2:
    print(f'Dado o número inteiro {nmr} a conversão OCTAL é \033[1;31;40m{oct(nmr)[2:]}\033[m')
elif opc == 3:
    print(f'Dado o númeor inteiro {nmr} a conversão HEXADECIMAL é \033[1;31;40m{hex(nmr)[2:]}\033[1;31;40m')
# print para o caso se haver algum comando inválido
else:
    print('Comando Inválido!')
