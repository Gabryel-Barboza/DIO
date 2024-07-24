import pandas as pd

# Dataframes são similares a planilhas excel, com um conjunto de linhas e colunas

# Leitura de arquivo csv, parametro error_bad_lines=False para pular linhas com erro, parâmetro sep="" para indicar um separador diferente de , (padrão)
df = pd.read_csv("./datasets/products dataset/orders.csv")

# Retorna as 5 primeiras linhas do dataframe, recebe por parâmetro o limite de retorno
print("="*50)
print(df.head())

# Renomeando colunas 
print("="*50)
df = df.rename(columns={"order_id": "id_ordem", "order_date": "data_ordem", "product_id": "id_produto", "quantity": "quantidade", "total_price": "preco_total"})

print(df.head(10))
# Proporção do dataframe (linhas, colunas)
print(df.shape)
print(df.columns)
# Retorna o tipo das colunas
print(df.dtypes)

# Retornando as últimas linhas, recebe o limite por parametro
print("="*50)
print(df.tail())

# Descrever o dataframe, count=contagem, mean=média, std=desvio padrão, min=minimo
print("="*50)
print(df.describe())

# Retornando valores únicos
print("="*50)
print(df["id_ordem"].unique())

# Retornando um dataframe com valores especificados, utilize [[]] para retornar um dataframe
precos = df.loc[df["preco_total"] > 1000]
print(precos.head(10))

# Método groupby para agrupar por determinada coluna, pega os elementos de id_produto e retorna um número de elementos únicos
print("="*50)
print(df.groupby("id_ordem")["id_produto"].nunique())

# df[""].mean() para tirar a média
# df[""].sum() para tirar a soma
# df[""].mul(df[""]) para multiplicar
