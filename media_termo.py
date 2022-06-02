# Escreva um programa em Python que leia um
# conjunto de medidas de temperatura de um
# paciente internado ao longo de um
# determinado dia. As medições devem ser
# feitas a cada três horas.

# A seguir, calcule a temperatura média do dia
# e exiba esse valor na tela.

# Por fim, verifique e indique quantas vezes e
# em quais horários a temperatura ficou acima
# da temperatura média do dia.

tempe = []
maiores = []
media = 0
t = 0
h = []

for i in range(8):
    t += 1
    print('informe a temperatura', t)
    ratura = float(input())
    tempe.append(ratura)

print(tempe,'\n')

for i in range(8):
    media = media + tempe[i]

mediaf = media/8

print(mediaf,'\n')

for i in range(8):
    if mediaf < tempe[i]:
        maiores.append(tempe[i])
        h.append(i)

print('as temperaturas maiores foram', sorted(maiores),'nos horarios', sorted(h))
