# from evolucao_basquete import get_dados_notion, treated_data
import streamlit as st
# import numpy as np
# import scipy
# from scipy.stats import shapiro
# import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px
import os

# defining page settings
st.set_page_config(
    layout="wide",  
    page_title="🏀 Evolução de Basquete 🏀")

token = os.getenv('NOTION_BASQUETE_TOKEN')
database_id = os.getenv('NOTION_DATABASE_ID')

dados_coletados = get_dados_notion(token, database_id)
df_treated_data = treated_data(dados_coletados)

# introducing context for the analysis
st.title("Análise de evolução de Basquete")
st.header("Essa análise é focada em entender se há uma tendência entre as variáveis coletadas depois de um jogo de basquete.")
st.write("""Gosto bastante de jogar basquete, e quero entender se há essa correlação entre as variáveis, e se estou tendo algum avanço na nota que dou para meu jogo.""")

# showing descriptive statistics metrics and some insights
col1, col2 = st.columns([2,3])
col1.write(df_treated_data.describe())

col2.subheader("Boxplot dos dias que joguei")
fig = px.line(df_treated_data.sort_values(by='dia', ascending=True), 
                 y = 'pai', 
                 x = 'dia',
                 markers=True)
fig.update_layout(
    autosize=False,
    width=600,
    height=300,
    margin=dict(
        l=30,
        r=30,
        b=60,
        t=30,
        pad=4
    ))
col2.plotly_chart(fig, theme=None)