# Escreva um programa em Python que gere valores aleatórios de temperatura simulando leituras em um termômetro a cada hora ao longo de um dia. Os valores gerados devem seguir aproximadamente os valores reais de temperatura em sua localidade. Por exemplo, em uma cidade do interior do RN, valores típicos de temperatura variam entre 15°C e 45ºC, decaindo na madrugada até o nascer do sol, depois aumentando até as 15h aproximadamente e, em seguida, decaindo novamente até a meia-noite.

from random import randint




for hora in range(24):
    c = randint(15,45)
    while c > 22 and hora < 5:
        c = randint(15,45)

    print('as temperaturas em {}h foram: {}' .format(hora,c))