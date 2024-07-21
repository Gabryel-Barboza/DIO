from datetime import datetime

data = datetime.now()
data_hora_string = "30/04/2024 09:30"

mascara_ptbr = "%d/%m/%Y %H:%M"
mascara_ptbr_dia = "%d/%m/%Y %H:%M %a"
mascara_en = "%Y/%m/%d %H:%M"

# Formatando data e hora. String Format Time
print(data.strftime(mascara_ptbr))
print(data.strftime(mascara_ptbr_dia))
print(data.strftime(mascara_en))

# Convertendo string para datetime. String Parse Time
data_convertida = datetime.strptime(data_hora_string, mascara_ptbr)
print(data_convertida)
print(data_convertida.strftime("%Y"))