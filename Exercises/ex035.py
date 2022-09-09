"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""

peso = input('Digite seu peso, em KG: ')
peso_format = peso.replace(',', '.')
peso1 = float(peso_format)
altura = input('Digite sua altura, em M: ')
altura_format = altura.replace(',', '.')
altura1 = float(altura_format)
imc = peso1/(altura1**2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[1;33mVocê está abaixo do peso. Atenção!')
elif 18.5 <= imc < 25:
    print('\033[1;32mVocê está no peso ideal. Parabéns!!!')
elif 25 <= imc < 30:
    print('\033[1;33mVocê está com sobrepeso. Atenção!')
elif 30 <= imc <= 40:
    print('\033[1;31mVocê está com obsesidade. Muita atenção!')
else:
    print('\033[1;31mVOCÊ ESTÁ COM OBESIDADE MÓRBIDA. PROCURE AJUDA MÉDICA.')


