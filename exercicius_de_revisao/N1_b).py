import random
vjog = 0 
vcomp = 0
while vjog < 6 or vcomp < 6:
    jog = random.randint(1,6)
    comp = random.randint(1,6)
    print('Jogador: ', jog)
    print('Computador: ',comp)
    if (jog > comp):
        vjog+= 1
        print('Parabens, voce ganhou!')
    elif(comp > jog):
        vcomp+=1
        print('Infelizmente, o computador')
    else:
        print('Jogo Empatado!!!')
print('Fim do Programa')
print('O jogador ganhou:',vjog,'e o computador ganhou',vcomp)
