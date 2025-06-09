import pandas as pd

from readfile_controle_pos import *
  


#MAIO:

maio_total = "excel_file/vendedores_controle_maio.xlsx"

#MAIO_CONTROLE: 

ANA_maioc = pd.read_excel(maio_total, sheet_name="ANA")
ANA_maio_TOTALC = ANA_maioc["Produto"].isin(["CONTROLE"]).value_counts()

ANDERSON_maioc = pd.read_excel(maio_total, sheet_name="ANDERSON")
ANDERSON_maio_TOTALC = ANDERSON_maioc["Produto"].isin(["CONTROLE"]).value_counts()

CAROL_maioc = pd.read_excel(maio_total, sheet_name="CAROL")
CAROL_maio_TOTALC = CAROL_maioc["Produto"].isin(["CONTROLE"]).value_counts()

DAVIDG_maioc = pd.read_excel(maio_total, sheet_name="DAVIDG")
DAVIDG_maio_TOTALC = DAVIDG_maioc["Produto"].isin(["CONTROLE"]).value_counts()

DEBORA_maioc = pd.read_excel(maio_total, sheet_name="DEBORA")
DEBORA_maio_TOTALC = DEBORA_maioc["Produto"].isin(["CONTROLE"]).value_counts()

LENE_maioc = pd.read_excel(maio_total, sheet_name="LENE")
LENE_maio_TOTALC = LENE_maioc["Produto"].isin(["CONTROLE"]).value_counts()

WILLER_maioc = pd.read_excel(maio_total, sheet_name="WILLER")
WILLER_maio_TOTALC = WILLER_maioc["Produto"].isin(["CONTROLE"]).value_counts()

totalc = todo["Produto"].isin(["CONTROLE"]).value_counts()


#MAIO_PÓS: 

maio_totalp = "excel_file/vendedores_pós_maio.xlsx"

ANA_maiop = pd.read_excel(maio_totalp, sheet_name="ANA")
ANA_maio_TOTALP = ANA_maiop["Produto"].isin(["PÓS PAGO"]).value_counts()

ANDERSON_maiop = pd.read_excel(maio_totalp, sheet_name="ANDERSON")
ANDERSON_maio_TOTALP = ANDERSON_maiop["Produto"].isin(["PÓS PAGO"]).value_counts()

CAROL_maiop = pd.read_excel(maio_totalp, sheet_name="CAROL")
CAROL_maio_TOTALP = CAROL_maiop["Produto"].isin(["PÓS PAGO"]).value_counts()

DAVIDG_maiop = pd.read_excel(maio_totalp, sheet_name="DAVIDG")
DAVIDG_maio_TOTALP = DAVIDG_maiop["Produto"].isin(["PÓS PAGO"]).value_counts()

DEBORA_maiop = pd.read_excel(maio_totalp, sheet_name="DEBORA")
DEBORA_maio_TOTALP = DEBORA_maiop["Produto"].isin(["PÓS PAGO"]).value_counts()

LENE_maiop = pd.read_excel(maio_totalp, sheet_name="LENE")
LENE_maio_TOTALP = LENE_maiop["Produto"].isin(["PÓS PAGO"]).value_counts()

WILLER_maiop = pd.read_excel(maio_totalp, sheet_name="WILLER")
WILLER_maio_TOTALP = WILLER_maiop["Produto"].isin(["PÓS PAGO"]).value_counts()

cont_pos = totalpos["Produto"].isin(["PÓS PAGO"]).value_counts()


#MAIO_SEGURO: 

maio_totals = "excel_file/vendedores_seguro_maio.xlsx"

ANA_maios = pd.read_excel(maio_totals, sheet_name="ANA")
ANA_maio_TOTALS = ANA_maios["Serviço"].isin(["Seguro"]).value_counts()

ANDERSON_maios = pd.read_excel(maio_totals, sheet_name="ANDERSON")
ANDERSON_maio_TOTALS = ANDERSON_maios["Serviço"].isin(["Seguro"]).value_counts()

CAROL_maios = pd.read_excel(maio_totals, sheet_name="CAROL")
CAROL_maio_TOTALS = CAROL_maios["Serviço"].isin(["Seguro"]).value_counts()

DAVIDG_maios = pd.read_excel(maio_totals, sheet_name="DAVIDG")
DAVIDG_maio_TOTALS = DAVIDG_maios["Serviço"].isin(["Seguro"]).value_counts()

DEBORA_maios = pd.read_excel(maio_totals, sheet_name="DEBORA")
DEBORA_maio_TOTALS = DEBORA_maios["Serviço"].isin(["Seguro"]).value_counts()

LENE_maios = pd.read_excel(maio_totals, sheet_name="LENE")
LENE_maio_TOTALS = LENE_maios["Serviço"].isin(["Seguro"]).value_counts()

WILLER_maios = pd.read_excel(maio_totals, sheet_name="WILLER")
WILLER_maio_TOTALS = WILLER_maios["Serviço"].isin(["Seguro"]).value_counts()

cont_seguro = totalseguro["Serviço"].isin(["Seguro"]).value_counts()

#JUNHO: 

#JUNHO_CONTROLE: 

junho_total = "excel_file/vendedores_controle_junho.xlsx"

ANA_junhoc = pd.read_excel(junho_total, sheet_name="ANA")
ANA_junho_TOTALC = ANA_junhoc["Produto"].value_counts().get("CONTROLE",0)

AMANDA_junhoc = pd.read_excel(junho_total, sheet_name="AMANDA")
AMANDA_junho_TOTALC = AMANDA_junhoc["Produto"].value_counts().get("CONTROLE",0)

ANDERSON_junhoc = pd.read_excel(junho_total, sheet_name="ANDERSON")
ANDERSON_junho_TOTALC = ANDERSON_junhoc["Produto"].value_counts().get("CONTROLE",0)

CAROL_junhoc = pd.read_excel(junho_total, sheet_name="CAROL")
CAROL_junho_TOTALC = CAROL_junhoc["Produto"].value_counts().get("CONTROLE",0)

DAVIDG_junhoc = pd.read_excel(junho_total, sheet_name="DAVIDG")
DAVIDG_junho_TOTALC = DAVIDG_junhoc["Produto"].value_counts().get("CONTROLE",0)

DEBORA_junhoc = pd.read_excel(junho_total, sheet_name="DEBORA")
DEBORA_junho_TOTALC = DEBORA_junhoc["Produto"].value_counts().get("CONTROLE",0)

WILLER_junhoc = pd.read_excel(junho_total, sheet_name="WILLER")
WILLER_junho_TOTALC = WILLER_junhoc["Produto"].value_counts().get("CONTROLE",0)


junho_acumulado_controle = ( ANA_junho_TOTALC + AMANDA_junho_TOTALC + ANDERSON_junho_TOTALC 

+ CAROL_junho_TOTALC + DAVIDG_junho_TOTALC + DEBORA_junho_TOTALC + WILLER_junho_TOTALC )


#JUNHO_PÓS:


ANA_junhop = pd.read_excel(junho_total, sheet_name="ANA")
ANA_junho_TOTALP = ANA_junhop["Produto"].value_counts().get("PÓS PAGO",0)

AMANDA_junhop = pd.read_excel(junho_total, sheet_name="AMANDA")
AMANDA_junho_TOTALP = AMANDA_junhop["Produto"].value_counts().get("PÓS PAGO",0)

ANDERSON_junhop = pd.read_excel(junho_total, sheet_name="ANDERSON")
ANDERSON_junho_TOTALP = ANDERSON_junhop["Produto"].value_counts().get("PÓS PAGO",0)

CAROL_junhop = pd.read_excel(junho_total, sheet_name="CAROL")
CAROL_junho_TOTALP = CAROL_junhop["Produto"].value_counts().get("PÓS PAGO",0)

DAVIDG_junhop = pd.read_excel(junho_total, sheet_name="DAVIDG")
DAVIDG_junho_TOTALP = DAVIDG_junhop["Produto"].value_counts().get("PÓS PAGO",0)

DEBORA_junhop = pd.read_excel(junho_total, sheet_name="DEBORA")
DEBORA_junho_TOTALP = DEBORA_junhop["Produto"].value_counts().get("PÓS PAGO",0)

WILLER_junhop = pd.read_excel(junho_total, sheet_name="WILLER")
WILLER_junho_TOTALP = WILLER_junhop["Produto"].value_counts().get("PÓS PAGO",0)

#junho_acuumulado_pós: 

junho_acumulado_pós = ( ANA_junho_TOTALP + AMANDA_junho_TOTALP + ANDERSON_junho_TOTALP 

+ CAROL_junho_TOTALP + DAVIDG_junho_TOTALP + DEBORA_junho_TOTALP + WILLER_junho_TOTALP )



#JUNHO_SEGURO: 

ANA_junhos = pd.read_excel(junho_total, sheet_name="ANA")
ANA_junho_TOTALS = ANA_junhos["Serviço"].value_counts().get("Seguro",0)

AMANDA_junhos = pd.read_excel(junho_total, sheet_name="AMANDA")
AMANDA_junho_TOTALS = AMANDA_junhos["Serviço"].value_counts().get("Seguro",0)

ANDERSON_junhos = pd.read_excel(junho_total, sheet_name="ANDERSON")
ANDERSON_junho_TOTALS = ANDERSON_junhos["Serviço"].value_counts().get("Seguro",0)

CAROL_junhos = pd.read_excel(junho_total, sheet_name="CAROL")
CAROL_junho_TOTALS = CAROL_junhos["Serviço"].value_counts().get("Seguro",0)

DAVIDG_junhos = pd.read_excel(junho_total, sheet_name="DAVIDG")
DAVIDG_junho_TOTALS = DAVIDG_junhos["Serviço"].value_counts().get("Seguro",0)

DEBORA_junhos = pd.read_excel(junho_total, sheet_name="DEBORA")
DEBORA_junho_TOTALS = DEBORA_junhos["Serviço"].value_counts().get("Seguro",0)

WILLER_junhos = pd.read_excel(junho_total, sheet_name="WILLER")
WILLER_junho_TOTALS = WILLER_junhos["Serviço"].value_counts().get("Seguro",0)

#JUNHO_ACUMULADO_SEGURO: 

junho_acumulado_seguro = ( ANA_junho_TOTALS + AMANDA_junho_TOTALS + ANDERSON_junho_TOTALS 

+ CAROL_junho_TOTALS + DAVIDG_junho_TOTALS + DEBORA_junho_TOTALS + WILLER_junho_TOTALS )
