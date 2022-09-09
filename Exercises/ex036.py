"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

cost = input('Digite o preço do produto: R$')
costnocomma = cost.replace(',', '.')
cost_format = float(costnocomma)
print()
print('Selecione agora a opção de pagamento:')
print('1 - À vista no dinheiro ou cheque: 10% de desconto')
print('2 - À vista no cartão: 5% de desconto')
print('3 - Em até 2x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20% de juros')
option = int(input('Digite o opção desejada: '))
if option < 1 or option > 4:
    print('\033[1;31mOpção inválida!')
elif option == 1:
    custo = cost_format - (cost_format * 0.10)
    print('Seu produto custou R${:.2f}'.format(cost_format))
    print('Nessa forma de pagamento, o valor total será de R${:.2f}'.format(custo))
elif option == 2:
    custo = cost_format - (cost_format * 0.05)
    print('Seu produto custou R${:.2f}'.format(cost_format))
    print('Nessa forma de pagamento, o valor total será de R${:.2f}'.format(custo))
elif option == 3:
    custo = cost_format/2
    print('Seu produto custou R${:.2f}'.format(cost_format))
    print('Nessa forma de pagamento, o valor total será de duas parcelas de R${:.2f}'.format(custo))
else:
    vezes = int(input('Selecione a quantidade de vezes no cartão: '))
    custo = (cost_format*1.20)/vezes
    print('Seu produto custou R${:.2f}'.format(cost_format))
    print('Você selecionou o pagamento em {} vezes.'.format(vezes))
    print('O valor de cada parcela será de R${:.2f}'.format(custo))


