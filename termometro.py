# Escreva um programa em Python que gere valores aleatórios de temperatura simulando leituras em um termômetro a cada hora ao longo de um dia. Os valores gerados devem seguir aproximadamente os valores reais de temperatura em sua localidade. Por exemplo, em uma cidade do interior do RN, valores típicos de temperatura variam entre 15°C e 45ºC, decaindo na madrugada até o nascer do sol, depois aumentando até as 15h aproximadamente e, em seguida, decaindo novamente até a meia-noite.

from random import randint, random, uniform


temp = []
aux = 0
saia = False
for hora in range(24):
    c = uniform(15,45)
    while c > 25 and hora < 9 or c > 30 and hora > 20 and saia == False:
        c = uniform(15,45)
        print('aaa')
        saia == True
    temp.append(c)
    tam = len(temp)
    
    if tam > 1:
        aux = tam-2

    while (((c - temp[aux] > 4 or c - temp[aux] < -4) and (hora < 10 or hora >18) and saia == False)):
        c = uniform(15,45)
        # print('entrou')
        saia == True
    
    
    saia == False 

    while (((c - temp[aux] > 2 or c - temp[aux] < -4) and (hora > 10 or hora <18) and saia == False)):
        c = uniform(20,45)
        # print('entrou')
        saia == True

    temp.append(c)
    
    print('as temperaturas em %d h foram: %.2f, ' %(hora,c))
