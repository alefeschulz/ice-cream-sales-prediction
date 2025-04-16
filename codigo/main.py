import pandas as pd

# Criando os dados simulados
dados = {
    "Mês": [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio",
        "Junho", "Julho", "Agosto", "Setembro", "Outubro",
        "Novembro", "Dezembro"
    ],
    "Temperatura Média (°C)": [30, 31, 28, 25, 22, 18, 17, 20, 23, 26, 28, 29],
    "Vendas (R$ mil)": [120, 110, 95, 80, 75, 60, 55, 65, 85, 100, 115, 130]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Salvando os dados em um arquivo CSV
df.to_csv("dados_exemplo.csv", index=False)

print("Dados de exemplo criados e salvos no arquivo dados_exemplo.csv!")
