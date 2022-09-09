def main():

    ano = int(input('Digite um ano: '))
    print('Para sair do programa, digite 0.')
    while ano != 0:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            print('O ano de {} é bissexto.'.format(ano))
            main()
        else:
            print('O ano de {} não é bissexto.'.format(ano))
            main()
    quit()


main()
