# Henrique Poledna e EduaRdo Machado
import random

Inicio = input('Você quer jogar com quantos jogadores?[1/2]:')
Dificuldade = input('Qual a dificuladade do jogo?[Facíl, Médio ou Difícil]:').lower()

import random

if Inicio == '1':

    if Dificuldade == 'fácil'or Dificuldade == 'facil': #modo facil do jogo

        print('O jogo vai ser para apenas 1 pessoa')

        Num1f = random.randint(-10, 10)
        Num2f = random.randint(-10, 10)

        Rf1 = input(f'{Num1f} + {Num2f}=')  #primeira pegunta do facil +
        Rf1 = int(Rf1)
        if Rf1 == Num1f + Num2f:
            print('você acertou')
        else:
            print('você errou')

        Num3f = random.randint(-10, 10)
        Num4f = random.randint(-10, 10)

        Rf2 = input(f'{Num3f} - {Num4f}=')  #segunda pergunda do facil -
        Rf2 = int(Rf2)
        if Rf2 == Num3f-Num4f:
            print('você acertou')
        else:
            print('você errou')

        Num5f = random.randint(-10, 10)
        Num6f = random.randint(-10, 10)

        Rf3 = input(f'{Num5f} * {Num6f}=')  #terceira pergunta do facil *
        Rf3 = int(Rf3)
        if Rf3 == Num5f * Num6f:
            print('você acertou')
        else:
            print('você errou')

        Num7f = random.randint(-10, 10)
        Num8f = random.randint(-10, 10)

        Rf4 = input(f'{Num7f} // {Num8f}=') #quarta pergunta do facil //
        Rf4 = int(Rf4)
        if Rf4 == Num7f // Num8f:
            print('você acertou')
        else:
            print('você errou')

    elif Dificuldade == 'médio' or Dificuldade == 'medio':  #dificuldade medio

        print('O jogo vai ser para apenas 1 pessoa')

        Num1m = random.randint(-100, 100)
        Num2m = random.randint(-100, 100)

        Rm1 = input(f'{Num1m} + {Num2m}=')    #primeira pergunta do medio +
        Rm1 = int(Rm1)
        if Rm1 == Num1m + Num2m:
            print('você acertou')
        else:
            print('você errou')

        Num3m = random.randint(-100, 100)
        Num4m = random.randint(-100, 100)

        Rm2 = input(f'{Num3m} - {Num4m}=')    #segunda pergunta do medio -
        Rm2 = int(Rm2)
        if Rm2 == Num3m - Num4m:
            print('você acertou')
        else:
            print('você errou')

        Num5m = random.randint(-100, 100)
        Num6m = random.randint(-100, 100)

        Rm3 = input(f'{Num5m} * {Num6m}=')    #terceir pergunta do medio *
        Rm3 = int(Rm3)
        if Rm3 == Num5m * Num6m:
            print('você acertou')
        else:
            print('você errou')

        Num7m = random.randint(-100, 100)
        Num8m = random.randint(-100, 100)

        Rm4 = input(f'{Num7m} // {Num8m}=')   #quarta pegunta do medio //
        Rm4 = int(Rm4)
        if Rm4 == Num7m // Num8m:
            print('você acertou')
        else:
            print('você errou')


    elif Dificuldade == 'difícil' or Dificuldade == ('dificil'):    #dificuldade dificil

        print('O jogo vai ser para apenas 1 pessoa')

        Num1d = random.randint(-1000, 1000)
        Num2d = random.randint(-1000, 1000)

        Rd1 = input(f'{Num1d} + {Num2d}=')    #primeira pergunta do dificil +
        Rd1 = int(Rd1)
        if Rd1 == Num1d + Num2d:
            print('você acertou')
        else:
            print('você errou')

        Num3d = random.randint(-1000, 1000)
        Num4d = random.randint(-1000, 1000)

        Rd2 = input(f'{Num3d} - {Num4d}=')    #segunda pergunta dificil -
        Rd2 = int(Rd2)
        if Rd2 == Num3d - Num4d:
            print('você acertou')
        else:
            print('você errou')

        Num5d = random.randint(-1000, 1000)
        Num6d = random.randint(-1000, 1000)

        Rd3 = input(f'{Num5d} * {Num6d}=')    #terceira pergunda do dificil *
        Rd3 = int(Rd3)
        if Rd3 == Num5d * Num6d:
            print('você acertou')
        else:
            print('você errou')

        Num7d = random.randint(-1000, 1000)
        Num8d = random.randint(-1000, 1000)

        Rd4 = input(f'{Num7d} // {Num8d}=')   #quarta pegunta do dificil //
        Rd4 = int(Rd4)
        if Rd4 == Num7d // Num8d:
            print('você acertou')
        else:
            print('você errou')

elif Inicio == '2':
#jogador um
    if Dificuldade == 'fácil'or Dificuldade == 'facil': #modo facil do jogo dupla
        print('O jogo vai ser para 2 pessoas')
        print('Vez do jogador Numero 1')
        Num1fd1 = random.randint(-10, 10)
        Num2fd1 = random.randint(-10, 10)

        Rf1d1 = input(f'{Num1fd1} + {Num2fd1}=')  #primeira pegunta do facil dupla +
        Rf1d1 = int(Rf1d1)
        if Rf1d1 == Num1fd1 + Num2fd1:
            print('você acertou')
        else:
            print('você errou')

        Num3fd1 = random.randint(-10, 10)
        Num4fd1 = random.randint(-10, 10)

        Rf2d1 = input(f'{Num3fd1} - {Num4fd1}=')  #segunda pergunda do facil dupla-
        Rf2d1 = int(Rf2d1)
        if Rf2d1 == Num3fd1-Num4fd1:
            print('você acertou')
        else:
            print('você errou')

        Num5fd1 = random.randint(-10, 10)
        Num6fd1 = random.randint(-10, 10)

        Rf3d1 = input(f'{Num5fd1} * {Num6fd1}=')  #terceira pergunta do facil dupla *
        Rf3d1 = int(Rf3d1)
        if Rf3d1 == Num5fd1 * Num6fd1:
            print('você acertou')
        else:
            print('você errou')

        Num7fd1 = random.randint(-10, 10)
        Num8fd1 = random.randint(-10, 10)

        Rf4d1 = input(f'{Num7fd1} // {Num8fd1}=') #quarta pergunta do facil dupla //
        Rf4d1 = int(Rf4d1)
        if Rf4d1 == Num7fd1 // Num8fd1:
            print('você acertou')
        else:
            print('você errou')

# jogador dois
        
        Num1fd2 = random.randint(-10, 10)
        Num2fd2 = random.randint(-10, 10)

        print('Vez do jogador Numero 2')
        input('Digite qualquer tecla para continuar')
        Rf1d2 = input(f'{Num1fd2} + {Num2fd2}=')  #primeira pegunta do facil dupla +
        Rf1d2 = int(Rf1d2)
        if Rf1d2 == Num1fd2 + Num2fd2:
            print('você acertou')
        else:
            print('você errou')

        Num3fd2 = random.randint(-10, 10)
        Num4fd2 = random.randint(-10, 10)

        Rf2d2 = input(f'{Num3fd2} - {Num4fd2}=')  #segunda pergunda do facil dupla-
        Rf2d2 = int(Rf2d2)
        if Rf2d2 == Num3fd2-Num4fd2:
            print('você acertou')
        else:
            print('você errou')

        Num5fd2 = random.randint(-10, 10)
        Num6fd2 = random.randint(-10, 10)

        Rf3d2 = input(f'{Num5fd2} * {Num6fd2}=')  #terceira pergunta do facil dupla *
        Rf3d2 = int(Rf3d2)
        if Rf3d2 == Num5fd2 * Num6fd2:
            print('você acertou')
        else:
            print('você errou')

        Num7fd2 = random.randint(-10, 10)
        Num8fd2 = random.randint(-10, 10)

        Rf4d2 = input(f'{Num7fd2} // {Num8fd2}=') #quarta pergunta do facil dupla //
        Rf4d2 = int(Rf4d2)
        if Rf4d2 == Num7fd2 // Num8fd2:
            print('você acertou')
        else:
            print('você errou')

    else:
        print('o')



else:
    print('Reinicie o jogo')


