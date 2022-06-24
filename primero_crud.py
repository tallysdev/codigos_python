# Agenda de contatos

go = input('Quer ver sua agenda de contatos?\t(s/n)\n')
agenda = []
tell = []
email = []
nome = []
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
            nome.append(cont)
            emai = input('Informe o email do contato {} \n' .format(i+1))
            email.append(email)
            num = input('Informe o numero do contato {} \n' .format(i+1))
            tell.append(num)

            agenda.append(nome)
            agenda.append(tell)
            agenda.append(email)

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
