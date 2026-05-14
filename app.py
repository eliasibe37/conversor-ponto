import streamlit as st
import pandas as pd
import pdfplumber
import re
from io import BytesIO

# Configuração visual da página
st.set_page_config(page_title="Conversor Ponto Parvi", page_icon="🕒")
st.title("🕒 Conversor de Cartão Ponto - RCR")
st.markdown("Suba o arquivo PDF para gerar a planilha limpa.")

# Campo para subir o arquivo
arquivo_pdf = st.file_uploader("Arraste o PDF aqui ou clique para selecionar", type=["pdf"])

if arquivo_pdf is not None:
    dados_finais = []
    
    with pdfplumber.open(arquivo_pdf) as pdf:
        for pagina in pdf.pages:
            # 1. Extração de Nome e Matrícula no topo da página
            texto_topo = pagina.extract_text()
            nome_f, mat_f = "N/A", "N/A"
            for linha in texto_topo.split('\n'):
                if "Matrícula:" in linha:
                    m = re.search(r"Matrícula:\s*(\d+)", linha)
                    if m: mat_f = m.group(1)
                if "Funcionário:" in linha:
                    nome_f = linha.split(":")[-1].strip()

            # 2. PAREDE DE SEGURANÇA (Corte no pixel 250)
            # Isso ignora fisicamente tudo à direita das batidas (CHP, Extras, etc)
            caixa_corte = (0, 0, 250, pagina.height)
            area_limpa = pagina.within_bbox(caixa_corte)
            palavras = area_limpa.extract_words()
            
            # Agrupar palavras por linha
            linhas_dict = {}
            for p in palavras:
                top = round(p['top'])
                encontrou = False
                for t in linhas_dict.keys():
                    if abs(t - top) <= 3:
                        linhas_dict[t].append(p)
                        encontrou = True
                        break
                if not encontrou:
                    linhas_dict[top] = [p]

            # 3. Processamento das batidas
            for top in sorted(linhas_dict.keys()):
                linha_objs = sorted(linhas_dict[top], key=lambda x: x['x0'])
                
                # Se a linha começa com data (DD/MM/AAAA)
                if len(linha_objs) > 0 and re.match(r"^\d{2}/\d{2}/\d{4}", linha_objs[0]['text']):
                    data_txt = linha_objs[0]['text']
                    dia_txt = linha_objs[1]['text'] if len(linha_objs) > 1 else ""
                    
                    # Pega apenas horários que sobraram dentro do limite de 250 pixels
                    horarios = [p['text'] for p in linha_objs if re.match(r"^\d{2}:\d{2}$", p['text'])]
                    
                    e1 = horarios[0] if len(horarios) >= 1 else ""
                    s1 = horarios[1] if len(horarios) >= 2 else ""
                    e2 = horarios[2] if len(horarios) >= 3 else ""
                    s2 = horarios[3] if len(horarios) >= 4 else ""
                    
                    dados_finais.append([mat_f, nome_f, data_txt, dia_txt, e1, s1, e2, s2])

    if dados_finais:
        # Criar DataFrame
        df = pd.DataFrame(dados_finais, columns=["Matricula", "Nome", "Data", "Dia", "Ent.1", "Sai.1", "Ent.2", "Sai.2"])
        
        st.success(f"✅ {len(dados_finais)} linhas processadas com sucesso!")
        st.dataframe(df) # Mostra a prévia na tela
        
        # Preparar o download para Excel
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        
        st.download_button(
            label="📥 Baixar Planilha Excel",
            data=output.getvalue(),
            file_name="ponto_rcr_finalizado.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("Nenhum dado de ponto foi encontrado. Verifique se o PDF está correto.")