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
            contato = input('Informe o nome do contato\n', (i+1))
            contatos.append(agenda)
            email = input('Informe o email do ccontato\n', (i+1))
            contatos.append(agenda)
            num = input('Informe o numero do contato\n', (i+1))
            contatos.append(agenda)
        print(contatos)

print('Voce saiu da agenda')
