from datetime import datetime
import pytz
import pandas as pd

# aprendizado o separador ; ou , importa muito e precisa ser especificado
planilha = pd.read_csv('/home/elcimar/Área de Trabalho/Percentual de eficiência ROBÔ MIGRAÇÃO (7 dias).csv', sep=";",
                       encoding="ISO-8859-1")

eficiencia_robo = (planilha["EFICIENCIA_ROBO"])


def retorna_coluna_csv():
    lista_eficiencia_robo = list(eficiencia_robo)
    eficiencia_listas = []
    for item in lista_eficiencia_robo:
        eficiencia_listas.append([item])
    return eficiencia_listas


def retorna_linha_csv():
    lista_eficiencia_robo = []
    data = str(datetime.now(pytz.timezone('America/Sao_Paulo')))
    lista_eficiencia_robo.append(data)
    for item in eficiencia_robo:
        lista_eficiencia_robo.append(str(item))

    return [lista_eficiencia_robo]


print(retorna_linha_csv())
