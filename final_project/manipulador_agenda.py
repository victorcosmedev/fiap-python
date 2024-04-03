contatos_suportados = ('telefone', 'email', 'endereco')

agenda = {
    'Pessoa 1': {
        'telefone': ['11 1234-5678'],
        'email': ['pessoa@email.com', 'email@profissional.com'],
        'endereco': ['rua 123']
    },
    'Pessoa 2': {
        'telefone': ['11 9874-5678'],
        'email': ['pessoa2@email.com', 'pessoa2@profissional.com'],
        'endereco': ['rua 456'],
    }
}

# exibição de todos os contatos de uma pessoa


def contato_para_texto(nome_contato: str, **formas_contato):
    formato_texto = f'{nome_contato}'
    for meio_de_contato, contato in formas_contato.items():
        formato_texto = f'{formato_texto}\n{meio_de_contato.upper()}'
        contador_formas = 1
        for valor in contato:
            formato_texto = f'{formato_texto}\n\t{contador_formas} - {valor.upper()}'
            contador_formas += 1

    return formato_texto


# print(contato_para_texto('Pessoa 2', **agenda['Pessoa 2']))

def exibir_agenda(**agenda_completa):
    formato_texto = ''
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f'{formato_texto} {contato_para_texto(nome_contato, **formas_contato)}\n'
        formato_texto = f'{formato_texto}'

    return formato_texto


print(exibir_agenda(**agenda))
