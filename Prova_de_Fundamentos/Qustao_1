# Questão 1

recursao=int(input("informe o valor de n: "))
 
#letra A
#A(n+1) - An = 2n + 3 , n>=0 A0=1
#A(n+1) = 2n + 3 + An
#An = 2(n-1) + 3 + A(n-1)

print("Questão 1°:\n")

print("Letra A:")

an=1
loop=1

for j in range(1,recursao+1):
    loop = 2*(j-1) + 3 + (loop)


print("Por Loop: ",loop)

def solucaoLetraA(n):
  return 1+(n)*(n+2)

print("Por Solução:", solucaoLetraA(recursao))

def recursaoLetraA(n):
  if n==0:
    return 1
  else:
    return 2*(n-1) + 3 + recursaoLetraA(n-1)

print("Usano a Recursão:",recursaoLetraA(recursao))
print()

#letra B
#A(n+1) - An = 3(n^2) - n , n>=0 A0=3
#A(n+1) = 3(n^2) - n  + An
#An = 3((n-1)^2) - (n-1)  + A(n-1)

print("Letra B:")

anB=3

for i in range(1,recursao+1):
  anB=3*((i-1)**2)-(i-1)+anB

print("Por Loop: ",anB)

def solucaoLetraB(x):
  return 3+((x-1)**3)+((x-1)**2)

print("Por Solução:", solucaoLetraB(recursao))

def recursaoLetraB(x):
  if x==0:
    return 3
  else:
    return 3*((x-1)**2) - (x-1) + recursaoLetraB(x-1)

print("Usano a Recursão:",recursaoLetraB(recursao))
print()


#letra C
#A(n+1) - 2An = 5 , n>=0 A0=1
#A(n+1) = 5 + 2An
#An = 5 + 2A(n-1)

print("Letra C:")

AnC=1

for i in range(1,recursao+1):
  AnC=5+2*AnC

print("Por Loop: ",AnC)

def solucaoLetraC(y):
  return 12*(2**(y-1))-5 

print("Por Solução:", solucaoLetraC(recursao))

def recursaoLetraC(y):
  if y==0:
    return 1
  else:
    return 5 + 2*recursaoLetraC(y-1)

print("Usano a Recursão:",recursaoLetraC(recursao))
print()

#letra D
#A(n+1) - 2An = 2^n , n>=0 A0=1
#A(n+1) = 2^n + 2An
#An = 2^(n-1) + 2A(n-1)

print("Letra D:")

AnD=1

for i in range(1,recursao+1):
  AnD=(2**(i-1))+2*AnD

print("Por Loop: ",AnD)

def solucaoLetraD(z):
  return  (2**(z-1))*(3+(z-1))

print("Por Solução:", solucaoLetraD(recursao))

def recursaoLetraD(z):
  if z==0:
    return 1
  else:
    return (2**(z-1)) + 2*recursaoLetraD(z-1)

print("Usando a Recursão:",recursaoLetraD(recursao))
print()