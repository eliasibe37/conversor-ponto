import streamlit as st

# Configuração da página - Mantendo o layout Wide para os cards ficarem bem distribuídos
st.set_page_config(
    page_title="Portal de Utilitários",
    page_icon="📊",
    layout="wide"
)

# ESTILIZAÇÃO CSS - RIGOROSAMENTE IGUAL À ANTERIOR (Cores e Alinhamentos)
st.markdown("""
    <style>
        .stApp { background-color: #ffffff; }
        .header { text-align: center; margin-bottom: 3rem; padding-top: 1rem; }
        .header h1 { color: #0f172a; font-size: 2.2rem; font-weight: 700; margin-bottom: 0.5rem; }
        .header p { color: #64748b; font-size: 1.1rem; }
        
        .card { 
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-top: 5px solid #00c4b4; /* Verde solicitado nos títulos/bordas */
            border-radius: 12px;
            padding: 24px;
            height: 220px; 
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            text-align: center;
            transition: all 0.2s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        .card h3 { color: #00c4b4; font-size: 1.25rem; margin: 0 0 10px 0; }
        .card p { color: #475569; font-size: 0.95rem; line-height: 1.5; margin-bottom: 15px; }
        
        /* Estilo dos botões centralizados e verdes */
        div.stButton > button { 
            background-color: #00c4b4 !important; 
            color: white !important; 
            border-radius: 8px !important;
            border: none !important; 
            padding: 8px 16px !important;
            font-weight: 600 !important;
            width: auto !important; 
            margin: 0 auto !important;
            display: block !important;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="header"><h1>Portal de Utilitários</h1><p>Automação e Gestão de Planejamento Operacional</p></div>', unsafe_allow_html=True)

# Lista de Apps (Título, Descrição, Link, Nome do Botão)
# Incluindo o novo app: Folgas Trabalhadas
apps = [
    ("Sem Movimento", "Controle de jornadas e indicadores operacionais.", "pages/Sem_Movimento.py", "Listar Sem Movimento"),
    ("Listagem De Movimentos", "Tratamento de arquivos TXT de ponto e filtros.", "pages/Listagem_De_Movimentos.py", "Frequência"),
    ("Unificador De PDF", "Agrupamento ágil de relatórios e escalas.", "pages/Unificador_De_PDF.py", "Unificar PDF"),
    ("Conversor de Ponto", "Normalização de registros para sistemas.", "pages/Conversor_De_Registros_De_Ponto.py", "Converter Registros"),
    ("Folgas Trabalhadas", "Gestão de registros de folgas operacionais.", "pages/Folgas_Trabalhadas.py", "Folgas Trabalhadas")
]

# Organização em Grid para 5 cards (3 em cima e 2 embaixo)
row1 = st.columns(3)
row2 = st.columns(3) # Usando 3 colunas também embaixo para manter o tamanho dos cards igual

# Linha 1 (Cards 1, 2 e 3)
for i in range(3):
    titulo, desc, link, btn_nome = apps[i]
    with row1[i]:
        st.markdown(f'<div class="card"><div><h3>{titulo}</h3><p>{desc}</p></div></div>', unsafe_allow_html=True)
        if st.button(btn_nome, key=f"btn_{i}"):
            st.switch_page(link)

# Linha 2 (Cards 4 e 5)
for i in range(3, 5):
    titulo, desc, link, btn_nome = apps[i]
    with row2[i-3]: # i-3 para usar as colunas 0 e 1 da linha 2
        st.markdown(f'<div class="card"><div><h3>{titulo}</h3><p>{desc}</p></div></div>', unsafe_allow_html=True)
        if st.button(btn_nome, key=f"btn_{i}"):
            st.switch_page(link)

st.markdown('<div style="margin-top: 50px; text-align: center; color: #94a3b8; font-size: 0.8rem;">Setor de Planejamento - Parvi Transportes & RCR Locação</div>', unsafe_allow_html=True)
