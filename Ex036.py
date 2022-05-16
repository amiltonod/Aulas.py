# variaveis para o questionário
casa = float(input('Qual o valor da casa?: R$ '))
salario = float(input('Qual é o seu salário?: R$ '))
pagamento = int(input('Em quantos mesês você quer pagar?: '))
# divisão entre o valor da casa e a quantidade de meses que será pago o empréstimo
pres = casa / pagamento
# atribuindo valor minimo de pagamento
minimo = 30 / 100 * salario
# atribuindo condições no aninhamento
if pres >= minimo:
    print(f'Valor parcelamento R${pres:.2f} por ter excedido o valor de 30% da sua renda o empréstimo foi NEGADO!')
else:
    print(f'As parcelas ficaram em R${pres:.2f} empréstimo APROVADO!')
print('Nubank agradece a preferência!')
