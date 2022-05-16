n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m >= 7:
    print(f'PARABÉNS sua média é {m:.1f} você foi aprovado!')
else:
    print(f'REPROVADO sua média foi {m:.1f}')
