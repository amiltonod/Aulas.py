import random
import time
print('_' * 15)
print('   JO-KEN-PÔ')
print('_' * 15)
print('[ 0 ] = Pedra \n[ 1 ] = Papel \n[ 2 ] = Tesoura')
jog = int(input('Qual a jogada?: '))
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ!')
time.sleep(1)
itens = ('Pedra', 'Papel', 'Tesoura')
maq = [0, 1, 2]
jogm = random.choice(maq)
pedra = 0
papel = 1
tesoura = 2
print(f'Jogador jogou {itens[jog]}.')
time.sleep(1)
print(f'Maquina jogou {itens[jogm]}')
if jog == 0: # pedra
    if jogm == 0:
        print('EMPATE')
    elif jogm == 1:
        print('VOCÊ PERDEU!')
    elif jogm == 2:
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA')
elif jog == 1: # papel
    if jogm == 1:
        print('EMPATE')
    elif jogm == 2:
        print('VOCÊ PERDEU!')
    elif jogm == 0:
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA')
elif jog == 2: # tesouta
    if jogm == 2:
        print('EMPATE!')
    elif jogm == 0:
        print('VOCÊ PERDEU!')
    elif jogm == 1:
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
