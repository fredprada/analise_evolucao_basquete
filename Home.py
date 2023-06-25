import streamlit as st

###################################################################
# Defining the page title
st.set_page_config(page_title = "Evolução de Basquete", page_icon = "🏀", layout="wide")

###################################################################
# Adding a GIF to the main page
col1, col2, col3 = st.columns([1,6,1])
col1.write("")
col2.image("https://media.tenor.com/_u-gDFZQuIQAAAAC/basketball-sports.gif", width=400)
col3.write("")

###################################################################
# Creating a "learn more" section
if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Saiba mais sobre o projeto ⮟', on_click=click_button)

if st.session_state.button:
    st.write(
    """
    Esse projeto surgiu da vontade de saber a minha evolução jogando basquete, já que eu jogava na adolescência, parei durante vários anos, e retornei com 25 anos.\n
    Mas não queria entender essa evolução somente de modo subjetivo, que é literalmente vendo se acerto mais cestas, mas também utilizando dados pra isso.\n
    Outros pontos que quis melhorar foram minha habilidade com banco de dados, ETL, análise e visualização de dados, storytelling e programação.
    """
        )

###################################################################
# Defining the title and texts of the page
st.title("""
        Aqui você vai conseguir entender um pouco mais da sua \
        evolução e estatísticas!
        """)
st.subheader("""
        Fique a vontade para analisar \
        e saber mais sobre cada jogo seu!
        """)

st.write(
    """
    Sobre o app, navegue no menu lateral para:
    - Adicionar um novo jogo
    - Ver seu Dashboard

    O Dashboard possui informações sobre quantidade de jogos, número de PAI ganho, calorias queimadas, nota do jogo, entre outros valores!
    """
)