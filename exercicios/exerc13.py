while True:
    base = input("Digite a base da exponenciacao: ")
    expoente = input("Digite o expoente: ")

    if base.isdigit() and expoente.isdigit():
        base = int(base)
        expoente = int(expoente)
        break

    print("Algo deu errado.\n")

exponenciacao = 1
for i in range(1, expoente + 1):
    exponenciacao *= base

print(f'{exponenciacao=}')
