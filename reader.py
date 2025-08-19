import pandas as pd
import streamlit as st

coletor = st.file_uploader("Carregue a planilha do formato solicitado: ", type=["xlsx","ods"])

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

    def ler_planilha_aparelho(coletor,aba,contar="Aparelhos"):
        leitor6 = pd.read_excel(coletor, sheet_name=aba)
        total_aparelho = (leitor6["Serviço"] == contar).sum()
        return total_aparelho

    def ler_planilha_acessorio(coletor,aba,contar="Acessórios"):
        leitor7 = pd.read_excel(coletor, sheet_name=aba)
        total_acessorio = (leitor7["Serviço"] == contar).sum()
        return total_acessorio

#CONTROLE
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

