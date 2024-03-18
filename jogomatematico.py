# Henrique Poledna e EduaRdo Machado
import random

Inicio = input('Você quer jogar com quantos jogadores?[1/2]:')
Dificuldade = input('Qual a dificuladade do jogo?[Facíl, Médio ou Difícil]:').lower()

import random

if Inicio == '1':

    # modo facil do jogo
    if Dificuldade == 'fácil'or Dificuldade == 'facil':

        print('O jogo vai ser para apenas 1 pessoa')

        Num1f = random.randint(-10, 10)
        Num2f = random.randint(-10, 10)

        # primeira pegunta do facil +
        Rf1 = input(f'{Num1f} + {Num2f}=')
        Rf1 = int(Rf1)
        if Rf1 == Num1f + Num2f:
            print('você acertou')
        else:
            print('você errou')

        Num3f = random.randint(-10, 10)
        Num4f = random.randint(-10, 10)

        # segunda pergunda do facil -
        Rf2 = input(f'{Num3f} - {Num4f}=')
        Rf2 = int(Rf2)
        if Rf2 == Num3f-Num4f:
            print('você acertou')
        else:
            print('você errou')

        Num5f = random.randint(-10, 10)
        Num6f = random.randint(-10, 10)

        # terceira pergunta do facil *
        Rf3 = input(f'{Num5f} * {Num6f}=')
        Rf3 = int(Rf3)
        if Rf3 == Num5f * Num6f:
            print('você acertou')
        else:
            print('você errou')

        Num7f = random.randint(-10, 10)
        Num8f = random.randint(-10, 10)

        # quarta pergunta do facil //
        Rf4 = input(f'{Num7f} // {Num8f}=')
        Rf4 = int(Rf4)
        if Rf4 == Num7f // Num8f:
            print('você acertou')
        else:
            print('você errou')

    # dificuldade medio
    elif Dificuldade == 'médio' or Dificuldade == 'medio':

        print('O jogo vai ser para apenas 1 pessoa')

        Num1m = random.randint(-100, 100)
        Num2m = random.randint(-100, 100)

        # primeira pergunta do medio +
        Rm1 = input(f'{Num1m} + {Num2m}=')
        Rm1 = int(Rm1)
        if Rm1 == Num1m + Num2m:
            print('você acertou')
        else:
            print('você errou')

        Num3m = random.randint(-100, 100)
        Num4m = random.randint(-100, 100)

        # segunda pergunta do medio -
        Rm2 = input(f'{Num3m} - {Num4m}=')
        Rm2 = int(Rm2)
        if Rm2 == Num3m - Num4m:
            print('você acertou')
        else:
            print('você errou')

        Num5m = random.randint(-100, 100)
        Num6m = random.randint(-100, 100)

        # terceira pergunta do medio *
        Rm3 = input(f'{Num5m} * {Num6m}=')
        Rm3 = int(Rm3)
        if Rm3 == Num5m * Num6m:
            print('você acertou')
        else:
            print('você errou')

        Num7m = random.randint(-100, 100)
        Num8m = random.randint(-100, 100)

        # quarta pegunta do medio //
        Rm4 = input(f'{Num7m} // {Num8m}=')
        Rm4 = int(Rm4)
        if Rm4 == Num7m // Num8m:
            print('você acertou')
        else:
            print('você errou')

    # dificuldade dificil
    elif Dificuldade == 'difícil' or Dificuldade == ('dificil'):

        print('O jogo vai ser para apenas 1 pessoa')

        Num1d = random.randint(-1000, 1000)
        Num2d = random.randint(-1000, 1000)

        # primeira pergunta do dificil +
        Rd1 = input(f'{Num1d} + {Num2d}=')
        Rd1 = int(Rd1)
        if Rd1 == Num1d + Num2d:
            print('você acertou')
        else:
            print('você errou')

        Num3d = random.randint(-1000, 1000)
        Num4d = random.randint(-1000, 1000)

        # segunda pergunta dificil -
        Rd2 = input(f'{Num3d} - {Num4d}=')
        Rd2 = int(Rd2)
        if Rd2 == Num3d - Num4d:
            print('você acertou')
        else:
            print('você errou')

        Num5d = random.randint(-1000, 1000)
        Num6d = random.randint(-1000, 1000)

        # terceira pergunta do dificil *
        Rd3 = input(f'{Num5d} * {Num6d}=')
        Rd3 = int(Rd3)
        if Rd3 == Num5d * Num6d:
            print('você acertou')
        else:
            print('você errou')

        Num7d = random.randint(-1000, 1000)
        Num8d = random.randint(-1000, 1000)

        # quarta pegunta do dificil //
        Rd4 = input(f'{Num7d} // {Num8d}=')
        Rd4 = int(Rd4)
        if Rd4 == Num7d // Num8d:
            print('você acertou')
        else:
            print('você errou')

elif Inicio == '2':
# jogador um
    # modo facil do jogo dupla
    if Dificuldade == 'fácil'or Dificuldade == 'facil':
        print('O jogo vai ser para 2 pessoas')
        print('Vez do jogador Numero 1')
        Num1fd1 = random.randint(-10, 10)
        Num2fd1 = random.randint(-10, 10)

        # primeira pegunta do facil dupla +
        Rf1d1 = input(f'{Num1fd1} + {Num2fd1}=')
        Rf1d1 = int(Rf1d1)
        if Rf1d1 == Num1fd1 + Num2fd1:
            print('você acertou')
        else:
            print('você errou')

        Num3fd1 = random.randint(-10, 10)
        Num4fd1 = random.randint(-10, 10)

        # segunda pergunda do facil dupla -
        Rf2d1 = input(f'{Num3fd1} - {Num4fd1}=')
        Rf2d1 = int(Rf2d1)
        if Rf2d1 == Num3fd1-Num4fd1:
            print('você acertou')
        else:
            print('você errou')

        Num5fd1 = random.randint(-10, 10)
        Num6fd1 = random.randint(-10, 10)

        # terceira pergunta do facil dupla *
        Rf3d1 = input(f'{Num5fd1} * {Num6fd1}=')
        Rf3d1 = int(Rf3d1)
        if Rf3d1 == Num5fd1 * Num6fd1:
            print('você acertou')
        else:
            print('você errou')

        Num7fd1 = random.randint(-10, 10)
        Num8fd1 = random.randint(-10, 10)

        # quarta pergunta do facil dupla //
        Rf4d1 = input(f'{Num7fd1} // {Num8fd1}=')
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
        
        # primeira pegunta do facil dupla +
        Rf1d2 = input(f'{Num1fd2} + {Num2fd2}=')
        Rf1d2 = int(Rf1d2)
        if Rf1d2 == Num1fd2 + Num2fd2:
            print('você acertou')
        else:
            print('você errou')

        Num3fd2 = random.randint(-10, 10)
        Num4fd2 = random.randint(-10, 10)

        # segunda pergunda do facil dupla -
        Rf2d2 = input(f'{Num3fd2} - {Num4fd2}=')
        Rf2d2 = int(Rf2d2)
        if Rf2d2 == Num3fd2-Num4fd2:
            print('você acertou')
        else:
            print('você errou')

        Num5fd2 = random.randint(-10, 10)
        Num6fd2 = random.randint(-10, 10)

        # terceira pergunta do facil dupla *
        Rf3d2 = input(f'{Num5fd2} * {Num6fd2}=')
        Rf3d2 = int(Rf3d2)
        if Rf3d2 == Num5fd2 * Num6fd2:
            print('você acertou')
        else:
            print('você errou')

        Num7fd2 = random.randint(-10, 10)
        Num8fd2 = random.randint(-10, 10)

        # quarta pergunta do facil dupla //
        Rf4d2 = input(f'{Num7fd2} // {Num8fd2}=')
        Rf4d2 = int(Rf4d2)
        if Rf4d2 == Num7fd2 // Num8fd2:
            print('você acertou')
        else:
            print('você errou')
# jogador um
    # modo medio do jogo dupla
    elif Dificuldade == 'médio'or Dificuldade == 'medio':
        print('O jogo vai ser para 2 pessoas')
        print('Vez do jogador Numero 1')
        Num1md1 = random.randint(-100, 100)
        Num2md1 = random.randint(-100, 100)

        # primeira pegunta do médio dupla +
        Rm1d1 = input(f'{Num1md1} + {Num2md1}=')
        Rm1d1 = int(Rm1d1)
        if Rm1d1 == Num1md1 + Num2md1:
            print('você acertou')
        else:
            print('você errou')

        Num3md1 = random.randint(-100, 100)
        Num4md1 = random.randint(-100, 100)

        # segunda pergunda do medio dupla -
        Rm2d1 = input(f'{Num3md1} - {Num4md1}=')
        Rm2d1 = int(Rm2d1)
        if Rm2d1 == Num3md1-Num4md1:
            print('você acertou')
        else:
            print('você errou')

        Num5md1 = random.randint(-100, 100)
        Num6md1 = random.randint(-100, 100)

        # terceira pergunta do medio dupla *
        Rm3d1 = input(f'{Num5md1} * {Num6md1}=')
        Rm3d1 = int(Rm3d1)
        if Rm3d1 == Num5md1 * Num6md1:
            print('você acertou')
        else:
            print('você errou')

        Num7md1 = random.randint(-100, 100)
        Num8md1 = random.randint(-100, 100)

        # quarta pergunta do medio dupla //
        Rm4d1 = input(f'{Num7md1} // {Num8md1}=')
        Rm4d1 = int(Rm4d1)
        if Rm4d1 == Num7md1 // Num8md1:
            print('você acertou')
        else:
            print('você errou')

# jogador dois
        
        Num1md2 = random.randint(-100, 100)
        Num2md2 = random.randint(-100, 100)

        print('Vez do jogador Numero 2')
        input('Aperte ENTER para continuar')
        
        # primeira pegunta do medio dupla +
        Rm1d2 = input(f'{Num1md2} + {Num2md2}=')
        Rm1d2 = int(Rm1d2)
        if Rm1d2 == Num1md2 + Num2md2:
            print('você acertou')
        else:
            print('você errou')

        Num3md2 = random.randint(-100, 100)
        Num4md2 = random.randint(-100, 100)

        # segunda pergunda do facil dupla -
        Rm2d2 = input(f'{Num3md2} - {Num4md2}=')
        Rm2d2 = int(Rm2d2)
        if Rm2d2 == Num3md2-Num4md2:
            print('você acertou')
        else:
            print('você errou')

        Num5md2 = random.randint(-100, 100)
        Num6md2 = random.randint(-100, 100)
        # terceira pergunta do facil dupla *
        Rm3d2 = input(f'{Num5md2} * {Num6md2}=')
        Rm3d2 = int(Rm3d2)
        if Rm3d2 == Num5md2 * Num6md2:
            print('você acertou')
        else:
            print('você errou')

        Num7md2 = random.randint(-100, 100)
        Num8md2 = random.randint(-100, 100)

        # quarta pergunta do medio dupla //
        Rm4d2 = input(f'{Num7md2} // {Num8md2}=')
        Rm4d2 = int(Rm4d2)
        if Rm4d2 == Num7md2 // Num8md2:
            print('você acertou')
        else:
            print('você errou')
# jogador um
    # modo dificil do jogo dupla
    if Dificuldade == 'difícil'or Dificuldade == 'dificil':
        print('O jogo vai ser para 2 pessoas')
        print('Vez do jogador Numero 1')
        Num1Dd1 = random.randint(-1000, 1000)
        Num2Dd1 = random.randint(-1000, 1000)

        # primeira pegunta do dificil dupla +
        RD1d1 = input(f'{Num1Dd1} + {Num2Dd1}=')
        RD1d1 = int(RD1d1)
        if RD1d1 == Num1Dd1 + Num2Dd1:
            print('você acertou')
        else:
            print('você errou')

        Num3Dd1 = random.randint(-1000, 1000)
        Num4Dd1 = random.randint(-1000, 1000)

        # segunda pergunda do dificil dupla -
        RD2d1 = input(f'{Num3Dd1} - {Num4Dd1}=')
        RD2d1 = int(RD2d1)
        if RD2d1 == Num3Dd1 - Num4Dd1:
            print('você acertou')
        else:
            print('você errou')

        Num5Dd1 = random.randint(-1000, 1000)
        Num6Dd1 = random.randint(-1000, 1000)

        # terceira pergunta do dificil dupla *
        RD3d1 = input(f'{Num5Dd1} * {Num6Dd1}=')
        RD3d1 = int(RD3d1)
        if RD3d1 == Num5Dd1 * Num6Dd1:
            print('você acertou')
        else:
            print('você errou')

        Num7Dd1 = random.randint(-1000, 1000)
        Num8Dd1 = random.randint(-1000, 1000)

        # quarta pergunta do facil dupla //
        RD4d1 = input(f'{Num7Dd1} // {Num8Dd1}=')
        RD4d1 = int(RD4d1)
        if RD4d1 == Num7Dd1 // Num8Dd1:
            print('você acertou')
        else:
            print('você errou')

# jogador dois
        
        Num1Dd2 = random.randint(-1000, 1000)
        Num2Dd2 = random.randint(-1000, 1000)

        print('Vez do jogador Numero 2')
        input('Aperte ENTER para continuar')
        
        # primeira pegunta do dificil dupla +
        RD1d2 = input(f'{Num1Dd2} + {Num2Dd2}=')
        RD1d2 = int(RD1d2)
        if RD1d2 == Num1Dd2 + Num2Dd2:
            print('você acertou')
        else:
            print('você errou')

        Num3Dd2 = random.randint(-1000, 1000)
        Num4Dd2 = random.randint(-1000, 1000)

        # segunda pergunda do dificil dupla -
        RD2d2 = input(f'{Num3Dd2} - {Num4Dd2}=')
        RD2d2 = int(RD2d2)
        if RD2d2 == Num3Dd2-Num4Dd2:
            print('você acertou')
        else:
            print('você errou')

        Num5Dd2 = random.randint(-1000, 1000)
        Num6Dd2 = random.randint(-1000, 1000)

        # terceira pergunta do facil dupla *
        RD3d2 = input(f'{Num5Dd2} * {Num6Dd2}=')
        RD3d2 = int(RD3d2)
        if RD3d2 == Num5Dd2 * Num6Dd2:
            print('você acertou')
        else:
            print('você errou')

        Num7Dd2 = random.randint(-1000, 1000)
        Num8Dd2 = random.randint(-1000, 1000)

        # quarta pergunta do dificil dupla //
        RD4d2 = input(f'{Num7Dd2} // {Num8Dd2}=')
        RD4d2 = int(RD4d2)
        if RD4d2 == Num7Dd2 // Num8Dd2:
            print('você acertou')
        else:
            print('você errou')


else:
    print('Reinicie o jogo')