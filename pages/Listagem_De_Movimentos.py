import streamlit as st
import pandas as pd
import re
import io

# Configuração da página e título oficial
st.set_page_config(page_title="Listagem de Movimentos", layout="wide")
st.title("📋 Listagem de Movimentos")

uploaded_file = st.file_uploader("Selecione o arquivo TXT", type=['txt'])

if uploaded_file is not None:
    content = uploaded_file.getvalue().decode("latin1")
    linhas = content.split('\n')
    dados = []
    matricula_atual = ""

    for l_orig in linhas:
        l = l_orig.replace('*', ' ')
        
        # Captura estrita da matrícula do funcionário
        if "Funcionario :" in l:
            match_mat = re.search(r"Funcionario\s*:\s*(\d+)", l)
            if match_mat: 
                matricula_atual = match_mat.group(1).zfill(6)
            continue

        # Verifica se a linha começa com uma data válida
        if re.match(r"^\d{2}/\d{2}/\d{4}", l.strip()):
            data = l[0:10].strip()
            dia  = l[11:14].strip()
            
            bloco_texto = l[15:].upper()
            
            ocorrencia_final = ""
            linha_qv_final = ""
            
            # --- IDENTIFICAÇÃO DE EVENTOS IMPEDITIVOS COM NOMES CORRIGIDOS ---
            is_afastamento = "AFAST" in bloco_texto or "AUXILIO" in bloco_texto
            
            if "ABONADO" in bloco_texto:
                ocorrencia_final = "DIA ABONADO"
            elif "FERIADO" in bloco_texto:
                ocorrencia_final = "FERIADO"
            elif is_afastamento:
                ocorrencia_final = "BENEFICIO"
            elif "ATESTADO" in bloco_texto or "MEDICO" in bloco_texto or "MÉDICO" in bloco_texto:
                ocorrencia_final = "ATESTADO"
            elif "FERIAS" in bloco_texto or "FERIA" in bloco_texto:
                ocorrencia_final = "FERIAS"
            elif "FALTA" in bloco_texto:
                ocorrencia_final = "FALTA"
            elif "COMPENSAD" in bloco_texto:
                ocorrencia_final = "FOLGA COMPENSADA"
            elif "FOLGA" in bloco_texto:
                ocorrencia_final = "FOLGA"
            elif "LICENÇA MATERNIDADE" in bloco_texto or "MATERNIDADE" in bloco_texto:
                ocorrencia_final = "LICENÇA MATERNIDADE"
            elif "PATERNIDADE" in bloco_texto:
                ocorrencia_final = "PATERNIDADE"
            elif "SUSPENSAO" in bloco_texto or "SUSPENSÃO" in bloco_texto:
                ocorrencia_final = "SUSPENSÃO"
            elif "ADMISSAO" in bloco_texto or "ADMISSÃO" in bloco_texto:
                ocorrencia_final = "ADMISSÃO"
            elif "MOVIMENTO" in bloco_texto or "M VIMENTO" in bloco_texto:
                ocorrencia_final = "SEM MOVIMENTO"
            elif "CURSO" in bloco_texto:
                ocorrencia_final = "CURSO"
            elif "CASAMENTO" in bloco_texto:
                ocorrencia_final = "CASAMENTO"
            elif "EXAME" in bloco_texto or "PERIODICO" in bloco_texto or "PERIÓDICO" in bloco_texto:
                # RETORNADO CIRURGICAMENTE: Exame Periódico voltou a ser evento que limpa horas
                ocorrencia_final = "EXAME PERIODICO"
            elif "DTRAB" in bloco_texto:
                ocorrencia_final = "DTRAB"
                # CORREÇÃO CRÍTICA: Remove cirurgicamente todos os horários (XX:XX) antes de isolar a Linha/QV
                trecho_anterior = l[15:l.upper().find("DTRAB")]
                trecho_limpo = re.sub(r'\d{1,2}:\d{2}', '', trecho_anterior)
                
                # Agora pegamos apenas o texto limpo que restou (Ex: "PREPARACAO")
                partes_texto = [p.strip() for p in trecho_limpo.split(" ") if p.strip()]
                if partes_texto:
                    linha_qv_final = " ".join(partes_texto)
            else:
                # Captura dinâmica para outras ocorrências de texto do sistema (FPAG, FER10, FPAGH, FOTRA, CONSM, HSABO, DECMD)
                ocorrencia_final = l[56:75].strip().upper()
                if ocorrencia_final == "6" or ocorrencia_final.isdigit():
                    ocorrencia_final = ""
                linha_qv_final = l[43:55].strip()

            # ALTERAÇÃO CIRÚRGICA: Apenas siglas reais que trazem horários permitidos
            liberam_horarios = ["DTRAB", "FPAG", "FER10", "FPAGH", "FOTRA", "CONSM", "HSABO", "DECMD"]
            is_evento = ocorrencia_final not in liberam_horarios and ocorrencia_final != ""
            
            # Inicializa todas as colunas de resultados vazias
            res = {col: "" for col in ["ENTRA", "I.INI", "I.FIN", "SAIDA", "NORMAL", "A.NOT", "EXTRA", "EX LN", "EXCES", "OUTRA", "C.NOT", "INCOM", "TOTAL"]}
            
            if not is_evento:
                # Define o divisor dinamicamente varrendo as siglas permitidas
                idx_divisor = -1
                for sigla in liberam_horarios:
                    idx_divisor = l.upper().find(sigla)
                    if idx_divisor != -1:
                        break
                
                if idx_divisor != -1:
                    # 1. PARTE ESQUERDA (BATIDAS REAIS DE PONTO)
                    trecho_ponto = l[15:idx_divisor]
                    batidas_ponto = re.findall(r'\d{1,2}:\d{2}', trecho_ponto)
                    
                    if len(batidas_ponto) == 4:
                        res["ENTRA"], res["I.INI"], res["I.FIN"], res["SAIDA"] = batidas_ponto
                    elif len(batidas_ponto) == 2:
                        res["ENTRA"], res["SAIDA"] = batidas_ponto
                    elif len(batidas_ponto) == 3:
                        res["ENTRA"], res["I.INI"], res["SAIDA"] = batidas_ponto
                    elif len(batidas_ponto) == 1:
                        res["ENTRA"] = batidas_ponto[0]
                    
                    # 2. PARTE DIREITA (CÁLCULOS DO SISTEMA) - ALINHAMENTO FIXO ABSOLUTO PRESERVADO
                    c_normal = l[74:81].strip()
                    c_anot   = l[81:88].strip()
                    c_extra  = l[88:95].strip()
                    c_exln   = l[95:102].strip()
                    c_exces  = l[102:109].strip()
                    c_outra  = l[109:116].strip()
                    c_cnot   = l[116:123].strip()
                    c_incom  = l[123:130].strip()
                    c_total  = l[130:142].strip()
                    
                    # Validação com Regex para garantir a integridade dos formatos de hora
                    if re.match(r'^\d{1,3}:\d{2}$', c_normal): res["NORMAL"] = c_normal
                    if re.match(r'^\d{1,3}:\d{2}$', c_anot):   res["A.NOT"]  = c_anot
                    if re.match(r'^\d{1,3}:\d{2}$', c_extra):  res["EXTRA"]  = c_extra
                    if re.match(r'^\d{1,3}:\d{2}$', c_exln):   res["EX LN"]  = c_exln
                    if re.match(r'^\d{1,3}:\d{2}$', c_exces):  res["EXCES"]  = c_exces
                    if re.match(r'^\d{1,3}:\d{2}$', c_outra):  res["OUTRA"]  = c_outra
                    if re.match(r'^\d{1,3}:\d{2}$', c_cnot):   res["C.NOT"]  = c_cnot
                    if re.match(r'^\d{1,3}:\d{2}$', c_incom):  res["INCOM"]  = c_incom
                    if re.match(r'^\d{1,3}:\d{2}$', c_total):  res["TOTAL"]  = c_total

            if is_evento: 
                linha_qv_final = ""

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
                "NORMAL": res["NORMAL"], "A.NOT": res["A.NOT"], "EXTRA": res["EXTRA"], "EX LN": res["EX LN"], 
                "EXCES": res["EXCES"], "OUTRA": res["OUTRA"], "C.NOT": res["C.NOT"], "INCOM": res["INCOM"], "TOTAL": res["TOTAL"], 
                "OBSERVAÇÃO": observacao
            })

    if dados:
        df = pd.DataFrame(dados)
        st.dataframe(df, use_container_width=True)
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        st.download_button(label="📥 BAIXAR PLANILHA", data=output.getvalue(), file_name="Listagem_de_Movimentos.xlsx")
