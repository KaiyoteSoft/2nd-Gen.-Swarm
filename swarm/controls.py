import pygame
from bullet import Bullet

try:
    import android
except ImportError:
    android = None

try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer

class Controls(pygame.sprite.Sprite):
    def __init__(self, control_type):
        pygame.sprite.Sprite.__init__(self)
        if control_type == "move":
            self.image = pygame.image.load("img/arrows_transparent.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.top = 170
            self.rect.left = 10
        elif control_type == "fire":
            self.image = pygame.image.load("img/arrows_fire_directions.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.top = 170
            self.rect.left = 320
        self.button_size = 50
        self.direction = "stop"
        self.shot = False

        
        
###### creating fonts / rectangles to blit bullets # to screen
        self.counter = 10
        self.RED = (255, 0, 0)
        self.LIME_GREEN = (139, 235, 103)
        self.gameFont = pygame.font.Font("fonts/ASTONISH.TTF", 20)
        self.bullet_counter_image = self.gameFont.render("Bullets:" + str(self.counter), True, self.RED)
        self.bullet_counter_rect = pygame.Rect(150, 5, 60, 23)
        
        
        

    
    def movement(self):
        
        pos = pygame.mouse.get_pos()
        
        ## creates rectangles for movement
        self.rect_right_leftedge = self.rect.right - self.button_size
        self.rect_right_topedge = self.rect.top + self.button_size
        self.right_rect = pygame.Rect(self.rect_right_leftedge, self.rect_right_topedge,
                                      self.button_size, self.button_size)
        if self.right_rect.collidepoint(pos):
            self.direction = "right"
        
        self.rect_left_leftedge = self.rect.left 
        self.rect_left_topedge = self.rect.top + self.button_size
        self.left_rect = pygame.Rect(self.rect_left_leftedge, self.rect_left_topedge,
                                     self.button_size, self.button_size)
        if self.left_rect.collidepoint(pos):
            self.direction = "left"
            
        self.rect_down_leftedge = self.rect.left + self.button_size
        self.rect_down_topedge = self.rect.top + self.button_size + self.button_size
        self.down_rect = pygame.Rect(self.rect_down_leftedge, self.rect_down_topedge,
                                     self.button_size, self.button_size)
        if self.down_rect.collidepoint(pos):
            self.direction = "down"
            
        self.rect_up_leftedge = self.rect.left + self.button_size
        self.rect_up_topedge = self.rect.top 
        self.up_rect = pygame.Rect(self.rect_up_leftedge, self.rect_up_topedge,
                                     self.button_size, self.button_size)
        if self.up_rect.collidepoint(pos):
            self.direction = "up"
            
        self.rect_stop_leftedge = self.rect.left + self.button_size
        self.rect_stop_topedge = self.rect.top + self.button_size
        self.stop_rect = pygame.Rect(self.rect_stop_leftedge, self.rect_stop_topedge,
                                     self.button_size, self.button_size)
        if self.stop_rect.collidepoint(pos):
            self.direction = "stop"
            
        return(self.direction)
        
    
    
    
    def firing(self, character, bullet_group, windowSurface):
        
        pos = pygame.mouse.get_pos()
        
        
        ### creates the rectangles for firing bullets and adds them to the list
        self.rect_right_leftedge = self.rect.right - self.button_size
        self.rect_right_topedge = self.rect.top + self.button_size
        self.right_rect = pygame.Rect(self.rect_right_leftedge, self.rect_right_topedge,
                                      self.button_size, self.button_size)
    
######## checking for number of bullets    
        if self.right_rect.collidepoint(pos) and self.counter > 0:
            direction = "right"
            bullet = Bullet(direction, character)
            bullet_group.add(bullet)
            self.counter = self.counter - 1
            self.shot = True 
            #print (self.counter)
        
        self.rect_left_leftedge = self.rect.left 
        self.rect_left_topedge = self.rect.top + self.button_size
        self.left_rect = pygame.Rect(self.rect_left_leftedge, self.rect_left_topedge,
                                     self.button_size, self.button_size)
        
        if self.left_rect.collidepoint(pos) and self.counter > 0:
            direction = "left"
            bullet = Bullet(direction, character)
            bullet_group.add(bullet)
            self.counter = self.counter - 1
            self.shot = True 
            
        self.rect_down_leftedge = self.rect.left + self.button_size
        self.rect_down_topedge = self.rect.top + self.button_size + self.button_size
        self.down_rect = pygame.Rect(self.rect_down_leftedge, self.rect_down_topedge,
                                     self.button_size, self.button_size)
        
        if self.down_rect.collidepoint(pos) and self.counter > 0:
            direction = "down"
            bullet = Bullet(direction, character)
            bullet_group.add(bullet)
            self.counter = self.counter - 1
            self.shot = True 
            
        self.rect_up_leftedge = self.rect.left + self.button_size
        self.rect_up_topedge = self.rect.top 
        self.up_rect = pygame.Rect(self.rect_up_leftedge, self.rect_up_topedge,
                                     self.button_size, self.button_size)
        
        if self.up_rect.collidepoint(pos) and self.counter > 0:
            direction = "up"
            bullet = Bullet(direction, character)
            bullet_group.add(bullet)
            self.counter = self.counter - 1
            self.shot = True 
        
        
        
        ### directions for diagonal shooting controls    
        self.rect_TopLeftDiag_leftedge = self.rect.left
        self.rect_TopLeftDiag_topedge = self.rect.top
        self.TopLeftDiag_rect = pygame.Rect(self.rect_TopLeftDiag_leftedge, self.rect_TopLeftDiag_topedge,
                                            self.button_size, self.button_size)
        
        if self.TopLeftDiag_rect.collidepoint(pos) and self.counter > 0:
            direction = "topLeft"
            bullet = Bullet(direction, character)
            bullet_group.add(bullet)
            self.counter = self.counter - 1
            self.shot = True 
            
        self.rect_BottomLeftDiag_leftedge = self.rect.left
        self.rect_BottomLeftDiag_topedge = self.rect.top + self.button_size + self.button_size
        self.BottomLeftDiag_rect = pygame.Rect(self.rect_BottomLeftDiag_leftedge, self.rect_BottomLeftDiag_topedge,
                                               self.button_size, self.button_size)
        
        if self.BottomLeftDiag_rect.collidepoint(pos) and self.counter > 0:
            direction = "bottomLeft"
            bullet = Bullet(direction, character)
            bullet_group.add(bullet)
            self.counter = self.counter - 1
            self.shot = True 
            
        self.rect_TopRightDiag_leftedge = self.rect.right - self.button_size
        self.rect_TopRightDiag_topedge = self.rect.top
        self.TopRightDiag_rect = pygame.Rect(self.rect_TopRightDiag_leftedge, self.rect_TopRightDiag_topedge,
                                             self.button_size, self.button_size)
        
        if self.TopRightDiag_rect.collidepoint(pos) and self.counter > 0:
            direction = "topRight"
            bullet = Bullet(direction, character)
            bullet_group.add(bullet)
            self.counter = self.counter - 1
            self.shot = True 
            
        self.rect_BottomRightDiag_leftedge = self.rect.right - self.button_size
        self.rect_BottomRightDiag_topedge = self.rect.top + self.button_size + self.button_size
        self.BottomRightDiag_rect = pygame.Rect(self.rect_BottomRightDiag_leftedge, self.rect_BottomRightDiag_topedge,
                                                self.button_size, self.button_size)
        
        if self.BottomRightDiag_rect.collidepoint(pos) and self.counter > 0:
            direction = "bottomRight"
            bullet = Bullet(direction, character)
            bullet_group.add(bullet)
            self.counter = self.counter - 1
            self.shot = True 
            
        #if self.counter == 0:
        #    self.elapsed_clock = pygame.time.get_ticks()
            
        return(bullet_group)
            