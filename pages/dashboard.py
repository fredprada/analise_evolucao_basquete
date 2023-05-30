import streamlit as st
# import plotly.express as px
import sys
sys.path.insert(0, "../pages")

try:
    from adc_novo_jogo import transform_to_dataframe
except ImportError:
    print('No Import')

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.header('Sobre o seu último jogo')
    dias_jogados = transform_to_dataframe()
    st.metric(label="Número de dias jogados", value=dias_jogados, delta=1)