def limpar_dados(usuarios):
    ativos = list(filter(lambda u: u["status_ativo"] == True, usuarios))
    
    for u in ativos:
        u["nome"] = u["nome"].upper()
        u["email"] = u["email"].lower()
        
    return ativos

dados_brutos = [
    {"nome": "Ana Julia matadora de lobisomem", "email": "ANACotatePerseguicao@gmail.com", "status_ativo": True},
    {"nome": "Ana Raquel Ratos e Fofos", "email": "rainhaDosRatos@gmail.com", "status_ativo": True},
    {"nome": "Fellype jumento", "email": "sehhorCapacho@gmail.com", "status_ativo": False}
]

print(limpar_dados(dados_brutos))