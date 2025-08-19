from reader import *
import pandas as pd

#CONTROLE

controle_acumulado = (consultor1_controle + consultor2_controle + consultor3_controle 
                      + consultor4_controle + consultor5_controle + consultor6_controle 
                      + consultor7_controle + consultor8_controle)

grafico_controle = pd.DataFrame ([{

'ANA' : consultor1_controle , 
'ANDERSON': consultor2_controle ,
'AMANDA': consultor3_controle ,
'DAVID GUSTAVO' : consultor4_controle ,
"DEBORA" : consultor5_controle ,
"LENILDA" : consultor6_controle ,
"LORENA": consultor7_controle ,
"WILLER" : consultor8_controle ,
"TOTAL" : controle_acumulado

}])

grafico_controle_melt = grafico_controle.melt(value_name = "valor" , var_name = "consultor")

#PÓS

pós_acumulado = (consultor1_pós + consultor2_pós + consultor3_pós 
                      + consultor4_pós + consultor5_pós + consultor6_pós 
                      + consultor7_pós + consultor8_pós)

grafico_pós = pd.DataFrame ([{

'ANA' : consultor1_pós , 
'ANDERSON': consultor2_pós ,
'AMANDA': consultor3_pós ,
'DAVID GUSTAVO' : consultor4_pós ,
"DEBORA" : consultor5_pós ,
"LENILDA" : consultor6_pós ,
"LORENA": consultor7_pós ,
"WILLER" : consultor8_pós ,
"TOTAL" : pós_acumulado

}])

grafico_pós_melt = grafico_pós.melt(value_name = "valor" , var_name = "consultor")

#FIXA

fixa_acumulado = (consultor1_fixa + consultor2_fixa + consultor3_fixa
                      + consultor4_fixa + consultor5_fixa + consultor6_fixa
                      + consultor7_fixa + consultor8_fixa)

grafico_fixa = pd.DataFrame ([{

'ANA' : consultor1_fixa , 
'ANDERSON': consultor2_fixa ,
'AMANDA': consultor3_fixa ,
'DAVID GUSTAVO' : consultor4_fixa ,
"DEBORA" : consultor5_fixa ,
"LENILDA" : consultor6_fixa ,
"LORENA": consultor7_fixa ,
"WILLER" : consultor8_fixa ,
"TOTAL" : fixa_acumulado

}])

grafico_fixa_melt = grafico_fixa.melt(value_name = "valor" , var_name = "consultor")

#SVA

sva_acumulado = (consultor1_sva + consultor2_sva + consultor3_sva 
                      + consultor4_sva + consultor5_sva + consultor6_sva 
                      + consultor7_sva + consultor8_sva)

grafico_sva = pd.DataFrame ([{

'ANA' : consultor1_sva , 
'ANDERSON': consultor2_sva ,
'AMANDA': consultor3_sva ,
'DAVID GUSTAVO' : consultor4_sva ,
"DEBORA" : consultor5_sva ,
"LENILDA" : consultor6_sva ,
"LORENA": consultor7_sva ,
"WILLER" : consultor8_sva ,
"TOTAL" : sva_acumulado

}])

grafico_sva_melt = grafico_sva.melt(value_name = "valor" , var_name = "consultor")

#SEGURO

seguro_acumulado = (consultor1_seguro + consultor2_seguro + consultor3_seguro 
                      + consultor4_seguro + consultor5_seguro + consultor6_seguro 
                      + consultor7_seguro + consultor8_seguro)

grafico_seguro = pd.DataFrame ([{

'ANA' : consultor1_seguro , 
'ANDERSON': consultor2_seguro ,
'AMANDA': consultor3_seguro ,
'DAVID GUSTAVO' : consultor4_seguro ,
"DEBORA" : consultor5_seguro ,
"LENILDA" : consultor6_seguro ,
"LORENA": consultor7_seguro ,
"WILLER" : consultor8_seguro ,
"TOTAL" : sva_acumulado

}])

grafico_seguro_melt = grafico_seguro.melt(value_name = "valor" , var_name = "consultor")

#aparelho


aparelho_acumulado = (consultor1_aparelho + consultor2_aparelho + consultor3_aparelho 
                      + consultor4_aparelho + consultor5_aparelho + consultor6_aparelho 
                      + consultor7_aparelho + consultor8_aparelho)

grafico_aparelho = pd.DataFrame ([{

'ANA' : consultor1_aparelho , 
'ANDERSON': consultor2_aparelho  ,
'AMANDA': consultor3_aparelho  ,
'DAVID GUSTAVO' : consultor4_aparelho  ,
"DEBORA" : consultor5_aparelho  ,
"LENILDA" : consultor6_aparelho  ,
"LORENA": consultor7_aparelho  ,
"WILLER" : consultor8_aparelho  ,
"TOTAL" : aparelho_acumulado

}])

grafico_aparelho_melt = grafico_aparelho.melt(value_name = "valor" , var_name = "consultor")

#acessórios

acessorio_acumulado = (consultor1_acessorio + consultor2_acessorio + consultor3_acessorio 
                      + consultor4_acessorio + consultor5_acessorio + consultor6_acessorio 
                      + consultor7_acessorio + consultor8_acessorio)

grafico_aparelho = pd.DataFrame ([{

'ANA' : consultor1_acessorio , 
'ANDERSON': consultor2_acessorio  ,
'AMANDA': consultor3_acessorio  ,
'DAVID GUSTAVO' : consultor4_acessorio  ,
"DEBORA" : consultor5_acessorio  ,
"LENILDA" : consultor6_acessorio  ,
"LORENA": consultor7_acessorio ,
"WILLER" : consultor8_acessorio  ,
"TOTAL" : acessorio_acumulado

}])

grafico_aparelho_melt = grafico_aparelho.melt(value_name = "valor" , var_name = "consultor")

