###########################Import################################

import pygame
from pygame.locals import *

############################DEFINE###############################

size = 1920, 1080
BLACK = 0, 0, 0
speed = 10
shot_range = 2000
shot_speed = 25
Attack_speed = 20
Waiting_attack = 0
loop = True
LeTire = 0

 ###########################INIT#################################
 
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('GAME')

IsaacPosX, IsaacPosY = 0, 0
shot = False
 
IsaacSprite=pygame.image.load('Sprite/nino.png')
TearSprite=pygame.image.load('Sprite/tacos.png')

############################Class################################

class Shoot :
    trajectoire = 'z'
    TearPosX = IsaacPosX
    TearPosY = IsaacPosY
    shot_range = shot_range
    
    def __init__(self, trajectoire, TearPosX, TearPosY, shot_range):
        self.trajectoire = trajectoire
        self.TearPosX = TearPosX
        self.TearPosY = TearPosY
        self.shot_range = shot_range
        

tire = [Shoot]

############################LOOP################################

while loop:
    # this adds the sprite at every frame rate
    screen.fill(BLACK)
    screen.blit(IsaacSprite,(IsaacPosX,IsaacPosY))
 
    for event in pygame.event.get():
        # this is to close the window
        if event.type==QUIT:
            loop = False
            #sys.exit() # this will close the kernel too
            # in development mode leave the comment above
    # this is the list with the keys being pressed

########################GESTION DEPLACEMENT######################

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        if (IsaacPosX > (0 + speed)):
            IsaacPosX -= speed
        elif (IsaacPosX > 0 and IsaacPosX < speed):
            IsaacPosX = 0   
            
    if keys[pygame.K_d]:
        if (IsaacPosX < (size[0] - speed - IsaacSprite.get_size()[0])):
            IsaacPosX += speed
        elif (IsaacPosX < size[0] and IsaacPosX > (size[0] - speed - IsaacSprite.get_size()[0])):
            IsaacPosX = size[0] - IsaacSprite.get_size()[0]
            
    if keys[pygame.K_z]:
        if (IsaacPosY > (0 + speed)):
            IsaacPosY -= speed
        elif (IsaacPosY > 0 and IsaacPosY < speed):
            IsaacPosY = 0  
            
    if keys[pygame.K_s]:
        if (IsaacPosY < (size[1] - speed - IsaacSprite.get_size()[1])):
            IsaacPosY += speed
        elif (IsaacPosY < size[1] and IsaacPosY > (size[1] - speed - IsaacSprite.get_size()[1])):
            IsaacPosY = size[1] - IsaacSprite.get_size()[1]
            
###########################GESTION TIRE#############################
            ###############TOUCHE##############
     
    if (Waiting_attack == 0):
        if keys[pygame.K_LEFT]:
            tire.append(Shoot('q', IsaacPosX, IsaacPosY, shot_range))
            Waiting_attack = Attack_speed

        elif keys[pygame.K_RIGHT]:
            tire.append(Shoot('d', IsaacPosX, IsaacPosY, shot_range))
            Waiting_attack = Attack_speed
            
        elif keys[pygame.K_UP]:
            tire.append(Shoot('z', IsaacPosX, IsaacPosY, shot_range))
            Waiting_attack = Attack_speed
            
        elif keys[pygame.K_DOWN]:
            tire.append(Shoot('s', IsaacPosX, IsaacPosY, shot_range))
            Waiting_attack = Attack_speed

            ################TRAVEL################

    while (LeTire < len(tire) and len(tire) > 0):
        screen.blit(TearSprite, (tire[LeTire].TearPosX, tire[LeTire].TearPosY))
        if (tire[LeTire].trajectoire == 'q' and tire[LeTire].shot_range > 0):
            tire[LeTire].TearPosX -= shot_speed
            tire[LeTire].shot_range -= shot_speed
            
        if (tire[LeTire].trajectoire == 'd' and tire[LeTire].shot_range > 0):
            tire[LeTire].TearPosX += shot_speed
            tire[LeTire].shot_range -= shot_speed
                
        if (tire[LeTire].trajectoire == 'z' and tire[LeTire].shot_range > 0):
            tire[LeTire].TearPosY -= shot_speed
            tire[LeTire].shot_range -= shot_speed
            
        if (tire[LeTire].trajectoire == 's' and tire[LeTire].shot_range > 0):
            tire[LeTire].TearPosY += shot_speed
            tire[LeTire].shot_range -= shot_speed
            
        if (tire[LeTire].shot_range < shot_speed):
            del tire[LeTire]
        LeTire += 1
    LeTire = 0
    if (Waiting_attack > 0):
        Waiting_attack -= 1
        
        
###########################################################################

    # we update the screen at every frame
    pygame.display.flip()
    # if we put the frame rate at 60 the sprite will move slower
    clock.tick(120)
 
pygame.quit()