#Simple Animation with PyGame, Tamia Ogletree, 01-6-22, 2:15pm, v0.1
 
 import pygame,sys, time
 from pygame.locals import

 # Setup Pygame 
pygame.init()

# Setup window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowsurface = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

