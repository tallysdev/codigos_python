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