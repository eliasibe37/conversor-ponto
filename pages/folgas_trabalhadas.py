import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuração inicial da página do Streamlit
st.set_page_config(page_title="Folgas Trabalhadas", layout="wide")

st.title("📊 Folgas Trabalhadas (Validação por Ciclo Real)")
st.markdown("Análise dinâmica de faturamento de folgas com base no ciclo trabalhado vs. descanso de direito.")

# Organização dos uploads na tela
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Escala (Cadastro do Modelo)")
    arquivo_escala = st.file_uploader("Upload da Escala (Excel)", type=["xlsx"])

with col2:
    st.subheader("2. Frequência / Movimentação Real")
    arquivo_movimento = st.file_uploader("Upload do Movimento (Excel)", type=["xlsx"])

with col3:
    st.subheader("3. Base de Folgas Trabalhadas")
    arquivo_folgas = st.file_uploader("Upload da Planilha Base de Folgas (Excel)", type=["xlsx"])

if arquivo_escala and arquivo_movimento and arquivo_folgas:
    if st.button("🚀 Processar e Validar Ciclos de Folga", use_container_width=True):
        with st.spinner("Analisando comportamento dos ciclos de trabalho de forma segura... Por favor, aguarde."):
            try:
                # 1. Leitura dos Arquivos
                df_escala = pd.read_excel(arquivo_escala, sheet_name=0)
                df_movimento = pd.read_excel(arquivo_movimento, sheet_name=0)
                df_folgas_base = pd.read_excel(arquivo_folgas, sheet_name=0)

                # --- FUNÇÃO DE TRATAMENTO DE DATAS SEGURO ---
                def forçar_conversão_data(valor):
                    if pd.isna(valor):
                        return None
                    texto = str(valor).strip()
                    if not texto or texto.upper() in ['DATA', 'NAN', 'NAT']:
                        return None
                    
                    try:
                        if '-' in texto:
                            return datetime.strptime(texto.split()[0], '%Y-%m-%d').date()
                    except Exception:
                        pass
                    
                    try:
                        if '/' in texto:
                            partes_data = texto.split()[0].split('/')
                            if len(partes_data[-1]) == 4:
                                return datetime.strptime(texto.split()[0], '%d/%m/%Y').date()
                            else:
                                return datetime.strptime(texto.split()[0], '%d/%m/%y').date()
                    except Exception:
                        pass
                    
                    try:
                        return pd.to_datetime(valor).date()
                    except Exception:
                        return None

                # --- FUNÇÃO DE BUSCA INTELIGENTE DE COLUNA DE MATRÍCULA ---
                def encontrar_coluna_matricula(df, nome_df):
                    for col in df.columns:
                        col_normalizada = str(col).strip().upper().replace('Í', 'I')
                        if 'MATRICULA' in col_normalizada or 'MAT.' in col_normalizada:
                            return col
                    raise KeyError(f"Não foi possível encontrar nenhuma coluna de Matrícula no arquivo de {nome_df}.")

                col_mat_escala = encontrar_coluna_matricula(df_escala, "Escala")
                col_mat_movimento = encontrar_coluna_matricula(df_movimento, "Frequência/Movimento")
                col_mat_folgas = encontrar_coluna_matricula(df_folgas_base, "Base de Folgas")

                # Localiza coluna de escala modelo
                col_escala_modelo = None
                for col in df_escala.columns:
                    if 'ESCALA' in str(col).strip().upper():
                        col_escala_modelo = col
                        break
                if not col_escala_modelo:
                    col_escala_modelo = df_escala.columns[-1]

                # Localiza colunas de data
                def encontrar_coluna_data(df):
                    for col in df.columns:
                        if str(col).strip().upper() == 'DATA':
                            return col
                    return 'DATA'

                col_data_folgas = encontrar_coluna_data(df_folgas_base)
                col_data_movimento = encontrar_coluna_data(df_movimento)

                # Limpeza de Matrículas
                def limpar_matricula(df, coluna):
                    df[coluna] = df[coluna].astype(str).str.strip().str.replace('.0', '', regex=False)
                    df[coluna] = df[coluna].str.zfill(4)
                    return df

                df_folgas_base = limpar_matricula(df_folgas_base, col_mat_folgas)
                df_escala = limpar_matricula(df_escala, col_mat_escala)
                df_movimento = limpar_matricula(df_movimento, col_mat_movimento)

                # Conversão de Datas
                df_folgas_base['DATA_CONVERTIDA'] = df_folgas_base[col_data_folgas].apply(forçar_conversão_data)
                df_movimento['DATA_CONVERTIDA'] = df_movimento[col_data_movimento].apply(forçar_conversão_data)

                # Drop linhas sem datas válidas na tabela de solicitações
                df_folgas_base = df_folgas_base.dropna(subset=['DATA_CONVERTIDA'])

                # Mapear escalas
                escala_motoristas = {}
                for _, linha in df_escala.iterrows():
                    mat = str(linha[col_mat_escala]).strip()
                    desc_escala = str(linha[col_escala_modelo]).strip().upper() if pd.notna(linha[col_escala_modelo]) else "NÃO INFORMADA"
                    escala_motoristas[mat] = desc_escala

                # 2. MAPEAMENTO DOS DIAS TRABALHADOS REAIS
                trabalhos_reais = {}
                for _, linha in df_movimento.iterrows():
                    mat = linha[col_mat_movimento]
                    data_mov = linha['DATA_CONVERTIDA']
                    
                    if data_mov is None:
                        continue
                    
                    ocorrencia = str(linha['OCORRENCIA']).strip().upper() if 'OCORRENCIA' in df_movimento.columns else ""
                    
                    flag_trabalhado = True
                    if ocorrencia in ['FOLGA', 'AFASTADO', 'FÉRIAS', 'AFASTADO INSS', 'FÉRAIS', 'ATESTADO', 'ADMISSÃO']:
                        if pd.isna(linha.get('ENTRA')) and pd.isna(linha.get('EXTRA')) and pd.isna(linha.get('NORMAL')):
                            flag_trabalhado = False
                    
                    if flag_trabalhado:
                        if mat not in trabalhos_reais:
                            trabalhos_reais[mat] = set()
                        trabalhos_reais[mat].add(data_mov)

                # 3. COMPUTAÇÃO INTELIGENTE DOS CICLOS DE ESCALA (CORRIGIDA)
                resultados = []
                motivos = []

                for idx, linha in df_folgas_base.iterrows():
                    matricula = linha[col_mat_folgas]
                    data_solicitada = linha['DATA_CONVERTIDA']
                    
                    tipo_escala = escala_motoristas.get(matricula, "NÃO ENCONTRADA")
                    dias_trabalhados_mot = trabalhos_reais.get(matricula, set())
                    
                    if tipo_escala == "NÃO ENCONTRADA":
                        resultados.append("Indevida")
                        motivos.append("Modelo de escala do motorista não localizado no arquivo de Cadastro.")
                        continue
                    
                    # Decodifica dias de trabalho alvo e folgas alvo (Ex: "5 X 2")
                    try:
                        if "X" in tipo_escala:
                            partes = tipo_escala.replace(" ", "").split("X")
                            dias_trabalho_alvo = int(partes[0])
                            dias_folga_alvo = int(partes[1])
                            escala_invalida = False
                        else:
                            dias_trabalho_alvo = 5
                            dias_folga_alvo = 2
                            escala_invalida = True
                    except Exception:
                        dias_trabalho_alvo = 5
                        dias_folga_alvo = 2
                        escala_invalida = True

                    # Validação 1: Teve batida de ponto/trabalho no dia solicitado?
                    trabalhou_no_dia = data_solicitada in dias_trabalhados_mot
                    if not trabalhou_no_dia:
                        resultados.append("Indevida")
                        motivos.append("Não consta nenhum registro de trabalho/viagem nesta data na movimentação real.")
                        continue

                    if escala_invalida:
                        resultados.append("Indevida")
                        motivos.append(f"Verificar RH: Escala cadastrada como '{tipo_escala}', inviabilizando ciclo automático.")
                        continue

                    # --- NOVA LÓGICA DE JANELA DINÂMICA DE FOLGA ---
                    # Avalia se existe um bloco de dias trabalhados consecutivamente que justifica essa folga atual
                    ciclo_completado = False
                    sequencia_encontrada = 0
                    
                    # Testamos deslocamentos possíveis para cobrir se ele está na primeira, segunda ou terceira folga do ciclo
                    for deslocamento_folga in range(0, dias_folga_alvo):
                        data_inicio_analise = data_solicitada - timedelta(days=deslocamento_folga + 1)
                        
                        contagem_retroativa = 0
                        data_teste = data_inicio_analise
                        
                        # Conta quantos dias ele trabalhou direto para trás a partir desse ponto de partida
                        for _ in range(dias_trabalho_alvo + 2):
                            if data_teste in dias_trabalhados_mot:
                                contagem_retroativa += 1
                            else:
                                break
                            data_teste = data_teste - timedelta(days=1)
                        
                        if contagem_retroativa >= dias_trabalho_alvo:
                            ciclo_completado = True
                            sequencia_encontrada = contagem_retroativa
                            break # Encontrou o bloco correspondente ao ciclo de esforço

                    if ciclo_completado:
                        resultados.append("Devida")
                        motivos.append(f"Válida: Identificado ciclo real anterior de {sequencia_encontrada} dias trabalhados seguidos para a escala {tipo_escala}. Esta data corresponde ao período legítimo de folga/descanso do ciclo.")
                    else:
                        # Se não achou em nenhuma janela, puxamos o comportamento padrão do dia imediatamente anterior para expor o motivo
                        contagem_padrao = 0
                        data_teste = data_solicitada - timedelta(days=1)
                        for _ in range(dias_trabalho_alvo):
                            if data_teste in dias_trabalhados_mot:
                                contagem_padrao += 1
                            else:
                                break
                            data_teste = data_teste - timedelta(days=1)
                            
                        resultados.append("Indevida")
                        motivos.append(f"Recusada: Não foi localizado bloco completo de {dias_trabalho_alvo} dias trabalhados consecutivamente antes do período de descanso da escala {tipo_escala} (Identificado apenas {contagem_padrao} dias).")

                # Inserindo resultados de validação no DataFrame principal
                df_folgas_base['Resultado_Validacao'] = resultados
                df_folgas_base['Motivo_Detalhado'] = motivos
                
                if 'DATA_CONVERTIDA' in df_folgas_base.columns:
                    df_folgas_base = df_folgas_base.drop(columns=['DATA_CONVERTIDA'])

                # 4. Apresentação do Painel no Streamlit
                st.success("🎯 Análise comportamental de ciclos concluída com sucesso!")
                
                total_analisado = len(df_folgas_base)
                devidas = resultados.count("Devida")
                indevidas = resultados.count("Indevida")
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Total de Linhas Analisadas", total_analisado)
                m2.metric("Folgas Devidas (Aprovar)", devidas)
                m3.metric("Folgas Indevidas (Recusar)", indevidas)

                st.markdown("---")
                st.subheader("📋 Relatório Detalhado de Validações")
                st.dataframe(df_folgas_base, use_container_width=True)

                # Preparação do ficheiro Excel final para download
                import io
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    df_folgas_base.to_excel(writer, index=False, sheet_name='Validação de Ciclos')
                
                st.download_button(
                    label="📥 Baixar Relatório de Ciclos Validado",
                    data=buffer.getvalue(),
                    file_name=f"Resultado_Ciclos_Folgas_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
                    mime="application/vnd.ms-excel"
                )

            except Exception as e:
                st.error(f"Ocorreu uma falha geral no processamento. Detalhe técnico interno: {e}")
else:
    st.info("💡 Por favor, carregue os 3 arquivos acima para liberar o processador de ciclos.")