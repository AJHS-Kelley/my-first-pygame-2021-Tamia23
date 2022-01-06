#Simple Animation with PyGame, Tamia Ogletree, 01-6-22, 2:39pm, v0.3
 
 from _typeshed import ReadableBuffer
import pygame,sys, time
 from pygame.locals import

 # Setup Pygame 
pygame.init()

# Setup window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowsurface = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Setupcolor values.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255,0)
BLUE = (0, 0, 255)