import os
import pygame

cactusPequeno = [pygame.image.load(os.path.join("../assets/cactos", "SmallCactus1.png")),
                pygame.image.load(os.path.join("../assets/cactos", "SmallCactus2.png")),
                pygame.image.load(os.path.join("../assets/cactos", "SmallCactus3.png"))]

cactusGrande = [pygame.image.load(os.path.join("../assets/cactos", "LargeCactus1.png")),
                pygame.image.load(os.path.join("../assets/cactos", "LargeCactus2.png")),
                pygame.image.load(os.path.join("../assets/cactos", "LargeCactus3.png"))]

passaro = [pygame.image.load(os.path.join("../assets/passaro", "Bird1.png")),
        pygame.image.load(os.path.join("../assets/passaro", "Bird2.png"))]

#Assets do dinossauro
correr = [pygame.image.load(os.path.join("../Assets/dinossauro", "DinoRun1.png")),
           pygame.image.load(os.path.join("../Assets/dinossauro", "DinoRun2.png"))]
pular = pygame.image.load(os.path.join("../Assets/dinossauro", "DinoJump.png"))
agachar = [pygame.image.load(os.path.join("../Assets/dinossauro", "DinoDuck1.png")),
           pygame.image.load(os.path.join("../Assets/dinossauro", "DinoDuck2.png"))]

planoDeFundo = pygame.image.load(os.path.join("../assets/others", "Track.png"))
nuvem = pygame.image.load(os.path.join("../Assets/others", "Cloud.png"))