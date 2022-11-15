import pygame,time,sys

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
print ("Mixer settings", pygame.mixer.get_init())
print ("Mixer channels", pygame.mixer.get_num_channels())
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.load("miam.mp3")
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
   clock.tick(30)