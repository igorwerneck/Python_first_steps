"""Exercício 041: Crie a tabuada do número que o usuário escolher, utilizando um laço for."""


num = int(input('Digite um número para estudar sua tabuada: '))
while num != 0:
    print('Tabuada do {}'.format(num))
    for termo1 in range(1, 11):
        print(termo1 * num)
    num = int(input('Digite outro número: '))
    print('Para sair, digite 0')