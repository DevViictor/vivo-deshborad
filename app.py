import streamlit as st
import pandas as pd
from PIL import Image
from readfile_controle_pos import ANA, ANDERSON , CAROL ,DEBORA , DAVIDG , WILLER , LENE
from readfile_controle_pos import ANA2, ANDERSON2 , CAROL2 ,DEBORA2 , DAVIDG2 , WILLER2 , LENE2
from readfile_Total_controle_pos import totalc
from readfile_Total_controle_pos import ANAT, ANDERSONT , CAROLT , DEBORAT , DAVIDGT , WILLERT , LENET
from readfile_Total_controle_pos import ANAT2, ANDERSONT2 , CAROLT2 , DEBORAT2 , DAVIDGT2 , WILLERT2 , LENET2


imagem = imagem = Image.open('imagem/vivop.png')


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
    st.dataframe(DAVIDG)
    st.dataframe(DEBORAT)

    st.text("LENE")
    st.dataframe(LENE)
    st.dataframe(LENET)

    st.text("WILLER")
    st.dataframe(WILLER)
    st.dataframe(WILLERT)

    st.text("Total")
    st.dataframe(totalc)

elif windows == "Inicio":
    st.header("Vivo Dashborad")
    st.subheader("Dashborad voltado para análise de produtos")
   
    st.image(imagem)

elif windows == "Pós":
    st.text("ANA")
    st.dataframe(ANA)
    st.dataframe(ANAT2)

    st.text("ANDERSON")
    st.dataframe(ANDERSON)
    st.dataframe(ANDERSONT2)

    st.text("CAROL")
    st.dataframe(CAROL)
    st.dataframe(CAROLT2)

    st.text("DAVIDG")
    st.dataframe(DAVIDG)
    st.dataframe(DAVIDGT2)

    st.text("DEBORA")
    st.dataframe(DEBORA)
    st.dataframe(DEBORAT2)

    st.text("LENE")
    st.dataframe(LENE)
    st.dataframe(LENET2)

    st.text("WILLER")
    st.dataframe(WILLER)
    st.dataframe(WILLERT2)


elif windows == "Sobre":
     st.text("Dados coletados dos consultores")