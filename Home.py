import streamlit as st

st.set_page_config(page_title="Portal de Utilitários", page_icon="📊", layout="wide")

# Estilização mantida conforme aprovado
st.markdown("""
    <style>
        .stApp { background-color: #ffffff; }
        .header { text-align: center; margin-bottom: 3rem; padding-top: 1rem; }
        .header h1 { color: #0f172a; font-size: 2.2rem; font-weight: 700; margin-bottom: 0.5rem; }
        .header p { color: #64748b; font-size: 1.1rem; }
        
        .card { 
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-top: 5px solid #00c4b4;
            border-radius: 12px;
            padding: 24px;
            height: 220px; 
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .card h3 { color: #00c4b4; font-size: 1.25rem; margin: 0 0 10px 0; }
        .card p { color: #475569; font-size: 0.95rem; line-height: 1.5; margin-bottom: 15px; }
        
        div.stButton > button { 
            background-color: #00c4b4 !important; 
            color: white !important; 
            border-radius: 8px !important;
            border: none !important; 
            padding: 8px 16px !important;
            font-weight: 600 !important;
            width: 100% !important; 
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>Portal de Utilitários</h1><p>Automação e Gestão de Planejamento Operacional</p></div>', unsafe_allow_html=True)

# Definição dos apps
apps = [
    ("Sem Movimento", "Controle de jornadas e indicadores.", "pages/Sem_Movimento.py", "Listar Sem Movimento"),
    ("Listagem De Movimentos", "Tratamento de arquivos TXT de ponto.", "pages/Listagem_De_Movimentos.py", "Frequência"),
    ("Unificador De PDF", "Agrupamento ágil de relatórios.", "pages/Unificador_De_PDF.py", "Unificar PDF"),
    ("Conversor de Ponto", "Normalização de registros.", "pages/Conversor_De_Registros_De_Ponto.py", "Converter Registros"),
    ("Folgas Trabalhadas", "Gestão de registros de folgas.", "pages/Folgas_Trabalhadas.py", "Folgas Trabalhadas")
]

# Linha 1: 4 colunas
cols1 = st.columns(4)
for i in range(4):
    with cols1[i]:
        st.markdown(f'<div class="
