month = input()

months_dict = {
    "1": "january",
    "2": "february",
    "3": "march",
    "4": "april",
    "5": "may",
    "6": "june",
    "7": "july",
    "8": "august",
    "9": "september",
    "10": "october",
    "11": "november",
    "12": "december"
}

''' 
TODO Faça uma relação entre as possíveis entradas e os meses (em inglês).
TODO Imprima o valor de cada chave em relação as entradas do programa com primeira letra maiúscula.
'''
print(months_dict[month].capitalize())
