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
for i in range(8):
    ratura = input('Informe a temperatura')
    tempe.append(ratura)
print(tempe)