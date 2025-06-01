
import pandas as pd

arquivo = "excel_file/controle_dados.xlsx"
arquivo_vendedores = "excel_file/vendedores_controle.xlsx"
Pos = "excel_file/vendedores_pós.xlsx"
pos_total ="excel_file/pós_dados.xlsx"


ANA = pd.read_excel(arquivo_vendedores,sheet_name="ANA" ,engine="openpyxl")


ANDERSON = pd.read_excel(arquivo_vendedores,sheet_name="ANDERSON",engine="openpyxl")


CAROL = pd.read_excel(arquivo_vendedores,sheet_name= "CAROL",engine="openpyxl")


DAVIDG = pd.read_excel(arquivo_vendedores,sheet_name="DAVIDG",engine="openpyxl")


DEBORA = pd.read_excel(arquivo_vendedores,sheet_name= "DEBORA",engine="openpyxl")


LENE = pd.read_excel(arquivo_vendedores,sheet_name="LENE",engine="openpyxl")


WILLER = pd.read_excel(arquivo_vendedores,sheet_name= "WILLER",engine="openpyxl")

todo = pd.read_excel(arquivo)




ANA2 = pd.read_excel(Pos,sheet_name="ANA" ,engine="openpyxl")


ANDERSON2 = pd.read_excel(Pos,sheet_name="ANDERSON",engine="openpyxl")


CAROL2 = pd.read_excel(Pos,sheet_name= "CAROL",engine="openpyxl")


DAVIDG2 = pd.read_excel(Pos,sheet_name="DAVIDG",engine="openpyxl")


DEBORA2 = pd.read_excel(Pos,sheet_name= "DEBORA",engine="openpyxl")


LENE2 = pd.read_excel(Pos,sheet_name="LENE",engine="openpyxl")


WILLER2 = pd.read_excel(Pos,sheet_name= "WILLER",engine="openpyxl")

totalpos = pd.read_excel(pos_total)






