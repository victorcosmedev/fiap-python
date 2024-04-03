populacao_a = 80000
populacao_b = 200000

taxa_a = 1.03
taxa_b = 1.015

anos = 0

# while usado porque não se sabe quantas vezes o loop será repetido
while populacao_a < populacao_b:
    populacao_a = int(populacao_a * taxa_a)
    populacao_b = int(populacao_b * taxa_b)

    print(populacao_a, populacao_b)

    anos += 1

print(f'A populacao do pais A devera superar a do pais B em {anos} anos')
