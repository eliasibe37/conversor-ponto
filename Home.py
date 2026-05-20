import streamlit as st

st.set_page_config(page_title="Portal de Utilitários", page_icon="📊", layout="wide")

# CSS refinado para tipografia e espaçamento profissional
st.markdown("""
    <style>
        .stApp { background-color: #fcfcfc; }
        .header { text-align: center; margin-bottom: 3rem; padding-top: 1rem; }
        .header h1 { color: #0f172a; font-size: 2.2rem; font-weight: 700; margin-bottom: 0.5rem; }
        .header p { color: #64748b; font-size: 1.1rem; }
        
        .card { 
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 24px;
            height: 200px; /* Altura fixa para todos os cartões */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.2s ease;
        }
        .card:hover { border-color: #007A78; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
        .card h3 { color: #007A78; font-size: 1.25rem; margin: 0 0 10px 0; }
        .card p { color: #475569; font-size: 0.95rem; line-height: 1.5; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="header"><h1>Portal de Utilitários</h1><p>Automação e Gestão de Planejamento Operacional</p></div>', unsafe_allow_html=True)

# Configuração dos cards
apps = [
    ("Sem Movimento", "Controle de jornadas e indicadores operacionais.", "pages/Sem_Movimento.py"),
    ("Listagem De Movimentos", "Tratamento de arquivos TXT de ponto e filtros.", "pages/Listagem_De_Movimentos.py"),
    ("Unificador De PDF", "Agrupamento ágil de relatórios e guias.", "pages/Unificador_De_PDF.py"),
    ("Conversor de Ponto", "Normalização de registros para sistemas.", "pages/Conversor_De_Registros_De_Ponto.py")
]

# Grid em 4 colunas
cols = st.columns(4)

for i, (titulo, desc, link) in enumerate(apps):
    with cols[i]:
        st.markdown(f'''
            <div class="card">
                <div>
                    <h3>{titulo}</h3>
                    <p>{desc}</p>
                </div>
            </div>
        ''', unsafe_allow_html=True)
        # O botão fica abaixo do card para não atrapalhar o design
        if st.button(f"Acessar {titulo.split()[0]}", key=f"btn_{i}", use_container_width=True):
            st.switch_page(link)

st.markdown('<div style="margin-top: 50px; text-align: center; color: #94a3b8; font-size: 0.8rem;">Setor de Planejamento - Parvi Transportes & RCR Locação</div>', unsafe_allow_html=True)
