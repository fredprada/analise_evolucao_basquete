import streamlit as st
# import plotly.express as px
from functions import transform_to_dataframe

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard")

col1, col2 = st.columns(2)

df_all_info = transform_to_dataframe()
dias_jogados = len(df_all_info['dia'].value_counts())

with col1:
    st.header('Sobre o seu último jogo')
    st.metric(label="Número de dias jogados", value=dias_jogados, delta=1)