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
            contato = input('Informe o nome do contato\n')
            contatos.append(contato)
            email = input('Informe o email do ccontato\n')
            contatos.append(email)
            num = input('Informe o numero do contato\n')
            contatos.append(num)
            agenda.append(contatos)
    elif opcao == '2':
        print()
        for i in agenda:
            print('Nome:\t', i[0] )
            print('Email:\t',i[1])
            print('Numero:\t',i[2])
    
    elif opcao == '3':
        print()
    
    print(agenda)

print('Voce saiu da agenda')
