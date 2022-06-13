# 1. O programa em Python a seguir simula um jogo de dados entre um jogador humano e o
# computador:
# Modifique o programa anterior de forma que possam ser disputadas várias partidas, até que
# um dos jogadores sagre-se vencedor. Em cada caso, identifique a estrutura de repetição e o
# critério de parada mais adequado para resolver o problema:

import random
jog = random.randint(1,6)
comp = random.randint(1,6)
print('Jogador: ', jog)
print('Computador: ',comp)
if (jog > comp):
    print('Parabens, voce ganhou!')
elif(comp > jog):
    print('Infelizmente, o computador')
else:
    print('Jogo Empatado!!!')
print('Fim do Programa')