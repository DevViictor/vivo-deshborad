import streamlit as st
import pandas as pd
from PIL import Image



arquivo = "data.xlsx"
arquivo_vendedores = "vendedores.xlsx"
imagem = imagem = Image.open('imagem/vivop.png')
Pos = "Pos.xlsx"
arquivo2 = "data2.xlsx"


ANA = pd.read_excel(arquivo_vendedores,sheet_name="ANA" ,engine="openpyxl")

ANDERSON = pd.read_excel(arquivo_vendedores,sheet_name="ANDERSON",engine="openpyxl")

CAROL = pd.read_excel(arquivo_vendedores,sheet_name= "CAROL",engine="openpyxl")

DAVIDG = pd.read_excel(arquivo_vendedores,sheet_name="DAVIDG",engine="openpyxl")

DEBORA = pd.read_excel(arquivo_vendedores,sheet_name= "DEBORA",engine="openpyxl")

LENE = pd.read_excel(arquivo_vendedores,sheet_name="LENE",engine="openpyxl")

WILLER = pd.read_excel(arquivo_vendedores,sheet_name= "WILLER",engine="openpyxl")





ANA2 = pd.read_excel(Pos,sheet_name="ANA" ,engine="openpyxl")

ANDERSON2 = pd.read_excel(Pos,sheet_name="ANDERSON",engine="openpyxl")

CAROL2 = pd.read_excel(Pos,sheet_name= "CAROL",engine="openpyxl")

DAVIDG2 = pd.read_excel(Pos,sheet_name="DAVIDG",engine="openpyxl")

DEBORA2 = pd.read_excel(Pos,sheet_name= "DEBORA",engine="openpyxl")

LENE2 = pd.read_excel(Pos,sheet_name="LENE",engine="openpyxl")

WILLER2 = pd.read_excel(Pos,sheet_name= "WILLER",engine="openpyxl")


sheetsT = pd.read_excel(arquivo,sheet_name= "Total",engine="openpyxl")
contcolums = sheetsT["Produto"].isin(["CONTROLE"]).value_counts()

sheetsT2 = pd.read_excel(arquivo2,sheet_name= "Total",engine="openpyxl")
contcolums2 = sheetsT["Produto"].isin(["PÓS PAGO"]).value_counts()





ANAT = ANA["Produto"].isin(["CONTROLE"]).value_counts()
ANDERSONT = ANDERSON["Produto"].isin(["CONTROLE"]).value_counts()
CAROLT = CAROL["Produto"].isin(["CONTROLE"]).value_counts()
DAVIDGT = DAVIDG["Produto"].isin(["CONTROLE"]).value_counts()
DEBORAT = DEBORA["Produto"].isin(["CONTROLE"]).value_counts()
LENET = LENE["Produto"].isin(["CONTROLE"]).value_counts()
WILLERT = WILLER["Produto"].isin(["CONTROLE"]).value_counts()

ANAT2 = ANA2["Produto"].isin(["PÓS PAGO"]).value_counts()
ANDERSONT2 = ANDERSON2["Produto"].isin(["PÓS PAGO"]).value_counts()
CAROLT2 = CAROL2["Produto"].isin(["PÓS PAGO"]).value_counts()
DAVIDGT2 = DAVIDG2["Produto"].isin(["PÓS PAGO"]).value_counts()
DEBORAT2 = DEBORA2["Produto"].isin(["PÓS PAGO"]).value_counts()
LENET2 = LENE2["Produto"].isin(["PÓS PAGO"]).value_counts()
WILLERT2 = WILLER2["Produto"].isin(["PÓS PAGO"]).value_counts()





windows = st.sidebar.radio("GUIA DE NAVEGAÇÃO", ["Inicio","Controle", "Pós" ,"Seguro","Gráficos","Sobre"])


if windows == "Controle":
    st.text("ANA")
    st.dataframe(ANA)
    st.dataframe(ANAT)

    st.text("ANDERSON")
    st.dataframe(ANDERSON)
    st.dataframe(ANDERSONT)

    st.text("CAROL")
    st.dataframe(CAROL)
    st.dataframe(CAROLT)

    st.text("DAVIDG")
    st.dataframe(DAVIDG)
    st.dataframe(DAVIDGT)

    st.text("DEBORA")
    st.dataframe(DEBORA)
    st.dataframe(DEBORAT)

    st.text("LENE")
    st.dataframe(LENE)
    st.dataframe(LENET)

    st.text("WILLER")
    st.dataframe(WILLER)
    st.dataframe(WILLERT)

    st.text("Total")
    st.dataframe(contcolums)

elif windows == "Inicio":
    st.header("Vivo Dashborad")
    st.subheader("Dashborad voltado para análise de produtos")
   
    st.image(imagem)

elif windows == "Pós":
    st.text("ANA")
    st.dataframe(ANA2)
    st.dataframe(ANAT2)

    st.text("ANDERSON")
    st.dataframe(ANDERSON2)
    st.dataframe(ANDERSONT2)

    st.text("CAROL")
    st.dataframe(CAROL2)
    st.dataframe(CAROLT2)

    st.text("DAVIDG")
    st.dataframe(DAVIDG2)
    st.dataframe(DAVIDGT2)

    st.text("DEBORA")
    st.dataframe(DEBORA2)
    st.dataframe(DEBORAT2)

    st.text("LENE")
    st.dataframe(LENE2)
    st.dataframe(LENET2)

    st.text("WILLER")
    st.dataframe(WILLER2)
    st.dataframe(WILLERT2)


elif windows == "Sobre":
     st.text("Dados coletados dos consultores")