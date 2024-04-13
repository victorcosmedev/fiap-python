# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# n = 10

# penultimo = 0
# ultimo = 1

# for i in range(n):
#     print(f'{i}: {ultimo}')
#     proximo = penultimo + ultimo

#     penultimo = ultimo
#     ultimo = proximo


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

n = 10

fibonacci = [1, 1]

for i in range(n - len(fibonacci)):

    proximo = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(proximo)

    print(f'{i}: {fibonacci}')

print(fibonacci)


# n = 10

# fibonacci = [1, 1]

# for i in range(n - len(fibonacci)):

#     # penultimo recebe o valor de ultimo e ultimo recebe a soma de penultimo + ultimo
#     penultimo, ultimo = ultimo, penultimo + ultimo
