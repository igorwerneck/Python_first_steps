import math
import time

catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
time.sleep (3)
print('Pelo Teorema de Pitágoras, sabemos que o valor da hipotenusa ao quadrado é igual a soma do quadrado dos catetos.')
hipotenusa = math.sqrt((pow(catop, 2) + pow(catad, 2)))
time.sleep(4)
print('Logo, o valor da hipotenusa desse triângulo retângulo será de {:.2f}.'.format(hipotenusa))
