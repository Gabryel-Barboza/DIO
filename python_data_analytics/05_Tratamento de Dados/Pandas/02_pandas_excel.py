import pandas as pd

# Parâmetros adicionais, sheet_name=1 para ler a 2º aba da planilha, skiprows=n para indicar quantas linhas pular na leitura. Outros que podem ser vistos com o IntelliSense
df = pd.read_excel("datasets/Excel/01. BD CURSOS-1.xlsx")

# df.concat([]) - recebe um iterável de dataframes para concatenar em um só dataframe, um abaixo do outro.
print(df.head())
# Retorna uma amostra de linhas aleatória do Dataframe
print(df.sample(5))

print(df.dtypes)
# Alterando os tipos de colunas no dataframe
df["IMPORTE COMERCIAL"] = df["IMPORTE COMERCIAL"].astype("object")

# Retorna a soma de valores nulos por coluna no dataframe
print(df.isnull().sum())
# Substituindo valores nulos na coluna com fillna, substitui campos nulos pela média da coluna, inplace=True para atribuir ao dataframe a modificação
df["IMPORTE PROFESSOR"].fillna(df["IMPORTE PROFESSOR"].mean(), inplace=True)
# inplace deixará de funcionar na versão 3.0 do pandas, utilize a atribuição normal ao dataframe ou veja a documentação para outras formas

# Apagar linhas de campos nulos
df.dropna(inplace=True)
# Apagar linhas com campos nulos na coluna COMERCIAL
df.dropna(subset=["COMERCIAL"], inplace=True)
# Apagando linhas com todas as colunas nulas
df.dropna(how="all", inplace=True)

print("#"*50)
# Criando novas colunas
print(df.head(10))
df["TESTE"] = "TESTE"
df["LUCROS"] = df["IMPORTE CLIENTE"] - (df["IMPORTE COMERCIAL"] + df["IMPORTE PROFESSOR"])
df["LUCROS"] = df["LUCROS"].astype("float64")

print("#"*50)
# Retornando máximo e minimo da coluna
print(df["LUCROS"])
print(df["LUCROS"].max())
print(df["LUCROS"].min())

print("#"*50)
# Retorna as linhas especificadas baseados no máximo/mínimo de uma coluna
print(df.nlargest(3, "LUCROS"))
print(df.nsmallest(3, "LUCROS"))

# Retorna um agrupamento por professor e total de lucros
print(df.groupby("PROFESSOR")["LUCROS"].sum())

# Ordena o dataframe com base na coluna, ascending=False para ordem decrescente
print(df.sort_values("DURAÇÃO", ascending=False).head())
