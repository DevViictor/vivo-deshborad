import pandas as pd
from readfile_Total_controle_pos_seguro import *



df = pd.DataFrame ([{

'TOTAL' : todo["Produto"].isin(["CONTROLE"]).sum(),
'ANA' : ANA_maioc["Produto"].isin(["CONTROLE"]).sum(),
'ANDERSON' : ANDERSON_maioc["Produto"].isin(["CONTROLE"]).sum(),
'CAROL' : CAROL_maioc["Produto"].isin(["CONTROLE"]).sum(),
'DAVIDG' : DAVIDG_maioc["Produto"].isin(["CONTROLE"]).sum(),
'DEBORA' : DEBORA_maioc ["Produto"].isin(["CONTROLE"]).sum(),
'LENET' : LENE_maioc["Produto"].isin(["CONTROLE"]).sum(),
'WILLERT' : WILLER_maioc["Produto"].isin(["CONTROLE"]).sum(),

}])

df_melt = df.melt(value_name = "valor" , var_name = "consultor")


df2 = pd.DataFrame ([{

'TOTAL' : totalpos["Produto"].isin(["PÓS PAGO"]).sum(),
'ANA' : ANA_maio_filtrop ["Produto"].isin(["PÓS PAGO"]).sum(),
'ANDERSON' : ANDERSON_maio_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'CAROL' : CAROL_maio_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'DAVIDG' : DAVIDG_maio_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'DEBORA' : DEBORA_maio_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'LENET' : LENE_maio_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'WILLERT' : WILLER_maio_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),

}])

df_melt2 = df2.melt(value_name = "valor" , var_name = "consultor")


df3 = pd.DataFrame ([{

'TOTAL' : totalseguro["Serviço"].isin(["Seguro"]).sum(),
'ANA' : ANA_maio_filtros ["Serviço"].isin(["Seguro"]).sum(),
'ANDERSON' : ANDERSON_maio_filtros["Serviço"].isin(["Seguro"]).sum(),
'CAROL' : CAROL_maio_filtros["Serviço"].isin(["Seguro"]).sum(),
'DAVIDG' : DAVIDG_maio_filtros["Serviço"].isin(["Seguro"]).sum(),
'DEBORA' : DEBORA_maio_filtros["Serviço"].isin(["Seguro"]).sum(),
'LENET' : LENE_maio_filtros["Serviço"].isin(["Seguro"]).sum(),
'WILLERT' : WILLER_maio_filtros["Serviço"].isin(["Seguro"]).sum(),

}])

df_melt3 = df3.melt(value_name = "valor" , var_name = "consultor")



#JUNHO

df_junho = pd.DataFrame ([{

'ANA' : ANA_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'ANDERSON' : ANA_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'CAROL' : CAROL_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'DAVIDG' : DAVIDG_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'DEBORA' : DEBORA_junho_filtro ["Produto"].isin(["CONTROLE"]).sum(),
'WILLERT' : WILLER_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),

}])

df_melt_junho_CONTROLE = df_junho.melt(value_name = "valor" , var_name = "consultor")


df_junho2 = pd.DataFrame ([{

'ANA' : ANA_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'ANDERSON' : ANA_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'CAROL' : CAROL_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'DAVIDG' : DAVIDG_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'DEBORA' : DEBORA_junho_filtrop ["Produto"].isin(["PÓS PAGO"]).sum(),
'WILLERT' : WILLER_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),

}])

df_melt_junho_PÓS = df_junho2.melt(value_name = "valor" , var_name = "consultor")


df_junho3 = pd.DataFrame ([{

'ANA' : ANA_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'ANDERSON' : ANDERSON_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'CAROL' : CAROL_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'DAVIDG' : DAVIDG_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'DEBORA' : DEBORA_junho_filtros ["Serviço"].isin(["Seguro"]).sum(),
'WILLERT' : WILLER_junho_filtros["Serviço"].isin(["Seguro"]).sum(),

}])

df_melt_junho_SEGURO = df_junho3.melt(value_name = "valor" , var_name = "consultor")


