import streamlit as st
import pandas as pd
from PIL import Image
from readfiles_excel import ANA_maio_filtro , ANDERSON_maio_filtro , CAROL_maio_filtro , DEBORA_maio_filtro , DAVIDG_maio_filtro , LENE_maio_filtro , WILLER_maio_filtro , ANA_maio_filtrop , ANDERSON_maio_filtrop  , CAROL_maio_filtrop , DAVIDG_maio_filtrop , DEBORA_maio_filtrop , LENE_maio_filtrop , WILLER_maio_filtrop , ANA_junho_filtro , AMANDA_junho_filtro , DAVIDG_junho_filtro , DEBORA_junho_filtro , CAROL_junho_filtro , WILLER_junho_filtro , ANA_maio_filtros , ANDERSON_maio_filtros , CAROL_maio_filtros , DEBORA_maio_filtros , DAVIDG_maio_filtros , LENE_maio_filtros , WILLER_maio_filtros , ANA_junho_filtrop , AMANDA_junho_filtrop , CAROL_junho_filtrop , DAVIDG_junho_filtrop , DEBORA_junho_filtrop , WILLER_junho_filtrop , AMANDA_junho_filtros , ANA_junho_filtros  , DEBORA_junho_filtros , DAVIDG_junho_filtros , CAROL_junho_filtros , WILLER_junho_filtros , ANDERSON_junho_filtros , ANDERSON_junho_filtro , ANDERSON_junho_filtrop
from readfile_Total import totalc , cont_seguro ,cont_pos, ANA_junho_TOTALC , AMANDA_junho_TOTALC , CAROL_junho_TOTALC , DAVIDG_junho_TOTALC , DEBORA_junho_TOTALC , WILLER_junho_TOTALC 
from readfile_Total import ANA_maio_TOTALC, ANDERSON_maio_TOTALC, CAROL_maio_TOTALC,DEBORA_maio_TOTALC, DAVIDG_maio_TOTALC, LENE_maio_TOTALC, WILLER_maio_TOTALC 
from readfile_Total import ANA_maio_TOTALP, ANDERSON_maio_TOTALP, CAROL_maio_TOTALP,DEBORA_maio_TOTALP, DAVIDG_maio_TOTALP, LENE_maio_TOTALP, WILLER_maio_TOTALP
from readfile_Total import ANA_maio_TOTALS , ANDERSON_maio_TOTALS , CAROL_maio_TOTALS , DEBORA_maio_TOTALS , DAVIDG_maio_TOTALS , LENE_maio_TOTALS , WILLER_maio_TOTALS , ANA_junho_TOTALP , AMANDA_junho_TOTALP , CAROL_junho_TOTALP , DAVIDG_junho_TOTALP , DEBORA_junho_TOTALP , WILLER_junho_TOTALP , ANA_junho_TOTALS , ANDERSON_junho_TOTALS , CAROL_junho_TOTALS ,DEBORA_junho_TOTALS , DAVIDG_junho_TOTALS , WILLER_junho_TOTALS ,AMANDA_junho_TOTALS , junho_acumulado_seguro , junho_acumulado_controle , junho_acumulado_pós , ANDERSON_junho_TOTALP , ANDERSON_junho_TOTALC
from readfile_Total import ANA_junho_filtroa , AMANDA_junho_filtroa , ANDERSON_junho_filtroa , CAROL_junho_filtroa , DEBORA_junho_filtroa , DAVIDG_junho_filtroa , WILLER_junho_filtroa , ANA_junho_TOTALA , ANDERSON_junho_TOTALA , DEBORA_junho_TOTALA , CAROL_junho_TOTALA , DAVIDG_junho_TOTALA, WILLER_junho_TOTALA ,AMANDA_junho_TOTALA , junho_acumulado_aparelho , ANA_junhoac , ANA_junho_filtroac , AMANDA_junho_filtroac , DAVIDG_junho_filtroac , DEBORA_junho_filtroac , WILLER_junho_filtroac ,ANDERSON_junho_filtroac , CAROL_junho_filtroac
from readfile_grafico import df_melt  , df_melt2 , df_melt3, df_melt_junho_CONTROLE, df_melt_junho_PÓS , df_melt_junho_SEGURO , df_melt_junho_APARELHO_ANA , df_melt_junho_APARELHO_AMANDA , df_melt_junho_APARELHO_ANDERSON , df_melt_junho_APARELHO_CAROL , df_melt_junho_APARELHO_DAVIDG , df_melt_junho_APARELHO_DEBORA , df_melt_junho_APARELHO_WILLER


imagem = imagem = Image.open('imagem/vivop.png')


windows = st.sidebar.radio("GUIA DE NAVEGAÇÃO", ["Inicio","Gráfico(Aparelho/Acessórios)","Tabela(Controle)", "Tabela(Pós)" ,"Tabela(Seguro)","Tabela(Aparelho/Acessórios)","Sobre"])
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
    st.subheader("Pós: ")
    st.bar_chart(df_melt_junho_PÓS.set_index('consultor'))
    st.subheader("Seguro: ")
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


#JUNHO

elif windows == "Tabela(Controle)" and box_mês == "Junho":

    st.header("Tabela (Controle)")
    

    st.text("ANA")
    st.dataframe(ANA_junho_filtro)
    st.write(ANA_junho_TOTALC)

    st.text("ANDERSON")
    st.dataframe(ANDERSON_junho_filtro)
    st.write(ANDERSON_junho_TOTALC)

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

    st.write("Total controle: ",junho_acumulado_controle)


elif windows == "Tabela(Pós)" and box_mês == "Junho":

    st.header("Tabela (Pós)")
    
    st.text("ANA")
    st.dataframe(ANA_junho_filtrop)
    st.write(ANA_junho_TOTALP)

    st.text("ANDERSON")
    st.dataframe(ANDERSON_junho_filtrop)
    st.write(ANDERSON_junho_TOTALP)

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

    st.write("Total pós: ",junho_acumulado_pós)


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

    
    st.write("Total seguro: ",junho_acumulado_seguro)


elif windows == "Tabela(Aparelho/Acessórios)" and box_mês == "Junho":

    st.header("Tabela (Aparelho/Acessórios)")

    st.write("ANA  APARELHOS", ANA_junho_TOTALA)
    st.dataframe(ANA_junho_filtroa)
    st.write("Acessórios:")
    st.write(ANA_junho_filtroac)

    st.write("ANDERSON  APARELHOS", ANDERSON_junho_TOTALA)
    st.dataframe(ANDERSON_junho_filtroa)
    st.write("Acessórios:")
    st.write(ANDERSON_junho_filtroac)

    st.write("AMANDA  APARELHOS", AMANDA_junho_TOTALA)
    st.dataframe(AMANDA_junho_filtroa)
    st.write("Acessórios:")
    st.write(AMANDA_junho_filtroac)

    st.write("CAROL  APARELHOS", CAROL_junho_TOTALA)
    st.dataframe(CAROL_junho_filtroa)
    st.write("Acessórios:")
    st.write(CAROL_junho_filtroac)

    st.write("DAVIDG  APARELHOS", DAVIDG_junho_TOTALA)
    st.dataframe(DAVIDG_junho_filtroa)
    st.write("Acessórios:")
    st.write(DAVIDG_junho_filtroac)

    st.write("DEBORA  APARELHOS", DEBORA_junho_TOTALA)
    st.dataframe(DEBORA_junho_filtroa)
    st.write("Acessórios:")
    st.write(DEBORA_junho_filtroac)

    st.write("WILLER  APARELHOS", WILLER_junho_TOTALA)
    st.dataframe(WILLER_junho_filtroa)
    st.write("Acessórios:")
    st.write(WILLER_junho_filtroac)

    st.write("Total Aparelho: ",junho_acumulado_aparelho)
    
elif windows == ("Gráfico(Aparelho/Acessórios)") and box_mês == "Junho":
    st.header("Vivo Dashborad")
    st.subheader("Dashboard voltado para análise de produtos")
    st.image(imagem)
    st.subheader("Gráfico(Aparelho/Acessórios)")
    st.subheader("ANA: ")
    st.bar_chart(df_melt_junho_APARELHO_ANA.set_index('consultor'))
    st.subheader("ANDERSON: ")
    st.bar_chart(df_melt_junho_APARELHO_ANDERSON.set_index('consultor'))
    st.subheader("AMANDA: ")
    st.bar_chart(df_melt_junho_APARELHO_AMANDA.set_index('consultor'))
    st.subheader("CAROL: ")
    st.bar_chart(df_melt_junho_APARELHO_CAROL.set_index('consultor'))
    st.subheader("DEBORA: ")
    st.bar_chart(df_melt_junho_APARELHO_DEBORA.set_index('consultor'))
    st.subheader("DAVIDG: ")
    st.bar_chart(df_melt_junho_APARELHO_DAVIDG.set_index('consultor'))
    st.subheader("WILLER: ")
    st.bar_chart(df_melt_junho_APARELHO_WILLER.set_index('consultor'))
    








elif windows == "Sobre":
    st.header("Referências")
    st.text("Dados coletados das planilhas dos consultores")
    st.text("Shopping Da Bahia")
    st.text("Vivo p2")

     
    

