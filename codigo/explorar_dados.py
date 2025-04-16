import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv("dados_exemplo.csv")
print("Exibindo os primeiros dados:")
print(df.head())  # Exibir as primeiras linhas

# Adicionar alguma análise simples
media_vendas = df["Vendas (R$ mil)"].mean()
print(f"Média de vendas: {media_vendas:.2f} R$ mil")
