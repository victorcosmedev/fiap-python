def notas_a_serem_usadas(*notas):
    notas = list(notas)
    menor_nota = min(notas)
    notas.remove(menor_nota)

    return notas

def media_anual(
    cp11, cp21, cp31, sp1, sp2, gs1,
    cp12, cp22, cp32, sp3, sp4, gs2):
    
    cp1 = notas_a_serem_usadas(cp11, cp21, cp32)
    cp2 = notas_a_serem_usadas(cp12, cp22, cp32)

    s1 = cp1[0] * .1 + cp1[1] * .1 + sp1 * .1 + sp2 * .1 + gs1 * .6
    s2 = cp2[0] * .1 + cp2[1] * .1 + sp3 * .1 + sp4 * .1 + gs2 * .6

    return s1 * .4 + s2 * .6