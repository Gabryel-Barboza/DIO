import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_excel("datasets/Excel/01. BD CURSOS-1.xlsx")

df["LUCROS"] = df["IMPORTE CLIENTE"] - (df["IMPORTE PROFESSOR"] - df["IMPORTE COMERCIAL"])
print(df.columns)

# Utiliza o módulo matplotlib para criação dos gráficos integrado ao pandas
# Instale o módulo primeiro
grafico_barras = df["CURSO"].value_counts().plot.bar()

# Utilize o módulo pyplot para visualizar o gráfico
plt.show()

# Gráfico de barras horizontal
df["CURSO"].value_counts(ascending=True).plot.barh()
plt.show()

# Gráfico de pizza
df.groupby(df["DATA CURSO"].dt.year)["LUCROS"].sum().plot.pie()
plt.show()

# Personalizando gráficos
df['CURSO'].value_counts().plot.bar(title="Total de Cursos Vendidos", color="purple")
plt.xlabel("Cursos")
plt.ylabel("Vendas")
plt.show()

# Alterando estilo do gráfico, veja a documentação do matplotlib
plt.style.use("ggplot")
df.groupby(df["CURSO"])["LUCROS"].sum().plot(marker="o")
plt.legend()
plt.show()

# Histograma
plt.hist(df["LUCROS"], color="yellow")
plt.show()

# Dispersão
plt.scatter(x=df["CURSO"], y=df["LUCROS"])
plt.show()

# Salvando o gráfico
df.groupby(df["CURSO"])["LUCROS"].sum().plot(marker="o")
plt.legend()
plt.savefig("./Pandas/grafico_linhas cursos x lucros.png")
plt.show()

# Salvando o dataframe, index=False para retirar a coluna de índice
df.to_excel("./Pandas/dataframe_curso.xlsx", index=False)
