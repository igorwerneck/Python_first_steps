"""Exercício 023: Desenvolva um programa que pergunte a distância de uma viagem de Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas."""

distancia = float(input('Digite a distância da viagem em Km/h: '))
if distancia <= 200:
    custo = distancia * 0.50
    print('O custo da passagem será de R${:,}.'.format(custo))
else:
    custo = distancia * 0.45
    print('O custo da passagem será de R${:,}.'.format(custo))
print('Obrigado por usar o programa!')
