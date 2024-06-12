# USE
# python -m streamlit run dashCredit.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Definir a configuração da página
st.set_page_config(layout="wide")

# Carregar os dados do CSV
df = pd.read_csv("credit_data.csv", sep=",")


# Contar as ocorrências de cada valor na coluna 'default'
ocorrencias_default = df['default'].value_counts().reset_index()
ocorrencias_default.columns = ['default', 'count']

# Configurar a interface do Streamlit
st.title("Gráfico de Ocorrências por Default")

# Criar o gráfico de barras
fig_default = px.bar(ocorrencias_default, x="default", y="count", color="default", title="Ocorrências por Default")

# Mostrar o gráfico no Streamlit
st.plotly_chart(fig_default, use_container_width=True)