"""Exercício 044: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input('Digite um número: '))
print('Para sair, digite 0')
while num != 0:
    lista = []
    for i in range(2, num):
        if num % i == 0:
            lista.append(i)
    n = len(lista)
    if n == 0:
        print('\033[32mO número {} é primo!\033[m'.format(num))
    else:
        print('\033[31mO número {} não é primo!\033[m'.format(num))
    print()
    num = int(input('Digite um número: '))
