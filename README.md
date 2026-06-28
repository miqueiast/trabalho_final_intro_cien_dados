# 🛒 Projeto Final ML - Predição de Vendas

Opa, e aí galera! Tudo certo?

Então, eu tô aqui pra explicar esse projeto que fiz. Basicamente, eu criei um programa que **preve quanto uma pessoa vai gastar** em um supermercado. Parece complicado? Mas na real é mais simples do que parece.

---

## 📖 Como é que Funciona?

Então, saca só: a gente tem um monte de dados históricos de vendas de supermercado, né. Com essas informações (quantos itens comprou, que tipo de produto é, qual avaliação deu, etc), o computador aprende a encontrar padrões.

Aí quando vem um cliente novo, você bota os dados dele no programa e ele fala: "ó, baseado no que aprendi, esse cliente vai gastar assim-assim".

É tipo quando você já viu tantas coisas iguais que você consegue adivinhar o próximo resultado, tá ligado?

---

## 🏗️ A Estrutura do Projeto

Basicamente tem 3 coisas acontecendo:

**1. O Notebook** - Onde a gente pega os dados, limpa, faz uns gráficos pra entender melhor, e depois treina o modelo. É o lugar onde o "aprendizado" acontece mesmo.

**2. O Modelo** - Depois que treina, a gente salva tudo em dois arquivos (`.pkl`). É tipo quando você estuda e coloca tudo na cabeça pra depois não esquecer.

**3. O App** - Aí vem a parte legal: criei um programinha com uns botões bonitinhos usando Streamlit. Você preenche os dados e ele mostra a previsão. Fica bem user-friendly mesmo.

---

## 📊 Os Dados

Os dados vêm desse dataset aí: https://www.kaggle.com/datasets/markmedhat/supermarket-sales

Tem:
- Quantidade de itens
- Preço unitário
- Tipo de produto (eletrônico, moda, alimento, etc)
- Avaliação do cliente
- Data da compra
- Forma de pagamento (dinheiro, cartão, e-wallet)
- E a gente quer prever: **o valor total da compra**

Simples assim.

---

## 🚀 Como Colocar pra Funcionar

### Passo 1: Instalar as coisas

Abre o terminal e manda:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

Pronto. Essas são as bibliotecas que a gente usa pro projeto.

---

### Passo 2: Pegar o Dataset

Vai lá no Kaggle, baixa o arquivo `supermarket_sales.csv` e coloca em uma pasta chamada `dados` dentro do seu projeto.

Fica assim:

```
seu_projeto/
├── notebook.ipynb
├── app.py
├── README.md (esse arquivo)
└── dados/
    └── supermarket_sales.csv
```

---

### Passo 3: Rodar o Notebook

Abre o Jupyter (ou Colab se preferir) e executa o notebook:

```bash
jupyter notebook notebook.ipynb
```

Basicamente você roda tudo de cima a baixo (`Ctrl+A` e `Shift+Enter`). Isso vai:
- Carregar os dados
- Fazer umas análises e gráficos
- Treinar dois modelos diferentes
- Salvar o melhor modelo em um arquivo

Quando terminar, aparece uma mensagem verde tipo: `✅ Tá pronto pro Streamlit!`

---

### Passo 4: Rodar o App

Abre o terminal na pasta do projeto e manda:

```bash
streamlit run app.py
```

Aí abre uma janela no navegador com a interface. Bem daora mesmo.

---

## 🎮 Usando o Programa

Quando abre, tem dois painéis:

**Esquerda:**
- Escolher quantos itens
- Digitar o preço unitário
- Slider pra nota (0-10)

**Direita:**
- Tipo de produto (dropdown)
- Forma de pagamento
- Qual filial
- Data da compra

Depois você clica em "🔮 Fazer Previsão" e o programa mostra quanto ele acha que vai custar. Mostra também a previsão, o preço médio por item e um resuminho do que você colocou.

---

## 🔧 Se der Ruim

### "Arquivo não encontrado"
Ó, você não botou o `supermarket_sales.csv` na pasta `dados`. Bota aí que funciona.

### "Coluna faltando" ou "Erro na previsão"
Roda o notebook novamente pra regenerar os arquivos do modelo. Aí tenta rodar o app de novo.

### Aparece umas mensagens estranhas em amarelo
Ó, é só aviso mesmo. O programa funciona normal. Não se preocupa.

---

## 📚 O Que Tem no Código

Se você quiser entender como funciona:

1. **Exploração dos dados** - Vejo o tamanho do dataset, que colunas tem, estatísticas
2. **Limpeza** - Tiro dados que não servem, converto categorias em números, extraio features úteis
3. **Visualização** - Faz uns gráficos pra entender os padrões
4. **Treinamento** - Treina um RandomForest e uma Regressão Linear
5. **Avaliação** - Calcula R², MAE, RMSE pra ver qual modelo é melhor
6. **Salvamento** - Salva o modelo em arquivo pra usar no app depois

Tem comentários em tudo, então dá pra entender o que cada coisa faz.

---

## 🔍 O Que Descobri

Fazendo esse projeto, algumas coisas que aprendi:

- Que a quantidade de itens é a coisa mais importante pra prever o preço (faz total sentido né)
- Que é bem mais fácil processar dados quando você tira as colunas que não servem
- Que RandomForest é bem melhor que regressão linear pra esse tipo de problema
- Como transformar um modelo em um programa que outras pessoas conseguem usar
- Como lidar com erro de compatibilidade de colunas (que foi meio chato de resolver, ngl)

---

## 💡 Por Que Isso Importa?

Empresas reais usam isso pra:
- Saber quanto de produto eles vão vender por mês
- Planejar quanto de dinheiro vai ter
- Entender quando é melhor vender certos produtos
- Tomar decisões melhores sobre estoque

Então não é só uma coisa aleatória, é algo que funciona de verdade.

---

## ✨ Coisas que Queria Ter Feito

Se tivesse mais tempo (ou menos coisa pra fazer):
- Adicionar mais inputs no app (tipo gênero do cliente)
- Mostrar gráficos de feature importance dentro do app
- Colocar isso na internet de graça (HuggingFace Spaces)
- Comparar os modelos em tempo real

Mas já tá bom assim, o importante é que funciona!

---

## 📋 Resumão

Essencialmente, é assim:
- Pego dados reais de supermercado
- Ensino o computador a reconhecer padrões
- Crio um programa pra usar o modelo
- Resultado: você bota uns dados e ele prevê quanto vai custar

E tudo tá bem documentado e comentado, então dá pra entender como funciona.

---

É isso aí! Se ficar com dúvida em algo específico do código, lê os comentários que tá tudo explicado. E se der algum erro, acompanha a seção de troubleshooting aí em cima.

Qualquer coisa, é só chamar!

Abs 🚀