import pygame

class Plant(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/treenarrow.png").convert_alpha()
        self.rect = self.image.get_rect()
        