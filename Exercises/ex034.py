print('\t\tCONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO')
print()
print('Sabe-se que um triângulo só existe se suas retas obedecerem ao seguinte paradigma:')
print()
print('\t\t\t\tb - c < a < b + c')
print('\t\t\t\ta - c < b < a + c')
print('\t\t\t\ta - b < c < a + b')
print()
a = float(input('Digite o valor da reta 1: '))
b = float(input('Digite o valor da reta 2: '))
c = float(input('Digite o valor da reta 3: '))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('É possível formar um triângulo com as retas {}, {} e {}.'.format(a, b, c))
    if a == b == c:
        print('Esse triângulo será EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('Esse triângulo será ISÓSCELES')
    else:
        print('Esse triângulo será ESCALENO')
else:
    print('Não é possível formar um triângulo com as retas {}, {} e {}.'.format(a, b, c))