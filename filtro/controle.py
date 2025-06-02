import pandas as pd 

vivo = pd.read_excel("excel_file/coleta_controle.xlsx")

vivo = vivo[vivo["Produto"].isin(["CONTROLE"])]

vivo = vivo[["DATA","Linha","Plano","Produto"]]

vivo.to_excel("excel_file/WILLER.xlsx")