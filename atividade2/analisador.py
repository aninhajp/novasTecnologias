frase = input("Digite uma frase: ").lower()
palavras = frase.split()

contagem = {}

for p in palavras:
    if p in contagem:
        contagem[p] += 1
    else:
        contagem[p] = 1

total_palavras = len(palavras)
palavras_unicas = len(contagem)

mais_frequente = max(contagem, key=contagem.get)

print(f"Total de palavras: {total_palavras}")
print(f"Palavras únicas: {palavras_unicas}")
print(f"Palavra mais frequente: '{mais_frequente}' ({contagem[mais_frequente]} vezes)")

print("Palavras que se repetem:")
for p in contagem:
    if contagem[p] > 1:
        print(f"{p}")