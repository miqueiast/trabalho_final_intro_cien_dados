import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# ========== CONFIGURAÇÃO INICIAL ==========

# Configurar a página (título, ícone, layout)
st.set_page_config(
    page_title="🛒 Previsão de Vendas - Supermercado",
    page_icon="🛒",
    layout="wide"
)

# Carregar o modelo treinado (com cache pra ser rápido)
@st.cache_resource
def carregar_modelo():
    """
    Carrega o modelo e as colunas que foram salvos no notebook.
    Usa @st.cache_resource pra só carregar UMA VEZ (depois reutiliza)
    """
    try:
        # Carregar o modelo treinado
        with open('dados/modelo_venda.pkl', 'rb') as f:
            modelo = pickle.load(f)
        
        # Carregar as colunas na ordem correta
        with open('dados/colunas_modelo.pkl', 'rb') as f:
            colunas = pickle.load(f)
        
        # ✅ IMPORTANTE: Garantir que colunas seja uma lista Python pura
        # (pode vir como pandas.Index e dar ruim depois)
        if not isinstance(colunas, list):
            colunas = list(colunas)
        
        return modelo, colunas
    
    except FileNotFoundError as e:
        st.error(f"❌ Erro ao carregar arquivos: {e}")
        st.info("💡 Certifique-se de que 'modelo_venda.pkl' e 'colunas_modelo.pkl' estão na mesma pasta do app.py")
        st.stop()
    except Exception as e:
        st.error(f"❌ Erro inesperado: {e}")
        st.stop()

# Tentar carregar o modelo
try:
    modelo, colunas = carregar_modelo()
except Exception as e:
    st.error(f"❌ Falha ao inicializar: {str(e)}")
    st.stop()

# ========== CABEÇALHO E TÍTULO ==========

st.title("🛒 Previsão de Vendas - Supermercado")
st.markdown("""
    **Modelo de Machine Learning** para prever o valor total de uma venda
    baseado nas características da compra.
    
    💡 **Como funciona:** Preencha os dados da compra abaixo e o modelo
    (treinado com dados reais de supermercado) vai fazer uma previsão do total!
    
    ---
""")

# ========== INPUTS DO USUÁRIO ==========

# Layout em duas colunas pra ficar organizado
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Informações da Compra")
    st.markdown("*Dados do cliente e do pedido*")
    
    # Quantidade de itens
    quantity = st.slider(
        "Quantidade de Itens",
        min_value=1, max_value=10, value=3, step=1,
        help="Quantos produtos o cliente tá levando?"
    )
    
    # Preço unitário
    unit_price = st.number_input(
        "Preço Unitário (R$)",
        min_value=10.0, max_value=1000.0, value=100.0, step=10.0,
        help="Qual é o preço de UM item?"
    )
    
    # Avaliação do cliente
    rating = st.slider(
        "Avaliação do Cliente (0-10)",
        min_value=0.0, max_value=10.0, value=5.0, step=0.5,
        help="Qual nota o cliente deu pra compra?"
    )

with col2:
    st.subheader("🏢 Categoria e Data")
    st.markdown("*Características do produto e da filial*")
    
    # Linha de produto
    product_line = st.selectbox(
        "Linha de Produto",
        ["Electronics", "Fashion accessories", "Food and beverages",
         "Health and beauty", "Home and garden", "Sports and travel"],
        help="Qual tipo de produto?"
    )
    
    # Forma de pagamento
    payment_method = st.selectbox(
        "Forma de Pagamento",
        ["Cash", "Credit card", "E-wallet"],
        help="Como o cliente vai pagar?"
    )
    
    # Filial
    branch = st.selectbox(
        "Filial",
        ["A", "B", "C"],
        help="Qual filial está vendendo?"
    )
    
    # Data da compra
    data = st.date_input(
        "Data da Compra",
        datetime.today(),
        help="Quando aconteceu a compra?"
    )
    
    # Extrair mês, dia da semana e trimestre da data
    month = data.month
    day_of_week = data.weekday()  # 0=Segunda, 6=Domingo
    quarter = (month - 1) // 3 + 1

st.markdown("---")

# ========== BOTÃO DE PREVISÃO ==========

if st.button("🔮 Fazer Previsão", use_container_width=True, type="primary"):
    try:
        # ========== FASE 1: MONTAR A ENTRADA ==========
        # Dicionário com os inputs do usuário
        entrada = {
            'Unit price': unit_price,
            'Quantity': quantity,
            'Rating': rating,
            'Month': month,
            'DayOfWeek': day_of_week,
            'Quarter': quarter,
            'Gender_encoded': 0,  # Padrão (não tem seleção de gênero no app)
            'Customer_type_encoded': 0,  # Padrão (não tem seleção de tipo no app)
        }
        
        # ========== FASE 2: ONE-HOT ENCODING ==========
        # Converter categorias em 0 e 1
        # Exemplo: se escolheu "Electronics" → ProductLine_Electronics=1, resto=0
        
        product_lines = ["Electronics", "Fashion accessories", "Food and beverages",
                        "Health and beauty", "Home and garden", "Sports and travel"]
        for pl in product_lines:
            entrada[f'ProductLine_{pl}'] = 1 if pl == product_line else 0
        
        payment_methods = ["Cash", "Credit card", "E-wallet"]
        for pm in payment_methods:
            entrada[f'Payment_{pm}'] = 1 if pm == payment_method else 0
        
        branches = ["A", "B", "C"]
        for br in branches:
            entrada[f'Branch_{br}'] = 1 if br == branch else 0
        
        # ========== FASE 3: CONVERTER PARA DATAFRAME ==========
        entrada_df = pd.DataFrame([entrada])
        
        # ========== FASE 4: AJUSTE CRÍTICO DE COMPATIBILIDADE ==========
        # O modelo foi treinado com colunas ESPECÍFICAS em ORDEM ESPECÍFICA
        # Se não for exatamente igual, o modelo não funciona direito!
        
        # Passo 1️⃣: Adicionar colunas que faltam com 0
        for col in colunas:
            if col not in entrada_df.columns:
                entrada_df[col] = 0
        
        # Passo 2️⃣: Remover colunas que sobraram
        entrada_df = entrada_df[[col for col in colunas]]
        
        # Passo 3️⃣: Reordenar EXATAMENTE como o modelo espera
        entrada_df = entrada_df[colunas]
        
        # ========== FASE 5: FAZER A PREVISÃO ==========
        previsao = modelo.predict(entrada_df)[0]
        
        # Validar se o resultado é válido
        if np.isnan(previsao) or np.isinf(previsao):
            st.error("❌ Erro na previsão: resultado inválido")
        else:
            # ========== FASE 6: EXIBIR RESULTADOS ==========
            st.success("✅ Previsão Realizada com Sucesso!")
            
            # Mostrar o resultado principal em destaque
            col_res1, col_res2 = st.columns(2)
            
            with col_res1:
                st.metric(
                    "💰 Valor Total Previsto",
                    f"R$ {previsao:.2f}"
                )
            
            with col_res2:
                preco_medio = previsao / quantity if quantity > 0 else 0
                st.metric(
                    "🏷️ Preço Médio por Item",
                    f"R$ {preco_medio:.2f}"
                )
            
            # Mostrar um resumo tabelado
            st.markdown("---")
            st.subheader("📊 Resumo da Previsão")
            
            resumo = pd.DataFrame({
                'Campo': ['Quantidade', 'Preço Unitário', 'Produto', 'Pagamento', 'Filial', 'Avaliação'],
                'Valor': [f"{quantity} itens", f"R$ {unit_price:.2f}", product_line,
                          payment_method, f"Filial {branch}", f"{rating}/10"]
            })
            
            st.dataframe(resumo, use_container_width=True, hide_index=True)
            
            # Disclaimer importante
            st.info(
                "📌 **Observações Importantes:**\n\n"
                "• Esta previsão é baseada em um modelo treinado com dados históricos\n"
                "• Use como referência, não como valor absoluto\n"
                "• Fatores não considerados (promoções, descontos, etc) podem afetar o valor real\n"
                "• O modelo tem uma margem de erro de ±5-10% em média"
            )
    
    # ========== TRATAMENTO DE ERROS ==========
    except KeyError as e:
        st.error(f"❌ Erro: Coluna faltante - {str(e)}")
        st.info("💡 Verifique se o arquivo 'colunas_modelo.pkl' está atualizado. "
                "Execute o notebook novamente pra regenerar os arquivos.")
    
    except ValueError as e:
        st.error(f"❌ Erro de tipo de dado: {str(e)}")
        st.info("💡 Verifique se todos os valores de entrada são válidos")
    
    except Exception as e:
        st.error(f"❌ Erro inesperado: {str(e)}")
        st.info("💡 Entre em contato com o desenvolvedor se o problema persistir")

# ========== FOOTER ==========
st.markdown("""
    ---
    <div style='text-align: center; font-size: 12px; color: #888;'>
    <b>Projeto Final de Machine Learning</b><br>
    Miqueias Teixeira<br>
    Dataset: Supermarket Sales (Kaggle)<br>
    <i>Modelo treinado com scikit-learn | Interface com Streamlit</i>
    </div>
    """, unsafe_allow_html=True)
