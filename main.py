list = []
tam_conv = int(input('qauntos convidados\t'))

for i in range(0, tam_conv):
        z = i + 1
        conv = input('Nome do convidado {} '.format(z))
        list.append(conv)
print('Lista de convidados:{}'.format(list))
