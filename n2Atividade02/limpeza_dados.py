import pandas as pd

df_rh = pd.read_csv('funcionarios.csv')

print("Valores Nulos por Coluna:")
print(df_rh.isnull().sum())

df_rh = df_rh.dropna(subset=['salario'])
df_rh['idade'] = df_rh['idade'].fillna(df_rh.groupby('departamento')['idade'].transform('mean'))

df_rh['data_admissao'] = pd.to_datetime(df_rh['data_admissao'])
hoje = pd.to_datetime('2026-05-20')
df_rh['anos_empresa'] = (hoje - df_rh['data_admissao']).dt.days / 365.25

df_rh['media_salario_dep'] = df_rh.groupby('departamento')['salario'].transform('mean')
funcionarios_criticos = df_rh[(df_rh['anos_empresa'] > 5) & (df_rh['salario'] < df_rh['media_salario_dep'])]

print("\nFuncionários com mais de 5 anos de empresa e salário abaixo da média do departamento:")
print(funcionarios_criticos[['nome', 'departamento', 'salario', 'anos_empresa']])