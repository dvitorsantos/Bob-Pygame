import random

from classes.obstaculo import Obstaculo

class CactusPequeno(Obstaculo):
    def __init__(self, imagem):
        self.tipoObstaculo = random.randint(0, 2)
        super().__init__(imagem, self.tipoObstaculo)
        self.rect.y = 325
