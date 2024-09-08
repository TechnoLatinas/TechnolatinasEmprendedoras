import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection


st.set_page_config(
    page_title="TechnoLatinas Emprendedoras",
    page_icon="imgs/TechnolatinasEmprendedorasLogo.png"
    )

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Add logo
st.image("imgs/logo.png", width=200)

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.Nombre} lidera :{row.Emprendimiento}:")

df = conn.read()

# Add title
#st.title("Directorio de TechnoLatinas Emprendedoras")
st.markdown("# :rainbow[Directorio de TechnoLatinas Emprendedoras]")

# st.markdown("""
# ### Our Mission
# Welcome to our Business Directory! This directory has been created to connect you with a wide range of businesses across different sectors, areas, and locations. Our goal is to empower local entrepreneurs and provide a centralized platform for users to explore services and businesses that match their needs.

# ### How to Use
# - Use the **filters in the sidebar** to narrow down your search by selecting the **country**, **area**, or **cost range** that fits your preferences.
# - You can click on the **company links** to visit their websites directly.
# - If you’re looking for specific types of businesses, simply scroll through the directory or apply filters for better results.

# We hope you find what you’re looking for and that this directory helps foster connections between customers and businesses in your area!
# """)

with st.expander("Conoce más sobre el directorio"):
    st.markdown("""
    ### Nuestra Misión
    Este directorio un espacio dedicado a mostrar los increíbles talentos y negocios liderados por mujeres en ciencia, tecnología, ingeniería, artes y matemáticas.
    Nuestra misión es fomentar una comunidad donde las technolatinas emprendedoras puedan prosperar, hacer crecer sus negocios e inspirar a las generaciones futuras.

    ### Cómo usar
    - Utiliza los **filtros de la barra lateral** seleccionando el **país**, **rubro** o **rango de costos** y obtener resultados que se ajusten mejor a tus preferencias.
    - Haz clic en los **enlaces de empresas** para visitar sus sitios web directamente.
                
    Esperamos que este directorio se convierta en una herramienta valiosa para promover conexiones y oportunidades para las technolatinas emprendedoras. 💜
    """)

st.divider()

# Sidebar filters
st.sidebar.header("Filtrar Emprendimientos")

# Dropdowns for filtering based on available fields
country_filter = st.sidebar.selectbox("Selecciona País", options=["Todos"] + df["Country"].unique().tolist())
state_filter = st.sidebar.selectbox("Selecciona Región/Área/Estado", options=["Todos"] + df["State"].unique().tolist())
area_filter = st.sidebar.selectbox("Selecciona Rubro", options=["Todos"] + df["Area"].unique().tolist())

# Slider for filtering by cost
min_cost = int(df["Costo"].min())
max_cost = int(df["Costo"].max())
cost_range = st.sidebar.slider("Selecciona Rango de Costo", min_cost, max_cost, (min_cost, max_cost))

# Filter the data based on the selections
filtered_df = df.copy()

if country_filter != "Todos":
    filtered_df = filtered_df[filtered_df["Country"] == country_filter]

if state_filter != "Todos":
    filtered_df = filtered_df[filtered_df["State"] == state_filter]

if area_filter != "Todos":
    filtered_df = filtered_df[filtered_df["Area"] == area_filter]

# Apply cost filter
filtered_df = filtered_df[(filtered_df["Costo"] >= cost_range[0]) & (filtered_df["Costo"] <= cost_range[1])]

# Display filtered results
for _, row in filtered_df.iterrows():
    st.subheader(f"{row['Nombre']} lidera {row['Emprendimiento']}")
    st.write(f"**Area:** {row['Area']}")
    st.write(f"**Descripción:** {row['Description']}")
    st.write(f"**Costo:** {row['Costo']} {row['Moneda']}")
    st.write(f"**Modalidad:** {row['Modalidad']}")
    st.write(f"**Ubicación:** {row['Country']}, {row['State']}")
    
    # Display web page if available
    if pd.notna(row['PaginaWeb']):
        st.write(f"[Visita el sitio Web]({row['PaginaWeb']})")
    
    st.markdown("---")
    #st.markdown(social_media_section, iconstyle, unsafe_allow_html=True)