import streamlit as st

# Configuração da página - Wide para melhor aproveitamento de espaço
st.set_page_config(
    page_title="Portal de Utilitários",
    page_icon="📊",
    layout="wide"
)

# 1. ESTILIZAÇÃO CSS AVANÇADA (Ajustado para botões verdes)
st.markdown("""
    <style>
        /* Fonte e Fundo */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
        .stApp { background-color: #f8fafc; font-family: 'Inter', sans-serif; }

        /* Títulos e Textos Principais */
        .header { text-align: center; margin-bottom: 3.5rem; }
        .header h1 { color: #0f172a; font-size: 2.8rem; font-weight: 700; margin-bottom: 0.5rem; }
        .header p { color: #64748b; font-size: 1.15rem; }
        
        /* Estilização Profissional dos Cards */
        .card { 
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-top: 5px solid #00c4b4; /* Linha de destaque no topo */
            border-radius: 16px;
            padding: 30px;
            height: 220px; /* Altura fixa para simetria */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .card:hover { border-color: #00c4b4; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
        .card h3 { color: #00c4b4; font-size: 1.4rem; margin: 0 0 12px 0; font-weight: 600; }
        .card p { color: #475569; font-size: 1rem; line-height: 1.6; margin-bottom: 15px; }

        /* --- CORREÇÃO SOLICITADA: Botões no mesmo tom de verde --- */
        div.stButton > button { 
            background-color: #00c4b4 !important; /* Mesma cor do título h3 e da borda superior */
            color: white !important; /* Texto branco para contraste */
            border-radius: 12px !important;
            border: none !important; /* Remove a borda padrão cinza */
            padding: 10px 20px !important;
            font-weight: 600 !important;
            width: 100% !important; /* Botão ocupa a largura total */
            transition: background-color 0.2s ease !important;
        }
        
        /* Efeito de hover (quando passa o mouse) */
        div.stButton > button:hover { 
            background-color: #007A78 !important; /* Um tom de verde mais escuro para o hover */
            color: white !important;
        }

        /* Rodapé */
        .footer { text-align: center; color: #94a3b8; font-size: 0.85rem; margin-top: 70px; }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="header"><h1>Portal de Utilitários</h1><p>Automação e Gestão de Planejamento Operacional</p></div>', unsafe_allow_html=True)

# Configuração dos cards (Títulos, Descrições e Links)
apps = [
    ("Sem Movimento", "Controle de jornadas e indicadores operacionais.", "pages/Sem_Movimento.py"),
    ("Listagem De Movimentos", "Tratamento de arquivos TXT de ponto e filtros.", "pages/Listagem_De_Movimentos.py"),
    ("Unificador De PDF", "Agrupamento ágil de relatórios e escalas.", "pages/Unificador_De_PDF.py"),
    ("Conversor de Ponto", "Normalização de registros para sistemas.", "pages/Conversor_De_Registros_De_Ponto.py")
]

# Grid Profissional em 4 colunas (uma para cada card)
cols = st.columns(4, gap="large")

# Loop para gerar os cards dinamicamente
for i, (titulo, desc, link) in enumerate(apps):
    with cols[i]:
        # Título e Descrição dentro do HTML do card
        st.markdown(f'''
            <div class="card">
                <div>
                    <h3>{titulo}</h3>
                    <p>{desc}</p>
                </div>
            </div>
        ''', unsafe_allow_html=True)
        # O botão (Acessar...) fica fora do card mas herda o alinhamento e a estilização CSS
        if st.button(f"Acessar {titulo.split()[0]}", key=f"btn_{i}", use_container_width=True):
            st.switch_page(link)

st.markdown('<div class="footer">Setor de Planejamento - Parvi Transportes & RCR Locação</div>', unsafe_allow_html=True)
