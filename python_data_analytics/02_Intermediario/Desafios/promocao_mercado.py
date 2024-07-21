# Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia você comprar refrigerantes e levar os cascos vazios no dia seguinte, ela troca cada conjunto de K garrafas vazias  por uma garrafa cheia. Um cliente quer aproveitar ao máximo essa oferta e por isso comprou várias garrafas no primeiro dia da promoção. Agora ele quer saber quantas garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.

T = int(input())

for i in range(T):
    ''' 
    TODO Ler as variáveis de entrada N e K. Talvez seja necessário fazer um "split" na linha 
         para obtenção dos valores.
    TODO Calcular e imprimir o número de garrafas que o cliente terá no segundo dia, se aproveitar ao máximo a oferta.
    '''
    # Recebe a quantidade de garrafas, separa em uma lista e converte para inteiro
    # cria-se a formula com base nos resultados de exemplo: Se o 1º valor maior que o 2º, formula = 1º valor dividido pelo 2º + T
    # caso contrário, formula = 2º valor dividido por 1º valor + T
    
    garrafas = str(input())
    valores = garrafas.split(" ")
    valores = [int(valores[0]), int(valores[1])]
    if valores[0] > valores[1]:
        garrafas_cheias = valores[0] // valores[1] + T 
    else:
        garrafas_cheias = valores[1] // valores[0] + T
    print(garrafas_cheias)
    