import streamlit as st

# Configuração da página - Visual Profissional
st.set_page_config(
    page_title="Portal de Utilitários - Planejamento",
    page_icon="📊",
    layout="centered" # Deixando o conteúdo centralizado para ficar mais elegante
)

# Estilização CSS para cores inspiradas na logo (Verde Esmeralda / Ciano)
st.markdown("""
    <style>
        .main {
            background-color: #f0f7f7;
        }
        .main-title {
            color: #007A78;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-weight: 800;
            text-align: center;
            margin-top: 10px;
        }
        .card {
            background-color: white;
            border-top: 5px solid #00c4b4;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            height: 250px;
        }
        .card h3 {
            color: #004D40;
            margin-bottom: 15px;
        }
        .card p {
            color: #546E7A;
            font-size: 0.9rem;
            line-height: 1.4;
        }
        .footer {
            text-align: center;
            color: #90A4AE;
            font-size: 0.8rem;
            margin-top: 60px;
        }
        /* Ajuste para centralizar imagem */
        [data-testid="stImage"] {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# 1. Exibição da Logo (Arquivo que você subiu no GitHub)
try:
    st.image("logo_planejamento.png", width=350)
except:
    # Caso a imagem ainda não esteja no GitHub, ele mostra um texto elegante
    st.markdown("<h2 style='text-align: center; color: #007A78;'>Parvi / RCR</h2>", unsafe_allow_html=True)

# 2. Título Principal (Apenas Planejamento)
st.markdown('<h1 class="main-title">Portal de Utilitários do Planejamento</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #607D8B;'>Central de ferramentas e automações para suporte ao planejamento operacional.</p>", unsafe_allow_html=True)

st.write("---")

# 3. Cards das Ferramentas
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="card">
            <h3>📋 Movimentos</h3>
            <p>Processamento de arquivos TXT de ponto. Filtre por filiais, trate horas adicionais e confira escalas de forma automatizada.</p>
            <p style="color: #00c4b4; font-weight: bold; margin-top: 20px;">➔ Acesse pelo menu lateral</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <h3>📄 Unificador PDF</h3>
            <p>Agrupe múltiplos relatórios e documentos PDF num único arquivo organizado em segundos.</p>
            <p style="color: #00c4b4; font-weight: bold; margin-top: 20px;">➔ Acesse pelo menu lateral</p>
        </div>
    """, unsafe_allow_html=True)

# 4. Rodapé
st.markdown("""
    <div class="footer">
        Setor de Planejamento - Parvi Transportes & RCR Locação<br>
        © 2026 Portal de Automação
    </div>
""", unsafe_allow_html=True)
