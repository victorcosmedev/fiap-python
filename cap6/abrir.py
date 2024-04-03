with open('file.txt', mode='r', encoding='UTF-8') as file:
    # read a single line
    conteudo1 = file.readline()
    # list where each line of the text is an item of the list
    conteudo2 = file.readlines()
    conteudo3 = file.read().splitlines()

print(conteudo1)
print(conteudo2)
print(conteudo3)
