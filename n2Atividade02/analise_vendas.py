import pandas as pd

df_vendas = pd.read_csv('vendas.csv')
print(df_vendas.head(10))
df_vendas.info()

df_vendas['total_venda'] = df_vendas['quantidade'] * df_vendas['preco_unitario']

filtro_eletronicos = df_vendas[(df_vendas['categoria'] == 'Eletrônicos') & (df_vendas['total_venda'] > 1000)]
print("\nEletrônicos com venda > 1000:")
print(filtro_eletronicos[['produto', 'total_venda']])

media_cidade = df_vendas.groupby('cidade')['total_venda'].mean().sort_values(ascending=False)
print("\nMédia de Vendas por Cidade:")
print(media_cidade)