valid_numero = False
maior_numero = 0
for i in range(5):
    while not valid_numero:
        numero = input("Olá! Digite um número: ")
        if numero.isdigit():
            numero = int(numero)
            valid_numero = True
        else:
            print("Você digitou algo errado.\n")
    valid_numero = False

    if numero > maior_numero:
        maior_numero = numero

print(f"Maior número: {numero}")
