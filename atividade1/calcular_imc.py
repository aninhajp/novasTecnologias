def calcularIMC(peso, altura):
    valor_imc = peso / (altura ** 2)
    imc = round(valor_imc, 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Peso normal"
    elif imc <= 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
        
    return imc, classificacao

def imprimirResultado():
    nome = input("Qual o seu nome? ")
    p = float(input("Peso (kg): "))
    a = float(input("Altura (m): "))
    
    valor, status = calcularIMC(p, a)
    
    print(f"\nOlá, {nome}!")
    print(f"Seu IMC é: {valor}")
    print(f"Classificação: {status}")

imprimirResultado()