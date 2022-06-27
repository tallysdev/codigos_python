# Escreva um programa em Python que gere valores aleatórios de temperatura simulando leituras em um termômetro a cada hora ao longo de um dia. Os valores gerados devem seguir aproximadamente os valores reais de temperatura em sua localidade. Por exemplo, em uma cidade do interior do RN, valores típicos de temperatura variam entre 15°C e 45ºC, decaindo na madrugada até o nascer do sol, depois aumentando até as 15h aproximadamente e, em seguida, decaindo novamente até a meia-noite.

from random import randint
from tkinter import W


temp = []
aux = 0
for hora in range(24):
    c = randint(15,45)
    while c > 25 and hora < 10 or c > 35 and hora > 16:
        c = randint(15,45)
    temp.append(c)
    tam = len (temp)
    if tam > 1:
        aux = tam-1

    while c - temp[aux] > 4 or c - temp[aux] < -4:
        c = randint(15,45)

    print('as temperaturas em {}h foram: {}' .format(hora,c))
print(temp)