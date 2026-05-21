import numpy as np

imagem = np.array([
    [200, 180, 160, 140, 120, 100],
    [ 90,  80,  70,  60,  50,  40],
    [255, 240, 210, 190, 170, 150],
    [ 30,  20,  10,   5,   2,   0]
], dtype=np.uint8)

brilho_geral = np.mean(imagem)
brilho_linhas = np.mean(imagem, axis=1)
brilho_colunas = np.mean(imagem, axis=0)

linha_mais_escura = np.argmin(brilho_linhas)

print(f"Brilho médio geral: {brilho_geral}")
print(f"Brilho médio por linha: {brilho_linhas}")
print(f"Brilho médio por coluna: {brilho_colunas}")
print(f"A linha mais escura é a de índice {linha_mais_escura} (Média: {brilho_linhas[linha_mais_escura]})")

imagem_binaria = imagem.copy()

imagem_binaria[imagem >= 128] = 255
imagem_binaria[imagem < 128] = 0

print("\nImagem original:\n", imagem)
print("\nImagem Binarizada (Limiarização):\n", imagem_binaria)
