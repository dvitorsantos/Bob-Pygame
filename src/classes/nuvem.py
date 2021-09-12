import random

from config.settings import larguraTela, velocidadeJogo
from config.assets import nuvem

class Nuvem:
    def __init__(self):
        self.x = larguraTela + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.imagem = nuvem
        self.largura = self.imagem.get_width()

    def update(self):
        self.x -= velocidadeJogo
        if self.x < -self.largura:
            self.x = larguraTela + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, tela):
        tela.blit(self.imagem, (self.x, self.y))