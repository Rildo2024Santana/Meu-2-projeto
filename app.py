import streamlit as st
import pandas as pd

# Para colocar o icon aperta (windows mais ponto)
# Para colocar no centro da tela (Centered), para colocar a tela toda (Wide)

st.set_page_config(
    page_title="Meu sistema Streamlit",
    page_icon="🚥",
    layout="wide")

lateral = st.sidebar
data = lateral.date_input("Selecione a data", format="DD/MM/YYYY")
cidade = lateral.multiselect("Pesquisa do censo em 2010, Cidades mais populosas do Brasil?",
                          [ "  " ,"São Paulo (SP): 11.451.245","Rio de Janeiro (RJ): 6.211.423","Brasília (DF): 2.817.068",
                           "Fortaleza (CE): 2.428.678","Salvador (BA): 2.418.005","Belo Horizonte (MG): 2.315.560","Manaus (AM): 2.063.547",
                           "Curitiba (PR): 1.773.733","Recife (PE): 1.488.920","Goiânia (GO): 1.437.237","Porto Alegre (RS): 1.332.570",
                           "Belém (PA): 1.303.389","Guarulhos (SP): 1.291.784","Campinas (SP): 1.138.309","São Luís (MA): 1.037.775",
                           "Maceió (AL): 957.916","Campo Grande (MS): 897.938","São Gonçalo (RJ): 896.744","Teresina (PI): 866.300",
                           "João Pessoa (PB): 833.932",])

@st.cache_data
def carregar_dados():
    dados = pd.read_csv("acidentes.csv")
    return dados

# Tenho que abrir uma seção (session_state), ele cria um dicionario na menoria do computador
# Para vc de outra pagima chamar os arquino de outra pagima.

dados = carregar_dados()
st.session_state["dados"] = dados
st.session_state["data"] = data,format="DD/MM/YYYY"
st.session_state["cidade"] = cidade

st.title("Dados")

# você colocando Col isso quer dizer quantidade de colunas na tela , vc tb pode dar pocentagem para elas 
# 60% para uma e 40% pocento para outra({0,60, 0,40}) tem que tirar o numero 2 certo.

col1, col2 = st.columns(2)

# Agora vc vai trocar os st por col1 , col2 isso faz vc colocar cada uma ao lado planilha mais pocentagem.

tabela = col1.dataframe(dados)

# vou trocar bar_chart para line_chart.

mostrar_grafico = st.toggle("Mostrar gráfico")

if mostrar_grafico:
    municipio = dados["municipio"].value_counts()
    col2.line_chart(municipio)

# Para colocar a cidade na parte de baixou da planilha .

st.subheader("cidade")
st.write(f"A cidade selecionada foi:   {cidade}")

# Vamos crir pagimas e ler dados de uma pagima em outra pagima,
# vc tem que criar uma pasta chamada pages, dentro dela vc vai cria arquivos,
#  dados do sistema .py,dados do cliente.py

