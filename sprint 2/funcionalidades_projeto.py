from funcoes import *

cria_titulo('REPAROS - PORTO SEGURO')
print('Olá, usuário! Bem vindo ao sistema de reparos da Porto Seguro!\n')

# Atribuindo False para o usuário, já que ele só será verdadeiro após o cadastro do usuário
usuario = False
fim = False
while not fim:
    # Atribuindo para a variável opcao_selecionada a opção definida na função selecionar_operacao
    opcao_selecionada = selecionar_operacao()

    # Cadastrar novo cliente
    if opcao_selecionada == '1':
        # Cadastrar novo veículo
        usuario = cria_cadastro()
        print(usuario)

        print('Pronto, você foi cadastrado com sucesso!\n')

    elif opcao_selecionada == '2':
        cadastra_veiculo(usuario)

    elif opcao_selecionada == '3':
        visualizar_cadastro(usuario)
    else:
        fim = True
        print('\nAtendimento finalizado com sucesso!')
