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


def cria_cadastro():
    cria_titulo("CADASTRO DE USUARIO")

    valid_nome = False
    while not valid_nome:
        nome = input("Insira seu nome: ")

        # Se o nome for composto somente por letras e for composto por 3 ou mais letras
        # obs.:o menor nome próprio da língua portuguesa é "Ana", com 3 letras
        if len(nome) >= 3 and nome.isalpha():
            valid_nome = True
        else:
            print('O nome inserido não é válido.\n')
            #  Cadastrar novo veículo

    valid_idade = False
    while not valid_idade:

        idade = input('Insira sua idade: ')
        # Se o valor (string) inserido for numérico, então transforme o valor em inteiro
        if idade.isdigit():
            idade = int(idade)
            valid_idade = True
        else:
            print("O valor inserido não é válido. \n\n")

    valid_cep = False
    while not valid_cep:
        cep = input('Insira seu CEP (apenas números): ')

        # Verificação se o valor inserido do CEP é completamente numérico e tem 8 dígitos
        if len(cep) == 8 and cep.isdigit():
            # Neste caso, o CEP será mantido como string pois não será usado para cálculos matemáticos
            valid_cep = True
        else:
            print('O CEP inserido não é válido.\n')

    valid_numero_residencia = False
    while not valid_numero_residencia:
        numero_residencia = input('Insira o número da sua residência: ')

        if numero_residencia.isdigit():
            # Neste caso, o número da residência será mantido como string pois não será usado para cálculos
            valid_numero_residencia = True
        else:
            print('O número da residência inserido não é válido.\n')

    # Criação do "objeto" usuário
    usuario = {
        'nome': nome,
        'idade': idade,
        'cep': cep,
        'numero_residencia': numero_residencia,
        'veiculos': [],
    }

    return usuario


def cadastra_veiculo(usuario):

    cria_titulo("CADASTRO DE VEICULO")

    # Verifica se o usuário está cadastrado e se não há nenhum
    # Veículo associado a ele. Por enquanto, um usuário poderá ter somente um carro.
    if usuario:
        fim_cadastro_veiculo = False
        while not fim_cadastro_veiculo:
            valid_marca = False
            while not valid_marca:
                marca = input('Insira a marca do seu carro: ')
                if marca.isalpha():
                    valid_marca = True
                else:
                    print('A marca inserida é inválida!\n')

            valid_modelo = False
            while not valid_modelo:
                modelo = input('Insira o modelo do seu carro: ')
                if modelo.isalpha():
                    valid_modelo = True
                else:
                    print('O modelo inserido é inválido!\n')

            valid_ano = False
            while not valid_ano:
                ano = input('Insira o ano do seu carro: ')
                # Caso o valor de ano seja composto por 4 digitos e seja um inteiro, então converta para inteiro
                if ano.isdigit() and len(ano) == 4:
                    ano = int(ano)
                    valid_ano = True
                else:
                    print('O ano que você inseriu é inválido.\n')

            valid_placa = False
            while not valid_placa:
                placa = input('Insira a placa do seu carro: ')
                if len(placa) == 7:
                    valid_placa = True
                else:
                    print('A placa inserida é inválida!\n')

            # Criação do "objeto" veículo
            veiculo = {
                'marca': marca,
                'modelo': modelo,
                'ano': ano,
                'placa': placa,
            }
            # Associação do dicionário veículo ao dicionário usuário
            usuario['veiculos'].append(veiculo)

            print('Por favor, selecione uma das operações abaixo:')
            print('1 - Adicionar outro veículo')
            print('2 - Sair')
            opcao_selecionada = input(
                'Digite o número da operação desejada: ')

            print(
                "=====================================================================\n")

            if opcao_selecionada == '2':
                fim_cadastro_veiculo = True

    # Caso o usuario não esteja cadastrado, não é possível cadastrar um veículo.
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
                cont = 1
                # Exibindo a chave com a primeira letra maiúscula.
                print(f'{chave.capitalize()}: ')
                for veiculo in valor:
                    print("Veiculo" + cont)
                    # Para cada chave e valor dentro do dicionário (neste caso, o value
                    # do loop anterior), exibir o valor.
                    for key, value in veiculo.items():
                        print(f'\t{key.capitalize()}: {value}')

                    print(
                        "=====================================================================\n")
                    cont += 1
            else:
                print(f'{chave.capitalize()}: {valor}')

        print('Cadastro exibido com sucesso\n\n')
    else:
        print('Você não está cadastrado no sistema, volte ao cadastro de usuário.\n')
