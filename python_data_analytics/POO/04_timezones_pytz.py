from datetime import datetime
import pytz

# O mesmo exemplo, porém com uma biblioteca de terceiros
# Instalar pytz em um terminal shell com pip install pytz
data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data.time())
print(data2.time())