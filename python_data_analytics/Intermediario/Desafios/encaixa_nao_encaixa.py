
N = int(input())

''' 
TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
"encaixa" ou "não encaixa" seus últimos digitos, para cada uma das relações N vezes.
'''
while N > 0:
  # É recebida em um mesmo input, separado em dois pelo espaço e comparado se os últimos dígitos são iguais
  entrada = str(input())
  valores = entrada.split(" ")
  if valores[0].endswith(valores[1]):
    print("encaixa")
  else:
    print("nao encaixa")
  N -= 1