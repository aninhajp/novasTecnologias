def validar_senha():
    while True:
        senha = input("Digite uma senha: ")
        
        tamanho_ok = len(senha) >= 8
        tem_numero = any(char.isdigit() for char in senha)
        tem_maiuscula = any(char.isupper() for char in senha)
        
        if tamanho_ok and tem_numero and tem_maiuscula:
            print("\nsenha válida aceita!")
            return senha
        else:
            print("senha inválida! A senha deve ter 8+ caracteres, 1 número e 1 letra maiúscula.\n")

def gerar_relatorio(senha):
    tamanho = len(senha)
    letras = 0
    numeros = 0
    especiais = 0
    
    for char in senha:
        if char.isalpha():
            letras += 1
        elif char.isdigit():
            numeros += 1
        else:
            especiais += 1
            
    if 8 <= tamanho <= 9:
        nivel = "Fraca"
    elif 10 <= tamanho <= 12:
        nivel = "Média"
    else:
        nivel = "Forte"
        
    print(f"--- RELATÓRIO DE SEGURANÇA ---")
    print(f"Tamanho da senha: {tamanho}")
    print(f"Letras: {letras}")
    print(f"Números: {numeros}")
    print(f"Caracteres Especiais: {especiais}")
    print(f"Nível: {nivel}")

def iniciar_programa():
    senha_final = validar_senha()
    gerar_relatorio(senha_final)

iniciar_programa()