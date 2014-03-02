import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/blue_boy_small.png").convert_alpha()
        self.rect = self.image.get_rect(center = (240, 160))
        