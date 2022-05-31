com = []
def conjuntosnum(com):
    tam_conv = int(input('tamanho do conjuto numerico\t'))
    for i in range(0, tam_conv):
        z = i + 1
        conv = int(input('digite o numero:\t {} '.format(z)))
        com.append(conv)
    max_value = 0
    for num in com:
        if (max_value is None or num > max_value):
            max_value = num
    return print('Maximum value:', max_value)

conjuntosnum(com)