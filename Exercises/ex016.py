#Exercício 016: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO".

nome = input('Digite o nome da sua cidade: ')
nome = nome.upper()
nome2 = nome.split()
if nome2[0] == 'SANTO':
    print('A cidade começa com a palavra "Santo".')
else:
    print('A cidade não começa com a palavra "Santo".')
