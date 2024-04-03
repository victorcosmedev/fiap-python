limite = 500

fib = [1, 1]
checagem = 0
while checagem <= limite:
    proximo_num = fib[-1] + fib[-2]
    fib.append(proximo_num)

    checagem = fib[-1] + fib[-2]

print(fib)
