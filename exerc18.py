conjunto = {1, 2, 3, 5, 10, 15, 25, 300}
menor_numero = 10000000000000

for item in conjunto:
    if item < menor_numero:
        menor_numero = item

print(menor_numero)
