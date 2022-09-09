#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = int(input('Digite um número inteiro qualquer entre 0 e 9999: '))
print('O número digitado foi {}.'.format(numero))
if 0 <= numero <= 9:
    numero1 = str(numero)
    print('Unidade: {}'.format(numero1[0]))
elif 9 < numero <=99:
    numero1 = str(numero)
    print('Unidade: {}'.format(numero1[1]))
    print('Dezena: {}'.format(numero1[0]))
elif 100 <= numero <= 999:
    numero1 = str(numero)
    print('Unidade: {}'.format(numero1[2]))
    print('Dezena: {}'.format(numero1[1]))
    print('Centena: {}'.format(numero1[0]))
elif 1000 <= numero <= 9999:
    numero1 = str(numero)
    print('Unidade: {}'.format(numero1[3]))
    print('Dezena: {}'.format(numero1[2]))
    print('Centena: {}'.format(numero1[1]))
    print('Milhar: {}'.format(numero1[0]))