
import random

print('Bem Vindo ao  Jogo de advinhação')

go=input('Quer jogar?(S/N)\t')

comp = random.randint(1,100)

print('Ja escolhi o numero hehehe, dentre 1 a 100')

jog = int(input('tente acertar o numero\t'))

life = 1

teimoso = 0


    
while go.upper() == 'S' and life < 11:
        
    if jog == comp and life == 1:
        print('VOCÊ TEVE MUITA SORTE\n')
        partidas = partidas + 1
        go = input('quer jogar novamente?aa (s/n)\n')
        if go == 's':
            comp = random.randint(1,100)
            life = 0
            jog = int(input('digite o seu palpite\n'))

    elif jog == comp and life >=2 and life <=4:
        print('VOCÊ JOGA BEM, MAS AINDA CONTOU SORTE')
        partidas = partidas + 1
        go = input('quer jogar novamente?aa (s/n)\n')
        if go == 's':
            comp = random.randint(1,100)
            life = 0
            jog = int(input('digite o seu palpite\n'))
    
    elif jog == comp and life >=5 and life <=7:
        print('Acertou, VOCÊ É UM EXCELENTE ESTRATEGISTA\n ')
        partidas = partidas + 1    
        go = input(' quer jogar novamente?aa (s/n)\n')
        if go == 's':
            comp = random.randint(1,100)
            life = 0
            jog = int(input('digite o seu palpite\n'))

    elif jog == comp and life >=8 and life <=10 :
        print('Acertou, VOCÊ É UM EXCELENTE ESTRATEGISTA\n ')
        partidas = partidas + 1    
        go = input(' quer jogar novamente?aa (s/n)\n')
        if go == 's':
            comp = random.randint(1,100)
            life = 0
            jog = int(input('digite o seu palpite\n'))

    elif jog < comp and life < 11:
        life = life + 1 
        print(' errouuuu, digite um numero maior \n')
        teimoso = jog
        jog = int(input('digite outro valor\n'))
        if teimoso > jog:
            print('perdeu trouxa')
            go = 'xau' 
            break
        
    elif jog > comp and life < 11:
        life  = life + 1
        teimoso2 = jog
        print(('\nerrouuuu, digite um numero menor'))
        jog = int(input('digite outro valor\n'))
        if teimoso2 < jog:
            print('perdeu trouxa')
            go = 'xau'
            break
        #perdeu
    else:
        print('voce perdeu, acabou suas chances, \n \t ANALISE MELHOR SUA ESTRATÉGIA ANTES DE JOGAR NOVAMENTE\n')
        partidas = partidas + 1
        go = input('quer jogar novamente?aa (s/n)\n')
        if go == 's':
            comp = random.randint(1,100)
            life = 0
            jog = int(input('\nDiga seu Palpite\n'))
        else:
            break
    

print('Voce teve que usar', life+1, 'tentativas para acertar o resultado')        
print('FIm')     
