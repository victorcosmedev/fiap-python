media = 0
soma = 0

for i in range(5):

    while True:
        num = input("Digite um número: ")

        if num.isdigit():
            num = int(num)
            break

        print("O valor que você digitou não é um numero.\n")

    soma += num

media = soma / 5

print(f'{media=} \n{soma=}')
