
# Bibliotecas usadas na análise:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados do arquivo CSV
dados = pd.read_csv('https://raw.githubusercontent.com/GrupoProjetoAplicado/Projeto/main/Data/vaccination-data.csv')

# Métodos para explorar os dados
# Exibe as primeiras linhas do arquivo
print(dados.head())

# Exibe o número de linhas e colunas (e contagem de valores não nulos), o tipo de dado e a quantidade de memória usada
print(dados.info())

# Exibe contagem de valores não nulos, média, desvio padrão, valor mínimo, quartis e valor máximo
print(dados.describe())