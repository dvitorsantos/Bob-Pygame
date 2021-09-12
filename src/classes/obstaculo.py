from config.settings import larguraTela, velocidadeJogo

class Obstaculo:
    def __init__(self, imagem, tipoObstaculo):
        self.imagem = imagem
        self.tipoObstaculo = tipoObstaculo
        self.rect = self.imagem[self.tipoObstaculo].get_rect()
        self.rect.x = larguraTela

    def update(self):
        self.rect.x -= velocidadeJogo

    def draw(self, tela):
        tela.blit(self.imagem[self.tipoObstaculo], self.rect)