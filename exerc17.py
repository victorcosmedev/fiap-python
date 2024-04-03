num_valido = False


while not num_valido:
    num = input('Digite o número: ')

    if num.replace('-', '').isdigit():
        num = int(num)
        num_valido = True
    else:
        print('Algo deu errado.\n')

fatorial = num
for num in range(1, num):
    fatorial *= num
    print(f'{num=} {fatorial=}')
