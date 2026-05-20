import streamlit as st

st.set_page_config(page_title="Portal de Utilitários", page_icon="📊", layout="wide")

# Mantendo o visual exatamente como você aprovou
st.markdown("""
    <style>
        .stApp { background-color: #f8fafc; font-family: 'Inter', sans-serif; }
        .header { text-align: center; margin-bottom: 3.5rem; padding-top: 2rem; }
        .header h1 { color: #0f172a; font-size: 2.8rem; font-weight: 700; margin-bottom: 0.5rem; }
        .header p { color: #64748b; font-size: 1.15rem; }
        
        .card { 
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-top: 5px solid #00c4b4;
            border-radius: 16px;
            padding: 30px;
            height: 220px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .card:hover { border-color: #00c4b4; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
        .card h3 { color: #00c4b4; font-size: 1.4rem; margin: 0 0 12px 0; font-weight: 600; }
        .card p { color: #475569; font-size: 1rem; line-height: 1.6; margin-bottom: 15px; }

        div.stButton > button { 
            background-color: #00c4b4 !important; 
            color: white !important; 
            border-radius: 12px !important;
            border: none !important; 
            padding: 10px 20px !important;
            font-weight: 600 !important;
            width: 100% !important; 
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>Portal de Utilitários</h1><p>Automação e Gestão de Planejamento Operacional</p></div>', unsafe_allow_html=True)

cols = st.columns(4, gap="large")

# Card 1
with cols[0]:
    st.markdown('<div class="card"><h3>Sem Movimento</h3><p>Controle de jornadas e indicadores operacionais.</p></div>', unsafe_allow_html=True)
    if st.button("Listar Sem Movimento", key="btn1", use_container_width=True):
        st.switch_page("pages/Sem_Movimento.py")

# Card 2
with cols[1]:
