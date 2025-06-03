import pandas as pd

seguro = "excel_file/vendedores_seguro.xlsx"
seguro_total = "excel_file/seguro_dados.xlsx"

ANA_SEGURO = pd.read_excel(seguro,sheet_name="ANA" ,engine="openpyxl")
ANDERSON_SEGURO = pd.read_excel(seguro,sheet_name="ANDERSON" ,engine="openpyxl")
CAROL_SEGURO = pd.read_excel(seguro,sheet_name="CAROL" ,engine="openpyxl")
DAVIDG_SEGURO = pd.read_excel(seguro,sheet_name="DAVIDG" ,engine="openpyxl")
DEBORA_SEGURO = pd.read_excel(seguro,sheet_name="DEBORA" ,engine="openpyxl")
LENE_SEGURO = pd.read_excel(seguro,sheet_name="LENE" ,engine="openpyxl")
WILLER_SEGURO = pd.read_excel(seguro,sheet_name="WILLER" ,engine="openpyxl")

totalseguro = pd.read_excel(seguro_total)
