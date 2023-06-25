import streamlit as st

st.set_page_config(page_title = "Evolução de Basquete", page_icon = "🏀")

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Saiba mais sobre o projeto', on_click=click_button)

if st.session_state.button:
    st.write(
    """
    Esse projeto surgiu da vontade de saber se meu jogo está melhorando, não somente do modo subjetivo da coisa, que é literalmente vendo se acerto mais cestas, mas também utilizando dados pra isso.
    Outros pontos que quis melhorar foram minha habilidade com banco de dados, ETL, análise e visualização de dados, storytelling e programação.
    """
        )
else:
     pass


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