import pygame, sys, random
import time
import start_screen
from pygame.locals import *

import swarm
from swarm import Ground as Ground
from swarm import Plant as Plant
from swarm import Player as Player
from swarm import Bullet as Bullet
from swarm import Controls as Controls
from swarm import Monster as Monster
from swarm import Timer as Timer
from swarm import Sound as Sound

try:
    import android
except ImportError:
    android = None
    
try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer
   
## uncrowd algorithm

def uncrowd(mon_group):
    temp_group = mon_group.copy()
    for mon in mon_group:
        temp_group.remove(mon)
        if pygame.sprite.spritecollideany(mon, temp_group):
           mon.rect.centerx += random.randint(-10, 10)
           mon.rect.centery += random.randint(-10, 10)
        
        
           

            

####### uncompleted class for health        
class Health():
    def __init__(self):
        self.alive = True
            
           



def main():
    
    pygame.init()


    clock = pygame.time.Clock()
### timer for the bullets
    # start_clock = pygame.time.get_ticks()
    screen_start = 0
    start_clock = time.time()
    
    bullet_empty = False
    
    
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
    
#### surface for reloading
    reload_surface = no_font.render("RELOADING", True, (RED))
    reload_surface_2 = pygame.Surface((480, 320))
    reload_surface_2.set_alpha(50)
    reload_surface_2.fill(RED)
    reload_rect = reload_surface.get_rect(center = (220, 20))
    
    
    
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
    zombie = Monster("zombie")
    monster_group = pygame.sprite.Group()
    superMonster_group = pygame.sprite.Group()
    superMonster2_group = pygame.sprite.Group()
    for number in range(0, 8):
        monster = Monster("zombie")
        monster_group.add(monster)
    
    
    appear_crab = False
    appear_mummy = False
    
## instantiate the super zombie
    
    superMonster = Monster("mummy")
    if appear_mummy == True:
        superMonster_group.add(superMonster)

    
## instantiate the super zombie2 ze CRAB
    
    superMonster2 = Monster("crab")
    if appear_crab == True:
        superMonster2_group.add(superMonster2)
        

    

    ## initialize the clock
    timer = Timer()

    
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
    
    gameOn = True
    
    startScreen = start_screen.PreGame()
    

    sound = Sound()

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
                    #if event.key == K_p:
                    #    reload.play()
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
            
            
            
### check for the number of bullets
            #bullet_clock = elapsed_clock
            
            current_bullet_clock = time.time()
            elapsed_clock =  int(current_bullet_clock - start_clock)
            if bullet_empty == True:
                #print(elapsed_clock)
                if elapsed_clock > 3:
                    fire.counter = 10
                    bullet_empty = False
                    start_clock = 0 
                    
    
            
            if fire.counter == 0 and bullet_empty == False:
                start_clock = time.time()
                bullet_empty = True
                sound.reload.play()
    
### clock for the interval between levels
            #if timer.trigger == False and timer.level > 1:
            #    screen_start = time.time()
            #timer.elapsed_time = screen_start - time.time()
                
### play bullet sound
            if fire.shot == True:
                sound.bullet_sound.play()     
                fire.shot = False
            
            if timer.monster == True:
                #print("ROAR")
                sound.roar.play()
                timer.monster = False
                
            timer.elapsed_time = time.time()
            
####### speed check
            if timer.level == 3:
                appear_mummy = True
            if timer.level == 6:
                appear_crab = True
            ### adjust speed
            if timer.level == 2:
                superMonster.speed_trigger = 1
                superMonster2.current_trigger = 0
                zombie.speed_trigger = 2
            if timer.level == 3:
                zombie.speed_trigger = 1
                superMonster.speed_trigger = 2
            if timer.level == 4:
                zombie.speed_trigger = 3
                superMonster.speed_trigger = 3
            if timer.level == 5:
                zombie.speed_trigger = 2
                superMonster.speed_trigger = 2
            if timer.level == 6:
                zombie.speed_trigger = 3
                superMonster.speed_trigger = 4
                superMonster2.speed_trigger = 3
            if timer.level == 7:
                zombie.speed_trigger = 2
                superMonster.speed_trigger = 3
                superMonster2.speed_trigger = 4
            if timer.level == 8:
                zombie.speed_trigger = 3
                superMonster.speed_trigger = 4
                superMonster2.speed_trigger = 4
                           

            
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
            mummy = pygame.sprite.groupcollide(bullet_group, superMonster_group, True, False)
            
### mummy health
            if len(mummy) > 0:
                print ("HIT")
                superMonster.health = superMonster.health - 1
                if superMonster.health <= 0:
                    superMonster_group.empty()
                    timer.mummy_death = True
                    superMonster = Monster("mummy")
                    superMonster_group.add(superMonster)
                    
                    
        
        
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
                
            
            if bullet_empty == True:
                windowSurface.blit(reload_surface, (reload_rect))
                windowSurface.blit(reload_surface_2, (0,0))
            
                
            pygame.display.update()
            clock.tick(FPS)
            #bullet_clock.tick(FPS)
        
main()