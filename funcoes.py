x = 10

# def funcao(): -> assinatura da funcao

# def mensagem_padrao():
#    print('ola, mundo!')

# mensagem_padrao()

def mensagem_customizada(nome):
    print(f'Ola, {nome}!')


nome_input = 'teste'
mensagem_customizada(nome_input)

def mensagem_customizada2(nome, idade):
    print(f'Ola, {nome}!\nVoce tem {idade} anos?')

mensagem_customizada2('vasco', 25)
mensagem_customizada2(idade=45, nome='Vagner')


def parametro_default(param_1=3, param_2=10, param_3=3.14):
    print(f'{param_1}... {param_2}... {param_3}...')

# valor do param_3 é 3.14
parametro_default(1, 2)

# valor do param_3 é 5.0
parametro_default(param_3=5.0)

def calcular(valor_1, valor_2):
    return valor_1 ** valor_2 

print(calcular(2, 3))

y = mensagem_customizada('Victor')

print(y, y is None, sep=', ')

def divisao_inteira(dividendo, divisor):

    valor = dividendo // divisor
    resto = dividendo % divisor 

    return valor, resto

print(type(divisao_inteira(10, 3)))
print(divisao_inteira(10, 3))

a = divisao_inteira(10, 7)
print(a[1])

b, c = divisao_inteira(15, 2)
print(b)
