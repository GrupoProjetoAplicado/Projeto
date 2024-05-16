# Calcular a média de novos casos por país
media_novos_casos = dados_csv.groupby('Country')['New_cases'].mean().sort_values(ascending=False)

# Visualizar os países com maior carga da doença
plt.figure(figsize=(10, 6))
media_novos_casos.head(10).plot(kind='bar', color='salmon')
plt.title('Média de Novos Casos de COVID-19 por País')
plt.xlabel('País')
plt.ylabel('Média de Novos Casos')
plt.show()


# Calcular o coeficiente de variação (CV) dos casos por país
coef_variacao = dados_csv.groupby('Country')['New_cases'].std() / dados_csv.groupby('Country')['New_cases'].mean()

# Visualizar os países com maiores disparidades
plt.figure(figsize=(10, 6))
coef_variacao.sort_values(ascending=False).head(10).plot(kind='bar')
plt.title('Coeficiente de Variação dos Casos de COVID-19 por País')
plt.xlabel('País')
plt.ylabel('Coeficiente de Variação')
plt.show()


# Converter a coluna 'date_reported' para formato de data
dados_csv['Date_reported'] = pd.to_datetime(dados_csv['Date_reported'])

# Calcular a média móvel dos casos cumulativos para suavizar os dados e identificar tendências
window_size = 7  # tamanho da janela da média móvel
dados_csv['moving_average'] = dados_csv['Cumulative_cases'].rolling(window=window_size).mean()

# Plotar os casos cumulativos e a média móvel
plt.figure(figsize=(10, 6))
plt.plot(dados_csv['Date_reported'], dados_csv['Cumulative_cases'], label='Casos Cumulativos', color='blue', alpha=0.5)
plt.plot(dados_csv['Date_reported'], dados_csv['moving_average'], label=f'Média Móvel ({window_size} dias)', color='red')
plt.title('Tendência Temporal de Casos Cumulativos de COVID-19')
plt.xlabel('Data')
plt.ylabel('Casos Cumulativos')
plt.legend()
plt.grid(True)
plt.show()