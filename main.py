import pygame, sys, random
import start_screen
from pygame.locals import *

import swarm
from swarm import Ground as Ground
from swarm import Plant as Plant
from swarm import Player as Player
from swarm import Bullet as Bullet
from swarm import Controls as Controls
from swarm import Monster as Monster

try:
    import android
except ImportError:
    android = None

        





            
        
        
        
        


        

    
   
## uncrowd algorithm

def uncrowd(mon_group):
    temp_group = mon_group.copy()
    for mon in mon_group:
        temp_group.remove(mon)
        if pygame.sprite.spritecollideany(mon, temp_group):
           mon.rect.centerx += random.randint(-10, 10)
           mon.rect.centery += random.randint(-10, 10)
        
        
           
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
        
        
    def initTimer(self):
       self.gameFont = pygame.font.Font("fonts/ASTONISH.TTF", 16)
       self.timeSprite = pygame.sprite.Sprite()
       self.timeSprite.image = self.gameFont.render("Time: ", True , self.RED)
       self.timeSprite.rect = self.timeSprite.image.get_rect(left = 90, top = 10)
       self.time_group = pygame.sprite.Group(self.timeSprite)
        
     
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
        if len(self.monster_group) == 0 and self.level == 7:
            self.level = 8
            self.trigger = False
            
        if len(self.monster_group) == 0 and self.level == 6:
            self.level = 7
            self.trigger = False
            
        if len(self.monster_group) == 0 and self.level == 5:
            self.level = 6
            self.trigger = False
        
        if len(self.monster_group) == 0 and self.level == 4:
            self.level = 5
            self.trigger = False
            
        if len(self.monster_group) == 0 and self.level == 3:
            self.level = 4
            self.trigger = False
            
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
            pygame.time.wait(3000)
            self.character.rect.center = (240, 160)
            self.direction = "stop"
            
            ## blits the super Monsters at the beginning of each level
            superMonster2 = Monster()
            superMonster2.image = pygame.image.load("img/superMonster_crab.png").convert_alpha()
            superMonster2.rect.center = (random.randint(400, 500), random.randint(-120, 20))
            superMonster2.speed_trigger = 1
            superMonster2.current_trigger = 0
            self.superMonster2_group.empty()
            if self.level >= 6:
                self.superMonster2_group.add(superMonster2)
            
            superMonster = Monster()
            superMonster.image = pygame.image.load("img/SuperMonster_mummy.png")
            superMonster.image.convert_alpha()
            superMonster.rect.center = (random.randint(400, 500), random.randint(150, 340))
            superMonster.speed_trigger = 1
            superMonster.current_trigger = 0
            self.superMonster_group.empty()
            if self.level >= 3:    
                self.superMonster_group.add(superMonster)
                
        ### counter for the monsters speed
            zombie = Monster()
            zombie.speed_trigger = 1
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
                monster = Monster()
                self.monster_group.add(monster)
                
                
            self.trigger = True
            

####### uncompleted class for health        
class Health():
    def __init__(self):
        self.alive = True
            
           



def main():
    
    pygame.init()
    
    clock = pygame.time.Clock()
    FPS = 30
    
    ### Load the awesome sunset
    sunset = pygame.image.load("img/sunset.jpg")
    
    windowSurface = pygame.display.set_mode((480, 320), 0, 32)
    warningSurface = pygame.Surface((480, 320))
    warning_rect = warningSurface.get_rect()
    warningSurface.fill((0, 0, 255))
    warningSurface.set_alpha(150)
    
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    PINK = (254, 15, 234)
    direction = ("stop")
    LIGHTBLUE = (0, 255, 252)
    DARKRED = (198, 46, 46)
    GREEN = (0, 255, 0)
    
    field_column = []
    forest_group = pygame.sprite.Group()
    
    for y in range(0, 320, 32):
        grass = Ground()
        grass.rect.right = 480
        grass.rect.top = y
        field_column.append(grass)
    
    ### initialize the tree + set pos
    x = 150
    for y in range(150, 320, 64):
        tree = Plant()
        tree.rect.center = (x, y)
        x = x + 32
        forest_group.add(tree)
        
    ## initialize the controls for player
    controls = Controls("move")
    
    ## initialize the controls for shooting
    fire = Controls("fire")
    stop = pygame.sprite.Sprite()
    stop.image = pygame.Surface((40, 40))
    stop.rect = stop.image.get_rect()
    stop.rect.center = controls.rect.center
    stop.image.fill((199, 255, 0))
    stop.image.set_alpha(85)
    controls_group = pygame.sprite.Group(controls, fire, stop)
    

    ## instantiate the condition of the players life
    health = Health()
        
    
    ## Create a rectangle for the "Player DEAD :)
    endFont = pygame.font.Font("fonts/BLOODY.ttf", 130)
    endText = endFont.render("DEAD", True , RED)
    endText_rect = pygame.Rect(80, 150, 200, 200)
    
    ### Create a rectangle for Play Again 
    playAgain_font = pygame.font.Font("fonts/ASTONISH.TTF", 80)
    playAgain_text = playAgain_font.render("Play Again? ", True, LIGHTBLUE)
    playAgain_rect = pygame.Rect(10, 10, 480, 180)
    
    ### Create a rectangle for Play Again = No
    no_font = pygame.font.Font("fonts/BLOODY.ttf", 45)
    no_text = no_font.render("No...", True, DARKRED)
    no_rect = pygame.Rect(320, 100, 150, 60)
    
    ### Create a rectangle for Play Again = Yes
    yes_font = pygame.font.Font("fonts/ASTONISH.TTF", 60)
    yes_text = yes_font.render("YES!!!", True, GREEN)
    yes_rect = pygame.Rect(40, 90, 150, 60)
    
    ### Create a rectangle for the PLAYER HERO :)
    winFont = pygame.font.Font("fonts/ASTONISH.TTF", 90)
    winText = winFont.render("HERO", True, PINK)
    winText_rect = pygame.Rect(60, 230, 200, 200)
    
    ## Create a rectangle for large hero
    char_large = pygame.image.load("img/blue_boy_large.png")
    char_rect = char_large.get_rect(left = 220, bottom = 240)
            
    ## Create rectangle for girl
    girl = pygame.image.load("img/girl.png")
    girl_rect = girl.get_rect(left = 170, bottom = 210)
            
    ## initialize the player
    character = Player()
    
    ## initialize the bullet + create the bullet_group
    bullet_group = pygame.sprite.Group()
    
    ### initialize the monseter
    zombie = Monster()
    zombie.speed_trigger = 1
    zombie.current_trigger = 0
    monster_group = pygame.sprite.Group()
    superMonster_group = pygame.sprite.Group()
    superMonster2_group = pygame.sprite.Group()
    for number in range(0, 8):
        monster = Monster()
        monster_group.add(monster)
    
    
    appear_crab = False
    appear_mummy = False
    
## instantiate the super zombie
    
    superMonster = Monster()
    superMonster.image = pygame.image.load("img/SuperMonster_mummy.png")
    superMonster.image.convert_alpha()
    superMonster.rect.center = (random.randint(400, 500), random.randint(150, 340))
    superMonster.speed_trigger = 1
    superMonster.current_trigger = 0
    if appear_mummy == True:
        superMonster_group.add(superMonster)

    
## instantiate the super zombie2 ze CRAB
    
    superMonster2 = Monster()
    superMonster2.image = pygame.image.load("img/superMonster_crab.png").convert_alpha()
    superMonster2.rect.center = (random.randint(400, 500), random.randint(-120, 20))
    superMonster2.speed_trigger = 1
    superMonster2.current_trigger = 0
    if appear_crab == True:
        superMonster2_group.add(superMonster2)
        

    

    ## initialize the clock
    timer = Timer()
    

    
    
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
    
    gameOn = True
    
    startScreen = start_screen.PreGame()
    
    while gameOn:
### start screen
        
        if timer.level == 0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            startScreen.start()
            windowSurface.blit(startScreen.start(), (0, 0))
            timer.level = startScreen.checkLevel()
            pygame.display.update()
        else:
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    bullet_group = fire.firing(character, bullet_group, windowSurface)
                   # print (fire.counter)
                    direction = controls.movement()
                    if health.alive == False:
                        if no_rect.collidepoint(pygame.mouse.get_pos()):
                            pygame.quit()
                            sys.exit()
                        elif yes_rect.collidepoint(pygame.mouse.get_pos()):
                            main()
                    
           
            for x in range(480, 0, -32):
                for grass in field_column:
                    grass.rect.right = x
                    windowSurface.blit(grass.image, grass.rect)
                    
        
                    
            ## blits the tree
            for tree in forest_group:
                windowSurface.blit(tree.image, tree.rect)
            
            ## blit the controls for the player and shooting
            controls_group.draw(windowSurface)
        
            
                
            
            ### blit the timer onto the screen
            monster_group, time_group, windowSurface, superMonster_group, superMonster2_group, character, direction, forest_group = timer.update(monster_group, windowSurface,
                                                                             superMonster_group, superMonster2_group, character, direction, forest_group)
            
                
                
            
            time_group.draw(windowSurface)
            
            
            
            
            ## movement for character
            if direction == "right" and character.rect.right <= 480:
                character.rect.centerx = character.rect.centerx + 5
            if direction == "left" and character.rect.left >= 0:
                character.rect.centerx = character.rect.centerx - 5
            if direction == "up" and character.rect.top >= 0:
                character.rect.centery = character.rect.centery - 5
            if direction == "down" and character.rect.bottom <= 320:
                character.rect.centery = character.rect.centery + 5
                
            
            ### Collision detection for trees
            for tree in forest_group:
                if tree.rect.collidepoint(character.rect.center):
                    direction = "stop"
            
            #print (controls.counter)
            fire.bullet_counter_image = fire.gameFont.render("Bullets:" + str(fire.counter), True, fire.RED)
            pygame.draw.rect(windowSurface, fire.LIME_GREEN, fire.bullet_counter_rect)
            windowSurface.blit(fire.bullet_counter_image, fire.bullet_counter_rect)
            
            ## blits the player
            windowSurface.blit(character.image, character.rect)
            
            
            ## blits the monster
            #monster_group.update(character, timer.level)
            
####### speed check
            if timer.level == 3:
                appear_mummy = True
            if timer.level == 6:
                appear_crab = True
            ### adjust speed
            if timer.level == 2:
                superMonster.speed_trigger = 1
                superMonster2.current_trigger = 0
                zombie.speed_trigger = 3
            if timer.level == 3:
                zombie.speed_trigger = 2
                superMonster.speed_trigger = 3
            if timer.level == 4:
                zombie.speed_trigger = 1
                superMonster.speed_trigger = 2
            if timer.level == 5:
                zombie.speed_trigger = 3
                superMonster.speed_trigger = 4
            if timer.level == 6:
                zombie.speed_trigger = 2
                superMonster.speed_trigger = 4
                superMonster2.speed_trigger = 4
            if timer.level == 7:
                zombie.speed_trigger = 2
                superMonster.speed_trigger = 3
                superMonster2.speed_trigger = 4
            if timer.level == 8:
                zombie.speed_trigger = 2
                superMonster.speed_trigger = 3
                superMonster2.speed_trigger = 3
                           

            
            if superMonster.current_trigger < superMonster.speed_trigger:
                superMonster.current_trigger = superMonster.current_trigger + 1
            else:
                superMonster_group.update(character, timer.level)
                superMonster.current_trigger = 0
            if superMonster2.current_trigger < superMonster2.speed_trigger:
                superMonster2.current_trigger = superMonster2.current_trigger + 1
            else:
                superMonster2_group.update(character, timer.level)
                superMonster2.current_trigger = 0
                
            if zombie.current_trigger < zombie.speed_trigger:
                zombie.current_trigger = zombie.current_trigger + 1
            else:
                monster_group.update(character, timer.level)
                zombie.current_trigger = 0
                
            monster_group.draw(windowSurface)
            uncrowd(monster_group)
            
            superMonster2_group.draw(windowSurface)
            superMonster_group.draw(windowSurface)
            
        
        
            
        ######## Test for collision between player and zombie
            if pygame.sprite.spritecollideany(character, superMonster_group):
                windowSurface.blit(warningSurface, warning_rect)
                health.alive = False
                
            if pygame.sprite.spritecollideany(character, superMonster2_group):
                windowSurface.blit(warningSurface, warning_rect)
                health.alive = False
            
            
            
            if health.alive == True and timer.level == 8 and len(monster_group) == 0:
                windowSurface.blit(sunset, warning_rect)
                windowSurface.blit(winText, winText_rect)
                windowSurface.blit(char_large, char_rect)
                windowSurface.blit(girl, girl_rect)
                superMonster_group.empty()
                superMonster2_group.empty()
                
            
            ## blits the bullets
            bullet_group.update()
            bullet_group.draw(windowSurface)
            
            ## collision detection for the monster and bullet
            pygame.sprite.groupcollide(bullet_group, monster_group, True, True)
            pygame.sprite.groupcollide(bullet_group, superMonster_group, True, False)
            pygame.sprite.groupcollide(bullet_group, forest_group, True, False)
            pygame.sprite.groupcollide(bullet_group, superMonster2_group, True, False)
                
                
            if pygame.sprite.spritecollideany(character, monster_group):
                windowSurface.blit(warningSurface, warning_rect)
                health.alive = False
            if health.alive == False:
                # blit statement for "Player DEAD"
                windowSurface.fill(BLACK)
                windowSurface.blit(endText, endText_rect)
                windowSurface.blit(playAgain_text, playAgain_rect)
                
                windowSurface.blit(no_text, no_rect)
                windowSurface.blit(yes_text, yes_rect)
                
    
            
                
            pygame.display.update()
            clock.tick(FPS)
        
main()