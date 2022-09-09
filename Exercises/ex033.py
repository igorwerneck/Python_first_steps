"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: mirim
- Até 14 anos: infantil
- Até 19 anos: junior
- Até 20 anos: sênior
- Acima: master"""

Data = 2022
ano = int(input('Digite seu ano de nascimento: '))
idade = Data - ano
print()
print('Você tem {} anos e...'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19:
    print('Sua categoria é JUNIOR.')
elif idade <= 20:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
