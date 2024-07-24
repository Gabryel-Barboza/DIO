import pandas as pd

df = pd.read_excel("datasets/Excel/01. BD CURSOS-1.xlsx")


# Convertendo alguma coluna para o tipo date, método do pandas
df["DATA CURSO"] = pd.to_datetime(df["DATA CURSO"])
print(df.dtypes)
print(df["DATA CURSO"].head(10))

# Agrupando por ano
print(df.groupby(df["DATA CURSO"].dt.year))
# Criando colunas separadas de ano, mês e dia
df["ANO"] = df["DATA CURSO"].dt.year
df["MÊS"] = df["DATA CURSO"].dt.month
df["DIA"] = df["DATA CURSO"].dt.day

print(df["ANO"].sort_values())
print("#"*50)
print(df["MÊS"].sort_values())
print("#"*50)
print(df["DIA"].sort_values())

# Funções max e min para datas
print(df["DATA CURSO"].min())

# Operações com datas
df['DIFERENÇA_DIAS'] = df["DATA CURSO"] - df["DATA CURSO"].min()
print(df["DIFERENÇA_DIAS"].head())

# Trimestres
df["TRIMESTRE"] = df["DATA CURSO"].dt.quarter
print(df["TRIMESTRE"].head())
print("#"*50)

# Retornando um novo dataframe com cursos do mês de março
cursos_marco = df.loc[df["DATA CURSO"].dt.month == 3]
print(cursos_marco)

# Contando o total de valores
print(cursos_marco["CURSO"].value_counts(ascending=False))
