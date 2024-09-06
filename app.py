import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.Nombre} lidera :{row.Emprendimiento}:")

df = conn.read()

# Add title
st.title("Business Directory")

# Sidebar filters
st.sidebar.header("Filter Businesses")

# Dropdowns for filtering based on available fields
country_filter = st.sidebar.selectbox("Select Country", options=["All"] + df["Country"].unique().tolist())
area_filter = st.sidebar.selectbox("Select Area", options=["All"] + df["Area"].unique().tolist())

# Filter the data based on the selections
filtered_df = df.copy()

if country_filter != "All":
    filtered_df = filtered_df[filtered_df["Country"] == country_filter]

if area_filter != "All":
    filtered_df = filtered_df[filtered_df["Area"] == area_filter]

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