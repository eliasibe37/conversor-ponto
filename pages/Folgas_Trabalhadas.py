import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portal de Utilitários", page_icon="📊", layout="wide")

# CSS para garantir padronização absoluta
st.markdown("""
    <style>
        .card { 
            background: #ffffff; 
            border: 1px solid #e2e8f0; 
            border-top: 5px solid #00c4b4; 
            border-radius: 12px; 
            padding: 25px; 
            height: 200px; 
            text-align: center; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .card h3 { color: #00c4b4; font-size: 1.2rem; margin-bottom: 10px; }
        .card p { color: #475569; font-size: 0.9rem; line-height: 1.5; }
        div.stButton > button { 
            background-color: #00c4b4 !important; 
            color: white !important; 
            border-radius: 6px !important;
            width: 100% !important; 
            font-weight: 600 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Portal de Utilitários")
st.subheader("Automação e Gestão de Planejamento Operacional")
st.write("---")

# Lista centralizada de aplicativos (mantenha a ordem aqui)
apps = [
    ("Sem Movimento", "Controle de jornadas e indicadores.", "pages/Sem_Movimento.py", "Acessar"),
    ("Listagem Movimentos", "Tratamento de arquivos TXT de ponto.", "pages/Listagem_De_Movimentos.py", "Acessar"),
    ("Unificador PDF", "Agrupamento ágil de relatórios.", "pages/Unificador_De_PDF.py", "Acessar"),
    ("Conversor Ponto", "Normalização de registros.", "pages/Conversor_De_Registros_De_Ponto.py", "Acessar"),
    ("Folgas Trabalhadas", "Gestão de registros de folgas.", "pages/Folgas_Trabalhadas.py", "Acessar")
]

# Grid profissional de 3 colunas
cols = st.columns(3)

# O loop distribui os itens automaticamente em colunas alinhadas
for i, app in enumerate(apps):
    with cols[i % 3]:
        st.markdown(f'<div class="card"><h3>{app[0]}</h3><p>{app[1]}</p></div>', unsafe_allow_html=True)
        if st.button(app[3], key=f"btn_{i}"):
            st.switch_page(app[2])
