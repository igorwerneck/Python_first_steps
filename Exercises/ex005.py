altura = float(input('Digite a altura da parede, em metros: '))
largura = float(input('Digite a largura da parede, em metros: '))
area = altura*largura
tinta = area/2
print('A parede possui uma área de {} metros quadrados. Para pintá-la, você irá precisar de {} litros de tinta.'.format(area, tinta))
