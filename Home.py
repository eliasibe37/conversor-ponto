import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portal de Utilitários", layout="wide")

# Estilização
st.markdown("""
    <style>
        .card { background-color: white; border-top: 6px solid #00c4b4; padding: 25px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); height: 200px; }
        .stButton button { width: 100%; border-radius: 10px; background-color: #007A78; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("Portal de Utilitários")

# --- DEFINIÇÃO DOS CALLBACKS DE NAVEGAÇÃO ---
# Isso separa a lógica de navegação da renderização da página
def ir_para_sem_movimento():
    st.switch_page("pages/Sem_Movimento.py")

def ir_para_listagem():
    st.switch_page("pages/Listagem_De_Movimentos.py")

def ir_para_pdf():
    st.switch_page("pages/Unificador_De_PDF.py")

# --- LAYOUT DOS CARTOES ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h3>Sem Movimento</h3><p>Controle de jornadas e acompanhamento.</p></div>', unsafe_allow_html=True)
    st.button("Abrir Sem Movimento", on_click=ir_para_sem_movimento, key="btn1")

with col2:
    st.markdown('<div class="card"><h3>Listagem De Movimentos</h3><p>Tratamento de arquivos TXT de ponto.</p></div>', unsafe_allow_html=True)
    st.button("Abrir Listagem De Movimentos", on_click=ir_para_listagem, key="btn2")

with col3:
    st.markdown('<div class="card"><h3>Unificador De PDF</h3><p>Agrupamento ágil de relatórios.</p></div>', unsafe_allow_html=True)
    st.button("Abrir Unificador De PDF", on_click=ir_para_pdf, key="btn3")
