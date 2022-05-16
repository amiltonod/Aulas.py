# importando a data atual com o datetime
from datetime import date
# interface e entrada
print('   Alistamento Militar  ')
print('X=X' * 8)
# váriaveis para execução do programa
print('[ 1 ] Masculino ' '[ 2 ] Feminino')
sexo = int(input('Qual seu genêro: '))
mascuilno = 1
feminino = 2
nas = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nas
print(f'Sua idade é {idade} anos')
# condições para cada faixa de idade
if idade < 17 and sexo == 1:
    print('Não é necessário fazer o alistamento esse ano.')
    print(f'Faltam {17 - idade} anos para você se alistar fique atendo.')
elif idade == 17 and sexo == 1:
    print('Já está na hora de você se alistar.')
    print('Acesse o site da Junta Militar e se alliste nas FORÇAS ARMADAS.')
elif idade > 17 and sexo == 1:
    print(f'Você passou {idade - 17} anos do seu alistamento.')
    print('Acesse o site da Junta Militar para maiores informações.')
elif sexo == 2:
    print('No Brasil o serviço militar obrigatório se destina apenas para homens.')
    print('Acesse o site das forças armadas e procure formas de engresso.')
else:
    print('COMANDO INVÁLIDO TENTE NOVAMENTE.')
print('\033[1;37;40m BRASIL ACIMA DE TUDO!')
