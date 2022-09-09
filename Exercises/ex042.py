"""Exercício 042: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o."""

lista = []
lista2 = []
termos = int(input('Digite a quantidade de termos: '))
for i in range(1, termos+1):
    num = int(input('Digite um valor inteiro: '))
    lista.append(num)
for c in lista:
    if c % 2 == 0:
        lista2.append(c)
m = sum(lista2)
print(m)