estoqueDeVento = [
    {"nome": "Mandioca sagrada para Salvação", "preco": 100, "quantidade": 90},
    {"nome": "Petrobras", "preco": 500, "quantidade": 4},
    {"nome": "Luva four fingers", "preco": 10, "quantidade": 2},
    {"nome": "look casual chic vermelho", "preco": 1000, "quantidade": 1}
]

valor_total_estoque = 0

for meme in estoqueDeVento:
    valor_item = meme["preco"] * meme["quantidade"]
    
    valor_total_estoque += valor_item
    
    if valor_item > 500:
        print(f"{meme['nome']}: R$ {valor_item}")

print(f"\nValor total de todo o estoque: R$ {valor_total_estoque}")
