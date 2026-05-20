import streamlit as st

# Configuração da página - Wide para melhor aproveitamento de espaço
st.set_page_config(
    page_title="Portal de Utilitários - Planejamento",
    page_icon="📊",
    layout="wide"
)

# 1. ESTILIZAÇÃO CSS AVANÇADA
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
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            margin-bottom: 15px;
        }
        .card:hover { transform: translateY(-8px); box-shadow: 0 12px 30px rgba(0,0,0,0.1); }
        .card h3 { color: #0f172a; margin-bottom: 15px; font-size: 1.4rem; font-family: 'Poppins', sans-serif; }
        .card p { color: #475569; font-size: 0.95rem; line-height: 1.6; font-family: 'Inter', sans-serif; }

        div.stButton > button { background-color: #007A78 !important; color: white !important; border-radius: 12px !important; border: none !important; font-weight: 600 !important; }
        div.stButton > button:hover { background-color: #00c4b4 !important; color: white !important; }
        
        .footer { text-align: center; color: #94a3b8; font-size: 0.85rem; margin-top: 80px; font-family: 'Inter', sans-serif; }
    </style>
""", unsafe_allow_html=True)

# --- CONTEÚDO ---
st.markdown('<h1 class="main-title">Portal de Utilitários</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Inteligência e automação para o planejamento operacional.</p>', unsafe_allow_html=True)

# Criando as 3 colunas
col1, col2, col3 = st.columns(3, gap="large")

# Card 1: Sem Movimento
with col1:
    st.markdown("""
        <div class="card">
            <h3>Sem Movimento</h3>
            <p>Visão geral e painel de indicadores relacionados, controle de jornadas e acompanhamento operacional.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Abrir Sem Movimento", key="btn_sem_mov", use_container_width=True):
        st.switch_page("pages/Sem_Movimento.py")

# Card 2: Listagem De Movimentos
with col2:
    st.markdown("""
        <div class="card">
            <h3>Listagem De Movimentos</h3>
            <p>Tratamento de arquivos TXT de ponto. Filtragem por filiais, tratamento de horas extras e folgas.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Abrir Listagem De Movimentos", key="btn_mov", use_container_width=True):
        st.switch_page("pages/Listagem_De_Movimentos.py")

# Card 3: Unificador De PDF
with col3:
    st.markdown("""
        <div class="card">
            <h3>Unificador De PDF</h3>
            <p>Agrupamento ágil de múltiplos arquivos PDF. Junte relatórios, escalas de serviço e guias em um único documento.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Abrir Unificador De PDF", key="btn_pdf", use_container_width=True):
        st.switch_page("pages/Unificador_De_PDF.py")

st.markdown('<div class="footer">Setor de Planejamento - Parvi Transportes & RCR Locação</div>', unsafe_allow_html=True)
