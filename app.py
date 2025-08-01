import streamlit as st
import pandas as pd
from PIL import Image
from Filtros import  Select_Filtro , Select_Coluns, Select_Coluns2, Select_Coluns3 , Select_Filtro2 ,Select_Filtro3 ,Select_Filtro4 ,Select_Filtro5 ,Select_Filtro6 


imagem = imagem = Image.open('imagem/estoque.png')


windows = st.sidebar.radio("GUIA DE NAVEGAÇÃO", ["Inicio","Gráfico(Aparelho/Acessórios)","Tabela(Controle)", "Tabela(Pós)" ,"Tabela(Seguro)","Tabela(Fibra)","Tabela(Aparelho/Acessórios)","Sobre"])

arquivo = st.file_uploader("Carregue a Planilha Modelo_Vendedores_P2",type="xlsx")

if arquivo is not None:
    # JUNHO_CONTROLE
    ANA_junho = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="ANA")
    ANA_junho_filtro = ANA_junho[ANA_junho["Produto"] == Select_Filtro]
    ANA_junho_TOTALC = ANA_junho["Produto"].value_counts().get("CONTROLE", 0)

    AMANDA_junho = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="AMANDA")
    AMANDA_junho_filtro = AMANDA_junho[AMANDA_junho["Produto"] == Select_Filtro]
    AMANDA_junho_TOTALC = AMANDA_junho["Produto"].value_counts().get("CONTROLE", 0)

    ANDERSON_junho = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="ANDERSON")
    ANDERSON_junho_filtro = ANDERSON_junho[ANDERSON_junho["Produto"] == Select_Filtro]
    ANDERSON_junho_TOTALC = ANDERSON_junho["Produto"].value_counts().get("CONTROLE", 0)

    DAVIDG_junho = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="DAVIDG")
    DAVIDG_junho_filtro = DAVIDG_junho[DAVIDG_junho["Produto"] == Select_Filtro]
    DAVIDG_junho_TOTALC = DAVIDG_junho["Produto"].value_counts().get("CONTROLE", 0)

    DEBORA_junho = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="DEBORA")
    DEBORA_junho_filtro = DEBORA_junho[DEBORA_junho["Produto"] == Select_Filtro]
    DEBORA_junho_TOTALC = DEBORA_junho["Produto"].value_counts().get("CONTROLE", 0)

    WILLER_junho = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="WILLER")
    WILLER_junho_filtro = WILLER_junho[WILLER_junho["Produto"] == Select_Filtro]
    WILLER_junho_TOTALC = WILLER_junho["Produto"].value_counts().get("CONTROLE", 0)

    junho_acumulado_controle = ( ANA_junho_TOTALC + AMANDA_junho_TOTALC + ANDERSON_junho_TOTALC 

 + DAVIDG_junho_TOTALC + DEBORA_junho_TOTALC + WILLER_junho_TOTALC )


    # JUNHO_PÓS
    ANA_junhop = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="ANA")
    ANA_junho_filtrop = ANA_junhop[ANA_junhop["Produto"] == Select_Filtro2]
    ANA_junho_TOTALP = ANA_junhop["Produto"].value_counts().get("PÓS PAGO", 0)

    AMANDA_junhop = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="AMANDA")
    AMANDA_junho_filtrop = AMANDA_junhop[AMANDA_junhop["Produto"] == Select_Filtro2]
    AMANDA_junho_TOTALP = AMANDA_junhop["Produto"].value_counts().get("PÓS PAGO", 0)

    ANDERSON_junhop = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="ANDERSON")
    ANDERSON_junho_filtrop = ANDERSON_junhop[ANDERSON_junhop["Produto"] == Select_Filtro2]
    ANDERSON_junho_TOTALP = ANDERSON_junhop["Produto"].value_counts().get("PÓS PAGO", 0)

    DAVIDG_junhop = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="DAVIDG")
    DAVIDG_junho_filtrop = DAVIDG_junhop[DAVIDG_junhop["Produto"] == Select_Filtro2]
    DAVIDG_junho_TOTALP = DAVIDG_junhop["Produto"].value_counts().get("PÓS PAGO", 0)

    DEBORA_junhop = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="DEBORA")
    DEBORA_junho_filtrop = DEBORA_junhop[DEBORA_junhop["Produto"] == Select_Filtro2]
    DEBORA_junho_TOTALP = DEBORA_junhop["Produto"].value_counts().get("PÓS PAGO", 0)

    WILLER_junhop = pd.read_excel(arquivo, usecols=Select_Coluns, sheet_name="WILLER")
    WILLER_junho_filtrop = WILLER_junhop[WILLER_junhop["Produto"] == Select_Filtro2]
    WILLER_junho_TOTALP = WILLER_junhop["Produto"].value_counts().get("PÓS PAGO", 0)

    junho_acumulado_pós = (
    ANA_junho_TOTALP + AMANDA_junho_TOTALP + ANDERSON_junho_TOTALP +
     DAVIDG_junho_TOTALP + DEBORA_junho_TOTALP + WILLER_junho_TOTALP)


    
    # JUNHO_SEGURO
    ANA_junhos = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="ANA")
    ANA_junho_filtros = ANA_junhos[ANA_junhos["Serviço"] == Select_Filtro3]
    ANA_junho_TOTALS = ANA_junhos["Serviço"].value_counts().get("Seguro", 0)

    AMANDA_junhos = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="AMANDA")
    AMANDA_junho_filtros = AMANDA_junhos[AMANDA_junhos["Serviço"] == Select_Filtro3]
    AMANDA_junho_TOTALS = AMANDA_junhos["Serviço"].value_counts().get("Seguro", 0)

    ANDERSON_junhos = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="ANDERSON")
    ANDERSON_junho_filtros = ANDERSON_junhos[ANDERSON_junhos["Serviço"] == Select_Filtro3]
    ANDERSON_junho_TOTALS = ANDERSON_junhos["Serviço"].value_counts().get("Seguro", 0)

    DAVIDG_junhos = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="DAVIDG")
    DAVIDG_junho_filtros = DAVIDG_junhos[DAVIDG_junhos["Serviço"] == Select_Filtro3]
    DAVIDG_junho_TOTALS = DAVIDG_junhos["Serviço"].value_counts().get("Seguro", 0)

    DEBORA_junhos = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="DEBORA")
    DEBORA_junho_filtros = DEBORA_junhos[DEBORA_junhos["Serviço"] == Select_Filtro3]
    DEBORA_junho_TOTALS = DEBORA_junhos["Serviço"].value_counts().get("Seguro", 0)

    WILLER_junhos = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="WILLER")
    WILLER_junho_filtros = WILLER_junhos[WILLER_junhos["Serviço"] == Select_Filtro3]
    WILLER_junho_TOTALS = WILLER_junhos["Serviço"].value_counts().get("Seguro", 0)

    junho_acumulado_seguro = (
    ANA_junho_TOTALS + AMANDA_junho_TOTALS + ANDERSON_junho_TOTALS +
     DAVIDG_junho_TOTALS + DEBORA_junho_TOTALS + WILLER_junho_TOTALS)
    

    # JUNHO_APARELHOS
    ANA_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="ANA")
    ANA_junho_filtroa = ANA_junhoa[ANA_junhoa["Serviço"] == Select_Filtro4]
    ANA_junho_TOTALA = ANA_junhoa["Serviço"].value_counts().get("Aparelho", 0)

    AMANDA_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="AMANDA")
    AMANDA_junho_filtroa = AMANDA_junhoa[AMANDA_junhoa["Serviço"] == Select_Filtro4]
    AMANDA_junho_TOTALA = AMANDA_junhos["Serviço"].value_counts().get("Aparelho", 0)


    ANDERSON_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="ANDERSON")
    ANDERSON_junho_filtroa = ANDERSON_junhoa[ANDERSON_junhoa["Serviço"] == Select_Filtro4]
    ANDERSON_junho_TOTALA = ANDERSON_junhos["Serviço"].value_counts().get("Aparelho", 0)

    DAVIDG_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="DAVIDG")
    DAVIDG_junho_filtroa = DAVIDG_junhoa[DAVIDG_junhoa["Serviço"] == Select_Filtro4]
    DAVIDG_junho_TOTALA = DAVIDG_junhos["Serviço"].value_counts().get("Aparelho", 0)

    DEBORA_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="DEBORA")
    DEBORA_junho_filtroa = DEBORA_junhoa[DEBORA_junhoa["Serviço"] == Select_Filtro4]
    DEBORA_junho_TOTALA = DEBORA_junhos["Serviço"].value_counts().get("Aparelho", 0)

    WILLER_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="WILLER")
    WILLER_junho_filtroa = WILLER_junhoa[WILLER_junhoa["Serviço"] == Select_Filtro4]
    WILLER_junho_TOTALA = WILLER_junhos["Serviço"].value_counts().get("Aparelho", 0)

    #TOTAL_APARELHOS_ACUMULADO

    junho_acumulado_aparelho = ( ANA_junho_TOTALA + AMANDA_junho_TOTALA + ANDERSON_junho_TOTALA 

 + DAVIDG_junho_TOTALA + DEBORA_junho_TOTALA + WILLER_junho_TOTALA )



    # JUNHO_ACESSORIOS
    ANA_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="ANA")
    ANA_junho_filtroac = ANA_junhoa[ANA_junhoa["Serviço"] == Select_Filtro5]
    ANA_junho_TOTALAC = ANA_junhoa["Serviço"].value_counts().get("Acessórios", 0)

    AMANDA_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="AMANDA")
    AMANDA_junho_filtroac = AMANDA_junhoa[AMANDA_junhoa["Serviço"] == Select_Filtro5]
    AMANDA_junho_TOTALAC = AMANDA_junhoa["Serviço"].value_counts().get("Acessórios", 0)

    ANDERSON_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="ANDERSON")
    ANDERSON_junho_filtroac = ANDERSON_junhoa[ANDERSON_junhoa["Serviço"] == Select_Filtro5]
    ANDERSON_junho_TOTALAC = ANDERSON_junhoa["Serviço"].value_counts().get("Acessórios", 0)

    DAVIDG_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="DAVIDG")
    DAVIDG_junho_filtroac = DAVIDG_junhoa[DAVIDG_junhoa["Serviço"] == Select_Filtro5]
    DAVIDG_junho_TOTALAC = DAVIDG_junhoa["Serviço"].value_counts().get("Acessórios", 0)

    DEBORA_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="DEBORA")
    DEBORA_junho_filtroac = DEBORA_junhoa[DEBORA_junhoa["Serviço"] == Select_Filtro5]
    DEBORA_junho_TOTALAC = DEBORA_junhoa["Serviço"].value_counts().get("Acessórios", 0)

    WILLER_junhoa = pd.read_excel(arquivo, usecols=Select_Coluns2, sheet_name="WILLER")
    WILLER_junho_filtroac = WILLER_junhoa[WILLER_junhoa["Serviço"] == Select_Filtro5]
    WILLER_junho_TOTALAC = WILLER_junhoa["Serviço"].value_counts().get("Acessórios", 0)


   
    # JUNHO_FIBRA
    ANA_junhof = pd.read_excel(arquivo, usecols=Select_Coluns3, sheet_name="ANA")
    ANA_junho_filtrof = ANA_junhof[ANA_junhof["Serviço"] == Select_Filtro6]
    ANA_junho_TOTALf = ANA_junhof["Serviço"].value_counts().get("Fixa", 0)

    AMANDA_junhof = pd.read_excel(arquivo, usecols=Select_Coluns3, sheet_name="AMANDA")
    AMANDA_junho_filtrof = AMANDA_junhof[AMANDA_junhof["Serviço"] == Select_Filtro6]
    AMANDA_junho_TOTALf = AMANDA_junhof["Serviço"].value_counts().get("Fixa", 0)

    ANDERSON_junhof = pd.read_excel(arquivo, usecols=Select_Coluns3, sheet_name="ANDERSON")
    ANDERSON_junho_filtrof = ANDERSON_junhof[ANDERSON_junhof["Serviço"] == Select_Filtro6]
    ANDERSON_junho_TOTALf = ANDERSON_junhof["Serviço"].value_counts().get("Fixa", 0)

    DAVIDG_junhof = pd.read_excel(arquivo, usecols=Select_Coluns3, sheet_name="DAVIDG")
    DAVIDG_junho_filtrof = DAVIDG_junhof[DAVIDG_junhof["Serviço"] == Select_Filtro6]
    DAVIDG_junho_TOTALf = DAVIDG_junhof["Serviço"].value_counts().get("Fixa", 0)

    DEBORA_junhof = pd.read_excel(arquivo, usecols=Select_Coluns3, sheet_name="DEBORA")
    DEBORA_junho_filtrof = DEBORA_junhof[DEBORA_junhof["Serviço"] == Select_Filtro6]
    DEBORA_junho_TOTALf = DEBORA_junhof["Serviço"].value_counts().get("Fixa", 0)

    WILLER_junhof = pd.read_excel(arquivo, usecols=Select_Coluns3, sheet_name="WILLER")
    WILLER_junho_filtrof = WILLER_junhof[WILLER_junhof["Serviço"] == Select_Filtro6]
    WILLER_junho_TOTALf = WILLER_junhof["Serviço"].value_counts().get("Fixa", 0)

    #total
    junho_acumulado_fibra = ( ANA_junho_TOTALf + AMANDA_junho_TOTALf + ANDERSON_junho_TOTALf

 + DAVIDG_junho_TOTALf + DEBORA_junho_TOTALf + WILLER_junho_TOTALf )

#junho_grafico_controle

df_junho = pd.DataFrame ([{

'ANA' : ANA_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'ANDERSON' : ANDERSON_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'AMANDA' :  AMANDA_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'DAVIDG' : DAVIDG_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'DEBORA' : DEBORA_junho_filtro ["Produto"].isin(["CONTROLE"]).sum(),
'WILLER' : WILLER_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
"Total" : junho_acumulado_controle,
}])

df_melt_junho_CONTROLE = df_junho.melt(value_name = "valor" , var_name = "consultor")


#junho_grafico_pós

df_junho2 = pd.DataFrame ([{

'ANA' : ANA_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'ANDERSON' : ANDERSON_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'AMANDA'  : AMANDA_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'DAVIDG' : DAVIDG_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'DEBORA' : DEBORA_junho_filtrop ["Produto"].isin(["PÓS PAGO"]).sum(),
'WILLER' : WILLER_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
"TOTAL" : junho_acumulado_pós,

}])

df_melt_junho_PÓS = df_junho2.melt(value_name = "valor" , var_name = "consultor")

#junho_grafico_seguro

df_junho3 = pd.DataFrame ([{

'ANA' : ANA_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'ANDERSON' : ANDERSON_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'AMANDA' : AMANDA_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'DAVIDG' : DAVIDG_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'DEBORA' : DEBORA_junho_filtros ["Serviço"].isin(["Seguro"]).sum(),
'WILLER' : WILLER_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
"Total" : junho_acumulado_seguro,

}])

df_melt_junho_SEGURO = df_junho3.melt(value_name = "valor" , var_name = "consultor")


#junho_grafico_aparelho

df_junho_ANAAP = pd.DataFrame ([{

"AP" : ANA_junho_TOTALA , 
"AC" : ANA_junho_TOTALAC

}])

df_melt_junho_APARELHO_ANA = df_junho_ANAAP.melt(value_name = "valor" , var_name = "consultor")



df_junho_ANDERSONAP = pd.DataFrame ([{

"AP" : ANDERSON_junho_TOTALA , 
"AC" : ANDERSON_junho_TOTALAC

}])

df_melt_junho_APARELHO_ANDERSON = df_junho_ANDERSONAP.melt(value_name = "valor" , var_name = "consultor")


df_junho_AMANDAAP = pd.DataFrame ([{

"AP" : AMANDA_junho_TOTALA , 
"AC" : AMANDA_junho_TOTALC

}])

df_melt_junho_APARELHO_AMANDA = df_junho_AMANDAAP.melt(value_name = "valor" , var_name = "consultor")



df_junho_DEBORAAP = pd.DataFrame ([{

"AP" : DEBORA_junho_TOTALA , 
"AC" : DEBORA_junho_TOTALAC

}])

df_melt_junho_APARELHO_DEBORA = df_junho_DEBORAAP.melt(value_name = "valor" , var_name = "consultor")


df_junho_DAVIDGAP = pd.DataFrame ([{

"AP" : DAVIDG_junho_TOTALA , 
"AC" : DAVIDG_junho_TOTALAC

}])

df_melt_junho_APARELHO_DAVIDG = df_junho_DAVIDGAP.melt(value_name = "valor" , var_name = "consultor")


df_junho_WILLERAP = pd.DataFrame ([{

"AP" : WILLER_junho_TOTALA , 
"AC" : WILLER_junho_TOTALAC

}])

df_melt_junho_APARELHO_WILLER = df_junho_WILLERAP.melt(value_name = "valor" , var_name = "consultor")


#Junho_fibra_grafico

df_junho4 = pd.DataFrame ([{

'ANA' : ANA_junho_filtrof["Serviço"].isin(["Fixa"]).sum(),
'ANDERSON' : ANDERSON_junho_filtrof["Serviço"].isin(["Fixa"]).sum(),
'AMANDA' : AMANDA_junho_filtrof["Serviço"].isin(["Fixa"]).sum(),
'DAVIDG' : DAVIDG_junho_filtrof["Serviço"].isin(["Fixa"]).sum(),
'DEBORA' : DEBORA_junho_filtrof ["Serviço"].isin(["Fixa"]).sum(),
'WILLER' : WILLER_junho_filtrof["Serviço"].isin(["Fixa"]).sum(),
"Total" : junho_acumulado_fibra,

}])

df_melt_junho_fibra = df_junho4.melt(value_name = "valor" , var_name = "consultor")



if windows == "Inicio"  :

    st.subheader("Dashboard voltado para análise de qualidade")
    st.image(imagem)
    st.subheader("Gráfico relacionado ao mês")

    st.subheader("Controle: ")
    st.bar_chart(df_melt_junho_CONTROLE.set_index('consultor'))

    st.subheader("Pós: ")
    st.bar_chart(df_melt_junho_PÓS.set_index('consultor'))

    st.subheader("Seguro: ")
    st.bar_chart(df_melt_junho_SEGURO.set_index('consultor'))

    st.subheader("Fibra: ")
    st.bar_chart(df_melt_junho_fibra.set_index('consultor'))


elif windows == "Tabela(Controle)" :
    
    st.header("Tabela (Controle)")
    st.write("ANA: ",ANA_junho_TOTALC)
    st.dataframe(ANA_junho_filtro)
    

    st.write("ANDERSON: ",ANDERSON_junho_TOTALC)
    st.dataframe(ANDERSON_junho_filtro)


    st.write("AMANDA: ",AMANDA_junho_TOTALC)
    st.dataframe(AMANDA_junho_filtro)


    st.write("DEBORA: ",DEBORA_junho_TOTALC)
    st.dataframe(DEBORA_junho_filtro)
    

    st.write("DAVIDG: ",DAVIDG_junho_TOTALC)
    st.dataframe(DAVIDG_junho_filtro)
    

    st.write("WILLER: ",WILLER_junho_TOTALC)
    st.dataframe(WILLER_junho_filtro)


    st.write("Total controle: ",junho_acumulado_controle)
    
    

elif windows == "Tabela(Pós)" :

    st.header("Tabela (Pós)")
    
    st.write("ANA: ", ANA_junho_TOTALP)
    st.dataframe(ANA_junho_filtrop)

    st.write("ANDERSON: ", ANDERSON_junho_TOTALP)
    st.dataframe(ANDERSON_junho_filtrop)

    st.write("AMANDA: ", AMANDA_junho_TOTALP)
    st.dataframe(AMANDA_junho_filtrop)

    st.write("DEBORA: ", DEBORA_junho_TOTALP)
    st.dataframe(DEBORA_junho_filtrop)

    st.write("DAVIDG: ", DAVIDG_junho_TOTALP)
    st.dataframe(DAVIDG_junho_filtrop)

    st.write("WILLER:", WILLER_junho_TOTALP)
    st.dataframe(WILLER_junho_filtrop)


    st.write("Total pós: ",junho_acumulado_pós)


elif windows == "Tabela(Seguro)" :

    st.header("Tabela (Seguro)")
    
    st.write("ANA: ", ANA_junho_TOTALS)
    st.dataframe(ANA_junho_filtros)

    st.write("ANDERSON: ", ANDERSON_junho_TOTALS)
    st.dataframe(ANDERSON_junho_filtros)

    st.write("AMANDA: ", AMANDA_junho_TOTALS)
    st.dataframe(AMANDA_junho_filtros)

    st.write("DAVIDG: ", DAVIDG_junho_TOTALS)
    st.dataframe(DAVIDG_junho_filtros)

    st.write("DEBORA: ", DEBORA_junho_TOTALS)
    st.dataframe(DEBORA_junho_filtros)

    st.write("WILLER: ", WILLER_junho_TOTALS)
    st.dataframe(WILLER_junho_filtros)

    st.write("Total seguro: ",junho_acumulado_seguro)


elif windows == "Tabela(Fibra)" :

    st.header("Tabela (Fibra)")
    
    st.write("ANA: ", ANA_junho_TOTALf)
    st.dataframe(ANA_junho_filtrof)

    st.write("ANDERSON: ", ANDERSON_junho_TOTALf)
    st.dataframe(ANDERSON_junho_filtrof)

    st.write("AMANDA: ", AMANDA_junho_TOTALf)
    st.dataframe(AMANDA_junho_filtrof)

    st.write("DAVIDG: ", DAVIDG_junho_TOTALf)
    st.dataframe(DAVIDG_junho_filtrof)

    st.write("DEBORA: ", DEBORA_junho_TOTALf)
    st.dataframe(DEBORA_junho_filtrof)

    st.write("WILLER: ", WILLER_junho_TOTALf)
    st.dataframe(WILLER_junho_filtrof)

    st.write("Total fibra: ",junho_acumulado_fibra)




elif windows == "Tabela(Aparelho/Acessórios)" :

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
    
elif windows == ("Gráfico(Aparelho/Acessórios)") :

    st.subheader("Dashboard voltado para análise de qualidade")
    st.image(imagem)
    st.subheader("Gráfico(Aparelho/Acessórios)")
    st.subheader("ANA: ")
    st.bar_chart(df_melt_junho_APARELHO_ANA.set_index('consultor'))
    st.subheader("ANDERSON: ")
    st.bar_chart(df_melt_junho_APARELHO_ANDERSON.set_index('consultor'))
    st.subheader("AMANDA: ")
    st.bar_chart(df_melt_junho_APARELHO_AMANDA.set_index('consultor'))
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

     
    

