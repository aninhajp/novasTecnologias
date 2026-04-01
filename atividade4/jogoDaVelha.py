class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.turno = "X"

    def mostrar_tabuleiro(self):
        for linha in self.tabuleiro:
            print("|".join(linha))
            print("-" * 5)

    def fazer_jogada(self, l, c):
        if 0 <= l < 3 and 0 <= c < 3 and self.tabuleiro[l][c] == " ":
            self.tabuleiro[l][c] = self.turno
            self.turno = "O" if self.turno == "X" else "X"
            return True
        print("Jogada inválida!")
        return False

    def verificar_vencedor(self):
        t = self.tabuleiro
        for i in range(3):
            if t[i][0] == t[i][1] == t[i][2] != " ": return t[i][0]
            if t[0][i] == t[1][i] == t[2][i] != " ": return t[0][i]
        if t[0][0] == t[1][1] == t[2][2] != " ": return t[0][0]
        if t[0][2] == t[1][1] == t[2][0] != " ": return t[0][2]
        return None

    def jogar(self):
        while True:
            self.mostrar_tabuleiro()
            print(f"Turno do jogador: {self.turno}")
            lin = int(input("Linha (0-2): "))
            col = int(input("Coluna (0-2): "))
            
            if self.fazer_jogada(lin, col):
                vencedor = self.verificar_vencedor()
                if vencedor:
                    self.mostrar_tabuleiro()
                    print(f"O jogador {vencedor} venceu!")
                    break
                
if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()