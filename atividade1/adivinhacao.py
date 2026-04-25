def jogarAdivinhacao():
    NUMERO_SECRETO = 42
    MAX_TENTATIVAS = 5
    tentativa_atual = 1
    venceu = False

    while tentativa_atual <= MAX_TENTATIVAS:
        chute = int(input(f"Tentativa {tentativa_atual}/{MAX_TENTATIVAS}: "))
        
        if chute == NUMERO_SECRETO:
            print("Correto!")
            venceu = True
            break
        elif chute < NUMERO_SECRETO:
            print("Muito baixo! Tente maior.\n")
        else:
            print("Muito alto! Tente menor.\n")
            
        tentativa_atual += 1
    
    if venceu:
        print("Você ganhou!")
    else:
        print(f"Você perdeu! O número era {NUMERO_SECRETO}")

jogarAdivinhacao()
