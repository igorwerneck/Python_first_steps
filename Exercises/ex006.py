value = float(input('Digite o preço do produto: R$'))
finalprice = value-(5*value/100)
print('O produto receberá um desconto de 5%, resultando em um valor de R${}.'.format(finalprice))