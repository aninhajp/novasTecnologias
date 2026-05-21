import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dashboard de Qualidade", layout="wide")
st.title("Dashboard do Engenheiro de Qualidade")

@st.cache_data
def carregar_dados_commits():
    datas_fixas = [
        "2026-05-01", "2026-05-02", "2026-05-03", "2026-05-04", "2026-05-05",
        "2026-05-06", "2026-05-07", "2026-05-08", "2026-05-09", "2026-05-10"
    ] * 3
    
    dados = {
        'Data': pd.to_datetime(datas_fixas),
        'Desenvolvedor': ['Ana Silva'] * 10 + ['Carlos Santos'] * 10 + ['João Souza'] * 10,
        'Linhas_Adicionadas': [120, 45, 200, 15, 90, 300, 40, 85, 110, 50,
                               80, 150, 30, 400, 20, 70, 95, 120, 60, 85,
                               210, 90, 45, 130, 310, 25, 80, 190, 40, 150],
        'Linhas_Removidas': [30, 10, 50, 5, 20, 110, 15, 40, 35, 10,
                             40, 60, 10, 180, 5, 30, 20, 45, 15, 30,
                             90, 40, 15, 60, 140, 10, 35, 70, 10, 80],
        'Bugs_Gerados': [1, 0, 3, 0, 1, 4, 0, 1, 2, 0,
                         2, 1, 0, 5, 0, 1, 1, 2, 0, 1,
                         0, 1, 0, 2, 3, 0, 1, 2, 0, 1]
    }
    return pd.DataFrame(dados)

df_commits = carregar_dados_commits()

st.sidebar.header("Filtros de Análise")

dev_selecionado = st.sidebar.radio(
    "Selecione o Desenvolvedor:",
    options=df_commits['Desenvolvedor'].unique()
)

df_dev = df_commits[df_commits['Desenvolvedor'] == dev_selecionado].sort_values('Data')

st.subheader(f"Análise de Desempenho: {dev_selecionado}")

total_adicionadas = df_dev['Linhas_Adicionadas'].sum()
total_bugs = df_dev['Bugs_Gerados'].sum()

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total de Linhas Adicionadas", value=f"{total_adicionadas:,}")
with col2:
    st.metric(label="Total de Bugs Gerados", value=total_bugs)

st.write("### Evolução Temporal de Bugs Gerados")
st.line_chart(data=df_dev, x='Data', y='Bugs_Gerados')

st.write("---")
st.write("### Auditoria de Qualidade Coletiva")

if st.button("Exibir Dev com maior média de bugs por commit", key="btn_auditoria"):
    media_bugs_dev = df_commits.groupby('Desenvolvedor')['Bugs_Gerados'].mean()
    pior_dev = media_bugs_dev.idxmax()
    maior_media = media_bugs_dev.max()
    
    st.error(f"O desenvolvedor com maior média de bugs por commit é {pior_dev} com uma média de {maior_media:.2f} bugs por commit.")