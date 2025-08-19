import pandas as pd
import streamlit as st
from PIL import Image


coletor = st.file_uploader("Carregue a planilha", type=["xlsx","ods"])
imagem = imagem = Image.open('imagem/estoque.png')
windows = st.sidebar.radio("GUIA DE NAVEGAÇÃO", ["Inicio"])

st.header("Dashboard voltado para análise de qualidade")
st.image(imagem)

if coletor is not None :

    def ler_planilha(coletor,aba,contar ="CONTROLE"):
       leitor = pd.read_excel(coletor , sheet_name=aba)
       total = (leitor["Produto"] == contar).sum()
       return total

    def ler_planilha_pós(coletor,aba,contar ="PÓS PAGO"):
        leitor2 = pd.read_excel(coletor , sheet_name=aba) 
        total_pós = (leitor2["Produto"] == contar).sum()
        return total_pós
    
    def ler_planilha_Fixa(coletor,aba,contar = "Fixa"):
        leitor3 = pd.read_excel(coletor, sheet_name=aba)
        total_fixa = (leitor3["Serviço"] == contar).sum()
        return total_fixa
    
    def ler_planilha_sva(coletor,aba,contar="SVA"):
        leitor4 = pd.read_excel(coletor , sheet_name= aba)
        total_sva = (leitor4["Serviço"] == contar).sum()
        return total_sva
    
    def ler_planilha_seguro(coletor,aba,contar="Seguro"):
        leitor5 = pd.read_excel(coletor, sheet_name=aba)
        total_seguro = (leitor5["Serviço"] == contar).sum()
        return total_seguro

    def ler_planilha_aparelho(coletor,aba,contar="Aparelho"):
        leitor6 = pd.read_excel(coletor, sheet_name=aba)
        total_aparelho = (leitor6["Serviço"] == contar).sum()
        return total_aparelho

    def ler_planilha_acessorio(coletor,aba,contar="Acessórios"):
        leitor7 = pd.read_excel(coletor, sheet_name=aba)
        total_acessorio = (leitor7["Serviço"] == contar).sum()
        return total_acessorio
    
    consultor1_controle = ler_planilha(coletor,aba="consultor1")
    consultor2_controle = ler_planilha(coletor, aba="consultor2")
    consultor3_controle = ler_planilha(coletor, aba="consultor3")
    consultor4_controle = ler_planilha(coletor, aba="consultor4")
    consultor5_controle = ler_planilha(coletor, aba="consultor5")
    consultor6_controle = ler_planilha(coletor, aba="consultor6")
    consultor7_controle = ler_planilha(coletor, aba="consultor7")
    consultor8_controle = ler_planilha(coletor, aba="consultor8")


    #PÓS 
    consultor1_pós = ler_planilha_pós(coletor , aba= "consultor1")
    consultor2_pós = ler_planilha_pós(coletor, aba="consultor2")
    consultor3_pós = ler_planilha_pós(coletor, aba="consultor3")
    consultor4_pós = ler_planilha_pós(coletor, aba="consultor4")
    consultor5_pós = ler_planilha_pós(coletor, aba="consultor5")
    consultor6_pós = ler_planilha_pós(coletor, aba="consultor6")
    consultor7_pós = ler_planilha_pós(coletor, aba="consultor7")
    consultor8_pós = ler_planilha_pós(coletor, aba="consultor8")


    #Fixa
    consultor1_fixa = ler_planilha_Fixa(coletor , aba="consultor1")
    consultor2_fixa = ler_planilha_Fixa(coletor, aba="consultor2")
    consultor3_fixa = ler_planilha_Fixa(coletor, aba="consultor3")
    consultor4_fixa = ler_planilha_Fixa(coletor, aba="consultor4")
    consultor5_fixa = ler_planilha_Fixa(coletor, aba="consultor5")
    consultor6_fixa = ler_planilha_Fixa(coletor, aba="consultor6")
    consultor7_fixa = ler_planilha_Fixa(coletor, aba="consultor7")
    consultor8_fixa = ler_planilha_Fixa(coletor, aba="consultor8")


    #SVA
    consultor1_sva = ler_planilha_sva(coletor , aba= "consultor1")
    consultor2_sva = ler_planilha_sva(coletor, aba="consultor2")
    consultor3_sva = ler_planilha_sva(coletor, aba="consultor3")
    consultor4_sva = ler_planilha_sva(coletor, aba="consultor4")
    consultor5_sva = ler_planilha_sva(coletor, aba="consultor5")
    consultor6_sva = ler_planilha_sva(coletor, aba="consultor6")
    consultor7_sva = ler_planilha_sva(coletor, aba="consultor7")
    consultor8_sva = ler_planilha_sva(coletor, aba="consultor8")


    #SEGURO
    consultor1_seguro = ler_planilha_seguro(coletor , aba="consultor1")
    consultor2_seguro = ler_planilha_seguro(coletor, aba="consultor2")
    consultor3_seguro = ler_planilha_seguro(coletor, aba="consultor3")
    consultor4_seguro = ler_planilha_seguro(coletor, aba="consultor4")
    consultor5_seguro = ler_planilha_seguro(coletor, aba="consultor5")
    consultor6_seguro = ler_planilha_seguro(coletor, aba="consultor6")
    consultor7_seguro = ler_planilha_seguro(coletor, aba="consultor7")
    consultor8_seguro = ler_planilha_seguro(coletor, aba="consultor8")


    #APARELHO
    consultor1_aparelho = ler_planilha_aparelho(coletor , aba="consultor1")
    consultor2_aparelho = ler_planilha_aparelho(coletor, aba="consultor2")
    consultor3_aparelho = ler_planilha_aparelho(coletor, aba="consultor3")
    consultor4_aparelho = ler_planilha_aparelho(coletor, aba="consultor4")
    consultor5_aparelho = ler_planilha_aparelho(coletor, aba="consultor5")
    consultor6_aparelho = ler_planilha_aparelho(coletor, aba="consultor6")
    consultor7_aparelho = ler_planilha_aparelho(coletor, aba="consultor7")
    consultor8_aparelho = ler_planilha_aparelho(coletor, aba="consultor8")


    #ACESSÓRIO
    consultor1_acessorio = ler_planilha_acessorio(coletor, aba = "consultor1")
    consultor2_acessorio = ler_planilha_acessorio(coletor, aba="consultor2")
    consultor3_acessorio = ler_planilha_acessorio(coletor, aba="consultor3")
    consultor4_acessorio = ler_planilha_acessorio(coletor, aba="consultor4")
    consultor5_acessorio = ler_planilha_acessorio(coletor, aba="consultor5")
    consultor6_acessorio = ler_planilha_acessorio(coletor, aba="consultor6")
    consultor7_acessorio = ler_planilha_acessorio(coletor, aba="consultor7")
    consultor8_acessorio = ler_planilha_acessorio(coletor, aba="consultor8")

    #CONTROLE

    controle_acumulado = (consultor1_controle + consultor2_controle + consultor3_controle 
                        + consultor4_controle + consultor5_controle + consultor6_controle 
                        + consultor7_controle + consultor8_controle)

    grafico_controle = pd.DataFrame ([{

    'ANA' : consultor1_controle , 
    'ANDERSON': consultor2_controle ,
    'AMANDA': consultor3_controle ,
    'DAVID GUSTAVO' : consultor4_controle ,
    "DEBORA" : consultor5_controle ,
    "LENILDA" : consultor6_controle ,
    "LORENA": consultor7_controle ,
    "WILLER" : consultor8_controle ,
    "TOTAL" : controle_acumulado

    }])

    grafico_controle_melt = grafico_controle.melt(value_name = "valor" , var_name = "consultor")

    #PÓS

    pós_acumulado = (consultor1_pós + consultor2_pós + consultor3_pós 
                        + consultor4_pós + consultor5_pós + consultor6_pós 
                        + consultor7_pós + consultor8_pós)

    grafico_pós = pd.DataFrame ([{

    'ANA' : consultor1_pós , 
    'ANDERSON': consultor2_pós ,
    'AMANDA': consultor3_pós ,
    'DAVID GUSTAVO' : consultor4_pós ,
    "DEBORA" : consultor5_pós ,
    "LENILDA" : consultor6_pós ,
    "LORENA": consultor7_pós ,
    "WILLER" : consultor8_pós ,
    "TOTAL" : pós_acumulado

    }])

    grafico_pós_melt = grafico_pós.melt(value_name = "valor" , var_name = "consultor")

    #FIXA

    fixa_acumulado = (consultor1_fixa + consultor2_fixa + consultor3_fixa
                        + consultor4_fixa + consultor5_fixa + consultor6_fixa
                        + consultor7_fixa + consultor8_fixa)

    grafico_fixa = pd.DataFrame ([{

    'ANA' : consultor1_fixa , 
    'ANDERSON': consultor2_fixa ,
    'AMANDA': consultor3_fixa ,
    'DAVID GUSTAVO' : consultor4_fixa ,
    "DEBORA" : consultor5_fixa ,
    "LENILDA" : consultor6_fixa ,
    "LORENA": consultor7_fixa ,
    "WILLER" : consultor8_fixa ,
    "TOTAL" : fixa_acumulado

    }])

    grafico_fixa_melt = grafico_fixa.melt(value_name = "valor" , var_name = "consultor")

    #SVA

    sva_acumulado = (consultor1_sva + consultor2_sva + consultor3_sva 
                        + consultor4_sva + consultor5_sva + consultor6_sva 
                        + consultor7_sva + consultor8_sva)

    grafico_sva = pd.DataFrame ([{

    'ANA' : consultor1_sva , 
    'ANDERSON': consultor2_sva ,
    'AMANDA': consultor3_sva ,
    'DAVID GUSTAVO' : consultor4_sva ,
    "DEBORA" : consultor5_sva ,
    "LENILDA" : consultor6_sva ,
    "LORENA": consultor7_sva ,
    "WILLER" : consultor8_sva ,
    "TOTAL" : sva_acumulado

    }])

    grafico_sva_melt = grafico_sva.melt(value_name = "valor" , var_name = "consultor")

    #SEGURO

    seguro_acumulado = (consultor1_seguro + consultor2_seguro + consultor3_seguro 
                        + consultor4_seguro + consultor5_seguro + consultor6_seguro 
                        + consultor7_seguro + consultor8_seguro)

    grafico_seguro = pd.DataFrame ([{

    'ANA' : consultor1_seguro , 
    'ANDERSON': consultor2_seguro ,
    'AMANDA': consultor3_seguro ,
    'DAVID GUSTAVO' : consultor4_seguro ,
    "DEBORA" : consultor5_seguro ,
    "LENILDA" : consultor6_seguro ,
    "LORENA": consultor7_seguro ,
    "WILLER" : consultor8_seguro ,
    "TOTAL" : sva_acumulado

    }])

    grafico_seguro_melt = grafico_seguro.melt(value_name = "valor" , var_name = "consultor")

    #aparelho
    aparelho_acumulado = (consultor1_aparelho + consultor2_aparelho + consultor3_aparelho 
                        + consultor4_aparelho + consultor5_aparelho + consultor6_aparelho 
                        + consultor7_aparelho + consultor8_aparelho)

    grafico_aparelho = pd.DataFrame ([{

    'ANA' : consultor1_aparelho , 
    'ANDERSON': consultor2_aparelho  ,
    'AMANDA': consultor3_aparelho  ,
    'DAVID GUSTAVO' : consultor4_aparelho  ,
    "DEBORA" : consultor5_aparelho  ,
    "LENILDA" : consultor6_aparelho  ,
    "LORENA": consultor7_aparelho  ,
    "WILLER" : consultor8_aparelho  ,
    "TOTAL" : aparelho_acumulado

    }])

    grafico_aparelho_melt = grafico_aparelho.melt(value_name = "valor" , var_name = "consultor")

    #acessórios

    acessorio_acumulado = (consultor1_acessorio + consultor2_acessorio + consultor3_acessorio 
                        + consultor4_acessorio + consultor5_acessorio + consultor6_acessorio 
                        + consultor7_acessorio + consultor8_acessorio)

    grafico_acessorio = pd.DataFrame ([{

    'ANA' : consultor1_acessorio , 
    'ANDERSON': consultor2_acessorio  ,
    'AMANDA': consultor3_acessorio  ,
    'DAVID GUSTAVO' : consultor4_acessorio  ,
    "DEBORA" : consultor5_acessorio  ,
    "LENILDA" : consultor6_acessorio  ,
    "LORENA": consultor7_acessorio ,
    "WILLER" : consultor8_acessorio  ,
    "TOTAL" : acessorio_acumulado

    }])

    grafico_acessorio_melt = grafico_acessorio.melt(value_name = "valor" , var_name = "consultor")

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

else:
        st.warning("A planiha tem que ser no modelo solicitado")





