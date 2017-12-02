import pygame
import sys
from pygame.locals import *

pygame.init()
display_surf = pygame.display.set_mode((400,400))
pygame.display.set_caption('hello world!')
img = pygame.image.load('kl.png')
x,y = 10,10
FPS = 60
direction = 'right'

while True:
    display_surf.fill((255,255,255))
    if direction == 'right':
        x+=1
        if x > 380:
            direction = "down"
    elif direction == 'down':
        y += 1
        if y > 380:
            direction = 'left'
    elif direction == 'left':
        x-=1
        if x <10:
            direction = 'up'
    elif direction == 'up':
        y-=1
        if y <10:
            direction = 'right'
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surf.blit(img,(x,y))
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
