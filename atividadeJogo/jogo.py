import pygame, sys, random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sobrevivência - Versão Completa")
CLOCK = pygame.time.Clock()
imagem_fundo = pygame.image.load("atividadeJogo/imagens/fundo.png").convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (800, 600))


fonte_grande = pygame.font.SysFont("Arial", 48, bold=True)
fonte_normal = pygame.font.SysFont("Arial", 28)

CONFIG_NIVEIS = {
    1: {"vel_base": 3, "spawn_rate": 300},
    2: {"vel_base": 4, "spawn_rate": 200},
    3: {"vel_base": 5, "spawn_rate": 100}
}

class EntidadeBase:
    def __init__(self, x, y, largura, altura, cor):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

    def colidiu_com(self, outra):
        return self.rect.colliderect(outra.rect)

class Jogador(EntidadeBase):
    def __init__(self, x, y):

        super().__init__(x, y, 50, 50, (0, 150, 255))
        self.velocidade = 5
        self.direcao = "CIMA"
        self.imagem = pygame.image.load("atividadeJogo/imagens/dilma.jpg").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        
    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.x > 0: 
            self.rect.x -= self.velocidade
            self.direcao = "ESQUERDA"
        if teclas[pygame.K_RIGHT] and self.rect.x < 750: 
            self.rect.x += self.velocidade
            self.direcao = "DIREITA"
        if teclas[pygame.K_UP] and self.rect.y > 0: 
            self.rect.y -= self.velocidade
            self.direcao = "CIMA"
        if teclas[pygame.K_DOWN] and self.rect.y < 550: 
            self.rect.y += self.velocidade
            self.direcao = "BAIXO"
            
    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)
 

class Projetil(EntidadeBase):
    def __init__(self, x, y):
        super().__init__(x, y, 8, 16, (255, 255, 100))
        self.vel = 10

    def mover(self):
        self.rect.y -= self.vel

class Inimigo(EntidadeBase):
    def __init__(self, x, y, velocidade=3, largura=40, altura=40, cor=(255, 100, 0)):

        super().__init__(x, y, largura, altura, cor)
        self.velocidade = velocidade
        self.vida = 3
        self.imagem = pygame.image.load("atividadeJogo/imagens/petrobras.jpg").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (40, 40)) 

    def perseguir(self, alvo):
        if self.rect.x < alvo.rect.x: self.rect.x += self.velocidade
        if self.rect.x > alvo.rect.x: self.rect.x -= self.velocidade
        if self.rect.y < alvo.rect.y: self.rect.y += self.velocidade
        if self.rect.y > alvo.rect.y: self.rect.y -= self.velocidade
        
    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

class InimigoRapido(Inimigo):
    def __init__(self, x, y, vel_base):
        super().__init__(x, y, velocidade=vel_base * 2, largura=30, altura=30, cor=(255, 0, 255))
        self.vida = 2 

class InimigoGigante(Inimigo):
    def __init__(self, x, y, vel_base):
        super().__init__(x, y, velocidade=vel_base // 2 + 1, largura=80, altura=80, cor=(150, 0, 0))
        self.vida = 5

def desenhar_hud(tela, estado):
    texto_pont = fonte_normal.render(f"Pontuação: {estado['pontuacao']}", True, (255, 255, 255))
    texto_nivel = fonte_normal.render(f"Nível: {estado['nivel']}", True, (255, 255, 255))
    texto_vidas = fonte_normal.render(f"Vidas: {estado['vidas']}", True, (255, 80, 80))
    
    tela.blit(texto_pont, (10, 10))
    tela.blit(texto_nivel, (10, 40))
    tela.blit(texto_vidas, (700, 10))

def desenhar_game_over(tela):
    overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    tela.blit(overlay, (0, 0))
    texto = fonte_grande.render("GAME OVER", True, (255, 60, 60))
    tela.blit(texto, texto.get_rect(center=(400, 300)))

def spawn_inimigo(vel_base):
    x, y = random.randint(0, 750), random.randint(-100, -40)
    tipo = random.choice([1, 1, 1, 2, 3])
    if tipo == 1: return Inimigo(x, y, vel_base)
    elif tipo == 2: return InimigoRapido(x, y, vel_base)
    else: return InimigoGigante(x, y, vel_base)

jogador = Jogador(375, 275)
inimigos = []
tiros = []
estado = {"pontuacao": 0, "vidas": 5, "rodando": True, "nivel": 1}
timer_spawn = 0
msg_level_up = 0 

for _ in range(4):
    inimigos.append(spawn_inimigo(CONFIG_NIVEIS[1]["vel_base"]))

while estado["rodando"]:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                centro_x = jogador.rect.centerx - 4
                centro_y = jogador.rect.top
                
                tiros.append(Projetil(centro_x, centro_y))

    teclas = pygame.key.get_pressed()
    jogador.mover(teclas)
    
    nivel_atual = estado["nivel"]
    prox_nivel = (estado["pontuacao"] // 500) + 1
    if prox_nivel > nivel_atual and prox_nivel in CONFIG_NIVEIS:
        estado["nivel"] = prox_nivel
        msg_level_up = 120

    configs_atuais = CONFIG_NIVEIS.get(estado["nivel"], CONFIG_NIVEIS[3])
    
    for t in tiros[:]:
        t.mover()
        if t.rect.x < 0 or t.rect.x > 800 or t.rect.y < 0 or t.rect.y > 600:
            tiros.remove(t)
            continue
            
        for ini in inimigos[:]:
            if t.colidiu_com(ini):
                ini.vida -= 1
                if t in tiros: tiros.remove(t) 
                if ini.vida <= 0:
                    inimigos.remove(ini)
                    estado["pontuacao"] += 50
                break

    for ini in inimigos[:]:
        ini.perseguir(jogador)
        if jogador.colidiu_com(ini):
            estado["vidas"] -= 1
            inimigos.remove(ini)
            if estado["vidas"] <= 0:
                estado["rodando"] = False

    timer_spawn += 1
    if timer_spawn >= configs_atuais["spawn_rate"]:
        inimigos.append(spawn_inimigo(configs_atuais["vel_base"]))
        timer_spawn = 0

    estado["pontuacao"] += 1

    TELA.blit(imagem_fundo, (0, 0))
    jogador.desenhar(TELA)
    
    for t in tiros:
        t.desenhar(TELA)

    for ini in inimigos:
        ini.desenhar(TELA)
        
    desenhar_hud(TELA, estado)
    
    if msg_level_up > 0:
        texto_lvl = fonte_grande.render(f"LEVEL UP: NÍVEL {estado['nivel']}!", True, (255, 255, 0))
        TELA.blit(texto_lvl, texto_lvl.get_rect(center=(400, 300)))
        msg_level_up -= 1

    pygame.display.flip()
    CLOCK.tick(60)

desenhar_game_over(TELA)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
sys.exit()
