import streamlit as st
import pandas as pd
from PIL import Image
from readfile_controle_pos import ANA_maio_filtro , ANDERSON_maio_filtro , CAROL_maio_filtro , DEBORA_maio_filtro , DAVIDG_maio_filtro , LENE_maio_filtro , WILLER_maio_filtro , ANA_maio_filtrop , ANDERSON_maio_filtrop  , CAROL_maio_filtrop , DAVIDG_maio_filtrop , DEBORA_maio_filtrop , LENE_maio_filtrop , WILLER_maio_filtrop , ANA_junho_filtro , AMANDA_junho_filtro , DAVIDG_junho_filtro , DEBORA_junho_filtro , CAROL_junho_filtro , WILLER_junho_filtro , ANA_maio_filtros , ANDERSON_maio_filtros , CAROL_maio_filtros , DEBORA_maio_filtros , DAVIDG_maio_filtros , LENE_maio_filtros , WILLER_maio_filtros , ANA_junho_filtrop , AMANDA_junho_filtrop , CAROL_junho_filtrop , DAVIDG_junho_filtrop , DEBORA_junho_filtrop , WILLER_junho_filtrop , AMANDA_junho_filtros , ANA_junho_filtros  , DEBORA_junho_filtros , DAVIDG_junho_filtros , CAROL_junho_filtros , WILLER_junho_filtros , ANDERSON_junho_filtros
from readfile_Total_controle_pos_seguro import totalc , cont_seguro ,cont_pos, ANA_junho_TOTALC , AMANDA_junho_TOTALC , CAROL_junho_TOTALC , DAVIDG_junho_TOTALC , DEBORA_junho_TOTALC , WILLER_junho_TOTALC 
from readfile_Total_controle_pos_seguro import ANA_maio_TOTALC, ANDERSON_maio_TOTALC, CAROL_maio_TOTALC,DEBORA_maio_TOTALC, DAVIDG_maio_TOTALC, LENE_maio_TOTALC, WILLER_maio_TOTALC 
from readfile_Total_controle_pos_seguro import ANA_maio_TOTALP, ANDERSON_maio_TOTALP, CAROL_maio_TOTALP,DEBORA_maio_TOTALP, DAVIDG_maio_TOTALP, LENE_maio_TOTALP, WILLER_maio_TOTALP
from readfile_Total_controle_pos_seguro import ANA_maio_TOTALS , ANDERSON_maio_TOTALS , CAROL_maio_TOTALS , DEBORA_maio_TOTALS , DAVIDG_maio_TOTALS , LENE_maio_TOTALS , WILLER_maio_TOTALS , ANA_junho_TOTALP , AMANDA_junho_TOTALP , CAROL_junho_TOTALP , DAVIDG_junho_TOTALP , DEBORA_junho_TOTALP , WILLER_junho_TOTALP , ANA_junho_TOTALS , ANDERSON_junho_TOTALS , CAROL_junho_TOTALS ,DEBORA_junho_TOTALS , DAVIDG_junho_TOTALS , WILLER_junho_TOTALS ,AMANDA_junho_TOTALS
from readfile_grafico import df_melt  , df_melt2 , df_melt3, df_melt_junho_CONTROLE, df_melt_junho_PÓS , df_melt_junho_SEGURO


imagem = imagem = Image.open('imagem/vivop.png')


windows = st.sidebar.radio("GUIA DE NAVEGAÇÃO", ["Inicio","Tabela(Controle)", "Tabela(Pós)" ,"Tabela(Seguro)","Sobre"])
box_mês = st.sidebar.selectbox("Selecione o mês desejado:", ["Maio","Junho"])




if windows == "Inicio" and box_mês == "Maio":
    st.header("Vivo Dashborad")
    st.subheader("Dashborad voltado para análise de qualidade")
    st.image(imagem)
    st.subheader("Gráfico relacionado ao mês de maio: ")
    st.subheader("Controle: ")
    st.bar_chart(df_melt.set_index('consultor'))
    st.subheader("Pós: ")
    st.bar_chart(df_melt2.set_index('consultor'))
    st.subheader("Seguro: ")
    st.bar_chart(df_melt3.set_index('consultor'))

 
    
elif windows == "Inicio" and box_mês == "Junho" :
    st.header("Vivo Dashborad")
    st.subheader("Dashboard voltado para análise de produtos")
    st.image(imagem)
    st.subheader("Gráfico relacionado ao mês de Junho")
    st.subheader("Controle: ")
    st.bar_chart(df_melt_junho_CONTROLE.set_index('consultor'))
    st.subheader("PÓS: ")
    st.bar_chart(df_melt_junho_PÓS.set_index('consultor'))
    st.subheader("SEGURO: ")
    st.bar_chart(df_melt_junho_SEGURO.set_index('consultor'))
    


elif windows == "Tabela(Controle)" and box_mês == "Maio":

    st.text("ANA")
    st.dataframe(ANA_maio_filtro)
    st.write(ANA_maio_TOTALC)

    st.text("ANDERSON")
    st.dataframe(ANDERSON_maio_filtro)
    st.write(ANDERSON_maio_TOTALC)

    st.text("CAROL")
    st.dataframe(CAROL_maio_filtro)
    st.write(CAROL_maio_TOTALC)

    st.text("DAVIDG")
    st.dataframe(DAVIDG_maio_filtro)
    st.write(DAVIDG_maio_TOTALC)

    st.text("DEBORA")
    st.dataframe(DEBORA_maio_filtro)
    st.write(DEBORA_maio_TOTALC)

    st.text("LENE")
    st.dataframe(LENE_maio_filtro)
    st.write(LENE_maio_TOTALC)

    st.text("WILLER")
    st.dataframe(WILLER_maio_filtro)
    st.write(WILLER_maio_TOTALC)


    st.text("Total")
    st.write(totalc)
    

elif windows == "Tabela(Pós)" and box_mês == "Maio":
    st.header("Tabela Pós")
    
    st.text("ANA")
    st.dataframe(ANA_maio_filtrop)
    st.write(ANA_maio_TOTALP)

    st.text("ANDERSON")
    st.dataframe(ANDERSON_maio_filtrop)
    st.write(ANDERSON_maio_TOTALP)

    st.text("CAROL")
    st.dataframe(CAROL_maio_filtrop)
    st.write(CAROL_maio_TOTALP)

    st.text("DAVIDG")
    st.dataframe(DAVIDG_maio_filtrop)
    st.write(DAVIDG_maio_TOTALP)

    st.text("DEBORA")
    st.dataframe(DEBORA_maio_filtrop)
    st.write(DEBORA_maio_TOTALP)

    st.text("LENE")
    st.dataframe(LENE_maio_filtrop)
    st.write(LENE_maio_TOTALP)

    st.text("WILLER")
    st.dataframe(WILLER_maio_filtrop)
    st.write(WILLER_maio_TOTALP)

    st.text("Total")
    st.write(cont_pos)

elif windows == "Tabela(Seguro)" and box_mês == "Maio":
    st.header("Tabela Seguro")
    
    st.text("ANA")
    st.dataframe(ANA_maio_filtros)
    st.write(ANA_maio_TOTALS)

    st.text("ANDERSON")
    st.dataframe(ANDERSON_maio_filtros)
    st.write(ANDERSON_maio_TOTALS)

    st.text("CAROL")
    st.dataframe(CAROL_maio_filtros)
    st.write(CAROL_maio_TOTALS)

    st.text("DAVIDG")
    st.dataframe(DAVIDG_maio_filtros)
    st.write(DAVIDG_maio_TOTALS)

    st.text("DEBORA")
    st.dataframe(DEBORA_maio_filtros)
    st.write(DEBORA_maio_TOTALS)

    st.text("LENE")
    st.dataframe(LENE_maio_filtros)
    st.write(LENE_maio_TOTALS)

    st.text("WILLER")
    st.dataframe(WILLER_maio_filtros)
    st.write(WILLER_maio_TOTALS)

    st.text("Total")
    st.write(cont_seguro)

elif windows == "Sobre":
     st.text("Dados coletados dos consultores")
     st.text("Shopping Da Bahia")


#JUNHO

elif windows == "Tabela(Controle)" and box_mês == "Junho":

    st.header("Tabela (Controle)")
    

    st.text("ANA")
    st.dataframe(ANA_junho_filtro)
    st.write(ANA_junho_TOTALC)

    st.text("AMANDA")
    st.dataframe(AMANDA_junho_filtro)
    st.write(AMANDA_junho_TOTALC)

    st.text("CAROL")
    st.dataframe(CAROL_junho_filtro)
    st.write(CAROL_junho_TOTALC)

    st.text("DEBORA")
    st.dataframe(DEBORA_junho_filtro)
    st.write(DEBORA_junho_TOTALC)

    st.text("DAVIDG")
    st.dataframe(DAVIDG_junho_filtro)
    st.write(DAVIDG_junho_TOTALC)

    st.text("WILLER")
    st.dataframe(WILLER_junho_filtro)
    st.write(WILLER_junho_TOTALC)


elif windows == "Tabela(Pós)" and box_mês == "Junho":

    st.header("Tabela (Pós)")
    
    st.text("ANA")
    st.dataframe(ANA_junho_filtrop)
    st.write(ANA_junho_TOTALP)

    st.text("AMANDA")
    st.dataframe(AMANDA_junho_filtrop)
    st.write(AMANDA_junho_TOTALP)

    st.text("CAROL")
    st.dataframe(CAROL_junho_filtrop)
    st.write(CAROL_junho_TOTALP)

    st.text("DAVIDG")
    st.dataframe(DAVIDG_junho_filtrop)
    st.write(DAVIDG_junho_TOTALP)

    st.text("DEBORA")
    st.dataframe(DEBORA_junho_filtrop)
    st.write(DEBORA_junho_TOTALP)


    st.text("WILLER")
    st.dataframe(WILLER_junho_filtrop)
    st.write(WILLER_junho_TOTALP)


elif windows == "Tabela(Seguro)" and box_mês == "Junho":

    st.header("Tabela (Seguro)")
    
    st.text("ANA")
    st.dataframe(ANA_junho_filtros)
    st.write(ANA_junho_TOTALS)

    st.text("ANDERSON")
    st.dataframe(ANDERSON_junho_filtros)
    st.write(ANDERSON_junho_TOTALS)


    st.text("AMANDA")
    st.dataframe(AMANDA_junho_filtros)
    st.write(AMANDA_junho_TOTALS)

    st.text("CAROL")
    st.dataframe(CAROL_junho_filtros)
    st.write(CAROL_junho_TOTALS)

    st.text("DAVIDG")
    st.dataframe(DAVIDG_junho_filtros)
    st.write(DAVIDG_junho_TOTALS)

    st.text("DEBORA")
    st.dataframe(DEBORA_junho_filtros)
    st.write(DEBORA_junho_TOTALS)


    st.text("WILLER")
    st.dataframe(WILLER_junho_filtros)
    st.write(WILLER_junho_TOTALS)


