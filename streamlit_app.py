from evolucao_basquete import get_dados_notion, treated_data
import streamlit as st
import plotly.express as px
import os

# definindo configurações iniciais da página
st.set_page_config(
    layout="wide",  
    page_title="🏀 Análise de performance")

# coletando as credenciais para acessar API
token = os.getenv('NOTION_BASQUETE_TOKEN')
database_id = os.getenv('NOTION_DATABASE_ID')

# chamando funções de coleta e tratamento dos dados
dados_coletados = get_dados_notion(token, database_id)
df_treated_data = treated_data(dados_coletados)

# introdução de contexto da análise
st.title("Análise de evolução de Basquete")
st.header("Essa análise é focada em entender se há uma tendência entre as variáveis coletadas depois de um jogo de basquete.")
st.write("""Gosto bastante de jogar basquete, e quero entender se há essa correlação entre as variáveis, e se estou tendo algum avanço na nota que dou para meu jogo.""")

# apresentação de análise descritiva do dataframe
col1, col2 = st.columns([2,3])
col1.write(df_treated_data.describe())

# primeiro gráfico sobre 
fig = px.line(df_treated_data.sort_values(by='dia', ascending=True), 
                 y = 'nota', 
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
col2.caption("Gráfico do índice 'PAI' dos dias que joguei.")
col2.caption("PAI é o **personal activity intelligence, da Amazfit, que dá uma nota ao exercício físico de acordo com certos critérios.")
