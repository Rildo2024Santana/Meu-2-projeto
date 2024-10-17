import streamlit as st

st.set_page_config(
    page_title="Dados do Sistema",
    page_icon="♟️")

cidade = st.session_state["cidade"]

st.title("Dados do Sistema")
st.text(st.session_state["data", format="DD/MM/YYY"])
st.text(st.session_state["cidade"])

