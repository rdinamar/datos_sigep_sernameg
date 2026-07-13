import streamlit as st
from procesamiento import procesar_archivos

st.set_page_config(
    page_title="SIGEP PRODEMU",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Procesamiento de datos SIGEP")
st.write("Suba uno o más archivos Excel descargados desde SIGEP.")

uploaded_files = st.file_uploader(
    "Seleccione los archivos Excel",
    type=["xlsx"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(f"Se cargaron {len(uploaded_files)} archivos.")

    if st.button("Procesar información"):

        with st.spinner("Procesando información..."):

            output, nombre = procesar_archivos(uploaded_files)

        st.success("Proceso finalizado correctamente.")

        st.download_button(
            label="📥 Descargar archivo Excel",
            data=output,
            file_name=nombre,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
