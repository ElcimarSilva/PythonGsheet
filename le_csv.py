import pandas as pd
from IPython.core.display_functions import display

# aprendizado o separador ; ou , importa muito e precisa ser especificado
planilha = pd.read_csv('/home/elcimar/Downloads/Percentual de eficiência ROBÔ MIGRAÇÃO (7 dias).csv', sep=";", encoding="ISO-8859-1")

eficiencia_robo = (planilha["EFICIENCIA_ROBO"])


def retorna_csv_coluna():
    lista_eficiencia_robo = list(eficiencia_robo)
    eficiencia_listas =[]
    for item in lista_eficiencia_robo:
        eficiencia_listas.append([item])
    return eficiencia_listas


def retorna_csv_linha():
    lista_eficiencia_robo = list(eficiencia_robo)
    # precisa cada item ser uma string dentro da lista
    return lista_eficiencia_robo


print(retorna_csv_linha())