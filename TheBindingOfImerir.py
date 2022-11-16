import pygame
from pygame.locals import *
import random
import time
import sys
from button import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
def rot_center(image, angle):
    
    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

def KeyboardInput():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        if (player.rect.x > (0 + PLAYER_SPEED)):   
            player.rect.x -= PLAYER_SPEED
        elif (player.rect.x > 0 and player.rect.x < PLAYER_SPEED):   
            player.rect.x = 0

    if keys[pygame.K_d]:
        if (player.rect.x < (screen_width - PLAYER_SPEED - player.image.get_width())):   
            player.rect.x += PLAYER_SPEED
        elif (player.rect.x < screen_width and player.rect.x > (screen_width - PLAYER_SPEED - player.image.get_width())):   
            player.rect.x = screen_width

    if keys[pygame.K_z]:
        if (player.rect.y > (0 + PLAYER_SPEED)):   
            player.rect.y -= PLAYER_SPEED
        elif (player.rect.y > 0 and player.rect.y < PLAYER_SPEED):   
            player.rect.y = 0

    if keys[pygame.K_s]:
        if (player.rect.y < (screen_height - PLAYER_SPEED - player.image.get_height())):   
            player.rect.y += PLAYER_SPEED
        elif (player.rect.y < screen_height and player.rect.y > (screen_height - PLAYER_SPEED)):   
            player.rect.y = screen_height + player.image.get_height()
    
    if keys[pygame.K_LEFT]: 
            tears = Tears(SHOT_LEFT) 
            #tears.rect.x -= PLAYER_SHOOT_VELOCITY
            tears_list.add(tears)
            pygame.time.set_timer(COULDOWN,PLAYER_SHOOT_SPEED)

    elif keys[pygame.K_RIGHT]:
            tears = Tears(SHOT_RIGHT)
            #tears.rect.x += PLAYER_SHOOT_VELOCITY
            tears_list.add(tears)
            pygame.time.set_timer(COULDOWN,PLAYER_SHOOT_SPEED)

    elif keys[pygame.K_UP]:
        tears = Tears(SHOT_UP)
        #tears.rect.y -= PLAYER_SHOOT_VELOCITY
        tears_list.add(tears)
        pygame.time.set_timer(COULDOWN,PLAYER_SHOOT_SPEED)

    elif keys[pygame.K_DOWN]:
        tears = Tears(SHOT_DOWN)
        #tears.rect.y += PLAYER_SHOOT_VELOCITY
        tears_list.add(tears)
        pygame.time.set_timer(COULDOWN,PLAYER_SHOOT_SPEED)

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, image):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Load the image
        self.image = pygame.image.load(image).convert_alpha()
        # Set our transparent color
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

class Tears(pygame.sprite.Sprite):

    shot_range = 0
    trajectoire = 0


    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, direction):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Load the image
        self.image = pygame.image.load("Sprite/tears.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PLAYER_DAMAGE * 10, PLAYER_DAMAGE * 10))
        rot_center(self.image, direction)
        # Set our transparent color
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        all_sprites_list.add(self)
        self.trajectoire = direction
        self.shot_range = PLAYER_SHOOT_RANGE

    def update(self):
        if (self.trajectoire == SHOT_LEFT and self.shot_range > 0):
            self.rect.x -= PLAYER_SHOOT_SPEED
            self.shot_range -= PLAYER_SHOOT_SPEED
            
        if (self.trajectoire == SHOT_RIGHT and self.shot_range > 0):
            self.rect.x += PLAYER_SHOOT_SPEED
            self.shot_range -= PLAYER_SHOOT_SPEED
            
        if (self.trajectoire == SHOT_UP and self.shot_range > 0):
            self.rect.y -= PLAYER_SHOOT_SPEED
            self.shot_range -= PLAYER_SHOOT_SPEED
            
        if (self.trajectoire == SHOT_DOWN and self.shot_range > 0):
            self.rect.y += PLAYER_SHOOT_SPEED
            self.shot_range -= PLAYER_SHOOT_SPEED
            
        if (self.shot_range < PLAYER_SHOOT_SPEED):
            self.kill()
            

class Player(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, image):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Load the image
        self.image = pygame.image.load(image).convert_alpha()
        # Set our transparent color
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def options():
    global screen_height
    global screen_width
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(screen_width/2, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)


        AFFICHAGE_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(screen_width/2, screen_height/2 - 150), 
            text_input="Affichage", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(screen_width/2, screen_height/2),
            text_input="Sons", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        CONTROLS_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(screen_width/2, screen_height/2 + 150), 
            text_input="Controls", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(screen_width/2, screen_height/2 + 300), 
            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for button in [AFFICHAGE_BUTTON, SONS_BUTTON, CONTROLS_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AFFICHAGE_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    menu_affichage()
                if SONS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    menu_sons()
                if CONTROLS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    menu_controls()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return 0
                    #main_menu()

        pygame.display.update()

def menu_affichage():
    global screen_height
    global screen_width
    global FULLSCREEN
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the AFFICHAGE_SETTINGS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(screen_width/2, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)


        FULLSCREEN_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(screen_width/2, screen_height/2 - 150), 
            text_input="FULLSCREEN", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SD_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(screen_width/2, screen_height/2),
            text_input="720p", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        HD_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(screen_width/2, screen_height/2 + 150), 
            text_input="1080p", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(screen_width/2, screen_height/2 + 300), 
            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS) 
        OPTIONS_BACK.update(screen)

        for button in [FULLSCREEN_BUTTON, SD_BUTTON, HD_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FULLSCREEN_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.display.toggle_fullscreen()
                if SD_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    screen_width = 1080
                    screen_height = 720
                    pygame.display.set_mode((screen_width, screen_height))

                if HD_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    screen_width = 1920
                    screen_height = 1080
                    pygame.display.set_mode((screen_width, screen_height))

                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return 0
                    #main_menu()

        pygame.display.update()

def menu_sons():
    global screen_height
    global screen_width
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the SOUNDS_SETTINGS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(screen_width/2, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)


        MODIFIER4 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(screen_width/2, screen_height/2 - 150), 
            text_input="MODIFIER4", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MODIFIER5 = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(screen_width/2, screen_height/2),
            text_input="MODIFIER5", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MODIFIER6 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(screen_width/2, screen_height/2 + 150), 
            text_input="MODIFIER6", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(screen_width/2, screen_height/2 + 300), 
            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for button in [MODIFIER4, MODIFIER5, MODIFIER6]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MODIFIER4.checkForInput(OPTIONS_MOUSE_POS):
                    print("en developement")
                if MODIFIER5.checkForInput(OPTIONS_MOUSE_POS):
                    print("en developement")
                if MODIFIER6.checkForInput(OPTIONS_MOUSE_POS):
                    print("en developement")
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return 0
                    #main_menu()

        pygame.display.update()

def menu_controls():
    global screen_height
    global screen_width
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the CONTROLS_SETTINGS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(screen_width/2, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)


        MODIFIER1 = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(screen_width/2, screen_height/2 - 150), 
            text_input="MODIFIER1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MODIFIER2 = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(screen_width/2, screen_height/2),
            text_input="MODIFIER2", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MODIFIER3 = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(screen_width/2, screen_height/2 + 150), 
            text_input="MODIFIER3", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(screen_width/2, screen_height/2 + 300), 
            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for button in [MODIFIER1, MODIFIER2, MODIFIER3]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MODIFIER1.checkForInput(OPTIONS_MOUSE_POS):
                    print("en developement")
                if MODIFIER2.checkForInput(OPTIONS_MOUSE_POS):
                    print("en developement")
                if MODIFIER3.checkForInput(OPTIONS_MOUSE_POS):
                    print("en developement")
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return 0
                    #main_menu()

        pygame.display.update()


def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("The Binding Of Imerir", True, "#ED0010")
        MENU_RECT = MENU_TEXT.get_rect(center=(screen_width/2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(screen_width/2, screen_height/2 - 150), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(screen_width/2, screen_height/2),
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(screen_width/2, screen_height/2 + 150), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return 0
                elif OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()




isaac_pp="Sprite/isaac.png"
nino_pp="Sprite/nino.png"

PLAYER_HEALTH = 30
PLAYER_DAMAGE = 5
PLAYER_SPEED = 5
PLAYER_SHOOT_SPEED = 5
PLAYER_SHOOT_RANGE = 1000
PLAYER_SHOOT_VELOCITY = 10
PLAYER_LUCK = 5
PLAYER_DEVIL = 0
PLAYER_ANGEL = 0

FULLSCREEN = 0

SHOT_UP = 90
SHOT_RIGHT = 0
SHOT_LEFT = 180
SHOT_DOWN = 270


pygame.init()
pygame.mixer.init()
pygame.display.init()


# Set the height and width of the screen
screen_width = 1080
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg").convert_alpha()
pygame.transform.scale(BG, (screen_width, screen_height))

if(FULLSCREEN == 1):
    pygame.display.toggle_fullscreen()

# This is a list of 'sprites.' Each block in the program is
# added to this list.
# The list is managed by a class called 'Group.'

main_menu()

BG = pygame.image.load("assets/Background.png").convert_alpha()
BG = pygame.transform.scale(BG, (screen_width, screen_height))
rect = BG.get_rect()
rect = rect.move((screen_width / 2, screen_height / 2))
screen.blit(BG, rect)

screen = pygame.display.set_mode((screen_width, screen_height))
#debut jeux 
block_list = pygame.sprite.Group()
tears_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

##########################################################
for i in range(10):
    # This represents a block
    block = Block(isaac_pp)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
##########################################################
# Create a player sprite
player = Player(nino_pp)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

COULDOWN = pygame.USEREVENT + 0


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.blit(BG, (0, 0))
    KeyboardInput()
    #if(tears_list.has(Tears) == True):
    pygame.sprite.groupcollide(tears_list ,block_list ,True ,True)
    #blocks_hit_list = pygame.sprite.spritecollide(tears, block_list, True)
        
        #for block in blocks_hit_list:
        #    score +=1
        #    print(score)
    tears_list.update()
            #pygame.mixer.music.load("miam.mp3")
            #pygame.mixer.music.play()
    all_sprites_list.draw(screen)
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()