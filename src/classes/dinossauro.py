import pygame

from config.assets import agachar, correr, pular

class Dinossauro:
    posicaoX = 80
    posicaoY = 310
    posicaoY_agachado = 340
    velocidadePuloPadrao = 8.5

    def __init__(self):
        self.agacharImg = agachar
        self.correrImg = correr
        self.pularImg = pular

        #Variaveis de status
        self.isAgachado = False
        self.isCorrendo = True
        self.isPulando = False

        self.indexAnimacao = 0
        self.velocidadePulo = self.velocidadePuloPadrao
        self.imagem = self.correrImg[0]
        self.rect = self.imagem.get_rect()
        self.rect.x = self.posicaoX
        self.rect.y = self.posicaoY

    def pular(self):
        self.imagem = self.pularImg
        if self.isPulando:
            self.rect.y -= self.velocidadePulo * 4
            self.velocidadePulo -= 0.8
        if self.velocidadePulo < - self.velocidadePuloPadrao:
            self.isPulando = False
            self.velocidadePulo = self.velocidadePuloPadrao

    def correr(self):
        self.imagem = self.correrImg[self.indexAnimacao // 5]
        self.rect = self.imagem.get_rect()
        self.rect.x = self.posicaoX
        self.rect.y = self.posicaoY
        self.indexAnimacao += 1

    def agachar(self):
        self.imagem = self.agacharImg[self.indexAnimacao // 5]
        self.rect = self.imagem.get_rect()
        self.rect.x = self.posicaoX
        self.rect.y = self.posicaoY_agachado
        self.indexAnimacao += 1

    def update(self, tecla):
        if self.isAgachado:
            self.agachar()
        if self.isCorrendo:
            self.correr()
        if self.isPulando:
            self.pular()

        if self.indexAnimacao >= 10:
            self.indexAnimacao = 0

        if tecla[pygame.K_UP] and not self.isPulando:
            self.isAgachado = False
            self.isCorrendo = False
            self.isPulando = True
        elif tecla[pygame.K_DOWN] and not self.isPulando:
            self.isAgachado = True
            self.isCorrendo = False
            self.isPulando = False
        elif not (self.isPulando or tecla[pygame.K_DOWN]):
            self.isAgachado = False
            self.isCorrendo = True
            self.isPulando = False

    def draw(self, tela):
        tela.blit(self.imagem, (self.rect.x, self.rect.y))