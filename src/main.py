import pygame
import random
pygame.init()

#Importando a configuração básica
from config.settings import larguraTela, alturaTela, velocidadeJogo

#Importando as classes dos objetos do cenário
from classes.nuvem import Nuvem
from classes.dinossauro import Dinossauro, correr
from classes.cactusPequeno import CactusPequeno
from classes.cactusGrande import CactusGrande
from classes.passaro import Passaro

#Importando os assets dos objetos do cenário
from config.assets import passaro, cactusGrande, cactusPequeno, planoDeFundo

tela = pygame.display.set_mode((larguraTela, alturaTela))

def main():
    global velocidadeJogo, fundoPosicaoX, fundoPosicaoY, pontos, obstaculos
    rodando = True
    clock = pygame.time.Clock()

    nuvem = Nuvem()
    dinossauro = Dinossauro()
    
    #Definindo as variaveis globais do jogo
    velocidadeJogo = velocidadeJogo
    fundoPosicaoX = 0
    fundoPosicaoY = 380
    pontos = 0
    obstaculos = []
    contadorMortes = 0

    fonte = pygame.font.Font('freesansbold.ttf', 20)

    def pontuacao():
        global pontos, velocidadeJogo
        pontos += 1
        if pontos % 100 == 0:
            velocidadeJogo += 1

        textoInformativo = fonte.render("Pontos: " + str(pontos), True, (0, 0, 0))
        textoInformativoRect = textoInformativo.get_rect()
        textoInformativoRect.center = (1000, 40)

        tela.blit(textoInformativo, textoInformativoRect)

    def fundo():
        global fundoPosicaoX, fundoPosicaoY
        larguraImagem = planoDeFundo.get_width()

        tela.blit(planoDeFundo, (fundoPosicaoX, fundoPosicaoY))
        tela.blit(planoDeFundo, (larguraImagem + fundoPosicaoX, fundoPosicaoY))

        if fundoPosicaoX <= -larguraImagem:
            tela.blit(planoDeFundo, (larguraImagem + fundoPosicaoX, fundoPosicaoY))
            fundoPosicaoX = 0

        fundoPosicaoX -= velocidadeJogo

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill((255, 255, 255))
        tecla = pygame.key.get_pressed()

        dinossauro.draw(tela)
        dinossauro.update(tecla)

        if len(obstaculos) == 0:
            if random.randint(0, 2) == 0:
                obstaculos.append(CactusPequeno(cactusPequeno))
            elif random.randint(0, 2) == 1:
                obstaculos.append(CactusGrande(cactusGrande))
            elif random.randint(0, 2) == 2:
                obstaculos.append(Passaro(passaro))

        #Lógica para incluir os obstaculos na tela e detectar colisão
        for obstaculo in obstaculos:
            obstaculo.draw(tela)
            obstaculo.update()
            if obstaculo.rect.x < -obstaculo.rect.width:
                obstaculos.pop()
            if dinossauro.rect.colliderect(obstaculo.rect):
                pygame.time.delay(2000)
                contadorMortes += 1
                menu(contadorMortes)

        #Carregando cenário e interface de usuário
        fundo()
        nuvem.draw(tela)
        nuvem.update()
        pontuacao()

        clock.tick(30)
        pygame.display.update()

def menu(contadorMortes):
    global pontos
    jogoRodando = True
    while jogoRodando:
        tela.fill((255, 255, 255))
        fonte = pygame.font.Font('freesansbold.ttf', 30)

        if contadorMortes == 0:
            textoInformativo = fonte.render("Pressione uma tecla para jogar!", True, (0, 0, 0))
        elif contadorMortes > 0:
            textoInformativo = fonte.render("Pressione uma tecla para jogar novamente D:", True, (0, 0, 0))
            pontuacao = fonte.render("Sua pontuação: " + str(pontos), True, (0, 0, 0))
            pontuacaoRect = pontuacao.get_rect()
            pontuacaoRect.center = (larguraTela // 2, alturaTela // 2 + 50)
            tela.blit(pontuacao, pontuacaoRect)
        
        textoInformativoRect = textoInformativo.get_rect()
        textoInformativoRect.center = (larguraTela // 2, alturaTela // 2)

        tela.blit(textoInformativo, textoInformativoRect)
        tela.blit(correr[0], (larguraTela // 2 - 20, alturaTela // 2 - 140))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogoRodando = False
            if event.type == pygame.KEYDOWN:
                main()

menu(contadorMortes=0)