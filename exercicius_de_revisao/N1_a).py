# a. Disputar 5 partidas e identificar quantas partidas cada jogador venceu

import random
part = 0
vjog = 0
vcomp = 0
while part < 5:
    jog = random.randint(1,6)
    comp = random.randint(1,6)
    print('Jogador: ', jog)
    print('Computador: ',comp)
    if (jog > comp):
        print('Parabens, voce ganhou!')
        part = part + 1
        vjog = vjog + 1
    elif(comp > jog):
        print('Infelizmente, o computador ganhou')
        part = part + 1
        vcomp = vcomp + 1
    else:
        print('Jogo Empatado!!!')
        part = part + 1
        
print('Fim do Programa')
print('O jogador ganhou:',vjog,'e o computador ganhou',vcomp)
