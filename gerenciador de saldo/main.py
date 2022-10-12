import time
# import pandas

# planilha = pandas.read_excel('saldo.xlsx', engine='openpyxl')

opc = [
    'add ganhos','add gastos','add dividas','ver planilha']
banco 
def menu():
    cont = 1
    for i in opc:
        print(f'\033[33m {cont} \033[m - \033[34m {i} \033[m ')
        cont += 1
    escolha = int(input("qual a sua escolha :"))
    if escolha == 1:
        print('voce escoheu add ganhos')
    elif escolha == 2:
        print('voce esclheu add gastos ')
    elif escolha == 3:
        print('voce escolheu add diividas')
    elif escolha == 4:
        # print(planilha)
        time.sleep(1)
        menu()
    else:
        print('nao foi possivel entender a sua resposta tente novamente')
        menu()
menu()

