import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction, character):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((6, 6))
        #self.image.fill((255, 0, 0))
        pygame.draw.circle(self.image, (255, 255, 255), (3, 3), 3)
        pygame.draw.circle(self.image, (255, 0, 0), (3, 3), 1)
        self.image.convert()
        self.rect = self.image.get_rect()
        self.direction = direction
        self.speed = 7
        if self.direction == "right":
            self.rect.center = (character.rect.right, character.rect.centery)
        if self.direction == "left":
            self.rect.center = (character.rect.left, character.rect.centery)
        if self.direction == "up":
            self.rect.center = (character.rect.centerx, character.rect.top)
        if self.direction == "down":
            self.rect.center = (character.rect.centerx, character.rect.bottom)
        if self.direction == "topLeft":
            self.rect.center = (character.rect.left, character.rect.top)
        if self.direction == "bottomLeft":
            self.rect.center = (character.rect.left, character.rect.bottom)
        if self.direction == "topRight":
            self.rect.center = (character.rect.right, character.rect.top)
        if self.direction == "bottomRight":
            self.rect.center = (character.rect.right, character.rect.bottom)
    
        
            
    
    ### movement for bullet
    def update(self):
      
        if self.direction == "right":
            if self.rect.centerx < 480:
                self.rect.centerx += self.speed
            else:
                self.kill()
        if self.direction == "left":
            if self.rect.centerx > 0:
                self.rect.centerx -= self.speed
            else:
                self.kill()
        if self.direction == "up":
            if self.rect.centery > 0:
                self.rect.centery -= self.speed
            else:
                self.kill()
        if self.direction == "down":
            if self.rect.centery < 320:
                self.rect.centery += self.speed
            else:
                self.kill()
        ### Diagonal bullet firing movement
        if self.direction == "topLeft":
            if self.rect.centerx > 0 and self.rect.centery > 0:
                self.rect.centerx -= 4
                self.rect.centery -= 4
            else:
                self.kill()
           
        
        if self.direction == "bottomLeft":
            if self.rect.centerx > 0 and self.rect.centery < 320:
                self.rect.centerx -= 4
                self.rect.centery += 4
            else:
                self.kill()
            
            
        if self.direction == "topRight":
            if self.rect.centerx < 480 and self.rect.centery > 0:
                self.rect.centerx += 4
                self.rect.centery -= 4
            else:
                self.kill()
            
            
        if self.direction == "bottomRight":
            if self.rect.centerx < 480 and self.rect.centery < 320:
                self.rect.centerx += 4
                self.rect.centery += 4