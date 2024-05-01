def define_digito(soma):
    resto_divisao = soma % 11
    if resto_divisao == 0 or resto_divisao == 1:
        return 0
    else:
        digito = 11 - resto_divisao
        return digito


def calcula_cpf(cpf_sem_digitos):
    soma = 0
    fator_cpf = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    for digito, multiplicador in zip(cpf_sem_digitos, fator_cpf):
        soma += digito * multiplicador

    digito = define_digito(soma)
    cpf_com_digitos.append(digito)

    soma = 0
    for digito, multiplicador in zip(cpf_com_digitos[1:], fator_cpf):
        soma += digito * multiplicador

    digito = define_digito(soma)
    cpf_com_digitos.append(digito)

    return cpf_com_digitos


cpf_inserido = "34487846803"
cpf_inserido = list(cpf_inserido)
cpf_inserido = [int(i) for i in cpf_inserido]


cpf_inserido_sem_digitos = cpf_inserido[:-2]
print(cpf_inserido_sem_digitos)
cpf_sem_digitos = [2, 8, 0, 0, 1, 2, 3, 8, 9]
fator_cpf = [10, 9, 8, 7, 6, 5, 4, 3, 2]
cpf_com_digitos = cpf_sem_digitos


print(calcula_cpf(cpf_sem_digitos, fator_cpf))
