# Agenda de contatos
from curses import pair_number


go = input('Quer ver sua agenda de contatos?\t(s/n)\n')
while go == 's':
    print('##########################')
    print('### Agenda de contatos ###')
    print('## 1- Cadastrar usuario ##')
    print('## 2- Pesquisar contato ##')
    print('## 3- Atualizar contato ##')
    print('## 4- Apagar contato    ##')
    print('## 5- Listar todos      ##')
    print('## 0- Sair              ##')