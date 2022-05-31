# Escreva um programa em Python que leia a data de nascimento de um usuário, obtenha a data atual do sistema e calcule, exatamente, quantos anos ele possui, verificando se o usuário já completou ou não aniversário no ano atual.

# ATENÇÃO: Em caso de plágio, TODOS os envolvidos serão penalizados com avaliação negativa (receberão nota -1.0).

from datetime import date
dataatual = date.today()
dianasc = int(input('informe o dia que voce nasceu\t'))
mesnasc = int(input('informe o mes que voce nasceu\t'))
anonasc = int(input('informe o ano que voce nasceu\t'))

idade = dataatual.year - anonasc
if dataatual.month > mesnasc:
    print(idade, 'ta ficando velho hein')
elif dataatual.month == mesnasc:
    if dataatual.day >= dianasc:
        print(idade, 'Parabensss pelo seu aniversario') 
    else:
        idade-1
        print('Calma falta pouco para o seu aniersario jaja tu faz', (idade), 'tu ainda tem' , (idade-1))
else:
    idade-1
    print('Calma falta pouco para o seu aniersario jaja tu faz', (idade), 'tu ainda tem' , (idade-1))