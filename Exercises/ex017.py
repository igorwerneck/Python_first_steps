#Exercício 017: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite seu nome completo: ')
nome = nome.upper()
if ('SILVA' in nome) == True:
    print('Você possui a palavra "Silva" no seu nome. Legal!')
else:
    print('Você não possui a palavra "Silva" no seu nome.')