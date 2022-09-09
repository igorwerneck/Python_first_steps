"""Exercício 038: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo
de 10 até 0, com uma pausa de 1 segundo entre eles."""
import time
print('=-' * 20)
print('Contagem Regressiva para o Ano Novo!')
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('FELIZ ANO NOVO!!!!!')
print('=-' * 20)
