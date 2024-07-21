from datetime import date, datetime, time

# Veja a documentação em python.org

# data em formato AAAA/MM/DD
d = date(2023, 7, 10)
print(d)
# data de hoje
print(date.today())

# data e hora, minuto e segundo
data_hora = datetime(2023, 7, 10, 8, 39, 30)
print(data_hora)
print(datetime(2023, 7, 10))
print(datetime.today())
# horas
hora = time(8, 50, 0)
print(hora)
