import pandas as pd 

vivo = pd.read_excel("excel_file/coleta_seguro.xlsx")

vivo = vivo[vivo["Serviço"].isin(["Seguro"])]

vivo = vivo[["DATA","Linha","Serviço"]]

vivo.to_excel("excel_seguro/CAROL_seguro.xlsx")