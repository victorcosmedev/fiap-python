valor_valido = False

# enquanto o valor não for válido, repetir
while not valor_valido:

    nota = input('Informe uma nota entre 0 e 10: ')  # ponto de parada

    if nota.replace('-', '').isdigit():
        nota = int(nota)
        if nota >= 0 and nota <= 10:
            print(f'Nota: {nota}')
            valor_valido = True
        else:
            print('Valor incorreto! \n')
    else:
        print('Formato incorrreto! \n')
