def notas_a_serem_usadas(notas):
    notas = list(notas)
    menor_nota = min(notas)
    notas.remove(menor_nota)

    return notas

def media_semestral():
    cp1 *= 0.1
    cp2 *= 0.1
    ch1 *= 0.1
    ch2 *= 0.1
    gs *= 0.6

    media_semestral = cp1 + cp2 + ch1 + ch2 + gs
    return media_semestral

boletim_anual = (
    {
        'cp1': 8.0,
        'cp2': 9.0,
        'cp3': 10.0,
        'ch1': 5.0,
        'ch2': 7.5,
        'gs': 10.0,
    },
    {
        'cp1': 5.0,
        'cp2': 10.0,
        'cp3': 7.0,
        'ch1': 4.0,
        'ch2': 4.5,
        'gs': 8.0,
    }
)


def media_anual(*notas):
    medias = []
    notas_cp = []
    notas_ch = []

    for boletim in boletim_anual:
        for chave, valor in boletim.items():

            if chave[:2] == 'cp':
                notas_cp.append(valor)
            elif chave[:2] == 'ch':
                notas_ch.append(valor)
            else:
                gs = valor

            notas_cp = notas_a_serem_usadas(notas_cp)
            notas_ch = []

media_anual(boletim_anual)



