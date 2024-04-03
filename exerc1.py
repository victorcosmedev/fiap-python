valid_nota = False

while not valid_nota:

    nota = input("Digite uma nota: ")

    if nota.isdigit():
        nota = int(nota)
        print(type(nota))

        if nota < 0 or nota > 10:
            print("O valor que você inseriu está incorreto.")
        else: 
            print("Nota registrada com sucesso.")
            valid_nota = True
    else: 
        print("O valor que você inseriu não é um número.\n\n")