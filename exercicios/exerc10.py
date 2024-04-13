while True:
    num1 = input("Digite um número: ")
    num2 = input("Digite um número: ")

    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        break

    print("Um dos valores que você inseriu não é um número.\n")

if num1 > num2:
    maior_numero = num1
    menor_numero = num2
else:
    maior_numero = num2
    menor_numero = num1

for i in range(menor_numero + 1, maior_numero):
    print(i)
