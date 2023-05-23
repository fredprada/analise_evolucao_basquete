from evolucao_basquete import get_dados_notion, treated_data
import streamlit as st
# import numpy as np
# import scipy
# from scipy.stats import shapiro
# import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px

# defining page settings
st.set_page_config(
    layout="wide",  
    page_title="🏀 Evolução de Basquete 🏀")

dados_coletados = get_dados_notion()
df_treated_data = treated_data(dados_coletados)

# introducing context for the analysis
st.title("Análise de evolução de Basquete")
st.header("Essa análise é focada em entender se há uma tendência entre as variáveis coletadas depois de um jogo de basquete.")
st.write("""Gosto bastante de jogar basquete, e quero entender se há essa correlação entre as variáveis, e se estou tendo algum avanço na nota que dou para meu jogo.""")

# showing descriptive statistics metrics and some insights
# col1, col2, _ = st.columns([3,2,1])
col1 = st.columns([3])
col1.write(df_treated_data.describe())
# col2.markdown("- 75% dos ids possuem até 20 clientes somente.")
# col2.markdown("- 75% dos ids fizeram até 204 compras.")
# col2.markdown("- 75% dos ids não possuem nenhum fornecedor.")
# col2.markdown("- O número de outliers representa uma parcela perto de 25% dos conjuntos analisados.")
# col2.markdown("- As médias são muito afetadas pelos outliers do conjunto de dados.")
# col2.markdown("- Será necessário analisar as diferentes variáveis de acordo com essas parcelas, tanto dos ids até 75% quanto os 25% restantes.")


st.subheader("Box Plot dos dias que joguei")
fig = px.box(df_treated_data['pai'], x="dia")
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
st.plotly_chart(fig, theme=None)