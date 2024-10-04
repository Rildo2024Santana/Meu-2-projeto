import streamlit as st
import pandas as pd

# Para colocar o icon aperta (windows mais ponto)
# Para colocar no centro da tela (Centered), para colocar a tela toda (Wide)

st.set_page_config(
    page_title="Meu sistema Streamlit",
    page_icon="🕹️",
    layout="wide")

lateral = st.sidebar
data = lateral.date_input("Selecione a dara")
cidade = lateral.selectbox("Selecione a cidade",
                          ["Belo Horizonte","Rio de Janeiro","Manaus"])


@st.cache_data
def carregar_dados():
    dados = pd.read_csv("acidentes.csv")
    return dados

# Tenho que abrir uma seção (session_state), ele cria um dicionario na menoria do computador
# Para vc de outra pagima chamar os arquino de outra pagima.

dados = carregar_dados()
st.session_state["dados"] = dados
st.session_state["data"] = data
st.session_state["cidade"] = cidade

st.title("Dados")

# você colocando Col isso quer dizer contidade de colunas na tela , vc tb pode dar pocentagem para elas 
# 60% para uma e 40% pocento para outra({0,60, 0,40}) tem que tirar o numero 2 certo.

col1, col2 = st.columns(2)

# Agora vc vai trocar os st por col1 , col2 isso faz vc colocar cada uma ao lado planilha mais pocentagem.

tabela = col1.dataframe(dados)

municipio = dados["municipio"].value_counts()
col2.bar_chart(municipio)

# Para colocar a cidade na parte de baixou da planilha .

st.subheader("Cidade")
st.write(f"A cidade selecionada foi {cidade}")

# Vamos crir pagimas e ler dados de uma pagima em outra pagima,
# vc tem que criar uma pasta chamada pages, dentro dela vc vai cria arquivos,
#  dados do sistema .py,dados do cliente.py

