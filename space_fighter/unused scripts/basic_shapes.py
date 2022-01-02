import pygame
import sys
from pygame.locals import *

# init for pygame
pygame.init()

# FPS for game
FPS = 30
frame_per_sec = pygame.time.Clock()

# Color objects
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# setting up canvas 
Display_surface = pygame.display.set_mode((500,500))
Display_surface.fill(black)
pygame.display.set_caption("basic_shapes")

# Drawing shapes on canvas 

# house rect
# pygame.draw.line(Display_surface, white, (125, 300), (375, 300))
# pygame.draw.line(Display_surface, white, (125, 150), (375, 150))
# pygame.draw.line(Display_surface, white, (125, 150), (125, 300))
# pygame.draw.line(Display_surface, white, (375, 150), (375, 300))

pygame.draw.rect(Display_surface, white, (125, 150, 250, 150), 1)

# door
# pygame.draw.line(Display_surface, white, (225, 300), (275 ,300))
# pygame.draw.line(Display_surface, white, (225, 200), (225, 300))
# pygame.draw.line(Display_surface, white, (275, 200), (275, 300))
# pygame.draw.line(Display_surface, white, (225, 200), (275, 200))

pygame.draw.rect(Display_surface, white, (225, 200, 50, 100), 1)
# roof
pygame.draw.line(Display_surface, white, (125, 150), (250, 50))
pygame.draw.line(Display_surface, white, (375, 150), (250, 50))

#door knob
pygame.draw.circle(Display_surface, white, (231, 250), 2)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    frame_per_sec.tick(FPS) 