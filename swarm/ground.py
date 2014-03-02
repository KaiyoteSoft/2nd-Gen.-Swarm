import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("img/grass.png").convert()
        self.rect = self.image.get_rect()