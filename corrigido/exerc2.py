from getpass import getpass

credenciais_iguais = True

# enquanto o valor não for válido, repetir
while credenciais_iguais:
    print('\n\nNome de usuario nao pode ser igual a senha!')
    usuario = input('Informe um nome de usuário: ')
    senha = getpass('Informe uma senha: ')

    # se credenciais iguais for verdadeiro, o loop será repetido
    credenciais_iguais = usuario == senha
    # if usuario == senha:
    #     print('Nome de usuário não pode ser igual à senha! \n')
    # else:
    #     print(f'{usuario=} {senha=}')
    #     credenciais_iguais = False
