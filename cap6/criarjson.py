import json

dicio = {
    'nome': 'Victor',
    'idade': 19
}

# dump a string (dicio) into a json
content = (json.dumps(dicio, indent=4))

with open('file.json', mode='w', encoding='UTF-8') as file:
    file.write(content)
