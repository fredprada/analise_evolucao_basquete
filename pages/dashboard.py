import streamlit as st
# import plotly.express as px
import transform_to_dataframe

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.header('Sobre o seu último jogo')
    dias_jogados = transform_to_dataframe()
    st.metric(label="Número de dias jogados", value=dias_jogados, delta=1)