# Relatório de Análise 1

import pandas as pd

from pandas import read_excel

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pd.DataFrame(mydataset)
#
# print(myvar)

dados = pd.read_csv('aluguel.csv', sep=';')
print(dados)
print(dados.Tipo)
#
# #print(dados.head())
#
#tipos = pd.DataFrame(dados.dtypes, columns= ['Tipos de dados'])
#print(tipos)

#df_csv = pd.read_csv('atendimento.csv')

#print(df_csv)