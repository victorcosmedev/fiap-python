def selecionar_operacao():
    # Valor False para que ela se torne verdadeira dentro do loop e quebre-o
    validacao_opcao = False
    # Declarando o set de opções válidas para ser usado no teste lógico abaixo
    opcoes_validas = {'1', '2', '3', '4'}

    while not validacao_opcao:
        print('Por favor, selecione uma das operações abaixo:')
        print('1 - Cadastrar-se')
        print('2 - Cadastrar novo veículo')
        print('3 - Visualizar cadastro')
        print('4 - Finalizar o atendimento')
        opcao_selecionada = input('Digite o número da operação desejada: ')

        # Caso a opção selecionada para o usuário seja válida, o loop é quebrado
        if opcao_selecionada in opcoes_validas:
            validacao_opcao = True
        else:
            print('\nOPCÃO INVÁLIDA!\n')
    return opcao_selecionada


def cria_titulo(texto):
    tamanho_barra = len(
        "=====================================================================")
    tamanho_texto = len(texto)
    tamanho_espacamento = (tamanho_barra - tamanho_texto) // 2

    print("\n=====================================================================")
    print(' ' * tamanho_espacamento, texto)
    print("=====================================================================")


def valida_numero_residencia(numero_residencia):

    # Verifica se o único caractere alfabético contido no número da residência é o último.
    # Utilizado para verificar números como: casa 14A, casa 13C etc.
    for caractere in numero_residencia[:-1]:
        if not caractere.isdigit():
            return False

    return True


def cria_cadastro():
    cria_titulo("CADASTRO DE USUARIO")

    valid_nome = False
    while not valid_nome:
        nome = input("Insira seu nome: ")

        # Se o nome for composto somente por letras e for composto por 3 ou mais letras
        # obs.:o menor nome próprio da língua portuguesa é "Ana", com 3 letras
        if nome.replace(' ', '').isalpha():

            if len(nome) >= 3:
                valid_nome = True
            else:
                print("O nome inserido não existe.")
        else:
            print('Insira apenas caracteres alfabéticos no nome.\n')
            #  Cadastrar novo veículo

    valid_idade = False
    while not valid_idade:

        idade = input('Insira sua idade: ')
        # Se o valor (string) inserido for numérico, então transforme o valor em inteiro
        if idade.isdigit():

            # Validação para saber se o usuário é maior de idade
            if int(idade) >= 18:
                idade = int(idade)
                valid_idade = True
            else:
                print('Você precisa completar 18 anos para fazer cadastro.\n')
        else:
            print("Insira apenas valores numéricos.\n\n")

    valid_cep = False
    while not valid_cep:
        cep = input('Insira seu CEP (apenas números): ')

        # Verificação se o valor inserido do CEP é composto 100% por dígitos
        if cep.replace('-', '').isdigit():
            # Verificação se o CEP inserido atende aos requisitos
            if len(cep) == 9:
                valid_cep = True
            else:
                print(
                    'O CEP inserido não é válido. Insira o CEP no formato "12345-678"\n')
        else:
            print('O CEP inserido não é válido. Insira apenas caracteres numéricos"\n')

    valid_numero_residencia = False
    while not valid_numero_residencia:
        numero_residencia = input(
            'Insira o número da sua residência (ex.: 123, 14A, 13C): ')

        if numero_residencia.replace('-', '').isalnum():
            if valida_numero_residencia(numero_residencia):
                valid_numero_residencia = True
            else:
                print('Você inseriu o número da residência junto com textos!')
        else:
            print('Insira apenas números alfanuméricos!\n')

    # Criação do "objeto" usuário
    usuario = {
        'nome': nome,
        'idade': idade,
        'cep': cep,
        'numero_residencia': numero_residencia,
        'veiculos': [],
    }

    return usuario


def menu_cadastro_veiculo():
    print('Por favor, selecione uma das operações abaixo:')
    print('1 - Adicionar um veículo')
    print('2 - Alterar um veículo: ')
    print('3 - Excluir veículo')
    print('4 - Sair')
    opcao_selecionada = input(
        'Digite o número da operação desejada: ')

    opcoes_possiveis = {'1', '2', '3', '4'}

    print(
        "=====================================================================\n")

    while opcao_selecionada not in opcoes_possiveis:
        print('O número que você digitou não condiz com as opções possíveis.')
        print('Por favor, selecione uma das operações abaixo:')
        print('1 - Adicionar outro veículo')
        print('2 - Alterar um veículo: ')
        print('3 - Excluir veículo')
        print('4 - Sair')

        opcao_selecionada = input('Digite o número da opção selecionada: ')

    return opcao_selecionada


def valida_veiculo():
    valid_marca = False
    while not valid_marca:
        marca = input('Insira a marca do seu carro: ')
        if marca.replace(' ', '').isalpha():
            valid_marca = True
        else:
            print('A marca inserida é inválida!\n')

    valid_modelo = False
    while not valid_modelo:
        modelo = input('Insira o modelo do seu carro: ')

        # método alnum() verifica se a string é um valor alfanumérico, já que temos modelos como Fiat 500, BMW 320i etc.
        if modelo.replace(' ', '').isalnum():
            valid_modelo = True
        else:
            print('O modelo inserido é inválido!\n')

    valid_ano = False
    while not valid_ano:
        ano = input('Insira o ano do seu carro: ')
        # Caso o valor de ano seja composto por 4 digitos e seja um inteiro, então converta para inteiro
        if ano.isdigit():
            if len(ano) == 4:
                ano = int(ano)
                valid_ano = True
            else:
                print('Insira o ano com 4 dígitos (ex.: 2000).\n')
        else:
            print('Por favor, insira apenas números.\n')

    valid_placa = False
    while not valid_placa:
        placa = input('Insira a placa do seu carro (formato XXX-0000): ')
        if len(placa) == 8:
            if placa.replace('-', '').isalnum():
                valid_placa = True
            else:
                print('Insira apenas letras e números!\n')
        else:
            print('A placa inserida tem menos digitos do que deveria!\n')

    # Criação do "objeto" veículo
    veiculo = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'placa': placa,
    }

    return veiculo


def exibe_veiculos(usuario):
    for indice_veiculo, veiculo in enumerate(usuario['veiculos']):
        print(f'Veículo #{indice_veiculo + 1}')
        print(f'\tMarca: {veiculo["marca"]}')
        print(f'\tModelo: {veiculo["modelo"]}')
        print(f'\tAno: {veiculo["ano"]}')
        print(f'\tPlaca: {veiculo["placa"]}')
        print('')


def cadastra_veiculo(usuario):

    cria_titulo("CADASTRO DE VEICULO")

    # Verifica se o usuário está cadastrado (existe no sistema)
    if usuario:

        fim_cadastro_veiculo = False
        while not fim_cadastro_veiculo:
            opcao_selecionada = menu_cadastro_veiculo()

            # Adicionar um veículo
            if opcao_selecionada == '1':
                veiculo = valida_veiculo()

                # Associação do dicionário veículo ao dicionário usuário
                usuario['veiculos'].append(veiculo)
                print('Veículo cadastrado com sucesso!\n')

            # Alterar um veículo
            elif opcao_selecionada == '2':
                print('Qual o veículo que você deseja alterar?')

                exibe_veiculos(usuario)

                veiculo_alterado = False
                while not veiculo_alterado:
                    opcao_veiculo = input(
                        'Qual o veículo que você deseja alterar? Digite o número correspondente: ')

                    if opcao_veiculo.isdigit():
                        if int(opcao_veiculo) > 0 and int(opcao_veiculo) <= len(usuario['veiculos']):
                            veiculo_alterado = int(opcao_veiculo)
                        else:
                            print('O veículo que você deseja alterar não existe!\n')
                    else:
                        print('Insira apenas números!\n')

                indice_veiculo_alterado = veiculo_alterado - 1
                usuario['veiculos'].pop(indice_veiculo_alterado)

                print("\nPor favor, refaça o cadastro do seu pedido: ")

                # Criação do "objeto" veículo
                veiculo = valida_veiculo()
                # Associação do dicionário veículo ao dicionário usuário
                usuario['veiculos'].insert(
                    indice_veiculo_alterado, veiculo)

            # Exclusão de veículo
            elif opcao_selecionada == '3':
                exibe_veiculos(usuario)

                veiculo_excluido = input(
                    'Qual o veículo que você deseja remover?')
                verifica_numero = True

                # verificação de numero
                while verifica_numero:
                    if type(veiculo_excluido) != int and veiculo_excluido.isdigit() == False:
                        veiculo_excluido = input(
                            'O que você inseriu não é um número. Por favor, digite apenas números: ')
                    elif type(veiculo_excluido) != int and veiculo_excluido.isdigit() == True:
                        veiculo_excluido = int(veiculo_excluido)

                    elif veiculo_excluido > len(usuario['veiculos']) or veiculo_excluido <= 0:
                        veiculo_excluido = input(
                            'Digite o numero do veículo que deseja remover: ')

                    else:
                        verifica_numero = False

                usuario['veiculos'].pop(veiculo_excluido - 1)

            else:
                fim_cadastro_veiculo = True
    else:
        print('Você não está cadastrado no sistema, volte ao cadastro de usuário.\n')


def visualizar_cadastro(usuario):
    cria_titulo("VISUALIZAR CADASTRO")

    # Verificando se o usuário existe para mostrar o cadastro dele
    if usuario:
        # Loop for para exibir os valores do usuário.
        for chave, valor in usuario.items():
            # Já que temos valores do tipo dicionário, precisamos verificar se
            # o valor é um dicionário para exibi-lo corretamente.
            if isinstance(valor, list):
                # Exibindo a chave com a primeira letra maiúscula.
                print(f'{chave.capitalize()}: ')
                for indice_veiculo, veiculo in enumerate(valor):
                    print(f"\tVeiculo #{indice_veiculo + 1}")
                    # Para cada chave e valor dentro do dicionário (neste caso, o value
                    # do loop anterior), exibir o valor.
                    for key, value in veiculo.items():
                        print(f'\t{key.capitalize()}: {value}')

                    print(
                        "=====================================================================")
            else:
                print(f'{chave.capitalize()}: {valor}')

        print('Cadastro exibido com sucesso! Fim da operação\n')
    else:
        print('Você não está cadastrado no sistema, volte ao cadastro de usuário.\n')
