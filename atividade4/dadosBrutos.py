transacoes = [
    (1, "Infraestrutura", 1500.50),
    (2, "Licenças", 450.00),
    (3, "Infraestrutura", 3200.00),
    (4, "Marketing", 800.00),
    (5, "Licenças", 150.00)
]

categorias = set()
for t in transacoes:
    categorias.add(t[1])
print(f"Categorias únicas: {categorias}")

gastos_por_categoria = {}

for id_trans, categoria, valor in transacoes:
    if categoria in gastos_por_categoria:
        gastos_por_categoria[categoria] += valor
    else:
        gastos_por_categoria[categoria] = valor

print(f"Total por categoria: {gastos_por_categoria}")
