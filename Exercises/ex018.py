#Exercício 018: Faça um programa que leia uma frase pelo teclado e mostre:
#a) Quantas vezes aparece a letra 'a'
#b) Em que posição ela aparece a primeira vez.
#c) Em que posição ela aparece a última vez.


frase = input('Digite uma frase qualquer pelo teclado: ')
print('A frase digitada foi: {}'.format(frase))
frase = frase.lower()
print('Nessa frase, a letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A letra "e" aparece {} vezes.'.format(frase.count('e')))
print('A letra "i", por sua vez, aparece {} vezes.'.format(frase.count('i')))
print('A letra "o" aparece {} vezes.'.format(frase.count('o')))
print('Já a letra "u" aparece {} vezes na sua frase.\n\n'.format(frase.count('u')))
print('A letra "a" aparece, pela primeira vez, na posiçõe {} do texto e, pela última vez, na posição {}'.format(frase.find('a'), frase.rfind('a')))

