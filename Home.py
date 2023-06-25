import streamlit as st

st.set_page_config(page_title = "Evolução de Basquete", page_icon = "🏀")

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
    Esse projeto surgiu da vontade de saber se meu jogo está melhorando, não somente do modo subjetivo da coisa, que é literalmente vendo se acerto mais cestas, mas também utilizando dados pra isso.
    Outros pontos que quis melhorar foram minha habilidade com banco de dados, ETL, análise e visualização de dados, storytelling e programação.
    """
)
st.write(
    """
    Navegue no menu lateral para:
    - Adicionar um novo jogo
    - Ver seu Dashboard

    O Dashboard possui informações sobre quantidade de jogos, número de PAI ganho, calorias queimadas, nota do jogo, entre outros valores!
    """
)