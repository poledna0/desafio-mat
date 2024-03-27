# Henrique Poledna , Eduardo Machado de Oliveira , Arthur Ascione de Carvalho , Arthur Gabriel Goes e Pedro Lucas Gomes Vitorino

import random
import time

Inicio = input('Você quer jogar com quantos jogadores?[1/2]:')
print('1 - FÁCIL')
print('2 - MEDIO')
print('3 - DIFICIL\n')
Dificuldade = int(input('Sua escolha: '))

# modo facil do jogo
Multiplicador = 1
# modo médio do jogo
if Dificuldade == 2:
    Multiplicador = 10
# modo difícil do jogo
elif Dificuldade == 3:
    Multiplicador = 100

# declarando os numeros aleatorios
Num1f = random.randint(-10 * Multiplicador, 10 * Multiplicador)  
Num2f = random.randint(-10 * Multiplicador, 10 * Multiplicador)

# inicio da contagem de tempo
InicioTempoEX11 = int(time.time())

# primeira pegunta
Rf1 = int(input(f'{Num1f} + {Num2f}='))

# fim do tempo
FimDoTempoEX11 = int(time.time())
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
Num3f = random.randint(-10 * Multiplicador, 10 * Multiplicador)
Num4f = random.randint(-10 * Multiplicador, 10 * Multiplicador)

# inicio do tempo
InicioTempoEX12 = int(time.time())

# segunda pergunta
Rf2 = int(input(f'{Num3f} - {Num4f}='))

# fim do tempo
FimDoTempoEX12 = int(time.time())
ResultadoDoTempoEX12 = (FimDoTempoEX12 - InicioTempoEX12)

# respostas
if Rf2 == Num3f - Num4f:
    print('você acertou')
    if ResultadoDoTempoEX12 < 5:
        NotaFinalEX12 = 10
    elif ResultadoDoTempoEX12 < 30:
        NotaFinalEX12 = 10 - (ResultadoDoTempoEX12 * 0.2)
else:
    print('você errou')
    NotaFinalEX12 = 0

# declarando numero aleatorio
Num5f = random.randint(-10 * Multiplicador, 10 * Multiplicador)
Num6f = random.randint(-10 * Multiplicador, 10 * Multiplicador)

# inicio do tempo
InicioTempoEX13 = int(time.time())

# terceira pergunta 
Rf3 = int(input(f'{Num5f} * {Num6f}='))

# fim do tempo
FimDoTempoEX13 = int(time.time())
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
Num7f = random.randint(-10 * Multiplicador, 10 * Multiplicador )
Num8f = random.randint(-10 * Multiplicador, 10 * Multiplicador)

# inicio do temp
InicioTempoEX14 = int(time.time())

# quarta pergunta
Rf4 = int(input(f'{Num7f} // {Num8f}='))

# fim do tempo
FimDoTempoEX14 = int(time.time())
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

# mostrar nota
print(f" jogador 1 fez {NotaFinalEX11 + NotaFinalEX12 + NotaFinalEX13 + NotaFinalEX14} pontos ")

if Inicio == '2':

    if Dificuldade == 1:
        Multiplicador = 1
    elif Dificuldade == 2:
        Multiplicador = 10
    elif Dificuldade == 3:
        Multiplicador = 100

    Num1f = random.randint(-10 * Multiplicador, 10 * Multiplicador)
    Num2f = random.randint(-10 * Multiplicador, 10 * Multiplicador)

    print('Vez do jogador Numero 2')
    input('Digite qualquer tecla para continuar')

    # inicio tempo
    InicioTempoEX31 = int(time.time())

    # primeira pegunta
    Rf1 = int(input(f'{Num1f} + {Num2f}='))

    # fim do tempo
    FimDoTempoEX31 = int(time.time())
    ResultadoDoTempoEX31 = (FimDoTempoEX31 - InicioTempoEX31)

    # resposatas
    if Rf1 == Num1f + Num2f:
        print('você acertou')
        if ResultadoDoTempoEX31 < 5:
            NotaFinalEX31 = 10
        elif ResultadoDoTempoEX31 < 30:
            NotaFinalEX31 = 10 - (ResultadoDoTempoEX31 * 0.2)
    else:
        print('você errou')
        NotaFinalEX31 = 0

    # declarando numero aleatorio
    Num3fd2 = random.randint(-10 * Multiplicador, 10 * Multiplicador)
    Num4fd2 = random.randint(-10 * Multiplicador, 10 * Multiplicador)

    # inicio tempo
    InicioTempoEX32 = int(time.time())

    # segunda pergunda
    Rf2d2 = int(input(f'{Num3fd2} - {Num4fd2}='))

    # fim do tempo
    FimDoTempoEX32 = int(time.time())
    ResultadoDoTempoEX32 = (FimDoTempoEX32 - InicioTempoEX32)

    # respostas
    if Rf2d2 == Num3fd2 - Num4fd2:
        print('você acertou')
        if ResultadoDoTempoEX32 < 5:
            NotaFinalEX32 = 10
        elif ResultadoDoTempoEX32 < 30:
            NotaFinalEX32 = 10 - (ResultadoDoTempoEX32 * 0.2)
    else:
        print('você errou')
        NotaFinalEX32 = 0

    # declarando numero aleatorio
    Num5fd2 = random.randint(-10 * Multiplicador, 10 * Multiplicador)
    Num6fd2 = random.randint(-10 * Multiplicador, 10 * Multiplicador)

    # inicio do tempo
    InicioTempoEX33 = int(time.time())

    # terceira pergunta
    Rf3d2 = int(input(f'{Num5fd2} * {Num6fd2}='))

    # fim do tempo
    FimDoTempoEX33 = int(time.time())
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
    Num7fd2 = random.randint(-10 * Multiplicador, 10 * Multiplicador)
    Num8fd2 = random.randint(-10 * Multiplicador, 10 * Multiplicador)

    # inicio do tempo
    InicioTempoEX34 = int(time.time())

    # quarta pergunta
    Rf4d2 = int(input(f'{Num7fd2} // {Num8fd2}='))

    # fim do tempo
    FimDoTempoEX34 = int(time.time())

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
    print(f" jogador 1 fez {NotaFinalEX11 + NotaFinalEX12 + NotaFinalEX13 + NotaFinalEX14} pontos ")
    print(f" jogador 2  fez {NotaFinalEX31 + NotaFinalEX32 + NotaFinalEX33 + NotaFinalEX34} pontos ")
else:
    print('Reinicie o jogo')
