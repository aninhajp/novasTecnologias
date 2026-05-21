import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df_titanic = pd.read_csv(url)

print(" 5 Primeiras Linhas do Dataset ")
print(df_titanic.head())
print("\n" + "="*50 + "\n")

print(" Diagnóstico Inicial (info) ")
df_titanic.info()
print("\n" + "="*50 + "\n")

print(f"Dimensão do Dataset (Linhas, Colunas): {df_titanic.shape}")
print("\n" + "="*50 + "\n")


print(" Estatísticas Descritivas ")
print(df_titanic.describe())
print("\n" + "="*50 + "\n")

classes_unicas = df_titanic['Pclass'].nunique()
print(f"Quantidade de classes de embarque diferentes: {classes_unicas}")
print("\n" + "="*50 + "\n")

print(" Frequência de Passageiros por Sexo ")
print(df_titanic['Sex'].value_counts())
print("\n" + "="*50 + "\n")

