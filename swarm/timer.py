import pygame
import random
import time
from monster import Monster
from plant import Plant


class Timer():
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.trigger = False
##############
        self.level = 0
        self.RED = (255, 0, 0)
        self.lightBlue = (0, 254, 237)
        self.GreenYellow = (160, 195, 7)
        self.initTimer()
        self.monster = False
        self.mummy_death = False
        
    def initTimer(self):
       self.gameFont = pygame.font.Font("fonts/ASTONISH.TTF", 16)
       self.timeSprite = pygame.sprite.Sprite()
       self.timeSprite.image = self.gameFont.render("Time: ", True , self.RED)
       self.timeSprite.rect = self.timeSprite.image.get_rect(left = 90, top = 10)
       self.time_group = pygame.sprite.Group(self.timeSprite)
       self.elapsed_time = 0
        
     
## instantiate a bunch of stuff   
    def update(self, monster_group, windowSurface, superMonster_group, superMonster2_group, character, direction, forest_group):
        self.windowSurface = windowSurface
        self.monster_group = monster_group
        self.superMonster_group = superMonster_group
        self.character = character
        self.direction = direction
        self.forest_group = forest_group
        self.superMonster2_group = superMonster2_group
        self.elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        self.timeSprite.image = self.gameFont.render("Time: " + str(self.elapsed_time), True, self.RED, self.GreenYellow)
        self.CalcLevel()
        self.createMonsters()
        return(self.monster_group, self.time_group, self.windowSurface, self.superMonster_group,
               self.superMonster2_group, self.character, self.direction, self.forest_group)
    
    
    
        ### if the length of the monster group is zero then go to next level   
    def CalcLevel(self):
        superMonster = Monster("mummy")
        superMonster2 = Monster("crab")
        
        if len(self.monster_group) == 0 and self.level == 7 and self.mummy_death == True:
            self.level = 8
            self.trigger = False
            self.mummy_death = False
            
        if len(self.monster_group) == 0 and self.level == 6 and self.mummy_death == True:
            self.level = 7
            self.trigger = False
            self.mummy_death = False
            
        if len(self.monster_group) == 0 and self.level == 5 and self.mummy_death == True:
            self.level = 6
            self.trigger = False
            self.mummy_death = False
        
        if len(self.monster_group) == 0 and self.level == 4 and self.mummy_death == True:
            self.level = 5
            self.trigger = False
            self.mummy_death = False
            
        if len(self.monster_group) == 0 and self.level == 3 and self.mummy_death == True:
            self.level = 4
            self.trigger = False
            self.mummy_death = False
            
        if len(self.monster_group) == 0 and self.level == 2:
            self.level = 3
            self.trigger = False

        if len(self.monster_group) == 0 and self.level == 1:
            self.level = 2
            self.trigger = False
            
    
        
            
    def createMonsters(self):
        Green = (0, 255, 0)
        Pink = (255, 18, 248)
        level_rect = pygame.Rect(10, 10, 470, 310)
        level_rect2 = pygame.Rect(220, 85, 200, 100)
        levelFont = pygame.font.Font("fonts/BLOODY.ttf", 60)
        level_text = levelFont.render("Moving to Level ", False, Pink)
        level_text2 = levelFont.render(str(self.level), False, Pink)
        
### the transition surface between levels
        if self.trigger == False and self.level > 1:
            
            self.windowSurface.fill(Green)
            ## blit statement for the "changing levels
            self.windowSurface.blit(level_text, level_rect)
            self.windowSurface.blit(level_text2, level_rect2)
            pygame.display.update()
            #if self.elapsed_time > (3000):    
            self.monster = True
            pygame.time.wait(3000)
            self.character.rect.center = (240, 160)
            self.direction = "stop"
            
            ## blits the super Monsters at the beginning of each level
            superMonster2 = Monster("crab")
            #superMonster2.image = pygame.image.load("img/superMonster_crab.png").convert_alpha()
            superMonster2.rect.center = (random.randint(400, 500), random.randint(-120, 20))
            superMonster2.speed_trigger = 1
            superMonster2.current_trigger = 0
            self.superMonster2_group.empty()
            if self.level >= 6:
                self.superMonster2_group.add(superMonster2)
            
            superMonster = Monster("mummy")
            #superMonster.image = pygame.image.load("img/SuperMonster_mummy.png")
            #superMonster.image.convert_alpha()
            superMonster.rect.center = (random.randint(400, 500), random.randint(150, 340))
            superMonster.speed_trigger = 1
            superMonster.current_trigger = 0
            self.superMonster_group.empty()
            if self.level >= 3:    
                self.superMonster_group.add(superMonster)
                
        ### counter for the monsters speed
            zombie = Monster("zombie")
            zombie.speed_trigger = 2
            zombie.current_trigger = 0
            
            
            
##### instantiates the objects and addes them to the forest_group list
            if self.level == 2:
                tree = Plant()
                tree.rect.center = (15, 45)
                tree2 = Plant()
                tree2.rect.center = (460, 45)
                tree3 = Plant()
                tree3.rect.center = (15, 294)
                tree4 = Plant()
                tree4.rect.center = (460, 294)
                self.forest_group.add(tree, tree2, tree3, tree4)
                
            
            if self.level == 3:
                self.forest_group.empty()
                for x in range(10, 470, 32):
                    y = 35
                    tree = Plant()
                    tree.rect.center = (x, y)
                    self.forest_group.add(tree)
            
            if self.level == 4:
                for x in range(10, 470, 32):
                    y = 310
                    cactus = Plant()
                    cactus.image = pygame.image.load("img/cactus.png")
                    cactus.image.convert_alpha()
                    cactus.rect.center = (x, y)
                    self.forest_group.add(cactus)
            
            if self.level == 5:
                self.forest_group.empty()
                for x1 in range(40, 440, 30):
                    y1 = 50
                    pillar = Plant()
                    pillar.image = pygame.image.load("img/pillar.png")
                    pillar.image.convert_alpha()
                    pillar.rect.center = (x1, y1)
                for x2 in range(40, 440, 30):
                    y2 = 100
                    pillar2 = Plant()
                    pillar2.image = pygame.image.load("img/pillar.png")
                    pillar.image.convert_alpha()
                    pillar2.rect.center = (x2, y2)
                for x3 in range(40, 440, 30):
                    y3 = 150
                    pillar3 = Plant()
                    pillar3.image = pygame.image.load("img/pillar.png")
                    pillar3.image.convert_alpha()
                    pillar3.rect.center = (x3, y3)
                for x4 in range(40, 440, 30):
                    y4 = 200
                    pillar4 = Plant()
                    pillar4.image = pygame.image.load("img/pillar.png")
                    pillar4.image.convert_alpha()
                    pillar4.rect.center = (x4, y4)
                    
                
                
                    self.forest_group.add(pillar, pillar2, pillar3, pillar4)
                    
            if self.level == 6:
                self.forest_group.empty()
                for y in range(40, 260, 70):
                    for x in range(180, 330, 70):
                        dragon = Plant()
                        dragon.image = pygame.image.load("img/dragon.png")
                        dragon.image.convert_alpha()
                        dragon.rect.center = (x, y)
                        self.forest_group.add(dragon)
                    
            
            if self.level == 7:
                self.forest_group.empty()
                for x1 in range(30, 100, 30):
                    y1 = 100
                    pillar1 = Plant()
                    pillar1.image = pygame.image.load("img/pillar.png")
                    pillar1.image.convert_alpha()
                    pillar1.rect = pillar1.image.get_rect()
                    pillar1.rect.center = (x1, y1)
                    self.forest_group.add(pillar1)
                for x2 in range(15, 65, 30):
                    y2 = 200
                    pillar2 = Plant()
                    pillar2.image = pygame.image.load("img/pillar.png")
                    pillar2.image.convert_alpha()
                    pillar2.rect = pillar2.image.get_rect()
                    pillar2.rect.center = (x2, y2)
                    self.forest_group.add(pillar2)
                    
                statue1 = Plant()
                statue1.image = pygame.image.load("img/statue.png")
                statue1.image.convert_alpha()
                statue1.rect = statue1.image.get_rect()
                statue1.rect.center = (240, 100)
                statue2 = Plant()
                statue2.image = pygame.image.load("img/statue.png")
                statue2.image.convert_alpha()
                statue2.rect = statue2.image.get_rect()
                statue2.rect.center = (240, 220)
                statue3 = Plant()
                statue3.image = pygame.image.load("img/statue.png")
                statue3.image.convert_alpha()
                statue3.rect = statue3.image.get_rect()
                statue3.rect.center = (180, 160)
                statue4 = Plant()
                statue4.image = pygame.image.load("img/statue.png")
                statue4.image.convert_alpha()
                statue4.rect = statue4.image.get_rect()
                statue4.rect.center = (300, 160)
                
                for x3 in range(380, 460, 30):
                    y3 = 100
                    rubble = Plant()
                    rubble.image = pygame.image.load("img/rubble.png")
                    rubble.image.convert_alpha()
                    rubble.rect = rubble.image.get_rect()
                    rubble.rect.center = (x3, y3)
                    self.forest_group.add(rubble)
                for x4 in range(380, 460, 30):
                    y4 = 200
                    bones = Plant()
                    bones.image = pygame.image.load("img/bones.png")
                    bones.image.convert_alpha()
                    bones.rect = bones.image.get_rect()
                    bones.rect.center = (x4, y4)
                    self.forest_group.add(bones)
                
                self.forest_group.add(statue1, statue2, statue3, statue4)
                
                
                
            if self.level == 8:
                self.forest_group.empty()
                lightThrone = Plant()
                lightThrone.image = pygame.image.load("img/lightThrone.png")
                lightThrone.image.convert_alpha()
                lightThrone.rect.center = (420, 120)
                
                darkThrone = Plant()
                darkThrone.image = pygame.image.load("img/darkThrone.png")
                darkThrone.image.convert_alpha()
                darkThrone.rect.center = (60, 120)
                
                coffin = Plant()
                coffin.image = pygame.image.load("img/coffin.png")
                coffin.image.convert_alpha()
                coffin.rect.center = (240, 160)
                
                for x in range(160, 320, 42):
                    y = 300
                    knight = Plant()
                    knight.image = pygame.image.load("img/knight.png")
                    knight.image.convert_alpha()
                    knight.rect.center = (x, y)
                    self.forest_group.add(knight)
                    
                for x2 in range(340, 420, 28):
                    y2 = 50
                    crystal = Plant()
                    crystal.image = pygame.image.load("img/crystal.png")
                    crystal.image.convert_alpha()
                    crystal.rect = crystal.image.get_rect()
                    crystal.rect.center = (x2, y2)
                    self.forest_group.add(crystal)
                    
                for x3 in range(60, 140, 32):
                    y3 = 50
                    bones = Plant()
                    bones.image = pygame.image.load("img/bones.png")
                    bones.image.convert_alpha()
                    bones.rect = bones.image.get_rect()
                    bones.rect.center = (x3, y3)
                    self.forest_group.add(bones)
                
                self.forest_group.add(lightThrone, darkThrone, coffin)
                
                    
            
            self.monster_num = 6 + (self.level * 3)
            print("The level is " + str(self.level))
            print(str(self.monster_num) + " monsters created")
            print ("--------------------------------")
            
            for number in range(0, self.monster_num):
                monster = Monster("zombie")
                self.monster_group.add(monster)
                
                
            self.trigger = True
            

            
            