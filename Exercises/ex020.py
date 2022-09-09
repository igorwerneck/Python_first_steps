import random
import time

def main():

    print('{:^60}'.format('Jogo de Adivinhação'))
    print()
    print('Tente adivinhar o número que estou pensando...')
    time.sleep(2)
    print('Vamos ver... Vou pensar em um número de 0 a 5, ok?')
    time.sleep(2)
    num = random.randint(0,5)
    guess = int(input('E aí? Em qual número eu pensei?: '))
    if guess == num:
         print('Parabéns, você acertou! Como sabia, hein?')
    else:
        print('Não, você errou. Eu venci! Hahaha!')
    option = str(input('Você gostaria de tentar mais uma vez? Digite S/N: '))
    if option == 'N':
        print('Obrigado por jogar! Volte sempre!')
        quit()
    else:
        while option == 'S':
            main()



main()