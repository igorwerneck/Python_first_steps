"""Exercício 039: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."""

pares = []
comeco = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
print('O programa irá mostrar todos os números pares do início ao fim:')
for num in range(comeco, fim+1):
    if num % 2 == 0:
        pares.append(num)
print(pares)
