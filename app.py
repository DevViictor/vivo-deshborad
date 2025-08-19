import pandas as pd
import streamlit as st
from graficos import grafico_controle_melt , grafico_pós_melt , grafico_fixa_melt , grafico_sva_melt , grafico_seguro_melt , grafico_aparelho_melt , grafico_acessorio_melt
from PIL import Image

imagem = imagem = Image.open('imagem/estoque.png')
windows = st.sidebar.radio("GUIA DE NAVEGAÇÃO", ["Inicio"])

st.header("Dashboard voltado para análise de qualidade")
st.image(imagem)

st.subheader("Gráfico relacionado ao mês")

st.subheader("CONTROLE")
st.bar_chart(grafico_controle_melt.set_index('consultor'))

st.subheader("PÓS")
st.bar_chart(grafico_pós_melt.set_index('consultor'))

st.subheader("FIXA")
st.bar_chart(grafico_fixa_melt.set_index('consultor'))

st.subheader("SVA")
st.bar_chart(grafico_sva_melt.set_index("consultor"))

st.subheader("SEGURO")
st.bar_chart(grafico_seguro_melt.set_index("consultor"))

st.subheader("APARELHO")
st.bar_chart(grafico_aparelho_melt.set_index("consultor"))

st.subheader("ACESSÓRIO")
st.bar_chart(grafico_acessorio_melt.set_index("consultor"))