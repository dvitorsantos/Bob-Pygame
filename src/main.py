import pygame
import random
pygame.init()

#Importando a configuração básica
from config.settings import larguraTela, alturaTela, velocidadeJogo

#Importando as classes dos objetos do cenário
from classes.bolha import Bolha
from classes.bobEsponja import BobEsponja
from classes.predio import Predio
from classes.robo import Robo

#Importando os assets dos objetos do cenário
from config.assets import robo, planoDeFundo, planoDeFundoMenu, obstaculosImg

tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('Bob Esponja')

def main():
    global velocidadeJogo, fundoPosicaoX, fundoPosicaoY, pontos, obstaculos
    rodando = True
    clock = pygame.time.Clock()

    bolha = Bolha()
    dinossauro = BobEsponja()
    
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
        fundo = pygame.transform.scale(planoDeFundo,(larguraTela ,alturaTela))
        tela.blit(fundo,(0,0))

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill((255, 255, 255))
        fundo()
        tecla = pygame.key.get_pressed()

        dinossauro.draw(tela)
        dinossauro.update(tecla)

        if len(obstaculos) == 0:
            if random.randint(0, 2) == 0:
                obstaculos.append(Predio(obstaculosImg))
            elif random.randint(0, 2) == 2:
                obstaculos.append(Robo(robo))

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
        bolha.draw(tela)
        bolha.update()
        pontuacao()

        clock.tick(30)
        pygame.display.update()

def menu(contadorMortes):
    global pontos
    fundo = pygame.transform.scale(planoDeFundoMenu,(larguraTela ,alturaTela))
    
    jogoRodando = True
    while jogoRodando:
        tela.fill((255, 255, 255))
        fonte = pygame.font.Font('freesansbold.ttf', 30)
        tela.blit(fundo,(0,0))
        if contadorMortes == 0:
            textoInformativo = fonte.render("Pressione uma tecla para jogar!", True, (255, 255, 255))
        elif contadorMortes > 0:
            textoInformativo = fonte.render("Pressione uma tecla para jogar novamente D:", True, (255, 255, 255))
            pontuacao = fonte.render("Sua pontuação: " + str(pontos), True, (255, 255, 255))
            pontuacaoRect = pontuacao.get_rect()
            pontuacaoRect.center = (larguraTela // 2, alturaTela // 2 + 50)
            tela.blit(pontuacao, pontuacaoRect)
        
        textoInformativoRect = textoInformativo.get_rect()
        textoInformativoRect.center = (larguraTela // 2, alturaTela // 2)

        tela.blit(textoInformativo, textoInformativoRect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogoRodando = False
            if event.type == pygame.KEYDOWN:
                main()

menu(contadorMortes=0)