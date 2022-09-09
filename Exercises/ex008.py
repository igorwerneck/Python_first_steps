import math
import time

num = float(input('Digite um número qualquer. Em caso de número decimal, use o ponto: '))
time.sleep(2)
print('O número digitado foi {}. Sua parte inteira é {:.0f}'.format(num, num))