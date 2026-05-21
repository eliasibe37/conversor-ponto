import streamlit as st

st.set_page_config(page_title="Portal de Utilitários", page_icon="📊", layout="wide")

# Estilização Profissional
st.markdown("""
    <style>
        .header { text-align: center; margin-bottom: 2.5rem; }
        .card { 
            background: #ffffff; 
            border: 1px solid #e2e8f0; 
            border-top: 5px solid #00c4b4; 
            border-radius: 10px; 
            padding: 20px; 
            height: 190px; 
            text-align: center; 
            box-shadow: 0 3px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .card h3 { color: #00c4b4; font-size: 1.4rem !important; margin-bottom: 12px; font-weight: 700; }
        .card p { color: #475569; font-size: 0.9rem; line-height: 1.4; margin-bottom: 15px; }
        
        div.stButton > button { 
            background-color: #00c4b4 !important; 
            color: white !important; 
            border-radius: 6px !important;
            padding: 6px 20px !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>Portal de Utilitários</h1><p>Automação e Gestão de Planejamento Operacional</p></div>', unsafe_allow_html=True)

apps = [
    ("Sem Movimento", "Controle de jornadas e indicadores.", "pages/Sem_Movimento.py", "Acessar"),
    ("Listagem Movimentos", "Tratamento de arquivos TXT de ponto.", "pages/Listagem_De_Movimentos.py", "Acessar"),
    ("Unificador PDF", "Agrupamento ágil de relatórios.", "pages/Unificador_De_PDF.py", "Acessar"),
    ("Conversor Ponto", "Normalização de registros.", "pages/Conversor_De_Registros_De_Ponto.py", "Acessar"),
    ("Folgas Trabalhadas", "Gestão de registros de folgas.", "pages/Folgas_Trabalhadas.py", "Acessar")
]

# Grid de 3 colunas para garantir o alinhamento
cols = st.columns(3)

for i, app in enumerate(apps):
    with cols[i % 3]:
        st.markdown(f'<div class="card"><h3>{app[0]}</h3><p>{app[1]}</p></div>', unsafe_allow_html=True)
        if st.button(app[3], key=f"btn_{i}"):
            st.switch_page(app[2])

# Rodapé corrigido sem erros de sintaxe
st.markdown('<div style="text-align: center; color: #94a3b8; font-size: 0.75rem; margin-top: 40px;">Setor de Planejamento - Parvi Transportes & RCR Locação</div>', unsafe_allow_html=True)
