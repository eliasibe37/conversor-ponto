import streamlit as st

# Configuração da página - Wide para melhor aproveitamento de espaço
st.set_page_config(
    page_title="Portal de Utilitários - Planejamento",
    page_icon="📊",
    layout="wide"
)

# 1. ESTILIZAÇÃO CSS AVANÇADA
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Poppins:wght@700&display=swap');

        .main { background-color: #f8fafc; }
        .main-title { color: #007A78; font-family: 'Poppins', sans-serif; font-weight: 700; text-align: center; margin-top: -20px; font-size: 2.8rem; }
        .sub-text { text-align: center; color: #64748b; font-family: 'Inter', sans-serif; margin-bottom: 30px; font-size: 1.1rem; }
        
        .card {
            background-color: white;
            border-top: 6px solid #00c4b4;
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 220px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            margin-bottom: 15px;
        }
        .card:hover { transform: translateY(-8px); box-shadow: 0 12px 30px rgba(0,0,0,0.1); }
        .card h3 { color: #0f172a; margin-bottom: 15px; font-size: 1.4rem; font-family: 'Poppins', sans-serif; }
        .card p { color: #475569; font-size: 0.95rem; line-height: 1.6; font-family: 'Inter', sans-serif; }

        div.stButton > button { background-color: #007A78 !important; color: white !important; border-radius: 12px !important; border: none !important; font-weight: 600 !important; }
        div.stButton > button:hover { background-color: #00c4b4 !important; color: white !important; }
        
        .footer { text-align: center; color: #94a3b8; font-
