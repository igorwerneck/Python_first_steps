def main():
    num = int(input('Digite um número inteiro qualquer: '))
    print('Para sair do programa, digite 0')
    while num != 0:
        if num % 2 == 0:
            print('Esse número é par.')
            main()
        else:
            print('Esse número é ímpar.')
            main()
    print('Obrigado por usar o programa!')
main()
