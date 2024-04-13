def soma(mult=1, *args):
    x = 0
    for i in args:
        x += i

    return x * mult

print(soma(5, 1, 2, 3, 4, 5, 6))

def cadastro(**kwargs):
    for k, v in kwargs.items():
        print(f'Atributo: {k} - valor: {v}')

usuario = {
    'nome': 'palmeiras',
    'idade': 110,
    'tamanho': 'maior de todos'
}

# cadastro(nome='Victor', idade=19, altura=1.7, peso=65.0, usuario_python=True)
cadastro(**usuario)

def funcao_principal(projeto, pi=3.14, *args, **kwargs):
    print(f'Nome do projeto: {projeto}')
    print(f'Valor de PI: {pi}')

    for i in args:
        print(i)
    
    for k, v in kwargs.items():
        print(f'{k} - {v}')