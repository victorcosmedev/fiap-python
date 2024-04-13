valid_nome = False

while not valid_nome: 
    nome = input("Olá! Digite o seu nome: ")

    if len(nome) <= 3:
        print("Nome muito curto. \n\n")
        continue
    else:
        valid_nome = True


valid_idade = False
while not valid_idade:
    idade = input("\nQual a sua idade? ")

    if idade.isdigit():
        idade = int(idade)

        if idade < 0 or idade > 150:
            print("Idade inválida. Insira novamente. \n\n")
        else: 
            valid_idade = True
    else:
        print("O valor que você inseriu não é um número. \n\n")

valid_salario = False

while not valid_salario: 
    salario = input("\nQual seu salário? ")

    if salario.isdigit():
        salario = int(salario)

        if salario < 0:
            print("O salário que você inseriu é inválido")
        else:
            valid_salario = True
    else: 
        print("O valor que você inseriu não é um número. \n\n")

valid_sexo = False
while not valid_sexo:
    sexo = input("Qual seu sexo? ")
    set_sexo = {'m', 'f'}

    if sexo.lower() not in set_sexo:
        print("Insira 'f' ou 'm'.\n")
    else: 
        valid_sexo = True

valid_civil = False
while not valid_civil:
    civil = input("Insira seu estado civil: ")
    set_civil = {'s', 'c', 'v', 'd'}

    if civil.lower() not in set_civil:
        print("Insira 's', 'c', 'v' ou 'd'")
    else:
        valid_civil = True

print(nome)
print(idade)
print(salario)
print(sexo)
print(civil)

    
