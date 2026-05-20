import streamlit as st

st.set_page_config(page_title="Portal de Utilitários", page_icon="📊", layout="wide")

# Estilização para garantir que os títulos fiquem verdes e o visual seja profissional
st.markdown("""
    <style>
        .header { text-align: center; margin-bottom: 3rem; }
        .card { 
            background: #ffffff; 
            border: 1px solid #e2e8f0; 
            border-radius: 12px; 
            padding: 20px; 
            height: 250px; 
            text-align: center; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>Portal de Utilitários</h1><p>Automação e Gestão de Planejamento Operacional</p></div>', unsafe_allow_html=True)

cols = st.columns(4)

# Configuração dos cards e botões
cards = [
    ("Sem Movimento", "Controle de jornadas e indicadores.", "Listar Sem Movimento", "pages/Sem_Movimento.py"),
    ("Listagem De Movimentos", "Tratamento de arquivos TXT de ponto.", "Frequência", "pages/Listagem_De_Movimentos.py"),
    ("Unificador De PDF", "Agrupamento ágil de relatórios.", "Unificar PDF", "pages/Unificador_De_PDF.py"),
    ("Conversor de Ponto", "Normalização de registros.", "Converter Registros", "pages/Conversor_De_Registros_De_Ponto.py")
]

for i, (titulo, desc, nome_btn, link) in enumerate(cards):
    with cols[i]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        # Título Verde (usando a cor primária do Streamlit)
        st.markdown(f"<h3 style='color: #00c4b4;'>{titulo}</h3>", unsafe_allow_html=True)
        st.write(desc)
        
        # Botão centralizado (o Streamlit centraliza botões em colunas automaticamente)
        if st.button(nome_btn, key=f"btn_{i}"):
            st.switch_page(link)
        st.markdown('</div>', unsafe_allow_html=True)
