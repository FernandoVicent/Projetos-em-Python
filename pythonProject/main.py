nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
data_nascimento = input('Digite sua data de nascimento: ')

def cria_user():

    senha = input('Digite uma senha: ')

    if nome in senha or sobrenome in senha:
        print('Sua senha não pode conter seus dados pessoais')
        cria_user()

    elif data_nascimento in senha:
        print('Sua senha não pode conter seus dados pessoais')
        cria_user()

    else:
        print('Usuário criado')

cria_user()