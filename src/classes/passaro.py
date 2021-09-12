from classes.obstaculo import Obstaculo

class Passaro(Obstaculo):
    def __init__(self, imagem):
        self.tipoObstaculo = 0
        super().__init__(imagem, self.tipoObstaculo)
        self.rect.y = 250
        self.index = 0

    def draw(self, tela):
        if self.index >= 9:
            self.index = 0
        tela.blit(self.imagem[self.index//5], self.rect)
        self.index += 1
