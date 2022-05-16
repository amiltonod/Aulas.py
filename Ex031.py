dis = float(input('Quantos Kms você viajou?: '))
# tudo que é identado para a esquerda sempre será executado.
if dis <= 200:
    val = dis * 0.50
else:
    val = dis * 0.45
print(f'O valor da sua viagem ficou R${val:.2f}')
