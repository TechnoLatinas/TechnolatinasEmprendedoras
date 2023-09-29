import streamlit as st
import pandas as pd
import requests
import io

# Título de la aplicación
st.title("Directorio desde CSV")

# Descarga y lee el archivo CSV desde Google Drive
file_id = '1YZA6d88XLkDo2tROBIQymnV8J1obBnd4GDn2HXzHsXE'
url = f'https://drive.google.com/uc?id={file_id}'
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

print("cargo")
print(df)
# Mostrar los datos como un directorio
st.header("Directorio de Datos")

# Crear un filtro para seleccionar columnas
columnas = df.columns
columna_seleccionada = st.selectbox("Seleccione una columna:", columnas)

# Mostrar los datos de la columna seleccionada
if columna_seleccionada:
    st.write(df[columna_seleccionada])
