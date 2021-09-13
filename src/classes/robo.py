from classes.obstaculo import Obstaculo
from config.settings import velocidadeAnimacao

class Robo(Obstaculo):
    def __init__(self, imagem):
        self.tipoObstaculo = 0
        super().__init__(imagem, self.tipoObstaculo)
        self.rect.y = 250
        self.index = 0

    def draw(self, tela):
        if self.index >= 2:
            self.index = 0
        tela.blit(self.imagem[int(self.index)], self.rect)
        self.index += velocidadeAnimacao
