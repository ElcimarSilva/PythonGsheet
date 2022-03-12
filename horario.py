import time
from datetime import datetime
import pytz

minuto = 0

while minuto < 1:
    data_hora_atual = datetime.now(pytz.timezone('America/Sao_Paulo'))
    minuto = data_hora_atual.minute
    print(data_hora_atual)
    time.sleep(2)
