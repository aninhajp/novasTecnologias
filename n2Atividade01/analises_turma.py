import numpy as np

notas = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [5.0, 4.5, 6.0, 5.5],
    [9.0, 9.5, 8.5, 10.0],
    [3.0, 4.0, 5.0, 4.5],
    [8.0, 7.5, 9.0, 8.5]
])

medias = np.mean(notas, axis=1)

indice_melhor_aluno = np.argmax(medias)

print("Médias de cada aluno:", medias)
print(f"O aluno com a maior média foi o de índice {indice_melhor_aluno} (Média: {medias[indice_melhor_aluno]})")

medias_colunas = np.mean(notas, axis=0)
desvios_colunas = np.std(notas, axis=0)

notas_normalizadas = (notas - medias_colunas) / desvios_colunas
print("\nNotas Normalizadas:\n", notas_normalizadas)

mascara_aprovados = medias >= 6.0
notas_aprovados = notas[mascara_aprovados]
print("\nNotas originais apenas dos aprovados:\n", notas_aprovados)
