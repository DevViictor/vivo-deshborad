import pandas as pd 

vivo = pd.read_excel("coleta_controle.xlsx")

vivo = vivo[vivo["Produto"].isin(["CONTROLE"])]

vivo = vivo[["DATA","Linha","Plano","Produto"]]

vivo.to_excel("DAVIDG.xlsx")