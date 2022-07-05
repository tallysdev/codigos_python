from math import sqrt
#questão 22
#Ln=L(n-1)+L(n-2) L1=1 L2=3 n>=3

recursao22=int(input("Questão 22 Digite um Valor:"))

print('\nQuestão 22\n')

def recursaoQ22(recursao22):
  if recursao22==1:
    return 1
  elif recursao22==2:
    return 3
  else:
    return recursaoQ22(recursao22-1) + recursaoQ22(recursao22-2)

print('Usando a Recursão:',recursaoQ22(recursao22))

a1_22=1
a0_22=3
resultado_22=1
if recursao22==2:
  resultado_22=a0_22
elif recursao22==1:
  resultado_22=a1_22
else:
  for i in range(3,recursao22+1):
      resultado_22=a1_22+a0_22
      a1_22=a0_22
      a0_22=resultado_22

print('Por loop:',resultado_22)



####################################################################

#questão 23
#9An=6A(n-1)-A(n-2) a0=6 a1=5
#An=(6A(n-1)-A(n-2))/9

reursao23=int(input("\nQuestão 23 Digite um Valor:"))

print('\nQuestão 23\n')

def recursaoq23(reursao23):
  if reursao23==0:
    return 6
  elif reursao23==1:
    return 5
  else:
    return (6*recursaoq23(reursao23-1)-recursaoq23(reursao23-2))/9

print('Usando a Recursão:',recursaoq23(reursao23))

a0_23=6
a1_23=5
resultado_23=6
if reursao23==1:
  resultado_23=5
else:
  for i in range(2,reursao23+1):
    resultado_23=(6*a1_23-a0_23)/9
    a0_23=a1_23
    a1_23=resultado_23

print('Por Loop:',resultado_23)


