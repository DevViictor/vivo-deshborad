import pandas as pd
from readfile_Total_controle_pos import *



df = pd.DataFrame ([{

'TOTAL' : todo["Produto"].isin(["CONTROLE"]).sum(),
'ANA' : ANA ["Produto"].isin(["CONTROLE"]).sum(),
'ANDERSON' : ANDERSON["Produto"].isin(["CONTROLE"]).sum(),
'CAROL' : CAROL["Produto"].isin(["CONTROLE"]).sum(),
'DAVIDG' : DAVIDG["Produto"].isin(["CONTROLE"]).sum(),
'DEBORA' : DEBORA["Produto"].isin(["CONTROLE"]).sum(),
'LENET' : LENE["Produto"].isin(["CONTROLE"]).sum(),
'WILLERT' : WILLER["Produto"].isin(["CONTROLE"]).sum(),

}])

df_melt = df.melt(value_name = "valor" , var_name = "consultor")

