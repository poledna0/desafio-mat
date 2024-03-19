<style type="text/css">
    ol { list-style-type: upper-alpha; }
</style>

# TDE 1

## Descrição

O objetivo deste trabalho é implementar um jogo que ofereça ao jogador operações básicas de matemática a serem resolvidas no menor tempo possível.

O jogo deve apresentar equações com as quatro operações básicas: soma(+), subtração(-), multiplicação(*) e divisão inteira (//). Os valores das equações são gerados aleatoriamente a cada jogada.

Além disso, o jogo deve permitir o modo individual ou um confronto entre duas pessoas.

Ao final um placar com as respostas e resultado final deve ser exibido. O jogo também deve incluir um limite de tempo, no qual os jogadores perdem pontos ao demorar para responder as questões. O jogo deve possuir três níveis de dificuldade nos quais o intervalo dos números gerados aumenta em cada nível.

## Dinâmica

Ao executar o programa, os jogadores devem ser apresentados a um menu com as opções de jogar individualmente ou em dupla. Posteriomente deve-se exibir 3 níveis de dificuldade: fácil, médio e difícil.

Então, os jogadores serão desafiados a responder 4 equações geradas aleatoriamente, com dois numerais apenas, tais como `10 + 5`, `3 – 7`, `2 * 7`, e assim por diante.

Primeiro será apresentada uma soma (+), depois uma subtração (-), posteriormente uma multiplicação (*) e finalmente uma dívisão inteira(//). Cada equação deve ser apresentada ao seu tempo, e o usuário deve responder em um limite de tempo de 30 segundos. Cada resposta correta resulta em 10 pontos para o jogador. Após o segundo 5, cada segundo reduz 2% da sua pontuação total para aquela questão.

<ol type="a">
  <li>De -10 a 10, para o modo Fácil</li>
  <li>De -100 a 100, para o modo Médio</li>
  <li>De -1000 a 1000, para o modo Difícil</li>
</ol>

Ao final do jogo, um placar com o resultado final da partida é apresentado, incluindo a pontuação de cada jogador e o tempo total de jogo. É importante ressaltar que as regras do jogo devem ser consistentes e justas para ambos os jogadores, além de garantir a segurança e integridade dos dados do programa.
