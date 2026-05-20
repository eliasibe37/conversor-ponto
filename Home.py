import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Portal de Utilitários",
    page_icon="📊",
    layout="wide"
)

# Estilização Profissional
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
            transition: background-color 0.2s ease !important;
        }
        div.stButton > button:hover { 
            background-color: #007A78 !important; 
        }
        .footer { text-align:
