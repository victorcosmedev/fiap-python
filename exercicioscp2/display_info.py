user = {
    'name': 'Victor',
    'age': 19,
    'email': 'victor.cosme@fiesp.com.br',
    'occupation': 'intern'
}


def display_info(**user):
    print("USER INFO")
    for key, value in user.items():
        print(f'{key.upper()}: {value}')


print(display_info(**user))
