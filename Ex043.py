# buscando as info
peso = float(input('Digite o seu peso: (Kg) '))
alt = float(input('Digite sua altura: (m) '))
# calculo imc
imc = peso / (alt ** 2)
# dando as condições
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f} você está abaixo do peso!')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC é {imc:.1f} esse é seu peso ideal!')
elif 25 <= imc <= 30:
    print(f'Seu IMC é {imc:.1f} você está com sobrepeso!')
elif 30 <= imc <= 40:
    print(f'Seu IMC é {imc:.1f} você está obeso!')
elif imc > 40:
    print(f'Seu IMC é {imc:.1f} você está com obesidade mórbida!')
else:
    print('Digite seu peso e altura para o cáculo do IMC.')
