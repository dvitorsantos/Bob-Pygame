import os
import pygame

correr = [pygame.image.load(os.path.join("../assets/bobesponja/run", "0.png")),
        pygame.image.load(os.path.join("../assets/bobesponja/run", "1.png")),
        pygame.image.load(os.path.join("../assets/bobesponja/run", "2.png")),
        pygame.image.load(os.path.join("../assets/bobesponja/run", "3.png")),
        pygame.image.load(os.path.join("../assets/bobesponja/run", "4.png")),
        pygame.image.load(os.path.join("../assets/bobesponja/run", "5.png")),
        pygame.image.load(os.path.join("../assets/bobesponja/run", "6.png")),
        pygame.image.load(os.path.join("../assets/bobesponja/run", "7.png")),
        pygame.image.load(os.path.join("../assets/bobesponja/run", "8.png"))]

pular = pygame.image.load(os.path.join("../assets/bobesponja/jump", "1.png"))

agachar = [pygame.image.load(os.path.join("../assets/bobesponja/crouch", "0.png")),
        pygame.image.load(os.path.join("../assets/bobesponja/crouch", "1.png")),]

obstaculosImg = [pygame.image.load(os.path.join("../assets/obstaculos", "0.png")),
        pygame.image.load(os.path.join("../assets/obstaculos", "1.png")),
        pygame.image.load(os.path.join("../assets/obstaculos", "2.png")),
        pygame.image.load(os.path.join("../assets/obstaculos", "3.png")),
        pygame.image.load(os.path.join("../assets/obstaculos", "4.png")),
        pygame.image.load(os.path.join("../assets/obstaculos", "bubble.png"))]

minhoca = [pygame.image.load(os.path.join("../assets/minhoca", "0.png")),
        pygame.image.load(os.path.join("../assets/minhoca", "1.png")),
        pygame.image.load(os.path.join("../assets/minhoca", "2.png")),
        pygame.image.load(os.path.join("../assets/minhoca", "3.png")),
        pygame.image.load(os.path.join("../assets/minhoca", "4.png")),
        pygame.image.load(os.path.join("../assets/minhoca", "5.png")),
        pygame.image.load(os.path.join("../assets/minhoca", "6.png")),
        pygame.image.load(os.path.join("../assets/minhoca", "7.png"))]

planoDeFundo = pygame.image.load(os.path.join("../assets/others", "background.jpg"))
planoDeFundoMenu = pygame.image.load(os.path.join("../assets/others", "BackgroundMenu.jpg"))
bolha = pygame.image.load(os.path.join("../Assets/others", "bolha.png"))