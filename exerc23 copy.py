num_valido = False

while not num_valido:
    num = input('Digite um número: ')

    if num.isdigit():
        num = int(num)
        num_valido = True
    else:
        print('Algo deu errado. Tente novamente!')

# for i in range(1, num + 1):
#     contador = 0
#     lista_divisores = []

#     for x in range(1, i + 1):
#         if i % x == 0:
#             contador += 1
#             lista_divisores.append(x)

#     if contador == 2:
#         print(
#             f'\n{i} é um número primo, pois ele foi dividido por {contador} vezes.')
#     else:
#         print(
#             f'\n{i} não é primo, pois foi dividido {contador} vezes e seus divisores são: ')
#         print(*lista_divisores, sep='\n')

for dividendo in range(1, num + 1):
    primo = True
    divisor_max = 1

    # se o número for maior que 2 e é par, logo ele não é primo, pois o único número primo par é 2
    if dividendo > 2 and (dividendo % 2 == 0):
        primo = False

    else:
        divisor = 2
        while primo and divisor < dividendo:

            resto = dividendo % divisor
            divisor_max = divisor
            resultado = dividendo // divisor

            print(
                f'Divisor:  {divisor} - Resultado: {resultado} - Resto {resto}')

            if resto == 0 and divisor != 1 and dividendo != divisor:
                primo = False

            divisor += 1

    if primo:
        print(f'{dividendo} é primo!')
    else:
        print(f'{dividendo} não é primo')

    print(f'Qtde de divisões: {divisor_max - 1}\n')
