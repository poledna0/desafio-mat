# Henrique Poledna , Eduardo Machado de Oliveira , Arthur Ascione de Carvalho , Arthur Gabriel Goes e Pedro Lucas Gomes Vitorino


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
        print(f" você fez um total de {NotaFinalEX11m + NotaFinalEX12m + NotaFinalEX13m + NotaFinalEX14m} pontos ")

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
        print(f" você fez um total de {NotaFinalEX11d + NotaFinalEX12d + NotaFinalEX13d + NotaFinalEX14d} pontos ")

elif Inicio == '2':
# jogador um
    # modo facil do jogo dupla
    if Dificuldade == 'fácil'or Dificuldade == 'facil':
        print('O jogo vai ser para 2 pessoas')
        print('Vez do jogador Numero 1')

        # declarando numeros aleatorios
        Num1fd1 = random.randint(-10, 10)
        Num2fd1 = random.randint(-10, 10)

        # inicio do tempo 
        InicioTempoEX21 = time.time()

        # primeira pegunta do facil dupla +
        Rf1d1 = input(f'{Num1fd1} + {Num2fd1}=')
        Rf1d1 = int(Rf1d1)

        # fim do tempo
        FimDoTempoEX21 = time.time()
        FimDoTempoEX21 = int(FimDoTempoEX21)
        InicioTempoEX21 = int(InicioTempoEX21)
        ResultadoDoTempoEX21 = (FimDoTempoEX21 - InicioTempoEX21)

        # respostas
        if Rf1d1 == Num1fd1 + Num2fd1:
            print('você acertou')

            if ResultadoDoTempoEX21 < 5: 
                NotaFinalEX21 = 10

            elif ResultadoDoTempoEX21 < 30:
                NotaFinalEX21 = 10 - (ResultadoDoTempoEX21 * 0.2)

        else:
            print('você errou')
            NotaFinalEX21 = 0

        # decalarando numero aleatorio
        Num3fd1 = random.randint(-10, 10)
        Num4fd1 = random.randint(-10, 10) 

        # inicio do tempo
        InicioTempoEX22 = time.time()

        # segunda pergunda do facil dupla -
        Rf2d1 = input(f'{Num3fd1} - {Num4fd1}=')
        Rf2d1 = int(Rf2d1)

        # fim do tempo
        FimDoTempoEX22 = time.time()
        FimDoTempoEX22 = int(FimDoTempoEX22)
        InicioTempoEX22 = int(InicioTempoEX22)
        ResultadoDoTempoEX22 = (FimDoTempoEX22 - InicioTempoEX22)

        # respostas
        if Rf2d1 == Num3fd1-Num4fd1:
            print('você acertou')

            if ResultadoDoTempoEX22 < 5: 
                NotaFinalEX22 = 10

            elif ResultadoDoTempoEX22 < 30:
                NotaFinalEX22 = 10 - (ResultadoDoTempoEX22 * 0.2)

        else:
            print('você errou')
            NotaFinalEX22 = 0
            
        # declarando numero aleatorio
        Num5fd1 = random.randint(-10, 10)
        Num6fd1 = random.randint(-10, 10)

        # inicio do tempo
        InicioTempoEX23 = time.time()

        # terceira pergunta do facil dupla *
        Rf3d1 = input(f'{Num5fd1} * {Num6fd1}=')
        Rf3d1 = int(Rf3d1)

        # fim do tempo
        FimDoTempoEX23 = time.time()
        FimDoTempoEX23 = int(FimDoTempoEX23)
        InicioTempoEX23 = int(InicioTempoEX23)
        ResultadoDoTempoEX23 = (FimDoTempoEX23 - InicioTempoEX23)

        # respostas 
        if Rf3d1 == Num5fd1 * Num6fd1:
            print('você acertou')

            if ResultadoDoTempoEX23 < 5: 
                NotaFinalEX23 = 10

            elif ResultadoDoTempoEX23 < 30:
                NotaFinalEX23 = 10 - (ResultadoDoTempoEX23 * 0.2)

        else:
            print('você errou')
            NotaFinalEX23 = 0

        # declarando numero aleatorio
        Num7fd1 = random.randint(-10, 10)
        Num8fd1 = random.randint(-10, 10)

        # inicio do tempo
        InicioTempoEX24 = time.time()

        # quarta pergunta do facil dupla //
        Rf4d1 = input(f'{Num7fd1} // {Num8fd1}=')
        Rf4d1 = int(Rf4d1)

        # fim do tempo 
        FimDoTempoEX24 = time.time()
        FimDoTempoEX24 = int(FimDoTempoEX24)
        InicioTempoEX24 = int(InicioTempoEX24)
        ResultadoDoTempoEX24 = (FimDoTempoEX24 - InicioTempoEX24)


        # respostas 
        if Rf4d1 == Num7fd1 // Num8fd1:
            print('você acertou')

            if ResultadoDoTempoEX24 < 5: 
                NotaFinalEX24 = 10

            elif ResultadoDoTempoEX24 < 30:
                NotaFinalEX24 = 10 - (ResultadoDoTempoEX24 * 0.2)

        else:
            print('você errou')
            NotaFinalEX24 = 0

# jogador dois
            
        # delcarando numero aleatorio         
        Num1fd2 = random.randint(-10, 10)
        Num2fd2 = random.randint(-10, 10)

        print('Vez do jogador Numero 2')
        input('Digite qualquer tecla para continuar')

        # inicio tempo
        InicioTempoEX31 = time.time()

        # primeira pegunta do facil dupla +
        Rf1d2 = input(f'{Num1fd2} + {Num2fd2}=')
        Rf1d2 = int(Rf1d2)

        # fim do tempo 
        FimDoTempoEX31 = time.time()
        FimDoTempoEX31 = int(FimDoTempoEX31)
        InicioTempoEX31 = int(InicioTempoEX31)
        ResultadoDoTempoEX31 = (FimDoTempoEX31 - InicioTempoEX31)

        # resposatas 
        if Rf1d2 == Num1fd2 + Num2fd2:
            print('você acertou')

            if ResultadoDoTempoEX31 < 5: 
                NotaFinalEX31 = 10

            elif ResultadoDoTempoEX31 < 30:
                NotaFinalEX31 = 10 - (ResultadoDoTempoEX31 * 0.2)

        else:
            print('você errou')
            NotaFinalEX31 = 0

        # declarando numero aleatorio 
        Num3fd2 = random.randint(-10, 10)
        Num4fd2 = random.randint(-10, 10)

        # inicio tempo 
        InicioTempoEX32 = time.time()

        # segunda pergunda do facil dupla -
        Rf2d2 = input(f'{Num3fd2} - {Num4fd2}=')
        Rf2d2 = int(Rf2d2)

        # fim do tempo 
        FimDoTempoEX32 = time.time()
        FimDoTempoEX32 = int(FimDoTempoEX32)
        InicioTempoEX32 = int(InicioTempoEX32)
        ResultadoDoTempoEX32 = (FimDoTempoEX32 - InicioTempoEX32)

        # respostas
        if Rf2d2 == Num3fd2-Num4fd2:
            print('você acertou')

            if ResultadoDoTempoEX32 < 5: 
                NotaFinalEX32 = 10

            elif ResultadoDoTempoEX32 < 30:
                NotaFinalEX32 = 10 - (ResultadoDoTempoEX32 * 0.2)

        else:
            print('você errou')
            NotaFinalEX32 = 0

        # declarando numero aleatorio
        Num5fd2 = random.randint(-10, 10)
        Num6fd2 = random.randint(-10, 10)

        # inicio do tempo
        InicioTempoEX33 = time.time()

        # terceira pergunta do facil dupla *
        Rf3d2 = input(f'{Num5fd2} * {Num6fd2}=')
        Rf3d2 = int(Rf3d2)

        # fim do tempo
        FimDoTempoEX33 = time.time()
        FimDoTempoEX33 = int(FimDoTempoEX33)
        InicioTempoEX33 = int(InicioTempoEX33)
        ResultadoDoTempoEX33 = (FimDoTempoEX33 - InicioTempoEX33)

        # respostas
        if Rf3d2 == Num5fd2 * Num6fd2:
            print('você acertou')

            if ResultadoDoTempoEX33 < 5: 
                NotaFinalEX33 = 10

            elif ResultadoDoTempoEX33 < 30:
                NotaFinalEX33 = 10 - (ResultadoDoTempoEX33 * 0.2)

        else:
            print('você errou')
            NotaFinalEX33 = 0

        # declarando numero aleatorio
        Num7fd2 = random.randint(-10, 10)
        Num8fd2 = random.randint(-10, 10)

        # inicio do tempo
        InicioTempoEX34 = time.time()

        # quarta pergunta do facil dupla //
        Rf4d2 = input(f'{Num7fd2} // {Num8fd2}=')
        Rf4d2 = int(Rf4d2)

        # fim do tempo
        FimDoTempoEX34 = time.time()
        FimDoTempoEX34 = int(FimDoTempoEX34)
        InicioTempoEX34 = int(InicioTempoEX34)
        ResultadoDoTempoEX34 = (FimDoTempoEX34 - InicioTempoEX34)

        # respostas 
        if Rf4d2 == Num7fd2 // Num8fd2:
            print('você acertou')

            if ResultadoDoTempoEX34 < 5: 
                NotaFinalEX34 = 10

            elif ResultadoDoTempoEX34 < 30:
                NotaFinalEX34 = 10 - (ResultadoDoTempoEX34 * 0.2)

        else:
            print('você errou')
            NotaFinalEX34 = 0
        # mostar nota
        print(f" jogador 1 fez {NotaFinalEX21 + NotaFinalEX22 + NotaFinalEX23 + NotaFinalEX24} pontos ")
        
        print(f" jogador 2  fez {NotaFinalEX31 + NotaFinalEX32 + NotaFinalEX33 + NotaFinalEX34} pontos ")

# jogador um
    # modo medio do jogo dupla
    elif Dificuldade == 'médio'or Dificuldade == 'medio':
        print('O jogo vai ser para 2 pessoas')
        print('Vez do jogador Numero 1')

        # declarando numeros aletorios 
        Num1md1 = random.randint(-100, 100)
        Num2md1 = random.randint(-100, 100)

        # inicio do tempo
        InicioTempoEX21m = time.time()

        # primeira pegunta do médio dupla +
        Rm1d1 = input(f'{Num1md1} + {Num2md1}=')
        Rm1d1 = int(Rm1d1)

        # fim do tempo
        FimDoTempoEX21m = time.time()
        FimDoTempoEX21m = int(FimDoTempoEX21m)
        InicioTempoEX21m = int(InicioTempoEX21m)
        ResultadoDoTempoEX21m = (FimDoTempoEX21m - InicioTempoEX21m)

        # respostas
        if Rm1d1 == Num1md1 + Num2md1:
            print('você acertou')

            if ResultadoDoTempoEX21m < 5: 
                NotaFinalEX21m = 10

            elif ResultadoDoTempoEX21m < 30:
                NotaFinalEX21m = 10 - (ResultadoDoTempoEX21m * 0.2)

        else:
            print('você errou')
            NotaFinalEX21m = 0

        # declarando numero aleatorio
        Num3md1 = random.randint(-100, 100)
        Num4md1 = random.randint(-100, 100)

        # inicio do tempo
        InicioTempoEX22m = time.time()

        # segunda pergunda do medio dupla -
        Rm2d1 = input(f'{Num3md1} - {Num4md1}=')
        Rm2d1 = int(Rm2d1)

        # fim do tempo
        FimDoTempoEX22m = time.time()
        FimDoTempoEX22m = int(FimDoTempoEX22m)
        InicioTempoEX22m = int(InicioTempoEX22m)
        ResultadoDoTempoEX22m = (FimDoTempoEX22m - InicioTempoEX22m)

        if Rm2d1 == Num3md1-Num4md1:
            print('você acertou')

            if ResultadoDoTempoEX22m < 5: 
                NotaFinalEX22m = 10

            elif ResultadoDoTempoEX22m < 30:
                NotaFinalEX22m = 10 - (ResultadoDoTempoEX22m * 0.2)

        else:
            print('você errou')
            NotaFinalEX22m = 0

        # declarando numero aleatorio
        Num5md1 = random.randint(-100, 100)
        Num6md1 = random.randint(-100, 100)

        # inicio do tempo
        InicioTempoEX23m = time.time()

        # terceira pergunta do medio dupla *
        Rm3d1 = input(f'{Num5md1} * {Num6md1}=')
        Rm3d1 = int(Rm3d1)

        # fim do tempo
        FimDoTempoEX23m = time.time()
        FimDoTempoEX23m = int(FimDoTempoEX23m)
        InicioTempoEX23m = int(InicioTempoEX23m)
        ResultadoDoTempoEX23m = (FimDoTempoEX23m - InicioTempoEX23m)

        # respostas 
        if Rm3d1 == Num5md1 * Num6md1:
            print('você acertou')

            if ResultadoDoTempoEX23m < 5: 
                NotaFinalEX23m = 10

            elif ResultadoDoTempoEX23m < 30:
                NotaFinalEX23m = 10 - (ResultadoDoTempoEX23m * 0.2)

        else:
            print('você errou')
            NotaFinalEX23m = 0

        # declarando numero aleatorio
        Num7md1 = random.randint(-100, 100)
        Num8md1 = random.randint(-100, 100)
        Num7md1 = int(Num7md1)
        Num8md1 = int(Num8md1)

        # inicio tempo
        InicioTempoEX24m = time.time()

        # quarta pergunta do medio dupla //
        Rm4d1 = input(f'{Num7md1} / {Num8md1}=')
        Rm4d1 = int(Rm4d1)

        # fim tempo 
        FimDoTempoEX24m = time.time()
        FimDoTempoEX24m = int(FimDoTempoEX24m)
        InicioTempoEX24m = int(InicioTempoEX24m)
        ResultadoDoTempoEX24m = (FimDoTempoEX24m - InicioTempoEX24m)

        # respostas
        if Rm4d1 == Num7md1 // Num8md1:
            print('você acertou')

            if ResultadoDoTempoEX24m < 5: 
                NotaFinalEX24m = 10

            elif ResultadoDoTempoEX24m < 30:
                NotaFinalEX24m = 10 - (ResultadoDoTempoEX24m * 0.2)

        else:
            print('você errou')
            NotaFinalEX24m = 0 

# jogador dois
        
        # decalrando numero aleatorio
        Num1md2 = random.randint(-100, 100)
        Num2md2 = random.randint(-100, 100)

        print('Vez do jogador Numero 2')
        input('Aperte ENTER para continuar')

        # inicio do tempo
        InicioTempoEX31m = time.time()
        
        # primeira pegunta do medio dupla +
        Rm1d2 = input(f'{Num1md2} + {Num2md2}=')
        Rm1d2 = int(Rm1d2)

        # fim do tempo
        FimDoTempoEX31m = time.time()
        FimDoTempoEX31m = int(FimDoTempoEX31m)
        InicioTempoEX31m = int(InicioTempoEX31m)
        ResultadoDoTempoEX31m = (FimDoTempoEX31m - InicioTempoEX31m)

        # respostas 
        if Rm1d2 == Num1md2 + Num2md2:
            print('você acertou')

            if ResultadoDoTempoEX31m < 5: 
                NotaFinalEX31m = 10

            elif ResultadoDoTempoEX31m < 30:
                NotaFinalEX31m = 10 - (ResultadoDoTempoEX31m * 0.2)

        else:
            print('você errou')
            NotaFinalEX31m = 0

        # declarando numero aleatorio
        Num3md2 = random.randint(-100, 100)
        Num4md2 = random.randint(-100, 100)

        # inicio tempo
        InicioTempoEX32m = time.time()

        # segunda pergunda do facil dupla -
        Rm2d2 = input(f'{Num3md2} - {Num4md2}=')
        Rm2d2 = int(Rm2d2)

        # fim tempo
        FimDoTempoEX32m = time.time()
        FimDoTempoEX32m = int(FimDoTempoEX32m)
        InicioTempoEX32m = int(InicioTempoEX32m)
        ResultadoDoTempoEX32m = (FimDoTempoEX32m - InicioTempoEX32m)

        # respostas
        if Rm2d2 == Num3md2-Num4md2:
            print('você acertou')

            if ResultadoDoTempoEX32m < 5: 
                NotaFinalEX32m = 10

            elif ResultadoDoTempoEX32m < 30:
                NotaFinalEX32m = 10 - (ResultadoDoTempoEX32m * 0.2)

        else:
            print('você errou')
            NotaFinalEX32m = 0

        # declarando numero aleatorio
        Num5md2 = random.randint(-100, 100)
        Num6md2 = random.randint(-100, 100)

        # inicio tempo
        InicioTempoEX33m = time.time()

        # terceira pergunta do facil dupla *
        Rm3d2 = input(f'{Num5md2} * {Num6md2}=')
        Rm3d2 = int(Rm3d2)

        # fim tempo 
        FimDoTempoEX33m = time.time()
        FimDoTempoEX33m = int(FimDoTempoEX33m)
        InicioTempoEX33m = int(InicioTempoEX33m)
        ResultadoDoTempoEX33m = (FimDoTempoEX33m - InicioTempoEX33m)

        # respostas 
        if Rm3d2 == Num5md2 * Num6md2:
            print('você acertou')

            if ResultadoDoTempoEX33m < 5: 
                NotaFinalEX33m = 10

            elif ResultadoDoTempoEX33m < 30:
                NotaFinalEX33m = 10 - (ResultadoDoTempoEX33m * 0.2)

        else:
            print('você errou')
            NotaFinalEX33m = 0

        # declarando numero aletorio
        Num7md2 = random.randint(-100, 100)
        Num8md2 = random.randint(-100, 100)

        # inicio tempo
        InicioTempoEX34m = time.time()

        # quarta pergunta do medio dupla //
        Rm4d2 = input(f'{Num7md2} // {Num8md2}=')
        Rm4d2 = int(Rm4d2)

        # fim do tempo
        FimDoTempoEX34m = time.time()
        FimDoTempoEX34m = int(FimDoTempoEX34m)
        InicioTempoEX34m = int(InicioTempoEX34m)
        ResultadoDoTempoEX34m = (FimDoTempoEX34m - InicioTempoEX34m)

        # respostas 
        if Rm4d2 == Num7md2 // Num8md2:
            print('você acertou')

            if ResultadoDoTempoEX34m < 5: 
                NotaFinalEX34m = 10

            elif ResultadoDoTempoEX34m < 30:
                NotaFinalEX34m = 10 - (ResultadoDoTempoEX34m * 0.2)

        else:
            print('você errou')
            NotaFinalEX34m = 0

        # mostar nota
        print(f" jogador 1 fez {NotaFinalEX21m + NotaFinalEX22m + NotaFinalEX23m + NotaFinalEX24m} pontos ")
        
        print(f" jogador 2  fez {NotaFinalEX31m + NotaFinalEX32m + NotaFinalEX33m + NotaFinalEX34m} pontos ")

# jogador um
    # modo dificil do jogo dupla
    if Dificuldade == 'difícil'or Dificuldade == 'dificil':

        print('O jogo vai ser para 2 pessoas')
        print('Vez do jogador Numero 1')

        # declarando numero aleatorio 
        Num1Dd1 = random.randint(-1000, 1000)
        Num2Dd1 = random.randint(-1000, 1000)

        # inicio tempo
        InicioTempoEX21d = time.time()

        # primeira pegunta do dificil dupla +
        RD1d1 = input(f'{Num1Dd1} + {Num2Dd1}=')
        RD1d1 = int(RD1d1)

        # fim tempo
        FimDoTempoEX21d = time.time()
        FimDoTempoEX21d = int(FimDoTempoEX21d)
        InicioTempoEX21d = int(InicioTempoEX21d)
        ResultadoDoTempoEX21d = (FimDoTempoEX21d - InicioTempoEX21d)

        # respostas
        if RD1d1 == Num1Dd1 + Num2Dd1:
            print('você acertou')

            if ResultadoDoTempoEX21d < 5: 
                NotaFinalEX21d = 10

            elif ResultadoDoTempoEX21d < 30:
                NotaFinalEX21d = 10 - (ResultadoDoTempoEX21d * 0.2)

        else:
            print('você errou')
            NotaFinalEX21d = 0

        # declarando numero aleatorio
        Num3Dd1 = random.randint(-1000, 1000)
        Num4Dd1 = random.randint(-1000, 1000)

        # inicio do tempo 
        InicioTempoEX22d = time.time()

        # segunda pergunda do dificil dupla -
        RD2d1 = input(f'{Num3Dd1} - {Num4Dd1}=')
        RD2d1 = int(RD2d1)

        # fim do tempo
        FimDoTempoEX22d = time.time()
        FimDoTempoEX22d = int(FimDoTempoEX22d)
        InicioTempoEX22d = int(InicioTempoEX22d)
        ResultadoDoTempoEX22d = (FimDoTempoEX22d - InicioTempoEX22d)


        # respostas
        if RD2d1 == Num3Dd1 - Num4Dd1:
            print('você acertou')

            if ResultadoDoTempoEX22d < 5: 
                NotaFinalEX22d = 10

            elif ResultadoDoTempoEX22d < 30:
                NotaFinalEX22d = 10 - (ResultadoDoTempoEX22d * 0.2)

        else:
            print('você errou')
            NotaFinalEX22d = 0

        # declarando numero aleatorio
        Num5Dd1 = random.randint(-1000, 1000)
        Num6Dd1 = random.randint(-1000, 1000)

        # inicio tempo
        InicioTempoEX23d = time.time()

        # terceira pergunta do dificil dupla *
        RD3d1 = input(f'{Num5Dd1} * {Num6Dd1}=')
        RD3d1 = int(RD3d1)

        # fim tempo
        FimDoTempoEX23d = time.time()
        FimDoTempoEX23d = int(FimDoTempoEX23d)
        InicioTempoEX23d = int(InicioTempoEX23d)
        ResultadoDoTempoEX23d = (FimDoTempoEX23d - InicioTempoEX23d)

        # repostas
        if RD3d1 == Num5Dd1 * Num6Dd1:
            print('você acertou')

            if ResultadoDoTempoEX23d < 5: 
                NotaFinalEX23d = 10

            elif ResultadoDoTempoEX23d < 30:
                NotaFinalEX23d = 10 - (ResultadoDoTempoEX23d * 0.2)

        else:
            print('você errou')
            NotaFinalEX23d = 0

        # declarando numero aleatorio
        Num7Dd1 = random.randint(-1000, 1000)
        Num8Dd1 = random.randint(-1000, 1000)

        # inicio tempo
        InicioTempoEX24d = time.time()


        # quarta pergunta do facil dupla //
        RD4d1 = input(f'{Num7Dd1} / {Num8Dd1}=')
        RD4d1 = int(RD4d1)

        # fim tempo
        FimDoTempoEX24d = time.time()
        FimDoTempoEX24d = int(FimDoTempoEX24d)
        InicioTempoEX24d = int(InicioTempoEX24d)
        ResultadoDoTempoEX24d = (FimDoTempoEX24d - InicioTempoEX24d)

        # respostas
        if RD4d1 == Num7Dd1 // Num8Dd1:
            print('você acertou')

            if ResultadoDoTempoEX24d < 5: 
                NotaFinalEX24d = 10

            elif ResultadoDoTempoEX24d < 30:
                NotaFinalEX24d = 10 - (ResultadoDoTempoEX24d * 0.2)

        else:
            print('você errou')
            NotaFinalEX24d = 0

# jogador dois
        
        # declarando numero aleatorio
        Num1Dd2 = random.randint(-1000, 1000)
        Num2Dd2 = random.randint(-1000, 1000)

        print('Vez do jogador Numero 2')
        input('Aperte ENTER para continuar')

        # inicio tempo
        InicioTempoEX31d = time.time()

        # primeira pegunta do dificil dupla +
        RD1d2 = input(f'{Num1Dd2} + {Num2Dd2}=')
        RD1d2 = int(RD1d2)

        # fim tempo
        FimDoTempoEX31d = time.time()
        FimDoTempoEX31d = int(FimDoTempoEX31d)
        InicioTempoEX31d = int(InicioTempoEX31d)
        ResultadoDoTempoEX31d = (FimDoTempoEX31d - InicioTempoEX31d)

        # respostas
        if RD1d2 == Num1Dd2 + Num2Dd2:
            print('você acertou')

            if ResultadoDoTempoEX31d < 5: 
                NotaFinalEX31d = 10

            elif ResultadoDoTempoEX31d < 30:
                NotaFinalEX31d = 10 - (ResultadoDoTempoEX31d * 0.2)

        else:
            print('você errou')
            NotaFinalEX31d = 0

        # declarando numero aleatorio
        Num3Dd2 = random.randint(-1000, 1000)
        Num4Dd2 = random.randint(-1000, 1000)

        # inicio do tempo
        InicioTempoEX32d = time.time()

        # segunda pergunda do dificil dupla -
        RD2d2 = input(f'{Num3Dd2} - {Num4Dd2}=')
        RD2d2 = int(RD2d2)

        # fim do tempo
        FimDoTempoEX32d = time.time()
        FimDoTempoEX32d = int(FimDoTempoEX32d)
        InicioTempoEX32d = int(InicioTempoEX32d)
        ResultadoDoTempoEX32d = (FimDoTempoEX32d - InicioTempoEX32d)

        # respostas
        if RD2d2 == Num3Dd2-Num4Dd2:
            print('você acertou')

            if ResultadoDoTempoEX32d < 5: 
                NotaFinalEX32d = 10

            elif ResultadoDoTempoEX32d < 30:
                NotaFinalEX32d = 10 - (ResultadoDoTempoEX32d * 0.2)

        else:
            print('você errou')
            NotaFinalEX32d = 0

        # declarando numero aleatorio
        Num5Dd2 = random.randint(-1000, 1000)
        Num6Dd2 = random.randint(-1000, 1000)

        # inicio tempo
        InicioTempoEX33d = time.time()

        # terceira pergunta do facil dupla *
        RD3d2 = input(f'{Num5Dd2} * {Num6Dd2}=')
        RD3d2 = int(RD3d2)

        # fim tempo
        FimDoTempoEX33d = time.time()
        FimDoTempoEX33d = int(FimDoTempoEX33d)
        InicioTempoEX33d = int(InicioTempoEX33d)
        ResultadoDoTempoEX33d = (FimDoTempoEX33d - InicioTempoEX33d)

        # respostas
        if RD3d2 == Num5Dd2 * Num6Dd2:
            print('você acertou')

            if ResultadoDoTempoEX33d < 5: 
                NotaFinalEX33d = 10

            elif ResultadoDoTempoEX33d < 30:
                NotaFinalEX33d = 10 - (ResultadoDoTempoEX33d * 0.2)

        else:
            print('você errou')
            NotaFinalEX33d = 0

        # declarando numero aleatorio
        Num7Dd2 = random.randint(-1000, 1000)
        Num8Dd2 = random.randint(-1000, 1000)

        # inicio tempo
        InicioTempoEX34d = time.time()

        # quarta pergunta do dificil dupla //
        RD4d2 = input(f'{Num7Dd2} // {Num8Dd2}=')
        RD4d2 = int(RD4d2)

        # fim tempo
        FimDoTempoEX34d = time.time()
        FimDoTempoEX34d = int(FimDoTempoEX34d)
        InicioTempoEX34d = int(InicioTempoEX34d)
        ResultadoDoTempoEX34d = (FimDoTempoEX34d - InicioTempoEX34d)

        # respostas
        if RD4d2 == Num7Dd2 // Num8Dd2:
            print('você acertou')

            if ResultadoDoTempoEX34d < 5: 
                NotaFinalEX34d = 10

            elif ResultadoDoTempoEX34d < 30:
                NotaFinalEX34d = 10 - (ResultadoDoTempoEX34d * 0.2)

        else:
            print('você errou')
            NotaFinalEX34d = 0

        # mostar nota
        print(f" jogador 1 fez {NotaFinalEX21d + NotaFinalEX22d + NotaFinalEX23d + NotaFinalEX24d} pontos ")
        
        print(f" jogador 2  fez {NotaFinalEX31d + NotaFinalEX32d + NotaFinalEX33d + NotaFinalEX34d} pontos ")


else:
    print('Reinicie o jogo')


