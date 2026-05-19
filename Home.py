import streamlit as st

# Configuração da página - Usando 'wide' para caber as 3 colunas perfeitamente
st.set_page_config(
    page_title="Portal de Utilitários - Planejamento",
    page_icon="📊",
    layout="wide"
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
            padding: 22px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            margin-bottom: 10px;
            height: 200px; /* Altura ajustada para os textos */
        }
        .card h3 {
            color: #004D40;
            margin-bottom: 12px;
            font-size: 1.3rem;
        }
        .card p {
            color: #546E7A;
            font-size: 0.88rem;
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

# 1. Exibição da Logo (Se estiver no GitHub)
try:
    st.image("logo_planejamento.png", width=350)
except:
    st.markdown("<h2 style='text-align: center; color: #007A78;'>Parvi / RCR</h2>", unsafe_allow_html=True)

# 2. Título Principal
st.markdown('<h1 class="main-title">Portal de Utilitários do Planejamento</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #607D8B;'>Central de ferramentas e automações para suporte ao planejamento operacional.</p>", unsafe_allow_html=True)

st.write("---")

# 3. Mapeamento das 3 colunas correspondentes ao menu lateral
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card">
            <h3>📊 Frequencia</h3>
            <p>Visão geral e painel de indicadores relacionados à frequência, controle de jornadas e acompanhamento operacional da equipe.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 Abrir Frequencia", use_container_width=True):
        st.switch_page("pages/Frequencia.py")

with col2:
    st.markdown("""
        <div class="card" style="border-top-color: #009688;">
            <h3>📋 Listagem De Movimentos</h3>
            <p>Tratamento de arquivos TXT de ponto. Filtragem por filiais, tratamento de horas extras, adicionais noturnos e folgas trabalhadas.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 Abrir Movimentos", use_container_width=True):
        st.switch_page("pages/Listagem_De_Movimentos.py")

with col3:
    st.markdown("""
        <div class="card" style="border-top-color: #0288D1;">
            <h3>📄 Unificador De PDF</h3>
            <p>Agrupamento ágil de múltiplos arquivos PDF. Junte relatórios, escalas de serviço e guias em um único documento em segundos.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 Abrir Unificador PDF", use_container_width=True):
        st.switch_page("pages/Unificador_De_PDF.py")

# 4. Rodapé
st.markdown("""
    <div class="footer">
        Setor de Planejamento - Parvi Transportes & RCR Locação<br>
        © 2026 Portal de Automação
    </div>
""", unsafe_allow_html=True)
