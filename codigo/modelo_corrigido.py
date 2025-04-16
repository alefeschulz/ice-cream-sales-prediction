# Importar bibliotecas necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Carregar os dados
df = pd.read_csv('dados_exemplo.csv')  # Certifique-se de que o arquivo está no diretório correto

# Exibir as primeiras linhas do DataFrame para confirmação
print("Visualizando os dados:")
print(df.head())

# Preparar os dados
X = df[["Temperatura Média (°C)"]]  # Nome correto da coluna
y = df["Vendas (R$ mil)"]  # Saída alvo

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de Regressão Linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões com o conjunto de teste
predictions = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, predictions)
print("\nErro Quadrático Médio (MSE):", mse)

# Exibir as previsões feitas pelo modelo
print("\nPrevisões do conjunto de teste:")
print(predictions)

# Prever vendas para novas temperaturas
nova_temperatura = pd.DataFrame({"Temperatura Média (°C)": [35, 20, 25]})
previsoes_novas = model.predict(nova_temperatura)
print("\nPrevisões para novas temperaturas (35°C, 20°C, 25°C):")
print(previsoes_novas)
