valid_senha = False

while not valid_senha:
    nome = input("Digite o seu nome: ")
    senha = input("Digite sua senha: ")

    if nome == senha:
        print("Sua senha não pode ser igual ao seu nome. Insira novamente. \n\n")
    else:
        print("Usuário cadastrado com sucesso.")
        valid_senha = True

print("fim")