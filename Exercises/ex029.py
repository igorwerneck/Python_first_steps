"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão: 1 - binário, 2 - octal, 3 - hexadecimal."""

num = int(input('Digite um número inteiro qualquer: '))
print('Selecione uma das rotinas a seguir:')
print('1 - Converter o número para binário.')
print('2 - Converter o número para octal.')
print('3 - Converter o número para hexadecimal.')
print('4 - Sair do programa.')
option = int(input('Digite a opção desejada: '))
if option > 4 or option < 1:
    print('\033[1;31mOpção inválida!')
elif option == 1:
    num_bin = bin(num)
    print('O número {} em binário é: {}'.format(num, num_bin))
elif option == 2:
    num_oct = oct(num)
    print('O número {} em octal é: {}'.format(num, num_oct))
elif option == 3:
    num_hex = hex(num)
    print('O número {} em hexadecimal é: {}'.format(num, num_hex))
elif option == 4:
    quit()


