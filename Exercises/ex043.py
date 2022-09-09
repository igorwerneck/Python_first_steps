"""Exercício 043: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão."""


def main():

    lista = []
    print('=.='*10)
    print('Software Progressão Aritmética')
    print()
    print('Opções:')
    print('1 - Imprimir uma PA com N termos em uma razão Z.')
    print('2 - Imprimir o termo X de uma PA com N termos em uma razão Z.')
    print('3 - Sair do programa.\n')
    opt1 = (input('Digite sua opção: '))
    if opt1 != '1' and opt1 != '2':
        while opt1 != '1' and opt1 != '2' and opt1 != '3':
            print('\033[31mOpção Inválida!\033[m')
            opt1 = (input('Digite uma opção válida (1, 2 ou 3): '))
    if opt1 == '1':
        termo = int(input('Digite o primeiro termo da PA: '))
        razao = int(input('Digite a razão: '))
        x = int(input('Digite o número desejado de termos: '))
        qtdterm = termo + (x - 1) * razao
        for i in range(termo, qtdterm+1, razao):
            print('{}'.format(i), end=' - ')
        print('Fim da PA')
        main()
    if opt1 == '2':
        termo = int(input('Digite o primeiro termo da PA: '))
        razao = int(input('Digite a razão: '))
        x = int(input('Digite o número desejado de termos: '))
        y = int(input('Qual termo você gostaria de visualizar? '))
        qtdterm = termo + (x - 1) * razao
        for i in range(termo, qtdterm+1, razao):
            lista.append(i)
        print('O termo na posição {} é {}.'.format(y, lista[y-1]))
        print('=.-='*10)
        main()
    if opt1 == '3':
        quit()


main()