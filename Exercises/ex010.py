import math

angulo = float(input('Digite o valor do ângulo: '))
rad = math.radians(angulo)
sen_a = math.sin(rad)
cos_a = math.cos(rad)
tan_a = math.tan(rad)
print('O ângulo escolhido foi de {}º. Seu seno vale {:.4f}, o cosseno {:.4f} e a tangente {:.4f}.'.format(angulo, sen_a, cos_a, tan_a))