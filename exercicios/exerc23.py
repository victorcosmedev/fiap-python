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

for i in range(1, num + 1):
    primo = True
    j_max = 0

    # se o número for maior que 2 e é par, logo ele não é primo, pois o único número primo par é 2
    if i > 2 and (i % 2 == 0):
        primo = False

    else:

        for j in range(2, i):

            resto = i % j
            j_max = j

            if resto == 0 and j != 1 and i != j:
                primo = False
                break

    if primo:
        print(f'{i} é primo!')
    else:
        print(f'{i} não é primo')

    print(f'Qtde de divisões: {j_max}\n')
