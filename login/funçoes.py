def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (valueError, typeError):
            print('\033[31mERRO: por favor, Digite um opção valida.\033[m')
            continue
        except (keyboardInterrupt):
            print('\n\033[32mUsuario preferiu nao digitat uma opção. \033[m')
            return 0
        else:
            return n

def linhas (tam = 42):
    return '_' * tam


def cabecalho(txt):
    print(linhas())
    print(txt.center(42))
    print(linhas())


def Menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f'\033[33m {c} \033[m - \033[34m{item}\033[m')
        c +=1
    print(linhas())
    opc = LeiaInt('\033[32mSua opção : \033[m ')
    return opc

