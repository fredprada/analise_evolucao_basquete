import streamlit as st

def new_game_forms():
    import streamlit as st

    st.write(
        """
        PÁGINA PARA ADC NOVO JOGO
        """
    )

page_names_to_funcs = {
    "new_game_forms Demo": new_game_forms
}

pages = st.sidebar.selectbox("Escolha uma página", page_names_to_funcs.keys())
page_names_to_funcs[pages]()