
import pandas as pd

arquivo = "excel_file/controle_dados.xlsx"
pos_total ="excel_file/pós_dados.xlsx"
seguro_dados ="excel_file/seguro_dados.xlsx"

todo = pd.read_excel(arquivo)

totalpos = pd.read_excel(pos_total)

totalseguro = pd.read_excel(seguro_dados)

#COLUNAS
Select_Coluns = ["DATA", "Linha" ,"Plano" , "Produto"]
Select_Coluns2 = ["DATA", "Linha" ,"Serviço"]
Select_Coluns3 = ["DATA", "CPF / CNPJ" ,"Serviço"]

#LINHAS
Select_Filtro = "CONTROLE"
Select_Filtro2 = "PÓS PAGO"
Select_Filtro3 = "Seguro"
Select_Filtro4 = "Aparelho"
Select_Filtro5 = "Acessórios"


#MAIO_CONTROLE

ANA_maio = pd.read_excel("excel_file/vendedores_controle_maio.xlsx", usecols= Select_Coluns, sheet_name="ANA")
ANA_maio_filtro = ANA_maio[ANA_maio["Produto"] == Select_Filtro]

ANDERSON_maio = pd.read_excel("excel_file/vendedores_controle_maio.xlsx", usecols=Select_Coluns, sheet_name="ANDERSON")
ANDERSON_maio_filtro = ANDERSON_maio[ANDERSON_maio["Produto"] == Select_Filtro]

CAROL_maio = pd.read_excel("excel_file/vendedores_controle_maio.xlsx", usecols=Select_Coluns, sheet_name="CAROL")
CAROL_maio_filtro = CAROL_maio[CAROL_maio["Produto"] == Select_Filtro]

DAVIDG_maio = pd.read_excel("excel_file/vendedores_controle_maio.xlsx", usecols=Select_Coluns, sheet_name="DAVIDG")
DAVIDG_maio_filtro = DAVIDG_maio[DAVIDG_maio["Produto"] == Select_Filtro]

DEBORA_maio = pd.read_excel("excel_file/vendedores_controle_maio.xlsx", usecols=Select_Coluns, sheet_name="DEBORA")
DEBORA_maio_filtro = DEBORA_maio[DEBORA_maio["Produto"] == Select_Filtro]

LENE_maio = pd.read_excel("excel_file/vendedores_controle_maio.xlsx", usecols=Select_Coluns, sheet_name="LENE")
LENE_maio_filtro = LENE_maio[LENE_maio["Produto"] == Select_Filtro]

WILLER_maio = pd.read_excel("excel_file/vendedores_controle_maio.xlsx", usecols=Select_Coluns, sheet_name="WILLER")
WILLER_maio_filtro = WILLER_maio[WILLER_maio["Produto"] == Select_Filtro]


#MAIO_PÓS

ANA_maiop = pd.read_excel("excel_file/vendedores_pós_maio.xlsx", usecols=Select_Coluns, sheet_name="ANA")
ANA_maio_filtrop = ANA_maiop[ANA_maiop["Produto"] == Select_Filtro2]

ANDERSON_maiop = pd.read_excel("excel_file/vendedores_pós_maio.xlsx", usecols=Select_Coluns, sheet_name="ANDERSON")
ANDERSON_maio_filtrop = ANDERSON_maiop[ANDERSON_maiop["Produto"] == Select_Filtro2]

CAROL_maiop = pd.read_excel("excel_file/vendedores_pós_maio.xlsx", usecols=Select_Coluns, sheet_name="CAROL")
CAROL_maio_filtrop = CAROL_maiop[CAROL_maiop["Produto"] == Select_Filtro2]

DAVIDG_maiop = pd.read_excel("excel_file/vendedores_pós_maio.xlsx", usecols=Select_Coluns, sheet_name="DAVIDG")
DAVIDG_maio_filtrop = DAVIDG_maiop[DAVIDG_maiop["Produto"] == Select_Filtro2]

DEBORA_maiop = pd.read_excel("excel_file/vendedores_pós_maio.xlsx", usecols=Select_Coluns, sheet_name="DEBORA")
DEBORA_maio_filtrop = DEBORA_maiop[DEBORA_maiop["Produto"] == Select_Filtro2]

LENE_maiop = pd.read_excel("excel_file/vendedores_pós_maio.xlsx", usecols=Select_Coluns, sheet_name="LENE")
LENE_maio_filtrop = LENE_maiop[LENE_maiop["Produto"] == Select_Filtro2]

WILLER_maiop = pd.read_excel("excel_file/vendedores_pós_maio.xlsx", usecols=Select_Coluns, sheet_name="WILLER")
WILLER_maio_filtrop = WILLER_maiop[WILLER_maiop["Produto"] == Select_Filtro2]


#MAIO_SEGURO

ANA_maios = pd.read_excel("excel_file/vendedores_seguro_maio.xlsx", usecols=Select_Coluns2, sheet_name="ANA")
ANA_maio_filtros = ANA_maios[ANA_maios["Serviço"] == Select_Filtro3]

ANDERSON_maios = pd.read_excel("excel_file/vendedores_seguro_maio.xlsx", usecols=Select_Coluns2, sheet_name="ANDERSON")
ANDERSON_maio_filtros = ANDERSON_maios[ANDERSON_maios["Serviço"] == Select_Filtro3]

CAROL_maios = pd.read_excel("excel_file/vendedores_seguro_maio.xlsx", usecols=Select_Coluns2, sheet_name="CAROL")
CAROL_maio_filtros = CAROL_maios[CAROL_maios["Serviço"] == Select_Filtro3]

DAVIDG_maios = pd.read_excel("excel_file/vendedores_seguro_maio.xlsx", usecols=Select_Coluns2, sheet_name="DAVIDG")
DAVIDG_maio_filtros = DAVIDG_maios[DAVIDG_maios["Serviço"] == Select_Filtro3]

DEBORA_maios = pd.read_excel("excel_file/vendedores_seguro_maio.xlsx", usecols=Select_Coluns2, sheet_name="DEBORA")
DEBORA_maio_filtros = DEBORA_maios[DEBORA_maios["Serviço"] == Select_Filtro3]

LENE_maios = pd.read_excel("excel_file/vendedores_seguro_maio.xlsx", usecols=Select_Coluns2, sheet_name="LENE")
LENE_maio_filtros = LENE_maios[LENE_maios["Serviço"] == Select_Filtro3]

WILLER_maios = pd.read_excel("excel_file/vendedores_seguro_maio.xlsx", usecols=Select_Coluns2, sheet_name="WILLER")
WILLER_maio_filtros = WILLER_maios[WILLER_maios["Serviço"] == Select_Filtro3]


#JUNHO_CONTROLE

ANA_junho = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="ANA")
ANA_junho_filtro = ANA_junho[ANA_junho["Produto"] == Select_Filtro]

AMANDA_junho = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="AMANDA")
AMANDA_junho_filtro = AMANDA_junho[AMANDA_junho["Produto"] == Select_Filtro]

ANDERSON_junho = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="ANDERSON")
ANDERSON_junho_filtro = ANDERSON_junho[ANDERSON_junho["Produto"] == Select_Filtro]

CAROL_junho = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="CAROL")
CAROL_junho_filtro = CAROL_junho[CAROL_junho["Produto"] == Select_Filtro]

DAVIDG_junho = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="DAVIDG")
DAVIDG_junho_filtro = DAVIDG_junho[DAVIDG_junho["Produto"] == Select_Filtro]

DEBORA_junho = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="DEBORA")
DEBORA_junho_filtro = DEBORA_junho[DEBORA_junho["Produto"] == Select_Filtro]

WILLER_junho = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="WILLER")
WILLER_junho_filtro = WILLER_junho[WILLER_junho["Produto"] == Select_Filtro]


#JUNHO_PÓS

ANA_junhop = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="ANA")
ANA_junho_filtrop = ANA_junhop[ANA_junhop["Produto"] == Select_Filtro2]

AMANDA_junhop = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="AMANDA")
AMANDA_junho_filtrop = AMANDA_junhop[AMANDA_junhop["Produto"] == Select_Filtro2]

ANDERSON_junhop = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="ANDERSON")
ANDERSON_junho_filtrop = ANDERSON_junhop[ANDERSON_junhop["Produto"] == Select_Filtro2]

CAROL_junhop = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="CAROL")
CAROL_junho_filtrop = CAROL_junhop[CAROL_junhop["Produto"] == Select_Filtro2]

DAVIDG_junhop = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="DAVIDG")
DAVIDG_junho_filtrop = DAVIDG_junhop[DAVIDG_junhop["Produto"] == Select_Filtro2]

DEBORA_junhop = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="DEBORA")
DEBORA_junho_filtrop = DEBORA_junhop[DEBORA_junhop["Produto"] == Select_Filtro2]

WILLER_junhop = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns, sheet_name="WILLER")
WILLER_junho_filtrop = WILLER_junhop[WILLER_junhop["Produto"] == Select_Filtro2]


#JUNHO_SEGURO

ANA_junhos = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns2, sheet_name="ANA")
ANA_junho_filtros = ANA_junhos[ANA_junhos["Serviço"] == Select_Filtro3]

AMANDA_junhos = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns2, sheet_name="AMANDA")
AMANDA_junho_filtros = AMANDA_junhos[AMANDA_junhos["Serviço"] == Select_Filtro3]

ANDERSON_junhos = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns2, sheet_name="ANDERSON")
ANDERSON_junho_filtros = ANDERSON_junhos[ANDERSON_junhos["Serviço"] == Select_Filtro3]

CAROL_junhos = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns2, sheet_name="CAROL")
CAROL_junho_filtros = CAROL_junhos[CAROL_junhos["Serviço"] == Select_Filtro3]

DAVIDG_junhos = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns2, sheet_name="DAVIDG")
DAVIDG_junho_filtros = DAVIDG_junhos[DAVIDG_junhos["Serviço"] == Select_Filtro3]

DEBORA_junhos = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns2, sheet_name="DEBORA")
DEBORA_junho_filtros = DEBORA_junhos[DEBORA_junhos["Serviço"] == Select_Filtro3]

WILLER_junhos = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns2, sheet_name="WILLER")
WILLER_junho_filtros = WILLER_junhos[WILLER_junhos["Serviço"] == Select_Filtro3]


#JUNHO_APARELHOS

ANA_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="ANA")
ANA_junho_filtroa = ANA_junhoa[ANA_junhoa["Serviço"] == Select_Filtro4]

AMANDA_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="AMANDA")
AMANDA_junho_filtroa = AMANDA_junhoa[AMANDA_junhoa["Serviço"] == Select_Filtro4]

ANDERSON_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="ANDERSON")
ANDERSON_junho_filtroa = ANDERSON_junhoa[ANDERSON_junhoa["Serviço"] == Select_Filtro4]

CAROL_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="CAROL")
CAROL_junho_filtroa = CAROL_junhoa[CAROL_junhoa["Serviço"] == Select_Filtro4]

DAVIDG_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="DAVIDG")
DAVIDG_junho_filtroa = DAVIDG_junhoa[DAVIDG_junhoa["Serviço"] == Select_Filtro4]

DEBORA_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="DEBORA")
DEBORA_junho_filtroa = DEBORA_junhoa[DEBORA_junhoa["Serviço"] == Select_Filtro4]

WILLER_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="WILLER")
WILLER_junho_filtroa = WILLER_junhoa[WILLER_junhoa["Serviço"] == Select_Filtro4]

#JUNHO_ACESSORIOS

ANA_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="ANA")
ANA_junho_filtroac = ANA_junhoa[ANA_junhoa["Serviço"] == Select_Filtro5]

AMANDA_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="AMANDA")
AMANDA_junho_filtroac = AMANDA_junhoa[AMANDA_junhoa["Serviço"] == Select_Filtro5]

ANDERSON_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="ANDERSON")
ANDERSON_junho_filtroac = ANDERSON_junhoa[ANDERSON_junhoa["Serviço"] == Select_Filtro5]

CAROL_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="CAROL")
CAROL_junho_filtroac = CAROL_junhoa[CAROL_junhoa["Serviço"] == Select_Filtro5]

DAVIDG_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="DAVIDG")
DAVIDG_junho_filtroac = DAVIDG_junhoa[DAVIDG_junhoa["Serviço"] == Select_Filtro5]

DEBORA_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="DEBORA")
DEBORA_junho_filtroac = DEBORA_junhoa[DEBORA_junhoa["Serviço"] == Select_Filtro5]

WILLER_junhoa = pd.read_excel("excel_file/vendedores_controle_junho.xlsx", usecols=Select_Coluns3, sheet_name="WILLER")
WILLER_junho_filtroac = WILLER_junhoa[WILLER_junhoa["Serviço"] == Select_Filtro5]



