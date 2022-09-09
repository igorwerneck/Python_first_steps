"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:
- Média abaixo de 5.0: reprovado
- Média entre 5.0 e 6.9: recuperação
- Média 7.0 ou superior: aprovado"""

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Média = {}'.format(media))
    print('\033[1;31mAluno reprovado!')
elif 5 <= media <= 6.9:
    print('Média = {}'.format(media))
    print('\033[1;33mAluno em recuperação!')
else:
    print('Média = {}'.format(media))
    print('\033[1;32mAluno aprovado!')

