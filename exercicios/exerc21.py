num_valido = False

while not num_valido:
    num = input('Insira um número: ')

    if num.replace('-', '').isdigit() and int(num) > 0:
        num = int(num)
        num_valido = True
    else:
        print('Numero invalido.\n')

contador = 0
for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

if contador == 2:
    print('Numero primo.')
else:
    print('O numero nao e primo')
