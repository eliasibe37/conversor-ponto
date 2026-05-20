import streamlit as st
import pdfplumber
import pandas as pd
import re
import io

st.set_page_config(page_title="Processador de Ponto", layout="centered")

st.title(" Conversor dos Registros de Ponto")
st.write("Suba o PDF abaixo para extrair os dados e gerar a planilha.")

# 1. Widget de Upload do Streamlit
uploaded_file = st.file_uploader("Escolha o arquivo PDF:", type="pdf")

if uploaded_file is not None:
    if st.button("Processar Arquivo"):
        dados_finais = []
        
        # Lê o arquivo diretamente da memória
        with pdfplumber.open(uploaded_file) as pdf:
            total_paginas = len(pdf.pages)
            
            # Barra de progresso do Streamlit
            bar = st.progress(0)
            
            for i, pagina in enumerate(pdf.pages):
                # Atualiza a barra de progresso
                bar.progress((i + 1) / total_paginas)
                
                texto_completo = pagina.extract_text()
                nome_f, mat_f = "N/A", "N/A"
                for linha in texto_completo.split('\n'):
                    if "Matrícula:" in linha: 
                        m = re.search(r"Matrícula:\s*(\d+)", linha)
                        if m: mat_f = m.group(1)
                    if "Funcionário:" in linha: 
                        nome_f = linha.split(":")[-1].strip()

                caixa_corte = (0, 0, 240, pagina.height)
                area_limpa = pagina.within_bbox(caixa_corte)
                palavras = area_limpa.extract_words()
                
                linhas_dict = {}
                for p in palavras:
                    top = round(p['top'])
                    encontrou = False
                    for t in linhas_dict.keys():
                        if abs(t - top) <= 3:
                            linhas_dict[t].append(p); encontrou = True; break
                    if not encontrou: linhas_dict[top] = [p]

                for top in sorted(linhas_dict.keys()):
                    linha_objs = sorted(linhas_dict[top], key=lambda x: x['x0'])
                    if len(linha_objs) > 0 and re.match(r"^\d{2}/\d{2}/\d{4}", linha_objs[0]['text']):
                        data_txt = linha_objs[0]['text']
                        dia_txt = linha_objs[1]['text'] if len(linha_objs) > 1 else ""
                        horarios = [p['text'] for p in linha_objs if re.match(r"^\d{2}:\d{2}$", p['text'])]
                        
                        e1 = horarios[0] if len(horarios) >= 1 else ""
                        s1 = horarios[1] if len(horarios) >= 2 else ""
                        e2 = horarios[2] if len(horarios) >= 3 else ""
                        s2 = horarios[3] if len(horarios) >= 4 else ""
                        
                        dados_finais.append([mat_f, nome_f, data_txt, dia_txt, e1, s1, e2, s2])

        # 2. Geração do Excel via Memória
        df = pd.DataFrame(dados_finais, columns=["Matricula", "Nome", "Data", "Dia", "Ent.1", "Sai.1", "Ent.2", "Sai.2"])
        
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        
        st.success("✅ Processamento concluído!")
        
        # 3. Botão de download do Streamlit
        st.download_button(
            label="Baixar Planilha Gerada",
            data=output.getvalue(),
            file_name="ponto_final_limpo.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
