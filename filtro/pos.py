import pandas as pd 

vivo = pd.read_excel("excel_file/coleta_pós.xlsx")

vivo = vivo[vivo["Produto"].isin(["PÓS PAGO"])]

vivo = vivo[["DATA","Linha","Plano","Produto"]]

vivo.to_excel("excel_pós/DAVIDG_pós.xlsx")