import pandas as pd
from readfile_Total import *



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
'LENE' : LENE_maio_filtros["Serviço"].isin(["Seguro"]).sum(),
'WILLER' : WILLER_maio_filtros["Serviço"].isin(["Seguro"]).sum(),

}])

df_melt3 = df3.melt(value_name = "valor" , var_name = "consultor")



#JUNHO

#junho_grafico_controle

df_junho = pd.DataFrame ([{

'ANA' : ANA_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'ANDERSON' : ANDERSON_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'AMANDA' :  AMANDA_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'CAROL' : CAROL_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'DAVIDG' : DAVIDG_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
'DEBORA' : DEBORA_junho_filtro ["Produto"].isin(["CONTROLE"]).sum(),
'WILLER' : WILLER_junho_filtro["Produto"].isin(["CONTROLE"]).sum(),
"Total" : junho_acumulado_controle,
}])

df_melt_junho_CONTROLE = df_junho.melt(value_name = "valor" , var_name = "consultor")


#junho_grafico_pós

df_junho2 = pd.DataFrame ([{

'ANA' : ANA_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'ANDERSON' : ANDERSON_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'AMANDA'  : AMANDA_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'CAROL' : CAROL_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'DAVIDG' : DAVIDG_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
'DEBORA' : DEBORA_junho_filtrop ["Produto"].isin(["PÓS PAGO"]).sum(),
'WILLER' : WILLER_junho_filtrop["Produto"].isin(["PÓS PAGO"]).sum(),
"TOTAL" : junho_acumulado_pós,

}])

df_melt_junho_PÓS = df_junho2.melt(value_name = "valor" , var_name = "consultor")

#junho_grafico_seguro

df_junho3 = pd.DataFrame ([{

'ANA' : ANA_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'ANDERSON' : ANDERSON_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'AMANDA' : AMANDA_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'CAROL' : CAROL_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'DAVIDG' : DAVIDG_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
'DEBORA' : DEBORA_junho_filtros ["Serviço"].isin(["Seguro"]).sum(),
'WILLER' : WILLER_junho_filtros["Serviço"].isin(["Seguro"]).sum(),
"Total" : junho_acumulado_seguro,

}])

df_melt_junho_SEGURO = df_junho3.melt(value_name = "valor" , var_name = "consultor")


#junho_grafico_aparelho

df_junho_ANAAP = pd.DataFrame ([{

"ANA" : ANA_junho_TOTALA , 
"AC" : ANA_junho_TOTALAC

}])

df_melt_junho_APARELHO_ANA = df_junho_ANAAP.melt(value_name = "valor" , var_name = "consultor")



df_junho_ANDERSONAP = pd.DataFrame ([{

"ANDERSON" : ANDERSON_junho_TOTALA , 
"AC" : ANDERSON_junho_TOTALAC

}])

df_melt_junho_APARELHO_ANDERSON = df_junho_ANDERSONAP.melt(value_name = "valor" , var_name = "consultor")


df_junho_AMANDAAP = pd.DataFrame ([{

"AMANDA" : AMANDA_junho_TOTALA , 
"AC" : AMANDA_junho_TOTALC

}])

df_melt_junho_APARELHO_AMANDA = df_junho_AMANDAAP.melt(value_name = "valor" , var_name = "consultor")


df_junho_CAROLAP = pd.DataFrame ([{

"CAROL" : ANA_junho_TOTALA , 
"AC" : ANA_junho_TOTALAC

}])

df_melt_junho_APARELHO_CAROL = df_junho_CAROLAP.melt(value_name = "valor" , var_name = "consultor")


df_junho_DEBORAAP = pd.DataFrame ([{

"DEBORA" : DEBORA_junho_TOTALA , 
"AC" : DEBORA_junho_TOTALAC

}])

df_melt_junho_APARELHO_DEBORA = df_junho_DEBORAAP.melt(value_name = "valor" , var_name = "consultor")


df_junho_DAVIDGAP = pd.DataFrame ([{

"DAVIDG" : DAVIDG_junho_TOTALA , 
"AC" : DAVIDG_junho_TOTALAC

}])

df_melt_junho_APARELHO_DAVIDG = df_junho_DAVIDGAP.melt(value_name = "valor" , var_name = "consultor")


df_junho_WILLERAP = pd.DataFrame ([{

"WILLER" : WILLER_junho_TOTALA , 
"AC" : WILLER_junho_TOTALAC

}])

df_melt_junho_APARELHO_WILLER = df_junho_WILLERAP.melt(value_name = "valor" , var_name = "consultor")



