lar = float(input('Qual a largura da parede?: '))
alt = float(input('Qual a altura da parede?: '))
area = lar * alt
print('Sua parede tem uma dimensão de {}x{} e sua área é de {}m².'.format(lar, alt, area))
tinta = area / 2
print('Para pintar essa área você precisara de {}l de tinta'.format(tinta))