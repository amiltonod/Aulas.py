import random
from time import sleep
random = (random.choice(range(0, 5))) # Esse comando faz o computador randomizar um número

print('-=-' * 20)
print('Vamos jogar! Em qual número estou pensando de 0 até 5')
print('-=-' * 20)
pct = int(input('E ai, qual número pensei?: ')) # O jogador tenta adivinhar aqui
print('PROCESSANDO...')
sleep(2)
if random == pct:
    print(f'Você venceu! Eu estava pensando no {random}, ué você agora é advinho(a)')
else:
    print(f'Você perdeu! Eu estava pensando no {random} zé ruela')
