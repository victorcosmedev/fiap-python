while True:
    populacao_a = input("Insira a população A: ")
    populacao_b = input("Insira a população B:")

    if not populacao_a.isdigit() or not populacao_b.isdigit():
        print("O valor que você inseriu não é um número.\n")
        continue

    populacao_a = int(populacao_a)
    populacao_b = int(populacao_b)
    break

quant_anos = 1
while populacao_a < populacao_b:
    populacao_a *= 1.03
    populacao_b *= 1.015

    print(f'\nANO {quant_anos}')
    print(f'Populacaoo A: {populacao_a:.0f} pessoas')
    print(f'Populacao B: {populacao_b:.0f} pessoas\n')
    quant_anos += 1
