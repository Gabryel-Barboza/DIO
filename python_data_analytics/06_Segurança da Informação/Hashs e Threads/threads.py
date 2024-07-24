from threading import Thread
from time import sleep, time


# Criando uma corrida de carros
def carro(piloto, velocidade: float):
    """Inicia a corrida com o piloto recebido, percorrendo a distância definida com base na velocidade do carro. Imprime o tempo total que o piloto precisou para percorrer o trajeto.

    :param piloto: Recebe um nome para o piloto do carro.
    :param velocidade: Recebe a velocidade do carro.
    """
    global distancia
    trajeto = 0
    tempo_inicial = time()
    while trajeto < distancia:
        trajeto += velocidade
        sleep(0.5)
        print(f"Carro de {piloto}:", f"{trajeto} KM")

    tempo_final = int(time() - tempo_inicial)
    print(f"\033[31m{piloto}\033[m terminou a corrida em {tempo_final}s!")


distancia = 200
# Cria threads para processar duas funções simultâneamente
thread_carro_a = Thread(target=carro, args=["Gabryel", 50])
thread_carro_b = Thread(target=carro, args=["Brayan", 20])

# Começa a execução das threads
thread_carro_a.start()
thread_carro_b.start()
