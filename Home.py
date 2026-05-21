import streamlit as st

st.set_page_config(page_title="Portal de Operações", layout="wide")

# CSS focado em "UI Corporativa"
st.markdown("""
    <style>
        .card { 
            background: #ffffff; 
            border: 1px solid #e2e8f0; 
            border-top: 6px solid #00c4b4; /* Cor da empresa */
            border-radius: 8px; 
            padding: 24px; 
            height: 180px; 
            text-align: center; 
            transition: transform 0.2s;
        }
        .card:hover { transform: translateY(-5px); border-top: 6px solid #008f83; }
        .card h3 { color: #1e293b; font-size: 1.1rem; margin-bottom: 8px; }
        .card p { color: #64748b; font-size: 0.8rem; margin-bottom: 20px; }
        .stButton button { background-color: #00c4b4 !important; color: white !important; width: 100%; border-radius: 4px !important; }
    </style>
""", unsafe_allow_html=True)

st.title("Portal de Operações")
st.markdown("---")

apps = [
    ("⚙️ Sem Movimento", "Controle de jornadas e indicadores.", "pages/Sem_Movimento.py", "Executar"),
    ("📋 Listagem", "Tratamento de arquivos TXT de ponto.", "pages/Listagem_De_Movimentos.py", "Processar"),
    ("📄 Unificador", "Agrupamento ágil de relatórios.", "pages/Unificador_De_PDF.py", "Unificar"),
    ("🔄 Conversor", "Normalização de registros.", "pages/Conversor_De_Registros_De_Ponto.py", "Converter"),
    ("📅 Folgas", "Gestão de registros de folgas.", "pages/Folgas_Trabalhadas.py", "Gerenciar")
]

cols = st.columns(3)
for i, app in enumerate(apps):
    with cols[i % 3]:
        st.markdown(f'<div class="card"><h3>{app[0]}</h3><p>{app[1]}</p>', unsafe_allow_html=True)
        if st.button(app[3], key=f"btn_{i}"):
            st.switch_page(app[2])
