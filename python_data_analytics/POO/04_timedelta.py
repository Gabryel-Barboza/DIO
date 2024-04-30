from datetime import datetime, timedelta, date, time
# Exemplo de um sistema de lava-jato que informa quando o carro estará pronto

tipo_carro = "G" # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_hoje = datetime.now() 

# Se carro pequeno, tempo é 30 minutos
if tipo_carro == "P":
    # Operações devem ser realizadas com um timedelta
    data_estimada = data_hoje + timedelta(minutes=tempo_pequeno)
    # weeks, days, hours, minutes...
    print(f"O carro chegou: {data_hoje}.\nFicará pronto:{data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_hoje + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_hoje}.\nFicará pronto:{data_estimada}")
else:
    data_estimada = data_hoje + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_hoje}.\nFicará pronto:{data_estimada}")


print(date.today() - timedelta(days=1))
# Para decrementar horas, é realizada a ação apenas com objetos datetime
'''print(time(9, 10, 35) - timedelta(hours=1))'''
# Criando um datetime com data e hora e decrementando em 1 hora
resultado = datetime(2023, 7, 25, 9, 14, 30) - timedelta(hours=1)
# Pegando apenas a parte de horas do resultado
print(resultado.time())
print(datetime.now().date())