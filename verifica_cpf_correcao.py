cpf = '35249903045'


def calcular_digito(cpf_base):
    soma_dv = cpf_base[0] * 10 + cpf_base[1] * \
        9 + cpf_base[2] * 8 + cpf_base[3] * 7 + \
        cpf_base[4] * 6 + cpf_base[5] * 5 + \
        cpf_base[6] * 4 + cpf_base[7] * 3 + cpf_base[8] * 2

    resto_dv = soma_dv % 11
    dv = 0 if resto_dv in [0, 1] else 11 - resto_dv
    return dv


def transforma_em_lista_inteiros(cpf):
    cpf = list(cpf)
    cpf = [int(i) for i in cpf]
    return cpf


def validar_cpf(cpf):
    cpf_base = cpf[:9]
    cpf_base = transforma_em_lista_inteiros(cpf_base)
    cpf_base = cpf[:9]

    dv1 = calcular_digito(cpf_base)
    cpf_base.append(dv1)

    dv2 = calcular_digito(cpf_base[1:])
    cpf_base.append(dv2)

    cpf = transforma_em_lista_inteiros(cpf)

    return cpf == cpf_base


print(validar_cpf('35249903045'))
