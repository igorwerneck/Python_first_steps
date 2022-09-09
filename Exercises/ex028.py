"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação
mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""

casa = float(input('Informe o valor do imóvel a ser adquirido: R$ '))
casa_format = 'R${:,.2f}'.format(casa)
print('O valor do imóvel é de: {}'.format(casa_format))
sal = float(input('Informe o salário do titular da compra: R$ '))
sal_format = 'R${:,.2f}'.format(sal)
print('O salário informado é de: {}'.format(sal_format))
meses = int(input('Em quantos meses deseja pagar o imóvel? '))
print()
prestacao = casa/meses
print('O valor da prestação será de R${:,.2f}.'.format(prestacao))
if prestacao > (sal * 0.3):
    print('O valor mensal excede o salário do titular em mais de 30%. \033[1;31mEMPRÉSTIMO NEGADO!')
else:
    print('O valor mensal está compatível com o salário do titular. \033[1;32mEMPRÉSTIMO VALIDADO!')
