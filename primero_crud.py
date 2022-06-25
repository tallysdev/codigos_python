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
        n = int(input('Deseja adcionar quantos contatos?\n'))
        for i in range(n):
            contatos = []
            cont = input('Informe o nome do contato {} \n'.format(i+1))
            contatos.append(cont)
            email = input('Informe o email do contato {} \n'.format(i+1))
            contatos.append(email)
            num = input('Informe o numero do contato {} \n'.format(i+1))
            contatos.append(num)       
            agenda.append(contatos)

    elif opcao == '2':
        print()
        busca_nome = input('Informe o nome do contato que voce quer buscar:\t')
        achou = False
        for busca in agenda:
            if busca_nome.upper() in busca[0].upper():
                achou = True
                print('Nome:\t', busca[0])
                print('Email:\t',busca[1])
                print('Numero:\t',busca[2])
                print()
                
            if not achou:
                print('Não encontramos esse nome')
    
    elif opcao == '3':
        print()
        busca_nome = input('Informe o nome do contato que voce quer alterar.\n')
        achou = False
        for att in agenda:
            if busca_nome.upper() in att[0].upper() and not achou:
                for att in agenda:
                    del agenda[0]
                contatos = []
                cont = input('Informe o novo nome do contato \n')
                contatos.append(cont)
                email = input('Informe o novo email do contato \n')
                contatos.append(email)
                num = input('Informe o novo numero do contato \n')
                contatos.append(num)       
                agenda.append(contatos)


            if not achou:
                print('Não encontramos esse nome')
    
    elif opcao == '4':
        print('heheh')
        busca_nome = input('Informe o nome do contato que voce quer alterar.\n')
        achou = False
        for dele in agenda:
            if busca_nome.upper() in dele[0].upper() and not achou:
                for att in agenda:
                    del agenda[0]
            
            if not achou:
                print('Não encontramos esse nome')

    elif opcao == '5':
        print()
        for i in agenda:
            print('Nome:\t', i[0])
            print('Número:\t', i[1])
            print('Email:\t', i[2])
            print()
        print()

    print(agenda)
print('Voce saiu da agenda')
