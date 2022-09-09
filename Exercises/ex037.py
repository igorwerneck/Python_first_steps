import time
import random


def ursopo(x, y):
    if x == y:
        print('\033[1;33mEmpate!\033[m')
    elif x == 'PEDRA' and y == 'PAPEL':
        print('\033[1;31mO computador ganhou!\033[m')
    elif x == 'PEDRA' and y == 'TESOURA':
        print('\033[1;32mParabéns, você ganhou!\033[m')
    elif x == 'PAPEL' and y == 'TESOURA':
        print('\033[1;31mO computador ganhou!\033[m')
    elif x == 'PAPEL' and y == 'PEDRA':
        print('\033[1;32mParabéns, você ganhou!\033[m')
    elif x == 'TESOURA' and y == 'PEDRA':
        print('\033[1;31mO computador ganhou!\033[m')
    elif x == 'TESOURA' and y == 'PAPEL':
        print('\033[1;32mParabéns, você ganhou!\033[m')


def main():

    print('\t\t\t\t\033[1;32mURSOPÔ - PEDRA, PAPEL & TESOURA')
    print()
    print('SELECIONE UMA DAS OPÇÕES DO MENU')
    print('1 - Regras do jogo')
    print('2 - Jogar contra o Computador')
    print('3 - Modo Multiplayer (2 jogadores)')
    print('4 - Sair do jogo')
    print()
    option1 = int(input('A opção desejada foi: '))
    if option1 < 1 or option1 > 4:
        print('\033[1;31mOpção Inválida!')
        main()
    elif option1 == 4:
        quit()
    elif option1 == 1:
        print('No UrsoPô, os jogadores devem escolher uma opção em seus turnos: 1 - Pedra, 2 - Papel, 3 - Tesoura.\n'
              'Depois de escolher, os jogadores comparam suas opções e a vitória se dá conforme o seguinte esquema:\n\n'
              'Pedra ganha da Tesoura (amassando-a ou quebrando-a)\nTesoura ganha do Papel (cortando-o) \nPapel ganha'
              ' da Pedra (embrulhando-a)\n\nGanha o jogador que tiver mais vitórias.\n\n')
        print()
        time.sleep(5)
        back = int(input('Voltar ao menu principal? 1 - SIM, 2 - NÃO: '))
        while back < 1 or back > 2:
            print('\033[1;31mOpção Inválida!\033[m')
            back = int(input('\033[1;32mVoltar ao menu principal? 1 - SIM, 2 - NÃO: \033[m'))
        if back == 2:
            quit()
        elif back == 1:
            main()
    elif option1 == 2:
        turnos = int(input('Quantos turnos terá a partida? '))
        for i in range(turnos):
            print('\033[1;32mSelecione sua escolha: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura')
            choice = int(input('Turno do jogador: '))
            while choice > 3 or choice < 1:
                choice = int(input('\033[1;31mDigite uma opção válida (1 - Pedra, 2 - Papel, 3 - Tesoura):\033[m '))
            if choice == 1:
                player = 'PEDRA'
            elif choice == 2:
                player = 'PAPEL'
            elif choice == 3:
                player = 'TESOURA'
            time.sleep(2)
            print('UR...')
            time.sleep(2)
            print('SO...')
            time.sleep(2)
            pcchoice = random.randint(1, 3)
            if pcchoice == 1:
                pc = 'PEDRA'
            elif pcchoice == 2:
                pc = 'PAPEL'
            elif pcchoice == 3:
                pc = 'TESOURA'
            print('PO!!!')
            print()
            print('O jogador escolheu {}!'.format(player))
            print('O computador escolheu {}!'.format(pc))
            a = ursopo(player, pc)
            print()

    elif option1 == 3:
        print('Opção não implementada')
        main()


main()
