import random


def calcular_digito(cpf_base):
    soma_dv = 0
    multiplicador = [10, 9, 8, 7, 6, 5, 4, 3, 2]  # range(10, 1, -1)
    for i, j in zip(cpf_base, multiplicador):  # range(10, 1, -1)
        soma_dv += int(i) * j

    resto_dv = soma_dv % 11
    dv = 0 if resto_dv in [0, 1] else 11 - resto_dv
    return str(dv)


def validar_cpf(cpf):
    cpf_base = cpf[:9]

    dv1 = calcular_digito(cpf_base)
    cpf_base += dv1

    dv2 = calcular_digito(cpf_base[1:])
    cpf_base += dv2

    return cpf == cpf_base


def gerar_cpf(uf=None):
    cpf_base = ''

    cadastro_uf = {
        'DF': '1',
        'AC': '2',
        'CE': '3',
        'AL': '4',
        'BA': '5',
        'MG': '6',
        'ES': '7',
        'SP': '8',
        'PR': '9',
        'RS': '0',
    }

    digitos = 8 if uf else 9
    for i in range(digitos):
        cpf_base += str(random.randint(0, 9))

    if uf:
        cpf_base += cadastro_uf[uf.upper()]

    dv1 = calcular_digito(cpf_base)
    cpf_base += dv1

    dv2 = calcular_digito(cpf_base[1:])
    cpf_base += dv2

    return cpf_base


cpf = gerar_cpf('RS')
print(cpf, validar_cpf(cpf))
