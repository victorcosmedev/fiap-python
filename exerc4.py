populacao_a = 80000
populacao_b = 200000

quant_anos = 1
while populacao_a < populacao_b:
    populacao_a *= 1.03
    populacao_b *= 1.015

    print(f'ANO {quant_anos}')
    print(f'Populacaoo A: {populacao_a:.0f} pessoas')
    print(f'Populacao B: {populacao_b:.0f} pessoas\n')
    quant_anos += 1
