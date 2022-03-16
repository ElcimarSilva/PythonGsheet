import pandas as pd
from IPython.core.display_functions import display

# aprendizado o separador ; ou , importa muito e precisa ser especificado
planilha = pd.read_csv('/home/elcimar/Downloads/Percentual de eficiência ROBÔ MIGRAÇÃO (7 dias).csv', sep=";", encoding="ISO-8859-1")

eficiencia_robo = (planilha["EFICIENCIA_ROBO"])
display(eficiencia_robo)

for linha in eficiencia_robo:
    pass # criar estrutura que mostre uma uma a linha da coluna eficiencia