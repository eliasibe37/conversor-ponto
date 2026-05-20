import streamlit as st

# 1. Configuração da página (Deve ser o primeiro comando do Streamlit)
st.set_page_config(
    page_title="Portal de Utilitários - Planejamento",
    page_icon="📊",
    layout="wide"
)

# 2. Estilização CSS
st.markdown("""
    <style>
        .card { 
            background-color: white; 
            border-top: 6px solid #00c4b4; 
            padding: 25px; 
            border-radius: 20px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.05); 
            height: 220px; 
            margin-bottom: 20px;
        }
        .main-title { color: #007A78; font-weight: 700; text-align: center; }
        div.stButton > button { width: 100%; border-radius: 10px; background-color: #007A78; color: white; font-weight: 600; }
        div.stButton > button:hover { background-color: #00c4b4; }
    </style>
""", unsafe_allow_html=True)

# 3. Conteúdo
st.markdown('<h1 class="main-title">Portal de Utilitários</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

# Card 1: Sem Movimento
with col1:
    st.markdown("""
        <div class="card">
            <h3>Sem Movimento</h3>
            <p>Visão geral e painel de indicadores, controle de jornadas e acompanhamento operacional.</p>
        </div>
    """, unsafe_allow_html=True)
    # A NAVEGAÇÃO OCORRE APENAS DENTRO DESTE IF
    if st.button("Abrir Sem Movimento", key="btn_sem_mov"):
        st.switch_page("pages/Sem_Movimento.py")

# Card 2: Listagem De Movimentos
with col2:
    st.markdown("""
        <div class="card">
            <h3>Listagem De Movimentos</h3>
            <p>Tratamento de arquivos TXT de ponto. Filtragem por filiais, horas extras e folgas.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Abrir Listagem De Movimentos", key="btn_mov"):
        st.switch_page("pages/Listagem_De_Movimentos.py")

# Card 3: Unificador De PDF
with col3:
    st.markdown("""
        <div class="card">
            <h3>Unificador De PDF</h3>
            <p>Agrupamento ágil de múltiplos arquivos PDF. Junte relatórios e escalas em um único documento.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Abrir Unificador De PDF", key="btn_pdf"):
        st.switch_page("pages/Unificador_De_PDF.py")
