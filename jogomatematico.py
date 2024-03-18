# Henrique Poledna e Eduardo Machado
import random

Inicio = input('Você quer jogar com quantos jogadores?[1/2]:')
Dificuldade = input('Qual a dificuladade do jogo?[Facíl, Médio ou Difícil]:').lower()

import random

if Inicio == '1':

    if Dificuldade == 'fácil'or Dificuldade == 'facil': #modo facil do jogo

        print('O jogo vai ser para apenas 1 pessoa')

        num1f = random.randint(-10, 10)
        num2f = random.randint(-10, 10)

        rf1 = input(f'{num1f} + {num2f}=')  #primeira pegunta do facil +
        rf1 = int(rf1)
        if rf1 == num1f + num2f:
            print('você acertou')
        else:
            print('você errou')

        num3f = random.randint(-10, 10)
        num4f = random.randint(-10, 10)

        rf2 = input(f'{num3f} - {num4f}=')  #segunda pergunda do facil -
        rf2 = int(rf2)
        if rf2 == num3f-num4f:
            print('você acertou')
        else:
            print('você errou')

        num5f = random.randint(-10, 10)
        num6f = random.randint(-10, 10)

        rf3 = input(f'{num5f} * {num6f}=')  #terceira pergunta do facil *
        rf3 = int(rf3)
        if rf3 == num5f * num6f:
            print('você acertou')
        else:
            print('você errou')

        num7f = random.randint(-10, 10)
        num8f = random.randint(-10, 10)

        rf4 = input(f'{num7f} // {num8f}=') #quarta pergunta do facil //
        rf4 = int(rf4)
        if rf4 == num7f // num8f:
            print('você acertou')
        else:
            print('você errou')

    elif Dificuldade == 'médio' or Dificuldade == 'medio':  #dificuldade medio

        print('O jogo vai ser para apenas 1 pessoa')

        num1m = random.randint(-100, 100)
        num2m = random.randint(-100, 100)

        rm1 = input(f'{num1m} + {num2m}=')    #primeira pergunta do medio +
        rm1 = int(rm1)
        if rm1 == num1m + num2m:
            print('você acertou')
        else:
            print('você errou')

        num3m = random.randint(-100, 100)
        num4m = random.randint(-100, 100)

        rm2 = input(f'{num3m} - {num4m}=')    #segunda pergunta do medio -
        rm2 = int(rm2)
        if rm2 == num3m - num4m:
            print('você acertou')
        else:
            print('você errou')

        num5m = random.randint(-100, 100)
        num6m = random.randint(-100, 100)

        rm3 = input(f'{num5m} * {num6m}=')    #terceir pergunta do medio *
        rm3 = int(rm3)
        if rm3 == num5m * num6m:
            print('você acertou')
        else:
            print('você errou')

        num7m = random.randint(-100, 100)
        num8m = random.randint(-100, 100)

        rm4 = input(f'{num7m} // {num8m}=')   #quarta pegunta do medio //
        rm4 = int(rm4)
        if rm4 == num7m // num8m:
            print('você acertou')
        else:
            print('você errou')


    elif Dificuldade == 'difícil' or Dificuldade == ('dificil'):    #dificuldade dificil

        print('O jogo vai ser para apenas 1 pessoa')

        num1d = random.randint(-1000, 1000)
        num2d = random.randint(-1000, 1000)

        rd1 = input(f'{num1d} + {num2d}=')    #primeira pergunta do dificil +
        rd1 = int(rd1)
        if rd1 == num1d + num2d:
            print('você acertou')
        else:
            print('você errou')

        num3d = random.randint(-1000, 1000)
        num4d = random.randint(-1000, 1000)

        rd2 = input(f'{num3d} - {num4d}=')    #segunda pergunta dificil -
        rd2 = int(rd2)
        if rd2 == num3d - num4d:
            print('você acertou')
        else:
            print('você errou')

        num5d = random.randint(-1000, 1000)
        num6d = random.randint(-1000, 1000)

        rd3 = input(f'{num5d} * {num6d}=')    #terceira pergunda do dificil *
        rd3 = int(rd3)
        if rd3 == num5d * num6d:
            print('você acertou')
        else:
            print('você errou')

        num7d = random.randint(-1000, 1000)
        num8d = random.randint(-1000, 1000)

        rd4 = input(f'{num7d} // {num8d}=')   #quarta pegunta do dificil //
        rd4 = int(rd4)
        if rd4 == num7d // num8d:
            print('você acertou')
        else:
            print('você errou')

elif Inicio == '2':
#jogador um
    if Dificuldade == 'fácil'or Dificuldade == 'facil': #modo facil do jogo dupla
        print('O jogo vai ser para 2 pessoas')
        print('Vez do jogador numero 1')
        num1fd1 = random.randint(-10, 10)
        num2fd1 = random.randint(-10, 10)

        rf1d1 = input(f'{num1fd1} + {num2fd1}=')  #primeira pegunta do facil dupla +
        rf1d1 = int(rf1d1)
        if rf1d1 == num1fd1 + num2fd1:
            print('você acertou')
        else:
            print('você errou')

        num3fd1 = random.randint(-10, 10)
        num4fd1 = random.randint(-10, 10)

        rf2d1 = input(f'{num3fd1} - {num4fd1}=')  #segunda pergunda do facil dupla-
        rf2d1 = int(rf2d1)
        if rf2d1 == num3fd1-num4fd1:
            print('você acertou')
        else:
            print('você errou')

        num5fd1 = random.randint(-10, 10)
        num6fd1 = random.randint(-10, 10)

        rf3d1 = input(f'{num5fd1} * {num6fd1}=')  #terceira pergunta do facil dupla *
        rf3d1 = int(rf3d1)
        if rf3d1 == num5fd1 * num6fd1:
            print('você acertou')
        else:
            print('você errou')

        num7fd1 = random.randint(-10, 10)
        num8fd1 = random.randint(-10, 10)

        rf4d1 = input(f'{num7fd1} // {num8fd1}=') #quarta pergunta do facil dupla //
        rf4d1 = int(rf4d1)
        if rf4d1 == num7fd1 // num8fd1:
            print('você acertou')
        else:
            print('você errou')

# jogador dois
        
        num1fd2 = random.randint(-10, 10)
        num2fd2 = random.randint(-10, 10)

        print('Vez do jogador numero 2')
        input('Digite qualquer tecla para continuar')
        rf1d2 = input(f'{num1fd2} + {num2fd2}=')  #primeira pegunta do facil dupla +
        rf1d2 = int(rf1d2)
        if rf1d2 == num1fd2 + num2fd2:
            print('você acertou')
        else:
            print('você errou')

        num3fd2 = random.randint(-10, 10)
        num4fd2 = random.randint(-10, 10)

        rf2d2 = input(f'{num3fd2} - {num4fd2}=')  #segunda pergunda do facil dupla-
        rf2d2 = int(rf2d2)
        if rf2d2 == num3fd2-num4fd2:
            print('você acertou')
        else:
            print('você errou')

        num5fd2 = random.randint(-10, 10)
        num6fd2 = random.randint(-10, 10)

        rf3d2 = input(f'{num5fd2} * {num6fd2}=')  #terceira pergunta do facil dupla *
        rf3d2 = int(rf3d2)
        if rf3d2 == num5fd2 * num6fd2:
            print('você acertou')
        else:
            print('você errou')

        num7fd2 = random.randint(-10, 10)
        num8fd2 = random.randint(-10, 10)

        rf4d2 = input(f'{num7fd2} // {num8fd2}=') #quarta pergunta do facil dupla //
        rf4d2 = int(rf4d2)
        if rf4d2 == num7fd2 // num8fd2:
            print('você acertou')
        else:
            print('você errou')

    else:
        print('o')



else:
    print('Reinicie o jogo')


