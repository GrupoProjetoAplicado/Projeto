
# Bibliotecas usadas na análise:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados do arquivo CSV
dados = pd.read_csv('https://raw.githubusercontent.com/GrupoProjetoAplicado/Projeto/main/Data/vaccination-data.csv')

# Métodos para explorar os dados
print(dados.head())

print(dados.info())

print(dados.describe())