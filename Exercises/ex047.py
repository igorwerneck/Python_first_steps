"""Exercício 047: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso
lidos."""
c = 0
lista = []
for i in range(0, 5):
    c += 1
    peso = float(input('Digite o peso da pessoa {}, em KG: '.format(c)))
    lista.append(peso)
lista.sort()
print('O menor peso lido foi {}KG e o maior foi {}KG.'.format(lista[0], lista[-1]))