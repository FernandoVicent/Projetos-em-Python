
while True:
    try:
        pergunta = int(input('digite um numero'))
        print(f'o numero que vc digitou foi: {pergunta}')
        break
    except ValueError:
        print('valor digitado invalido')