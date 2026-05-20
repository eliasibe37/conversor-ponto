import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Portal de Utilitários - Planejamento",
    page_icon="📊",
    layout="wide"
)

# 1. ESTILIZAÇÃO CSS (Fundo Branco)
st.markdown("""
    <style>
        .main { background-color: #ffffff; }
        .stApp { background-color: #ffffff; }
        .main-title { color: #007A78; font-family: sans-serif; font-weight: 700; text-align: center; margin-bottom: 30px; }
        .sub-text { text-align: center; color: #64748b; margin-bottom: 40px; }
        .card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-top: 5px solid #00c4b4;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            height: 180px;
            margin-bottom: 20px;
        }
        div.stButton > button { background-color: #007A78 !important; color: white !important; border-radius: 8px !important; border: none !important; width: 100%; }
        .footer { text-align: center; color: #94a3b8; font-size: 0.85rem; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Portal de Utilitários</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Inteligência e automação para o planejamento operacional.</p>', unsafe_allow_html=True)

# Organizando em 2 colunas para os 4 cards ficarem bem dimensionados
col1, col2 = st.columns(2, gap="large")
col3, col4 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="card"><h3>Sem Movimento</h3><p>Controle de jornadas e acompanhamento.</p></div>', unsafe_allow_html=True)
    if st.button("Abrir Sem Movimento", key="b1"):
        st.switch_page("pages/Sem_Movimento.py")

with col2:
    st.markdown('<div class="card"><h3>Listagem De Movimentos</h3><p>Tratamento de arquivos TXT de ponto.</p></div>', unsafe_allow_html=True)
    if st.button("Abrir Listagem", key="b2"):
        st.switch_page("pages/Listagem_De_Movimentos.py")

with col3:
    st.markdown('<div class="card"><h3>Unificador De PDF</h3><p>Agrupamento ágil de relatórios.</p></div>', unsafe_allow_html=True)
    if st.button("Abrir Unificador", key="b3"):
        st.switch_page("pages/Unificador_De_PDF.py")

with col4:
    st.markdown('<div class="card"><h3>Conversor de Ponto</h3><p>Normalização de registros de ponto.</p></div>', unsafe_allow_html=True)
    if st.button("Abrir Conversor", key="b4"):
        st.switch_page("pages/Conversor_De_Registros_De_Ponto.py")

st.markdown('<div class="footer">Setor de Planejamento - Parvi Transportes & RCR Locação</div>', unsafe_allow_html=True)
