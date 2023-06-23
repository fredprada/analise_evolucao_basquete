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
    🚧 Página inicial em construção 🚧
    """
)

# page_names_to_funcs = {
#     "new_game_forms Demo": new_game_forms
# }

# pages = st.sidebar.selectbox("Escolha uma página", page_names_to_funcs.keys())
# page_names_to_funcs[pages]()
page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
    }
    </style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)