import streamlit as st

# Todos arquivos estão vindo da pasta app.py, foi criado um dicionario.
st.set_page_config(
    page_title="Dados do Usuário",
    page_icon="♟️")

st.title("Dados do Usuário")
st.dataframe(st.session_state["dados"])

