# ice-cream-sales-prediction
Projeto de Machine Learning para prever vendas de sorvete com base na temperatura.

# Previsão de Vendas de Sorvete com Machine Learning 🍦📊

## Introdução

Este projeto tem como objetivo desenvolver um modelo de regressão preditiva para estimar as vendas diárias de sorvete com base na temperatura ambiente. A ideia surgiu da observação de que a demanda por sorvetes na sorveteria "ice-cream", localizada em uma cidade litorânea, está fortemente correlacionada com a temperatura. Ao construir um modelo de Machine Learning, buscamos fornecer uma ferramenta que auxilie o proprietário a otimizar a produção, reduzir desperdícios e maximizar os lucros através de um planejamento mais eficiente.

## Cenário

Imagine-se como o proprietário da "ice-cream". Você percebe uma clara ligação entre os dias quentes e o aumento nas vendas de sorvete. No entanto, sem uma análise precisa, fica difícil prever a quantidade ideal a ser produzida. Produzir demais pode levar a perdas com produtos estragados, enquanto produzir de menos resulta em perda de vendas e clientes insatisfeitos. A solução proposta é utilizar Machine Learning para criar um modelo que preveja as vendas com base na temperatura, permitindo um planejamento de produção mais inteligente.

## Objetivos

Este projeto visa atingir os seguintes objetivos:

✅ **Treinar um modelo de Machine Learning:** Desenvolver um modelo de regressão capaz de aprender a relação entre a temperatura do dia e as vendas de sorvete.
✅ **Registrar e gerenciar o modelo usando o MLflow:** Utilizar o MLflow para rastrear experimentos, salvar o modelo treinado e seus metadados, facilitando a gestão e a reprodução.
✅ **Implementar o modelo para previsões em tempo real (Conceitual):** Explorar a possibilidade de implementar o modelo em um ambiente de cloud computing para realizar previsões sob demanda através de uma API.
✅ **Criar um pipeline estruturado:** Definir um fluxo de trabalho para o treinamento e teste do modelo, garantindo a reprodutibilidade dos resultados.

## Metodologia

Embora este README descreva um projeto conceitual (já que não foram fornecidos dados específicos), a metodologia para um projeto real envolveria as seguintes etapas:

1.  **Coleta e Preparação dos Dados:**
    * Coletar dados históricos de vendas diárias de sorvete e as temperaturas correspondentes. Idealmente, esses dados abrangeriam um período significativo para capturar variações sazonais e outras tendências.
    * Realizar a limpeza dos dados, tratando valores ausentes, identificando e (se necessário) removendo outliers.
    * Preparar os dados para o treinamento do modelo, dividindo-os em conjuntos de treinamento e teste.

2.  **Análise Exploratória de Dados (EDA):**
    * Visualizar os dados para entender a relação entre a temperatura e as vendas (por exemplo, usando gráficos de dispersão).
    * Calcular estatísticas descritivas e a correlação entre as variáveis para quantificar a força e a direção da relação.

3.  **Seleção do Modelo:**
    * Considerando a natureza do problema (previsão de um valor contínuo), um modelo de regressão linear simples seria um bom ponto de partida devido à sua interpretabilidade. Modelos mais complexos (como regressão polinomial, Support Vector Regression ou Random Forest Regression) poderiam ser explorados para capturar relações não lineares, se identificadas na EDA.

4.  **Treinamento do Modelo:**
    * Implementar o modelo escolhido utilizando bibliotecas como scikit-learn em Python.
    * Treinar o modelo utilizando o conjunto de treinamento dos dados.
    * Ajustar os hiperparâmetros do modelo, se necessário, para otimizar seu desempenho.

5.  **Avaliação do Modelo:**
    * Utilizar o conjunto de teste para avaliar o desempenho do modelo em dados não vistos.
    * Calcular métricas de avaliação relevantes para regressão, como:
        * **Erro Médio Quadrático (MSE):** Média dos quadrados das diferenças entre os valores previstos e reais.
        * **Raiz do Erro Médio Quadrático (RMSE):** Raiz quadrada do MSE, fornecendo um erro na mesma unidade das vendas.
        * **Coeficiente de Determinação (R²):** Indica a proporção da variância nos dados dependentes que é previsível a partir das variáveis independentes.

6.  **Registro e Gerenciamento com MLflow:**
    * Integrar o MLflow para rastrear os parâmetros, métricas e artefatos do experimento de treinamento.
    * Registrar o modelo treinado no MLflow Model Registry, permitindo o versionamento e a gestão do ciclo de vida do modelo.

7.  **Implementação em Cloud (Conceitual):**
    * Em um cenário real, o modelo registrado no MLflow poderia ser implantado em uma plataforma de cloud computing (como AWS SageMaker, Google Cloud AI Platform ou Azure Machine Learning).
    * Criar uma API para receber dados de temperatura em tempo real e retornar a previsão de vendas correspondente.

8.  **Criação do Pipeline:**
    * Estruturar o código em um pipeline para automatizar as etapas de carregamento, preparação, treinamento e avaliação do modelo. Isso garante a reprodutibilidade e facilita a atualização do modelo com novos dados. Ferramentas como scikit-learn `Pipeline` ou frameworks mais robustos como Kedro poderiam ser utilizadas.

## Análise das Sentenças (Arquivo `inputs/sentencas.txt`)