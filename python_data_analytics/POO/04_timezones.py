from datetime import datetime, timezone, timedelta
# Os fuso-horários utilizam o relógio mundial como base
# Se um fuso-horário é GMT-3, isso significa que é o UTC - 3 horas


# fuso-horário de GMT+2
data_oslo = datetime.now(timezone(timedelta(hours=2)))
# fuso-horário de GMT-3, nome apenas para retorno quando necessário
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3), "BRT"))

print(data_oslo)
print(data_sao_paulo)
print(datetime.now())