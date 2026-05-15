import streamlit as st
import pandas as pd
import re
import io

# Alteração do título da aba e do cabeçalho da página
st.set_page_config(page_title="Listagem de Movimentos", layout="wide")
st.title("📋 Listagem de Movimentos")

uploaded_file = st.file_uploader("Selecione o arquivo TXT", type=['txt'])

if uploaded_file is not None:
    content = uploaded_file.getvalue().decode("latin1")
    linhas = content.split('\n')
    dados = []
    matricula_atual = ""

    for linha in linhas:
        l = linha.replace('*', ' ')
        if "Funcionario :" in l:
            match_mat = re.search(r"Funcionario\s*:\s*(\d+)", l)
            if match_mat: matricula_atual = match_mat.group(1).zfill(6)
            continue

        if re.match(r"^\d{2}/\d{2}/\d{4}", l.strip()):
            data = l[0:10].strip()
            dia  = l[11:14].strip()
            
            bloco_texto = l[15:100].upper()
            bloco_limpo = re.sub(r'\d{1,3}:\d{2}', '', bloco_texto)
            
            ocorrencia_final = ""
            linha_qv_final = ""
            
            # --- LISTA DE ELITE ---
            if "ABONADO" in bloco_limpo:
                ocorrencia_final = "DIA ABONADO"
            elif "FERIADO" in bloco_limpo:
                ocorrencia_final = "FERIADO"
            elif "ATESTADO" in bloco_limpo or "MEDICO" in bloco_limpo:
                ocorrencia_final = "ATESTADO MEDICO"
            elif "FERIAS" in bloco_limpo or "FERIA" in bloco_limpo:
                ocorrencia_final = "FERIAS"
            elif "FALTA" in bloco_limpo:
                ocorrencia_final = "FALTA"
            elif "FOLGA" in bloco_limpo:
                ocorrencia_final = "FOLGA"
            elif "MOVIMENTO" in bloco_limpo or "M VIMENTO" in bloco_limpo:
                ocorrencia_final = "SEM MOVIMENTO"
            elif "CURSO" in bloco_limpo:
                ocorrencia_final = "CURSO"
            elif "DTRAB" in bloco_limpo:
                ocorrencia_final = "DTRAB"
                linha_qv_final = l[43:55].strip()
            else:
                ocorrencia_final = l[56:75].strip().upper()
                linha_qv_final = l[43:55].strip()

            is_evento = ocorrencia_final != "DTRAB" and ocorrencia_final != ""
            horarios = re.findall(r'\d{1,3}:\d{2}', l[15:])
            res = {col: "" for col in ["ENTRA", "I.INI", "I.FIN", "SAIDA", "NORMAL", "A.NOT", "TOTAL"]}
            
            if not is_evento and len(horarios) >= 2:
                res["ENTRA"] = horarios[0]
                res["TOTAL"] = horarios[-1]
                if len(horarios) >= 6:
                    res["I.INI"], res["I.FIN"], res["SAIDA"], res["NORMAL"], res["A.NOT"] = horarios[1:6]
                elif len(horarios) == 4:
                    res["SAIDA"], res["NORMAL"] = horarios[1:3]
            
            if is_evento: linha_qv_final = ""

            # --- REGRA DE VERIFICAR DUPLICIDADE ---
            observacao = ""
            batidas = [res["ENTRA"], res["I.INI"], res["I.FIN"], res["SAIDA"]]
            batidas_reais = [b for b in batidas if b != "" and b != "0:00" and b != "00:00"]
            if len(batidas_reais) != len(set(batidas_reais)):
                observacao = "VERIFICAR"

            dados.append({
                "Matricula": matricula_atual, "DATA": data, "DIA": dia,
                "ENTRA": res["ENTRA"], "I.INI": res["I.INI"], "I.FIN": res["I.FIN"], "SAIDA": res["SAIDA"],
                "VAZIA": "", "LINHA/QV": linha_qv_final, "OCORRENCIA": ocorrencia_final,
                "NORMAL": res["NORMAL"], "A.NOT": res["A.NOT"], "EXTRA": "", "EX LN": "", 
                "EXCES": "", "OUTRA": "", "C.NOT": "", "INCOM": "", "TOTAL": res["TOTAL"], 
                "OBSERVAÇÃO": observacao
            })

    if dados:
        df = pd.DataFrame(dados)
        st.dataframe(df, use_container_width=True)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        st.download_button(label="📥 BAIXAR PLANILHA", data=output.getvalue(), file_name="Listagem_de_Movimentos.xlsx")