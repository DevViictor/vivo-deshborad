import streamlit as st
import pandas as pd



arquivo = "data.xlsx"
arquivo_vendedores = "vendedores.xlsx"



ANA = pd.read_excel(arquivo_vendedores,sheet_name="ANA" ,engine="openpyxl")

ANDERSON = pd.read_excel(arquivo_vendedores,sheet_name="ANDERSON",engine="openpyxl")

CAROL = pd.read_excel(arquivo_vendedores,sheet_name= "CAROL",engine="openpyxl")

DAVIDG = pd.read_excel(arquivo_vendedores,sheet_name="DAVIDG",engine="openpyxl")

DEBORA = pd.read_excel(arquivo_vendedores,sheet_name= "DEBORA",engine="openpyxl")

LENE = pd.read_excel(arquivo_vendedores,sheet_name="LENE",engine="openpyxl")

WILLER = pd.read_excel(arquivo_vendedores,sheet_name= "WILLER",engine="openpyxl")




sheetsT = pd.read_excel(arquivo,sheet_name= "Total",engine="openpyxl")




contcolums = sheetsT["Total"].isin(["CONTROLE"]).value_counts()

ANAT = ANA["Produto"].isin(["CONTROLE"]).value_counts()
ANDERSONT = ANDERSON["Produto"].isin(["CONTROLE"]).value_counts()
CAROLT = CAROL["Produto"].isin(["CONTROLE"]).value_counts()
DAVIDGT = DAVIDG["Produto"].isin(["CONTROLE"]).value_counts()
DEBORAT = DEBORA["Produto"].isin(["CONTROLE"]).value_counts()
LENET = LENE["Produto"].isin(["CONTROLE"]).value_counts()
WILLERT = WILLER["Produto"].isin(["CONTROLE"]).value_counts()




windows = st.sidebar.radio("GUIA DE NAVEGAÇÃO", ["Inicio","Tabela", "Gráficos"])

if windows == "Tabela":
    st.text("ANA")
    st.dataframe(ANA)
    st.dataframe(ANAT - 1)
    st.text("ANDERSON")
    st.dataframe(ANDERSON)
    st.dataframe(ANDERSONT - 1)
    st.text("CAROL")
    st.dataframe(CAROL)
    st.dataframe(CAROLT - 1)
    st.text("DAVIDG")
    st.dataframe(DAVIDG)
    st.dataframe(DAVIDGT - 1)
    st.text("DEBORA")
    st.dataframe(DEBORA)
    st.dataframe(DEBORAT - 1)
    st.text("LENE")
    st.dataframe(LENE)
    st.dataframe(LENET - 1)
    st.text("WILLER")
    st.dataframe(WILLER)
    st.dataframe(WILLERT - 1)
    st.text("Total")
    st.dataframe(contcolums)

elif windows == "Inicio":
    st.header("Vivo Deshborad")
    st.subheader("Deshborad voltados para análise de produtos")