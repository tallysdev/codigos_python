#questão 15
#An=6A(n-1)-8A(n-2) a0=1 a1=0

recursao15=int(input("informe o Valor de n para todas a questões:"))

def recursaoQ15(recursao15):
  if recursao15==0:
    return 1
  elif recursao15==1:
    return 0
  else:
    return 6*recursaoQ15(recursao15-1)-8*recursaoQ15(recursao15-2)

print('Questão 15:\n')
print('Usano a Recursão:',recursaoQ15(recursao15))

a0_15=1
a1_15=0
an_15=1
if recursao15==1:
  an_15=0
else:
  for i in range(2,recursao15+1):
    an_15=6*a1_15-8*a0_15
    a0_15=a1_15
    a1_15=an_15

print('Por Loop:',an_15)

def solucaoq15(n):
  return (-1)*(4**n)+2*(2**n)

print('Por Soluçaõ:', solucaoq15(recursao15))

#############################################################

#questão 16
#An=2A(n-1)+8A(n-2) a0=4 a1=10

recursao16 = recursao15

def recursaoQ16(recursao16):
  if recursao16==0:
    return 4
  elif recursao16==1:
    return 10
  else:
    return 2*recursaoQ16(recursao16-1)+8*recursaoQ16(recursao16-2)

print('\nQuestão 16:\n')
print('Usando a Recursão:',recursaoQ16(recursao16))

a0_16=4
a1_16=10
resultado_16=4
if recursao16==1:
  resultado_16=10
else:
  for i in range(2,recursao16+1):
    resultado_16=2*a1_16+8*a0_16
    a0_16=a1_16
    a1_16=resultado_16

print('Por loop:',resultado_16)

def solucaoq16(n):
  return 3*(4**n)+(-2)**n

print('Por Solução:', solucaoq16(recursao16))

#######################################################################

#questão 17
#An=7A(n-1)-10A(n-2) a0=5 a1=16

recursao17 = recursao15

def recursaoQ17(recursao17):
  if recursao17==0:
    return 5
  elif recursao17==1:
    return 16
  else:
    return 7*recursaoQ17(recursao17-1)-10*recursaoQ17(recursao17-2)

print('\nQuestão 17:\n')

print('Usando a Recursão:',recursaoQ17(recursao17))

a0_17=5
a1_17=16
resultado_17=5
if recursao17==1:
  resultado_17=16
else:
  for i in range(2,recursao17+1):
    resultado_17=7*a1_17-10*a0_17
    a0_17=a1_17
    a1_17=resultado_17

print('Por Loop:',resultado_17)

def solucaoq17(n):
  return 2*(5**n)+3*(2**n)

print('Por Solução:',solucaoq17(recursao17))

#####################################################################

#questão 18
#2*An=7A(n-1)-3A(n-2) a0=a1=1
#An=(7A(n-1)-3A(n-2))/2

print('\nQuestão 18:\n')


recursao18 = recursao15

def recursaoQ18(recursao18):
  if recursao18==0 or recursao18==1:
    return 1
  else:
    return (7*recursaoQ18(recursao18-1)-3*recursaoQ18(recursao18-2))/2

print('Usando a Recursão',recursaoQ18(recursao18))

a0_18=1
a1_18=1
resultado_18=1
for i in range(2,recursao18+1):
  resultado_18=(7*a1_18-3*a0_18)/2
  a0_18=a1_18
  a1_18=resultado_18
print('Por loop:',resultado_18)

def solucaoq18(n):
  return 2**(-n)*(0.2*(6**n)+0.8)

print('Por Solução',solucaoq18(recursao18))