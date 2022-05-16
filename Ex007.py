nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
nt3 = float(input('Digite a terceira nota: '))
media = (nt1 + nt2 + nt3) / 3
print(media)
if media >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')
