vel = float(input('Digite a velocidade do carro: '))
mul = 7
if vel > 80:
    val = (vel - 80) * 7
    print(f'Você excedeu o limite de velocidade de 80km/h e recebeu uma multa no valor de R${val}')
print('Boa viagem! Dirija com segurança!')
