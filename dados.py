###
### Programa Jogo de Dados
### tirado do slide
import random
vitjog = 0
vitcomp = 0
emp = 0 
play = input('Quer jogar?\t (S/N)')
while play == 's' or play == 'S':
    jog = random.randint(1,6)
    comp = random.randint(1,6)
    print("Jogador : ", jog)
    print("Computador: ", comp)
    if jog > comp:
        print("Jogador Ganhou!")
        vitjog +=1
    elif comp > jog:
        print("Computador Ganhou!")
        vitcomp += 1
    else:
        print("Empate!")
        emp +=1
    play = input('Quer jogar de novo?\t(s/n)')

print('\nVoce jogou', (vitcomp+vitjog+emp),'vezes,','\nempatando', emp, 'vezes,', '\ngannhando', vitjog, 'vezes', '\ne perdendo', vitcomp, 'vezes')
print("Fim do Jogo!")
