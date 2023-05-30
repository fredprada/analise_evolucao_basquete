import streamlit as st
from pages.adc_novo_jogo import transform_to_dataframe

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
    🚧 Página inicial em construção 🚧
    """
)

# page_names_to_funcs = {
#     "new_game_forms Demo": new_game_forms
# }

# pages = st.sidebar.selectbox("Escolha uma página", page_names_to_funcs.keys())
# page_names_to_funcs[pages]()