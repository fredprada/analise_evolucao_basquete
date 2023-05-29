import streamlit as st
# import plotly.express as px

###################################################################
# Defining page properties and title, header and subheader
st.set_page_config(page_title = "📈 Dashboard", page_icon = "📈")





# # introdução de contexto da análise
# st.title("Análise de evolução de Basquete")
# st.header("Essa análise é focada em entender se há uma tendência entre as variáveis coletadas depois de um jogo de basquete.")
# st.write("""Gosto bastante de jogar basquete, e quero entender se há essa correlação entre as variáveis, e se estou tendo algum avanço na nota que dou para meu jogo.""")

# # apresentação de análise descritiva do dataframe
# col1, col2 = st.columns([2,3])
# col1.write(df_raw_data.describe())

# # primeiro gráfico de linha mostrando a nota pelo dia
# col2.subheader("Gráfico de Nota pelo dia do jogo")
# fig = px.line(df_raw_data.sort_values(by='dia', ascending=True), 
#                  y = 'nota', 
#                  x = 'dia',
#                  markers=True)
# fig.update_layout(
#     autosize=False,
#     width=600,
#     height=300,
#     margin=dict(
#         l=30,
#         r=30,
#         b=60,
#         t=30,
#         pad=4
#     ))
# col2.plotly_chart(fig, theme=None)
# col2.caption("Gráfico do índice 'PAI' dos dias que joguei.")
# col2.caption("PAI é o *personal activity intelligence*, da Amazfit, que dá uma nota ao exercício físico de acordo com certos critérios.")

# st.metric(label="Número de dias jogados", value=dias_jogados, delta=1)