import pandas as pd

from readfile_controle_pos import *




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
