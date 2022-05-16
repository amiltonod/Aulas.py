n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nf = (n1 + n2) / 2
if nf <= 4.9:
    print(f'Sua nota foi {nf}. Você foi \033[0;31;40mREPROVADO!')
elif 7 < nf >= 5.0:
    print(f'Sua nota foi {nf}. Você está de \033[0;33;40mRECUPERAÇÃO!')
elif nf >= 7.0:
    print(f'Sua nota foi {nf}. Você foi \033[0;36;40mAPROVADO!')
