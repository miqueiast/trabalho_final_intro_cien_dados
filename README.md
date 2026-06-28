# 🛒 Projeto Final - Previsão de Vendas em Supermercado

**Aluno:** Miqueias Teixeira  
**Disciplina:** INTRODUÇÃO A CIÊNCIA DE DADOS (EAD)

---

## Descrição do Projeto

Este projeto desenvolvido uma solução de Machine Learning para prever o valor total de vendas em um supermercado. O objetivo é criar um modelo que, baseado em características da compra (quantidade de itens, tipo de produto, avaliação do cliente, etc), consiga fazer previsões precisas sobre o valor final.

O projeto é estruturado em três componentes principais:

1. **Análise e Treinamento (Notebook)** - Processamento de dados e desenvolvimento do modelo
2. **Modelo Treinado** - Arquivo contendo o modelo salvo para reutilização
3. **Interface de Usuário (Streamlit)** - Aplicação para fazer previsões

---

## Dataset

O dataset utilizado é o "Supermarket Sales", disponível na plataforma Kaggle:
https://www.kaggle.com/datasets/markmedhat/supermarket-sales

**Características do Dataset:**
- Total de registros: 1.000 vendas
- Variáveis disponíveis: Quantidade de itens, preço unitário, tipo de produto, forma de pagamento, data, avaliação do cliente
- Variável alvo: Valor total da venda

---

## Requisitos e Instalação

### Dependências

Certifique-se de ter Python 3.8 ou superior instalado. Instale as bibliotecas necessárias executando:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

As bibliotecas utilizadas são:
- **pandas**: Manipulação e análise de dados
- **numpy**: Operações numéricas
- **matplotlib e seaborn**: Visualização de dados
- **scikit-learn**: Modelos de Machine Learning
- **streamlit**: Framework para construção da interface

---

## Estrutura do Projeto

```
projeto/
├── notebook.ipynb                 # Análise e treinamento do modelo
├── app.py                         # Aplicação Streamlit
├── README.md                      # Este arquivo
└── dados/
    ├── supermarket_sales.csv      # Dataset (download necessário)
    ├── modelo_venda.pkl           # Modelo treinado (gerado)
    └── colunas_modelo.pkl         # Metadados das colunas (gerado)
```

---

## Como Executar

### Passo 1: Preparação dos Dados

1. Faça o download do arquivo `supermarket_sales.csv` no Kaggle
2. Crie uma pasta chamada `dados` no diretório do projeto
3. Coloque o arquivo CSV dentro desta pasta

### Passo 2: Treinar o Modelo

Abra o notebook em Jupyter ou Google Colab:

```bash
jupyter notebook notebook.ipynb
```

Execute todas as células do notebook (Ctrl+A, depois Shift+Enter). Este processo:
- Carrega e explora os dados
- Realiza limpeza e transformação de variáveis
- Treina dois modelos diferentes (Random Forest e Regressão Linear)
- Avalia o desempenho de cada modelo
- Salva o melhor modelo em arquivos (.pkl)

Quando o processo terminar, você verá a mensagem: `✅ Modelo treinado com sucesso!`

### Passo 3: Executar a Aplicação

Abra o terminal no diretório do projeto e execute:

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador em `http://localhost:8501`

---

## Utilizando a Aplicação

A interface está dividida em dois painéis:

**Painel Esquerdo - Informações da Compra:**
- Quantidade de itens (seletor de 1 a 10)
- Preço unitário em R$ (campo numérico)
- Avaliação da compra (escala de 0 a 10)

**Painel Direito - Características da Transação:**
- Linha de produto (dropdown com 6 opções)
- Forma de pagamento (dinheiro, cartão, e-wallet)
- Filial (A, B ou C)
- Data da compra (calendário)

Após preencher os dados, clique no botão "🔮 Fazer Previsão" para obter o resultado. A aplicação exibirá:
- O valor total previsto
- O preço médio por item
- Um resumo dos dados inseridos
- Observações importantes sobre a precisão

---

## Tratamento de Erros

### Erro: "Arquivo não encontrado"
**Causa:** O arquivo `supermarket_sales.csv` não está na pasta `dados/`  
**Solução:** Verifique se o arquivo está no local correto e com o nome exato.

### Erro: "Coluna faltante" ou erro na previsão
**Causa:** Os arquivos do modelo (.pkl) estão desatualizados  
**Solução:** Execute novamente o notebook completo para regenerar os arquivos, depois reinicie a aplicação.

### Aviso do scikit-learn
**Causa:** Incompatibilidade de versão entre scikit-learn  
**Solução:** Este é apenas um aviso e não afeta o funcionamento da aplicação. Funciona normalmente.

---

## Metodologia

### Análise Exploratória

O notebook contém uma análise inicial dos dados para compreender:
- Distribuição das variáveis
- Presença de valores faltantes
- Correlações entre variáveis
- Padrões visuais nos dados

### Preparação dos Dados

Os dados passam por transformações necessárias:
- Conversão de datas para extração de features temporais (mês, dia da semana, trimestre)
- Codificação de variáveis categóricas
- Aplicação de one-hot encoding para variáveis nominais
- Remoção de colunas desnecessárias

### Treinamento

Dois modelos são treinados e comparados:

1. **Random Forest** - Modelo de conjunto que captura padrões complexos
2. **Regressão Linear** - Modelo mais simples para comparação

### Avaliação

O desempenho é avaliado usando as seguintes métricas:
- **R²** (Coeficiente de Determinação) - Proporção da variância explicada
- **MAE** (Mean Absolute Error) - Erro médio absoluto em reais
- **RMSE** (Root Mean Squared Error) - Raiz do erro quadrático médio

---

## Estrutura do Notebook

O notebook está organizado nas seguintes seções:

1. **Importações** - Bibliotecas necessárias
2. **Carregamento dos Dados** - Leitura do CSV
3. **Exploração Inicial** - Análise exploratória dos dados
4. **Limpeza de Dados** - Tratamento de valores ausentes e conversões
5. **Visualizações** - Gráficos para compreensão dos padrões
6. **Preparação para Modelagem** - Feature engineering e split train/test
7. **Treinamento dos Modelos** - Desenvolvimento de RandomForest e Regressão Linear
8. **Avaliação** - Comparação de desempenho
9. **Salvamento** - Armazenamento dos modelos em arquivos

Cada seção contém comentários explicativos sobre as operações realizadas.

---

## Aplicação Streamlit

O arquivo `app.py` implementa a interface de usuário e realiza as seguintes operações:

1. **Carregamento do Modelo** - Lê os arquivos .pkl salvos
2. **Interface de Entrada** - Coleta dados do usuário
3. **Processamento** - Aplica as mesmas transformações do treinamento
4. **Predição** - Utiliza o modelo para gerar a previsão
5. **Exibição de Resultados** - Mostra o resultado de forma clara

A aplicação inclui tratamento de erros e validação de dados para garantir funcionamento robusto.

---

## Aprendizados do Projeto

Este projeto proporciona compreensão prática de:

- Processamento e limpeza de dados reais
- Feature engineering e preparação para modelagem
- Desenvolvimento e treinamento de modelos de regressão
- Avaliação de desempenho com múltiplas métricas
- Deploy de modelos em uma aplicação interativa
- Tratamento de problemas de compatibilidade em ambiente de produção

---

## Possíveis Melhorias Futuras

O projeto pode ser expandido com:

- Inclusão de mais variáveis de entrada (gênero do cliente, tipo de cliente)
- Implementação de validação cruzada (cross-validation)
- Análise de importância das features
- Otimização de hiperparâmetros
- Visualização de métricas em tempo real na aplicação
- Deploy online em plataforma como HuggingFace Spaces

---

## Referências

- Dataset: Supermarket Sales (Kaggle)
- Bibliotecas: Pandas, Scikit-Learn, Streamlit
- Tipo de Problema: Regressão Linear
- Modelos Utilizados: Random Forest, Linear Regression

---

**Desenvolvido por:** Miqueias Teixeira
**Data:** 2026