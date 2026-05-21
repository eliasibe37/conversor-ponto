import streamlit as st

st.set_page_config(page_title="Portal de Utilitários", page_icon="📊", layout="wide")

# CSS para garantir o padrão visual profissional
st.markdown("""
    <style>
        .header { text-align: center; margin-bottom: 3rem; }
        .card { 
            background: #ffffff; 
            border: 1px solid #e2e8f0; 
            border-top: 5px solid #00c4b4; 
            border-radius: 12px; 
            padding: 25px; 
            height: 240px; 
            text-align: center; 
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .card h3 { color: #00c4b4; font-size: 1.3rem; margin-bottom: 15px; }
        .card p { color: #475569; font-size: 0.95rem; line-height: 1.5; }
        div.stButton > button { 
            background-color: #00c4b4 !important; 
            color: white !important; 
            border-radius: 8px !important;
            width: 100% !important; 
            font-weight: 600 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>Portal de Utilitários</h1><p>Automação e Gestão de Planejamento Operacional</p></div>', unsafe_allow_html=True)

apps = [
    ("Sem Movimento", "Controle de jornadas e indicadores.", "pages/Sem_Movimento.py", "Listar Sem Movimento"),
    ("Listagem De Movimentos", "Tratamento de arquivos TXT de ponto.", "pages/Listagem_De_Movimentos.py", "Frequência"),
    ("Unificador De PDF", "Agrupamento ágil de relatórios.", "pages/Unificador_De_PDF.py", "Unificar PDF"),
    ("Conversor de Ponto", "Normalização de registros.", "pages/Conversor_De_Registros_De_Ponto.py", "Converter Registros"),
    ("Folgas Trabalhadas", "Gestão de registros de folgas.", "pages/Folgas_Trabalhadas.py", "Folgas Trabalhadas")
]

# Grid Profissional: 3 colunas base
# Criamos 2 linhas de colunas
cols1 = st.columns(3)
cols2 = st.columns(3)

# Renderiza os 3 primeiros na linha 1
for i in range(3):
    with cols1[i]:
        st.markdown(f'<div class="card"><h3>{apps[i][0]}</h3><p>{apps[i][1]}</p></div>', unsafe_allow_html=True)
        if st.button(apps[i][3], key=f"btn_{i}"):
            st.switch_page(apps[i][2])

# Renderiza os 2 últimos na linha 2, usando as colunas 1 e 2 para centralizar
with cols2[0]:
    st.markdown(f'<div class="card"><h3>{apps[3][0]}</h3><p>{apps[3][1]}</p></div>', unsafe_allow_html=True)
    if st.button(apps[3][3], key="btn_3"):
        st.switch_page(apps[3][2])

with cols2[1]:
    st.markdown(f'<div class="card"><h3>{apps[4][0]}</h3><p>{apps[4][1]}</p></div>', unsafe_allow_html=True)
    if st.button(apps[4][3], key="btn_4"):
        st.switch_page(apps[4][2])

st.markdown('<div style="text-align: center; color: #94a3b8; font-size: 0.8rem; margin-top: 50px;">Setor de Planejamento - Parvi Transportes & RCR Locação</div>', unsafe_allow_html=True)
