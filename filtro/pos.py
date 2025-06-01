import pandas as pd 

vivo = pd.read_excel("Geral.xlsx")

vivo = vivo[vivo["Produto"].isin(["PÓS PAGO"])]

vivo = vivo[["DATA","Linha","Plano","Produto"]]

vivo.to_excel("DAVIDG.xlsx")