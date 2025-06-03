import streamlit as st
import pandas as pd
from PIL import Image
from readfile_controle_pos import ANA, ANDERSON , CAROL ,DEBORA , DAVIDG , WILLER , LENE
from readfile_controle_pos import ANA2, ANDERSON2 , CAROL2 ,DEBORA2 , DAVIDG2 , WILLER2 , LENE2
from readfile_Total_controle_pos_seguro import totalc , cont_pos, cont_seguro
from readfile_Total_controle_pos_seguro import ANAT, ANDERSONT , CAROLT , DEBORAT , DAVIDGT , WILLERT , LENET
from readfile_Total_controle_pos_seguro import ANAT2, ANDERSONT2 , CAROLT2 , DEBORAT2 , DAVIDGT2 , WILLERT2 , LENET2 
from readfile_Total_controle_pos_seguro import ANA_SEGUROT,ANDERSON_SEGUROT,CAROL_SEGUROT,DAVIDG_SEGUROT,DEBORA_SEGUROT,LENE_SEGUROT,WILLER_SEGUROT
from readfile_grafico import df_melt , df_melt2 , df_melt3
from redfile_seguro import ANA_SEGURO,ANDERSON_SEGURO,CAROL_SEGURO,DAVIDG_SEGURO,DEBORA_SEGURO,LENE_SEGURO,WILLER_SEGURO,seguro_total

imagem = imagem = Image.open('imagem/vivop.png')


windows = st.sidebar.radio("GUIA DE NAVEGAÇÃO", ["Inicio","Tabela(Controle)", "Tabela(Pós)" ,"Tabela(Seguro)","Sobre"])
box_mês = st.sidebar.selectbox("Selecione o mês desejado:", ["Maio","Junho"])



if windows == "Tabela(Controle)" and box_mês == "Maio":
    st.header("Tabela Controle")
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

elif windows == "Inicio" and box_mês == "Maio":
    st.header("Vivo Dashborad")
    st.subheader("Dashborad voltado para análise de qualidade")
    st.image(imagem)
    st.subheader("Grafico relacionado ao mês de maio: ")
    st.subheader("Controle: ")
    st.bar_chart(df_melt.set_index('consultor'))
    st.subheader("Pós: ")
    st.bar_chart(df_melt2.set_index('consultor'))
    st.subheader("Seguro: ")
    st.bar_chart(df_melt3.set_index('consultor'))
    

elif windows == "Tabela(Pós)" and box_mês == "Maio":
    st.header("Tabela Pós")
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

    st.text("Total")
    st.dataframe(cont_pos)

elif windows == "Inicio" and box_mês == "Junho" :
    st.header("Vivo Dashborad")
    st.subheader("Dashborad voltado para análise de produtos")
    st.image(imagem)
    st.subheader("Gráfico relacionado ao mês de Junho")
    pass


elif windows == "Sobre":
     st.text("Dados coletados dos consultores")
     st.text("Shopping Da Bahia")

elif windows =="Tabela(Seguro)" and box_mês == "Maio":
    st.header("Tabela Seguro: ")
    st.text("ANA")
    st.dataframe(ANA_SEGURO)
    st.dataframe(ANA_SEGUROT)

    st.text("ANDERSON")
    st.dataframe(ANDERSON_SEGURO)
    st.dataframe(ANDERSON_SEGUROT)

    st.text("CAROL")
    st.dataframe(CAROL_SEGURO)
    st.dataframe(CAROL_SEGUROT)

    st.text("DAVIDG")
    st.dataframe(DAVIDG_SEGURO)
    st.dataframe(DAVIDG_SEGUROT)

    st.text("DEBORA")
    st.dataframe(DEBORA_SEGURO)
    st.dataframe(DEBORA_SEGUROT)

    st.text("LENE")
    st.dataframe(LENE_SEGURO)
    st.dataframe(LENE_SEGUROT)

    st.text("WILLER")
    st.dataframe(WILLER_SEGURO)
    st.dataframe(WILLER_SEGUROT)

    st.text("Total")
    st.dataframe(cont_seguro)
    