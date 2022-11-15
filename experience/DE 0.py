import pygame
import random
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def rot_center(image, angle):
    
    loc = image.get_rect().center  #rot_image is not defined 
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite
    
    # or return tuple: (Surface, Rect)
    # return rot_sprite, rot_sprite.get_rect()

def update(self):
    """ Called each frame. """
 
    # Move block down one pixel
    self.rect.y += 1

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

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, direction):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Load the image
        self.image = pygame.image.load("tears.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PLAYER_DAMAGE * 10, PLAYER_DAMAGE * 10))
        rot_center(self.image, direction)
        # Set our transparent color
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        all_sprites_list.add(self)

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

mob_pp="isaac.png"
nino_pp="nino.png"

PLAYER_DAMAGE = 5
PLAYER_SPEED = 5
PLAYER_SHOOT_SPEED = 5
PLAYER_SHOOT_RANGE = 20
PLAYER_SHOOT_VELOCITY = 5

pygame.init()
pygame.mixer.init()

# Set the height and width of the screen
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list.
# The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(10):
    # This represents a block
    block = Block(mob_pp)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Player(nino_pp)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        player.rect.x -= PLAYER_SPEED

    if keys[pygame.K_d]:
        player.rect.x += PLAYER_SPEED

    if keys[pygame.K_z]:
        player.rect.y -= PLAYER_SPEED

    if keys[pygame.K_s]:
        player.rect.y += PLAYER_SPEED

    if keys[pygame.K_LEFT]: 
        tears = Tears(180) 
        tears.rect.x -= PLAYER_SHOOT_VELOCITY

    if keys[pygame.K_RIGHT]:
        tears = Tears(0)
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY
        tears.rect.x += PLAYER_SHOOT_VELOCITY

    if keys[pygame.K_UP]:
        tears = Tears(90)
        tears.rect.y -= PLAYER_SHOOT_VELOCITY

    if keys[pygame.K_DOWN]:
        tears = Tears(270)
        tears.rect.y += PLAYER_SHOOT_VELOCITY
        
    if(pygame.sprite.Group.has(Tears) == True):
        blocks_hit_list = pygame.sprite.spritecollide(tears, block_list, True)
        for block in blocks_hit_list:
            score +=1
            print(score)
            #pygame.mixer.music.load("miam.mp3")
            #pygame.mixer.music.play()
    all_sprites_list.draw(screen)
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()