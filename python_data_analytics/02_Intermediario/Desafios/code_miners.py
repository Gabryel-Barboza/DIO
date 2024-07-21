# Com as máquinas pesadas agrupadas estrategicamente, graças ao seu algoritmo de cálculo energético, agora a mineração está muito mais eficiente! Com isso, os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados em seus discos de Mithril. Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade! Escreva um programa que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

# Entrada: Dois valores inteiros positivos, representando a capacidade atual total em teraflops e o aumento percentual, separados por espaço

capacidade_atual, aumento_percentual = map(int, input().split())
nova_capacidade = capacidade_atual + (capacidade_atual * (aumento_percentual / 100))

print(f"{nova_capacidade:.0f}")