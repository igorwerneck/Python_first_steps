"""Exercício 040: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500."""

comeco = int(input('Digite o começo: '))
fim = int(input('Digite o fim: '))
intervalo = []
print('O programa irá mostrar todos os números ímpares que são múltiplos de três no intervalo selecionado:')
for num in range(comeco, fim+1):
    if num % 2 != 0 and num % 3 == 0:
        intervalo.append(num)
print(intervalo)
