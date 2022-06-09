# Agenda de contatos

go = input('Quer ver sua agenda de contatos?\t(s/n)\n')
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
    opcao = input()
    # sair
    if opcao == '0':
        go = 'xau'
    elif opcao == '1':
        n = input('deseja adicionar quantos contatos?\n'))
        for i in range(n):
            contato = input('Informe o contato\n')
            contatos.append(contato)
        print(contatos)


print('Voce saiu da agenda')