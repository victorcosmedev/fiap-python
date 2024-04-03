while True:
    num = input("Digite um número: ")

    if num.isdigit():
        num = int(num)
        break
    else:
        print("Número inválido.\n")

multi = 0
for i in range(1, 11):
    multi = num * i
    print(f"Tabuada do {num}: ")
    print(f"{num} x {i} = {multi}")
