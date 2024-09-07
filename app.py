import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

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
st.title("Directorio de TechnoLatinas Emprendedoras")

# Sidebar filters
st.sidebar.header("Filtrar Emprendimientos")

# Dropdowns for filtering based on available fields
country_filter = st.sidebar.selectbox("Selecciona País", options=["All"] + df["Country"].unique().tolist())
state_filter = st.sidebar.selectbox("Selecciona Región", options=["All"] + df["State"].unique().tolist())
area_filter = st.sidebar.selectbox("Selecciona Rubro", options=["All"] + df["Area"].unique().tolist())

# Slider for filtering by cost
min_cost = int(df["Costo"].min())
max_cost = int(df["Costo"].max())
cost_range = st.sidebar.slider("Select Cost Range", min_cost, max_cost, (min_cost, max_cost))

# Filter the data based on the selections
filtered_df = df.copy()

if country_filter != "All":
    filtered_df = filtered_df[filtered_df["Country"] == country_filter]

if state_filter != "All":
    filtered_df = filtered_df[filtered_df["State"] == state_filter]

if area_filter != "All":
    filtered_df = filtered_df[filtered_df["Area"] == area_filter]

# Apply cost filter
filtered_df = filtered_df[(filtered_df["Costo"] >= cost_range[0]) & (filtered_df["Costo"] <= cost_range[1])]

# Display filtered results
for _, row in filtered_df.iterrows():
    st.subheader(f"{row['Nombre']} leads {row['Emprendimiento']}")
    st.write(f"**Area:** {row['Area']}")
    st.write(f"**Description:** {row['Description']}")
    st.write(f"**Cost:** {row['Costo']} {row['Moneda']}")
    st.write(f"**Modalidad:** {row['Modalidad']}")
    st.write(f"**Location:** {row['Country']}, {row['State']}")
    
    # Display web page if available
    if pd.notna(row['PaginaWeb']):
        st.write(f"[Visit Website]({row['PaginaWeb']})")
    
    st.markdown("---")
    #st.markdown(slider_style, unsafe_allow_html=True)