import streamlit as st
import pypdf
import io

# Configuração da página
st.set_page_config(page_title="Unificador de PDF Profissional", page_icon="📄")

st.title("📄 Unificador de PDFs")
st.markdown("""
Misture vários arquivos PDF em um só, mantendo **100% da qualidade original**.
A ordem de união seguirá a ordem da lista abaixo.
""")

# Upload dos arquivos
# O Streamlit mantém a ordem em que os arquivos são selecionados/exibidos
arquivos_pdf = st.file_uploader(
    "Arraste os PDFs aqui ou clique para selecionar", 
    type="pdf", 
    accept_multiple_files=True
)

if arquivos_pdf:
    st.subheader("Fila de Processamento")
    
    # Exibe a ordem para o usuário conferir
    for i, arquivo in enumerate(arquivos_pdf, 1):
        st.write(f"**[{i}]** {arquivo.name}")

    st.divider()

    # Botão para processar
    if st.button("🚀 Gerar PDF Único", use_container_width=True):
        if len(arquivos_pdf) < 2:
            st.warning("Por favor, adicione pelo menos 2 arquivos para unificar.")
        else:
            with st.spinner("Unificando arquivos..."):
                try:
                    # Criar o Writer (Unificador)
                    merger = pypdf.PdfWriter()
                    
                    # Adicionar cada arquivo na ordem da lista
                    for pdf in arquivos_pdf:
                        # O Streamlit entrega um objeto BytesIO, que o pypdf aceita direto
                        merger.append(pdf)
                    
                    # Salvar o resultado em um objeto de memória para download
                    output_pdf = io.BytesIO()
                    merger.write(output_pdf)
                    merger.close()
                    
                    # Preparar o arquivo para o botão de download
                    st.success("✅ PDF unificado com sucesso!")
                    
                    st.download_button(
                        label="⬇️ Baixar PDF Unificado",
                        data=output_pdf.getvalue(),
                        file_name="PDF_Unificado_Final.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
                    
                except Exception as e:
                    st.error(f"Erro ao processar os arquivos: {e}")

else:
    st.info("Aguardando upload de arquivos...")

# Rodapé informativo
st.caption("Nota: Este app não armazena seus arquivos. O processamento é feito em memória e descartado após a sessão.")