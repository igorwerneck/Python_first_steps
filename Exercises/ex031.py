"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

Data = 2022
ano = int(input('Informe seu ano de nascimento: '))
idade = Data - ano
idade_para = 18 - idade
idade_apos = idade - 18
if idade < 18:
    print('Você tem {} anos'.format(idade))
    print('\033[1;32mVocê ainda vai se alistar no Serviço Militar.')
    print('\033[mFalta(m) {} ano(s) para o seu alistamento.'.format(idade_para))
elif idade == 18:
    print('Você já completou {} anos.'.format(idade))
    print('\033[1;33mProcure a Junta Militar mais próxima da sua residência. Seu alistamento deve ser feito nesse ano!')
else:
    print('Você tem {} anos'.format(idade))
    print('\033[1;31mVocê deveria ter se alistado há {} anos, em {}.'.format(idade_apos, Data-idade_apos))
    print('\033[1;31mProcure a Junta Militar mais próxima do seu endereço para regularizar sua situação.')
