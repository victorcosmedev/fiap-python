import json

with open('file.json', mode='r', encoding='UTF-8') as file:
    content = file.read()


print(content)
print(type(content))
