import pandas as pd

df_est = pd.read_csv('estoque_atual.csv')
df_prod = pd.read_csv('produtos.csv')
df_vend_m = pd.read_csv('vendas_mensal.csv')

df_est_agrupado = df_est.groupby('produto_id', as_index=False)['quantidade'].sum()
df_vend_agrupado = df_vend_m.groupby('produto_id', as_index=False)['quantidade_vendida'].sum()

df_consolidado = df_prod.merge(df_est_agrupado, on='produto_id').merge(df_vend_agrupado, on='produto_id')

df_consolidado['custo_total_estoque'] = df_consolidado['quantidade'] * df_consolidado['preco_custo']
df_consolidado['valor_venda_mes'] = df_consolidado['quantidade_vendida'] * df_consolidado['preco_custo'] * 1.5
df_consolidado['custo_produtos_vendidos'] = df_consolidado['quantidade_vendida'] * df_consolidado['preco_custo']
df_consolidado['margem_bruta_estimada'] = df_consolidado['valor_venda_mes'] - df_consolidado['custo_produtos_vendidos']

estoque_negativo = df_consolidado[df_consolidado['quantidade'] <= 0]
estoque_insuficiente = df_consolidado[df_consolidado['quantidade_vendida'] > df_consolidado['quantidade']]

print(f"Produtos com estoque zerado/negativo: {len(estoque_negativo)}")
print(f"Produtos com estoque insuficiente para as vendas: {len(estoque_insuficiente)}")

resumo_categoria = df_consolidado.groupby('categoria').agg(
    total_em_estoque=('quantidade', 'sum'),
    total_vendido=('quantidade_vendida', 'sum'),
    margem_bruta_total=('margem_bruta_estimada', 'sum')
)
print("\nResumo por Categoria:")
print(resumo_categoria)