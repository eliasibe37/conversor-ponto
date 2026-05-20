import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Portal de Utilitários - Planejamento",
    page_icon="📊",
    layout="wide"
)

# 1. ESTILIZAÇÃO CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Poppins:wght@700&display=swap');
        .main { background-color: #f8fafc; }
        .main-title { color: #007A78; font-family: 'Poppins', sans-serif; font-weight: 700; text-align: center; margin-top: -20px; font-size: 2.8rem; }
        .sub-text { text-align: center; color: #64748b; font-family: 'Inter', sans-serif; margin-bottom: 30px; font-size: 1.1rem; }
        .card {
            background-color: white;
            border-top: 6px solid #00c4b4;
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 220px;
            margin-bottom: 20px;
        }
        .card:hover { transform: translateY(-8px); box-shadow: 0 12px 30px rgba(0,0,0,0.1); }
        .card h3 { color: #0f172a; margin-bottom: 15px; font-size: 1.4rem; font-family: 'Poppins', sans-serif; }
        .card p { color: #475569; font-size: 0.95rem; line-height: 1.6; }
        div.stButton > button { background-color: #007A78 !important; color: white !important; border-radius: 12px !important; font-weight: 600 !important; }
        .footer { text-align: center; color: #94a3b8; font-size: 0.85rem; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Portal de Utilitários</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Inteligência e automação para o planejamento operacional.</p>', unsafe_allow_html=True)

# Criando 2 linhas com 2 colunas cada para acomodar os 4 cards perfeitamente
row1_col1, row1_col2 = st.columns(2, gap="large")
row2_col1, row2_col2 = st.columns(2, gap="large")

# Card 1: Sem Movimento
with row1_col1:
    st.markdown('<div class="card"><h3>Sem Movimento</h3><p>Visão geral e painel de indicadores, controle de jornadas e acompanhamento operacional.</p></div>', unsafe_allow_html=True)
    if st.button("Abrir Sem Movimento", key="btn_sem", use_container_width=True):
        st.switch_page("pages/Sem_Movimento.py")

# Card 2: Listagem De Movimentos
with row1_col2:
    st.markdown('<div class="card"><h3>Listagem De Movimentos</h3><p>Tratamento de arquivos TXT de ponto. Filtragem por filiais, horas extras e folgas.</p></div>', unsafe_allow_html=True)
    if st.button("Abrir Listagem De Movimentos", key="btn_mov", use_container_width=True):
        st.switch_page("pages/Listagem_De_Movimentos.py")

# Card 3: Unificador De PDF
with row2_col1:
    st.markdown('<div class="card"><h3>Unificador De PDF</h3><p>Agrupamento ágil de múltiplos arquivos PDF. Junte relatórios e escalas em um único documento.</p></div>', unsafe_allow_html=True)
    if st.button("Abrir Unificador De PDF", key="btn_pdf", use_container_width=True):
        st.switch_page("pages/Unificador_De_PDF.py")

# Card 4: Conversor De Registros De Ponto (NOVO)
with row2_col2:
    st.markdown('<div class="card"><h3>Conversor de Ponto</h3><p>Conversão e normalização de registros de ponto para os padrões do sistema.</p></div>', unsafe_allow_html=True)
    if st.button("Abrir Conversor de Ponto", key="btn_conv", use_container_width=True):
        st.switch_page("pages/Conversor_De_Registros_De_Ponto.py")

st.markdown('<div class="footer">Setor de Planejamento - Parvi Transportes & RCR Locação</div>', unsafe_allow_html=True)
