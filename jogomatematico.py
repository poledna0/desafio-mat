# Henrique Poledna , Eduardo Machado de Oliveira , Arthur Ascione de Carvalho , Arthur Gabriel Goes e Pedro Lucas Gomes Vitorino
import random

Inicio = input('Você quer jogar com quantos jogadores?[1/2]:')
Dificuldade = input('Qual a dificuladade do jogo?[Facíl, Médio ou Difícil]:').lower()

import random
import time

if Inicio == '1':

    # modo facil do jogo
    if Dificuldade == 'fácil'or Dificuldade == 'facil':

        print('O jogo vai ser para apenas 1 pessoa')

        # declarnado os numeros aleatorios
        Num1f = random.randint(-10, 10)
        Num2f = random.randint(-10, 10)

        # inicio da contagem de tempo
        InicioTempoEX11 = time.time()

        # primeira pegunta do facil +
        Rf1 = input(f'{Num1f} + {Num2f}=')
        Rf1 = int(Rf1)

        # fim do tempo
        FimDoTempoEX11 = time.time()
        FimDoTempoEX11 = int(FimDoTempoEX11)
        InicioTempoEX11 = int(InicioTempoEX11)
        ResultadoDoTempoEX11 = (FimDoTempoEX11 - InicioTempoEX11)

        # resposta
        if Rf1 == Num1f + Num2f:
            print('você acertou')
            if ResultadoDoTempoEX11 < 5: 
                NotaFinalEX11 = 10

            elif ResultadoDoTempoEX11 < 30:
                NotaFinalEX11 = 10 - (ResultadoDoTempoEX11 * 0.2)

        else:
            print('você errou')
            NotaFinalEX11 = 0

        # declarando os numeros aleatorios
        Num3f = random.randint(-10, 10)
        Num4f = random.randint(-10, 10)

        # inicio do tempo
        InicioTempoEX12 = time.time()

        # segunda pergunda do facil -
        Rf2 = input(f'{Num3f} - {Num4f}=')
        Rf2 = int(Rf2)

        # fim do tempo
        FimDoTempoEX12 = time.time()
        FimDoTempoEX12 = int(FimDoTempoEX12)
        InicioTempoEX12 = int(InicioTempoEX12)
        ResultadoDoTempoEX12 = (FimDoTempoEX12 - InicioTempoEX12)

        # respostas
        if Rf2 == Num3f-Num4f:

            print('você acertou')

            if ResultadoDoTempoEX12 < 5: 
                NotaFinalEX12 = 10

            elif ResultadoDoTempoEX12 < 30:
                NotaFinalEX12 = 10 - (ResultadoDoTempoEX12 * 0.2)

        else:
            print('você errou')
            NotaFinalEX12 = 0
 

        # declarando numero aleatorio
        Num5f = random.randint(-10, 10)
        Num6f = random.randint(-10, 10)

        # inicio do tempo
        InicioTempoEX13 = time.time()

        # terceira pergunta do facil *
        Rf3 = input(f'{Num5f} * {Num6f}=')
        Rf3 = int(Rf3)

        # fim do tempo
        FimDoTempoEX13 = time.time()
        FimDoTempoEX13 = int(FimDoTempoEX13)
        InicioTempoEX13 = int(InicioTempoEX13)
        ResultadoDoTempoEX13 = (FimDoTempoEX13 - InicioTempoEX13)

        # respostas
        if Rf3 == Num5f * Num6f:
            print('você acertou')
            
            if ResultadoDoTempoEX13 < 5: 
                NotaFinalEX13 = 10

            elif ResultadoDoTempoEX12 < 30:
                NotaFinalEX13 = 10 - (ResultadoDoTempoEX13 * 0.2)

        else:
            print('você errou')
            NotaFinalEX13 = 0

        # declarando numero aleatorio 
        Num7f = random.randint(-10, 10)
        Num8f = random.randint(-10, 10)

        # inicio do temp
        InicioTempoEX14 = time.time()

        # quarta pergunta do facil //
        Rf4 = input(f'{Num7f} // {Num8f}=')
        Rf4 = int(Rf4)

        # fim do tempo
        FimDoTempoEX14 = time.time()
        FimDoTempoEX14 = int(FimDoTempoEX14)
        InicioTempoEX14 = int(InicioTempoEX14)
        ResultadoDoTempoEX14 = (FimDoTempoEX14 - InicioTempoEX14)

        # respostas
        if Rf4 == Num7f // Num8f:
            print('você acertou')

            if ResultadoDoTempoEX14 < 5: 
                NotaFinalEX14 = 10

            elif ResultadoDoTempoEX14 < 30:
                NotaFinalEX14 = 10 - (ResultadoDoTempoEX14 * 0.2)
            

        else:
            print('você errou')
            NotaFinalEX14 = 0

        # mostara nota
        print(f" você fez um total de {NotaFinalEX11 + NotaFinalEX12 + NotaFinalEX13 + NotaFinalEX14} pontos ")
    
    # dificuldade medio
    elif Dificuldade == 'médio' or Dificuldade == 'medio':
        print('O jogo vai ser para apenas 1 pessoa')

        # declarnado numeros aleatorios
        Num1m = random.randint(-100, 100)
        Num2m = random.randint(-100, 100)

        # inicio do tempo
        InicioTempoEX11m = time.time()

        # primeira pergunta do medio +
        Rm1 = input(f'{Num1m} + {Num2m}=')
        Rm1 = int(Rm1)

        # fim do tempo
        FimDoTempoEX11m = time.time()
        FimDoTempoEX11m = int(FimDoTempoEX11m)
        InicioTempoEX11m = int(InicioTempoEX11m)
        ResultadoDoTempoEX11m = (FimDoTempoEX11m - InicioTempoEX11m)

        # respostas
        if Rm1 == Num1m + Num2m:
            print('você acertou')

            if ResultadoDoTempoEX11m < 5: 
                NotaFinalEX11m = 10

            elif ResultadoDoTempoEX11m < 30:
                NotaFinalEX11m = 10 - (ResultadoDoTempoEX11m * 0.2)

        else:
            print('você errou')
            NotaFinalEX11m = 0

        # declarando numero aleatorio
        Num3m = random.randint(-100, 100)
        Num4m = random.randint(-100, 100)

        # inicio do tempo 
        InicioTempoEX12m = time.time()

        # segunda pergunta do medio -
        Rm2 = input(f'{Num3m} - {Num4m}=')
        Rm2 = int(Rm2)

        # fim do tempo 
        FimDoTempoEX12m = time.time()
        FimDoTempoEX12m = int(FimDoTempoEX12m)
        InicioTempoEX12m = int(InicioTempoEX12m)
        ResultadoDoTempoEX12m = (FimDoTempoEX12m - InicioTempoEX12m)

        # respostas
        if Rm2 == Num3m - Num4m:
            print('você acertou')

            if ResultadoDoTempoEX12m < 5: 
                NotaFinalEX12m = 10

            elif ResultadoDoTempoEX12m < 30:
                NotaFinalEX12m = 10 - (ResultadoDoTempoEX12m * 0.2)

        else:
            print('você errou')
            NotaFinalEX12m = 0

        # declarnado numero aleatorio
        Num5m = random.randint(-100, 100)
        Num6m = random.randint(-100, 100)

        # inicio do tempo
        InicioTempoEX13m = time.time()

        # terceira pergunta do medio *
        Rm3 = input(f'{Num5m} * {Num6m}=')
        Rm3 = int(Rm3)

        # fim do tempo
        FimDoTempoEX13m = time.time()
        FimDoTempoEX13m = int(FimDoTempoEX13m)
        InicioTempoEX13m = int(InicioTempoEX13m)
        ResultadoDoTempoEX13m = (FimDoTempoEX13m - InicioTempoEX13m)

        # respostas
        if Rm3 == Num5m * Num6m:
            print('você acertou')

            if ResultadoDoTempoEX13m < 5: 
                NotaFinalEX13m = 10

            elif ResultadoDoTempoEX13m < 30:
                NotaFinalEX13m = 10 - (ResultadoDoTempoEX13m * 0.2)

        else:
            print('você errou')
            NotaFinalEX13m = 0

        # declarnado numero aleatorio
        Num7m = random.randint(-100, 100)
        Num8m = random.randint(-100, 100)

        # inicio do tempo
        InicioTempoEX14m = time.time()

        # quarta pegunta do medio //
        Rm4 = input(f'{Num7m} // {Num8m}=')
        Rm4 = int(Rm4)

        # fim do tempo
        FimDoTempoEX14m = time.time()
        FimDoTempoEX14m = int(FimDoTempoEX14m)
        InicioTempoEX14m = int(InicioTempoEX14m)
        ResultadoDoTempoEX14m = (FimDoTempoEX14m - InicioTempoEX14m)

        # respostas
        if Rm4 == Num7m // Num8m:
            print('você acertou')

            if ResultadoDoTempoEX14m < 5: 
                NotaFinalEX13m = 10

            elif ResultadoDoTempoEX14m < 30:
                NotaFinalEX14m = 10 - (ResultadoDoTempoEX14m * 0.2)

        else:
            print('você errou')
            NotaFinalEX14m = 0
            
        # mostrar nota
        print(f" você fez um total de {NotaFinalEX11m + NotaFinalEX12m + NotaFinalEX13m + NotaFinalEX14m} ")

    # dificuldade dificil
    elif Dificuldade == 'difícil' or Dificuldade == ('dificil'):

        print('O jogo vai ser para apenas 1 pessoa')

        # declarando numero aleatorio 
        Num1d = random.randint(-1000, 1000)
        Num2d = random.randint(-1000, 1000)

        # inicio do tempo
        InicioTempoEX11d = time.time()

        # primeira pergunta do dificil +
        Rd1 = input(f'{Num1d} + {Num2d}=')
        Rd1 = int(Rd1)

        # fim do tempo  
        FimDoTempoEX11d = time.time()
        FimDoTempoEX11d = int(FimDoTempoEX11d)
        InicioTempoEX11d = int(InicioTempoEX11d)
        ResultadoDoTempoEX11d = (FimDoTempoEX11d - InicioTempoEX11d)

        # respostas
        if Rd1 == Num1d + Num2d:
            print('você acertou')

            if ResultadoDoTempoEX11d < 5: 
                NotaFinalEX11d = 10

            elif ResultadoDoTempoEX11d < 30:
                NotaFinalEX11d = 10 - (ResultadoDoTempoEX11d * 0.2)

        else:
            print('você errou')
            NotaFinalEX11d = 0

        # declarando numero aleatorio
        Num3d = random.randint(-1000, 1000)
        Num4d = random.randint(-1000, 1000)

        # inicio do tempo
        InicioTempoEX12d = time.time()

        # segunda pergunta dificil -
        Rd2 = input(f'{Num3d} - {Num4d}=')
        Rd2 = int(Rd2)

        # fim do tempo
        FimDoTempoEX12d = time.time()
        FimDoTempoEX12d = int(FimDoTempoEX12d)
        InicioTempoEX12d = int(InicioTempoEX12d)
        ResultadoDoTempoEX12d = (FimDoTempoEX12d - InicioTempoEX12d)

        # respostas 
        if Rd2 == Num3d - Num4d:
            print('você acertou')

            if ResultadoDoTempoEX12d < 5: 
                NotaFinalEX12d = 10

            elif ResultadoDoTempoEX12d < 30:
                NotaFinalEX12d = 10 - (ResultadoDoTempoEX12d * 0.2)

        else:
            print('você errou')
            NotaFinalEX12d = 0

        # declarando numero aleatorio
        Num5d = random.randint(-1000, 1000)
        Num6d = random.randint(-1000, 1000)

        # inicio do tempo
        InicioTempoEX13d = time.time()

        # terceira pergunta do dificil *
        Rd3 = input(f'{Num5d} * {Num6d}=')
        Rd3 = int(Rd3)

        # fim do tempo 
        FimDoTempoEX13d = time.time()
        FimDoTempoEX13d = int(FimDoTempoEX13d)
        InicioTempoEX13d = int(InicioTempoEX13d)
        ResultadoDoTempoEX13d = (FimDoTempoEX13d - InicioTempoEX13d)

        # respostas 
        if Rd3 == Num5d * Num6d:
            print('você acertou')

            if ResultadoDoTempoEX13d < 5: 
                NotaFinalEX13d = 10

            elif ResultadoDoTempoEX13d < 30:
                NotaFinalEX13d = 10 - (ResultadoDoTempoEX13d * 0.2)

        else:
            print('você errou')
            NotaFinalEX13d = 0

        # declarando numero aleatorio 
        Num7d = random.randint(-1000, 1000)
        Num8d = random.randint(-1000, 1000)

        # inicio tempo
        InicioTempoEX14d = time.time()

        # quarta pegunta do dificil //
        Rd4 = input(f'{Num7d} // {Num8d}=')
        Rd4 = int(Rd4)

        # fim do tempo
        FimDoTempoEX14d = time.time()
        FimDoTempoEX14d = int(FimDoTempoEX14d)
        InicioTempoEX14d = int(InicioTempoEX14d)
        ResultadoDoTempoEX14d = (FimDoTempoEX14d - InicioTempoEX14d)

        #respostas 
        if Rd4 == Num7d // Num8d:
            print('você acertou')

            if ResultadoDoTempoEX14d < 5: 
                NotaFinalEX14d = 10

            elif ResultadoDoTempoEX14d < 30:
                NotaFinalEX14d = 10 - (ResultadoDoTempoEX14d * 0.2)

        else:
            print('você errou')
            NotaFinalEX14d = 0

        # mostar nota
        print(f" você fez um total de {NotaFinalEX11d + NotaFinalEX12d + NotaFinalEX13d + NotaFinalEX14d} ")

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


