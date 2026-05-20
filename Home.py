import streamlit as st

st.set_page_config(page_title="Portal de Utilitários", layout="wide")

st.markdown("""
    <style>
        .card { background: #ffffff; border: 1px solid #e2e8f0; border-top: 5px solid #00c4b4; padding: 30px; border-radius: 16px; height: 220px; margin-bottom: 20px; }
        div.stButton > button { background-color: #00c4b4 !important; color: white !important; border-radius: 12px !important; width: 100% !important; font-weight: 600 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("Portal de Utilitários")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card"><h3>Sem Movimento</h3><p>Controle de jornadas e indicadores.</p></div>', unsafe_allow_html=True)
    if st.button("Listar Sem Movimento", key="btn1"):
        st.switch_page("pages/Sem_Movimento.py")

with col2:
    st.markdown('<div class="card"><h3>Listagem De Movimentos</h3><p>Tratamento de arquivos TXT de ponto.</p></div>', unsafe_allow_html=True)
    if st.button("Frequência", key="btn2"):
        st.switch_page("pages/Listagem_De_Movimentos.py")

with col3:
    st.markdown('<div class="card"><h3>Unificador De PDF</h3><p>Agrupamento ágil de relatórios.</p></div>', unsafe_allow_html=True)
    if st.button("Unificar PDF", key="btn3"):
        st.switch_page("pages/Unificador_De_PDF.py")

with col4:
    st.markdown('<div class="card"><h3>Conversor de Ponto</h3><p>Normalização de registros.</p></div>', unsafe_allow_html=True)
    if st.button("Converter Registros", key="btn4"):
        st.switch_page("pages/Conversor_De_Registros_De_Ponto.py")
