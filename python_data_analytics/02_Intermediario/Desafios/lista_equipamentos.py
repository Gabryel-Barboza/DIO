# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

for c in range(3):
  item = input()
  itens.append(item)



# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")