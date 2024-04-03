from getpass import getpass

# Nome
valor_correto = False

while not valor_correto:
    nome = input('Informe um nome: ')

    if len(nome) >= 3:
        valor_correto = True
    else:
        print('O nome deve ter mais do que 3 letras!\n')


# Idade
valor_correto = False

while not valor_correto:
    idade = input('Informe a idade: ')

    if idade.isdigit() and int(idade) >= 0 and int(idade) <= 150:
        valor_correto = True
    else:
        print('A idade deve estar entre 0 e 150 anos!\n')

# Salario
valor_correto = False

while not valor_correto:
    salario = input('Informe o salário: ')

    # replace troca o '-' do '-1' por nulo
    if salario.replace('-', '').isdigit() and int(salario) > 0:
        valor_correto = True
    else:
        print('O salário deve ser maior que zero!\n')

valor_correto = False

while not valor_correto:
    sexo = input('Informe o sexo: ')

    if sexo.lower() in ['m', 'f']:
        valor_correto = True
    else:
        print('Informe o sexo utilizando as opções: M, F \n')

valor_correto = False

while not valor_correto:
    estado_civil = input('Informe o estado civil: ')

    if estado_civil.lower() in ['s', 'c', 'v', 'd']:
        valor_correto = True
    else:
        print('Informe o estado civil utilizando as opções: S, C, V ou D \n')
