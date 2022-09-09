print('{:^60}'.format('LEITOR DE VELOCIDADE E CALCULADORA DE MULTA'))
print()
vel = float(input('Digite a velocidade do carro lida pelo radar, em Km/h: '))
if vel > 80:
    print('Sua velocidade está acima do limite permitido. Você foi multado!')
    multa = (vel - 80)*7
    print('O valor da sua multa será de R${:,}'.format(multa))
else:
    print('Sua velocidade está dentro do limite permitido.')
    print('Obrigado por respeitar a sinalização!')
    print('BOA VIAGEM!')
