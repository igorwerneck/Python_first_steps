"""Exercício 026: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%."""

sal = float(input('Digite o valor do salário do funcionário: '))
if sal > 1250.00:
    novosal = sal * 1.10
    aumento = sal * 0.10
    print('O novo salário será de R${:.2f}. O aumento foi de R${:.2f} (10%).'.format(novosal, aumento))
else:
    novosal = sal * 1.15
    aumento = sal * 0.15
    print('O novo salário será de R${:.2f}. O aumento foi de R${:.2f} (15%).'.format(novosal, aumento))
