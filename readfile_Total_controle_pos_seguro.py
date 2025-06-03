import pandas as pd

from readfile_controle_pos import *
from redfile_seguro import *    




ANAT = ANA ["Produto"].isin(["CONTROLE"]).value_counts()
ANDERSONT = ANDERSON["Produto"].isin(["CONTROLE"]).value_counts()
CAROLT = CAROL["Produto"].isin(["CONTROLE"]).value_counts()
DAVIDGT = DAVIDG["Produto"].isin(["CONTROLE"]).value_counts()
DEBORAT = DEBORA["Produto"].isin(["CONTROLE"]).value_counts()
LENET = LENE["Produto"].isin(["CONTROLE"]).value_counts()
WILLERT = WILLER["Produto"].isin(["CONTROLE"]).value_counts()

totalc = todo["Produto"].isin(["CONTROLE"]).value_counts()


ANAT2 = ANA2["Produto"].isin(["PÓS PAGO"]).value_counts()
ANDERSONT2 = ANDERSON2["Produto"].isin(["PÓS PAGO"]).value_counts()
CAROLT2 = CAROL2["Produto"].isin(["PÓS PAGO"]).value_counts()
DAVIDGT2 = DAVIDG2["Produto"].isin(["PÓS PAGO"]).value_counts()
DEBORAT2 = DEBORA2["Produto"].isin(["PÓS PAGO"]).value_counts()
LENET2 = LENE2["Produto"].isin(["PÓS PAGO"]).value_counts()
WILLERT2 = WILLER2["Produto"].isin(["PÓS PAGO"]).value_counts()

cont_pos = totalpos["Produto"].isin(["PÓS PAGO"]).value_counts()


ANA_SEGUROT = ANA_SEGURO["Serviço"].isin(["Seguro"]).value_counts()
ANDERSON_SEGUROT = ANDERSON_SEGURO["Serviço"].isin(["Seguro"]).value_counts()
CAROL_SEGUROT = CAROL_SEGURO["Serviço"].isin(["Seguro"]).value_counts()
DAVIDG_SEGUROT = DAVIDG_SEGURO["Serviço"].isin(["Seguro"]).value_counts()
DEBORA_SEGUROT = DEBORA_SEGURO["Serviço"].isin(["Seguro"]).value_counts()
LENE_SEGUROT = LENE_SEGURO["Serviço"].isin(["Seguro"]).value_counts()
WILLER_SEGUROT = WILLER_SEGURO["Serviço"].isin(["Seguro"]).value_counts()

cont_seguro = totalseguro["Serviço"].isin(["Seguro"]).value_counts()