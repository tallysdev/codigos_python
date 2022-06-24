# Agenda de contatos

go = input('Quer ver sua agenda de contatos?\t(s/n)\n')
agenda = []
contatos = []
while go == 's':
    print('##########################')
    print('### Agenda de contatos ###')
    print('## 1 - Cadastrar contato ##')
    print('## 2 - Pesquisar contato ##')
    print('## 3 - Atualizar contato ##')
    print('## 4 - Apagar contato    ##')
    print('## 5 - Listar todos      ##')
    print('## 0 - Sair              ##')
    opcao = input('\n')
    # sair
    if opcao == '0':
        go = 'xau'
    
    elif opcao == '1':

        n = int(input('deseja adicionar quantos contatos?\n'))
        for i in range(n):
            cont = input('Informe o nome do contato {} \n' .format(i+1))
            contatos.append(cont)
            email = input('Informe o email do contato {} \n' .format(i+1))
            contatos.append(email)
            num = input('Informe o numero do contato {} \n' .format(i+1))
            contatos.append(num)
            agenda.append(contatos)

    elif opcao == '2':
        print()
        for v in agenda:
            print('Nome:\t', i[0])
            print('Email:\t',i[1])
            print('Numero:\t',i[2])
    
    elif opcao == '3':
        print()
        busca_nome = input('Informe o nome do contato que voce quer buscar')
        achou = False
        for nome in agenda:
            if busca_nome.upper() in nome[0].upper():
                achou = True
                print('Nome:\t', i[0] )
                print('Email:\t',i[1])
                print('Numero:\t',i[2])
                print()
            if not achou:
                print('Não encontramos esse nome')
    
print('Voce saiu da agenda')
