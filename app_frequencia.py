import streamlit as st

# Configuração da página inicial do portal com o tema corporativo
st.set_page_config(
    page_title="Portal de Planejamento & RH - Parvi/RCR",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS personalizada para aplicar as cores da Parvi / RCR
st.markdown("""
    <style>
        /* Cor de fundo principal e fontes */
        .main-title {
            color: #007A78;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .subtitle {
            color: #1D3557;
            font-size: 1.2rem;
            margin-bottom: 25px;
        }
        /* Estilo dos cards das ferramentas */
        .card {
            background-color: #F4F9F9;
            border-left: 5px solid #009688;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .card h3 {
            color: #004D40;
            margin-top: 0;
        }
        .card p {
            color: #455A64;
            font-size: 0.95rem;
        }
        /* Rodapé customizado */
        .footer {
            text-align: center;
            color: #90A4AE;
            font-size: 0.85rem;
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #ECEFF1;
        }
    </style>
""", unsafe_allow_html=True)

# Layout de duas colunas para o Cabeçalho (Simulando as duas marcas do grupo)
col_logo1, col_logo2 = st.columns([1, 1])
with col_logo1:
    st.subheader("💚 Parvi Transportes")
with col_logo2:
    st.markdown("<h3 style='text-align: right; color: #007A78;'>RCR Locação 🏢</h3>", unsafe_allow_html=True)

st.markdown("---")

# Título Principal e Subtítulo da Home
st.markdown('<h1 class="main-title">📊 Portal de Planejamento & Recursos Humanos</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Bem-vindo ao centro de utilidades digitais da sua equipa. Selecione uma ferramenta no menu lateral esquerdo para iniciar as operações.</p>', unsafe_allow_html=True)

# Divisão em colunas para apresentar os Apps ativos no menu lateral
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="card">
            <h3>📋 Listagem de Movimentos</h3>
            <p><strong>Área de Frequência e Ponto:</strong> Submeta arquivos de dados no formato TXT para processamento automatizado, filtragem por filiais, tratamento de horas adicionais e conferência de escalas de colaboradores.</p>
            <p style="color: #009688; font-weight: bold; font-size: 0.85rem;">➔ Disponível no menu à esquerda</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card" style="border-left-color: #0288D1;">
            <h3 style="color: #01579B;">picture_as_pdf Unificador de PDF</h3>
            <p><strong>Utilitários de Documentos:</strong> Agrupe múltiplos ficheiros PDF num único documento de forma rápida, segura e organizada. Ideal para juntar relatórios e guias de entrega.</p>
            <p style="color: #0288D1; font-weight: bold; font-size: 0.85rem;">➔ Disponível no menu à esquerda</p>
        </div>
    """, unsafe_allow_html=True)

# Seção de avisos / notas importantes para o Planeamento
st.markdown("### 📢 Avisos Importantes")
st.info("""
* **Segurança de Dados:** Certifique-se de que os arquivos de ponto extraídos cumprem as diretrizes internas antes de realizar o upload.
* **Atualizações:** Este portal sincroniza diretamente com o repositório oficial. Novas ferramentas de automação de RH serão listadas aqui assim que forem homologadas.
""")

# Rodapé Corporativo
st.markdown("""
    <div class="footer">
        Parvi Transportes & RCR Locação © 2026 | Desenvolvido para Controle de Frequência & Planeamento de Pessoal
    </div>
""", unsafe_allow_html=True)
