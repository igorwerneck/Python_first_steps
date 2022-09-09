"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior, - o segundo valor é maior, - não existe valor maior, os dois são iguais."""

a = int(input('Digite o valor de X: '))
b = int(input('Digite o valor de Y: '))
if a == b:
    print('{} é igual a {}'.format(a, b))
elif a > b:
    print('{} é maior que {}'.format(a, b))
else:
    print('{} é maior que {}.'.format(b, a))
