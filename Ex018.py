# from math import radians, sin, cos, tan (Método de simplificar o código com a biblioteca)
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
consseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o CONSSENO de {:.2f}'.format(angulo, consseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TâNGENTE de {:.2f}'.format(angulo, tangente))
