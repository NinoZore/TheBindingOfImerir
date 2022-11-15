
import pygame
from pygame.locals import *
 
pygame.init()
clock = pygame.time.Clock()
size = 1920, 1080
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
speed = 3
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('GAME')
IsaacPosX, IsaacPosY = 960, 540
TearPosX, TearPosY = 960, 540

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load("nino.png").convert_alpha()
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
player = Player()
all_sprites_list.add(player)

IsaacSprite=pygame.image.load('nino.png')
TearSprite=pygame.image.load('tacos.png')
loop = True
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
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        IsaacPosX -= speed
    if keys[pygame.K_d]:
        IsaacPosX += speed
    if keys[pygame.K_z]:
        IsaacPosY -= speed
    if keys[pygame.K_s]:
        IsaacPosY += speed

    if keys[pygame.K_LEFT]:
        TearPosX = IsaacPosX
        TearPosY = IsaacPosY
        screen.blit(TearSprite,(TearPosX,TearPosY))
        #for i in range(5):
        #    TearPosX -= speed
    if keys[pygame.K_RIGHT]:
        TearPosX = IsaacPosX
        TearPosY = IsaacPosY
        screen.blit(TearSprite,(TearPosX,TearPosY))

    if keys[pygame.K_UP]:

        # Fire a bullet if the user clicks the mouse button
        bullet = Bullet()
        # Set the bullet so it is where the player is
        bullet.rect.x = player.rect.x
        bullet.rect.y = player.rect.y
        # Add the bullet to the lists
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)

    if keys[pygame.K_DOWN]:
        TearPosX = IsaacPosX
        TearPosY = IsaacPosY
        screen.blit(TearSprite,(TearPosX,TearPosY))

        # --- Game logic
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


    # we update the screen at every frame
    pygame.display.flip()
    # if we put the frame rate at 60 the sprite will move slower
    clock.tick(120)
 
pygame.quit()




 
