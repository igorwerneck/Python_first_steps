"""Exercício 046: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores."""
Data = 2022
anoNasc = []
maiores = []
menores = []
c = 0
for i in range(0, 7):
    c += 1
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    while ano > Data:
        print('Insira um ano válido!')
        ano = int(input('Digite um valor válido: '))
    anoNasc.append(ano)
for a in anoNasc:
    if 2022 - a >= 18:
        maiores.append(a)
    else:
        menores.append(a)
x = len(maiores)
y = len(menores)
print('Temos {} pessoas menores de idade, nascidas nos anos {}.'.format(y, menores))
print('Temos {} pessoas maiores de idade, nascidas nos anos {}.'.format(x, maiores))

