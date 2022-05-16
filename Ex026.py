# import unidecode para tirar os acentos
import unidecode
f = str(input('Digite uma frase: ')).upper().strip()
new_f = unidecode.unidecode(f)
print('A letra A aparece {} vezes na frase'.format(new_f.count('A')))
# +1 para pular uma casa na lista e contar a partir do 1
print('A primeira letra A apareceu na posição {}'.format(new_f.find('A') + 1))
# rfind para procurar primeiro o último.
print('Á ultima letra A apareceu na posição {}'.format(new_f.rfind('A') + 1))
