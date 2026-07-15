import streamlit as st
import pandas as pd
import glob
import numpy as np
from datetime import datetime
from io import BytesIO

st.set_page_config(
    page_title="SIGEP PRODEMU",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Procesamiento de datos SIGEP")
st.write("Suba uno o más archivos Excel descargados desde SIGEP.")

uploaded_file = st.file_uploader("Upload a Excel file", type=["xlsx"])


