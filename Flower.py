#pygame flowers!
#draws a simple flower made of basic shapes to a game window

import pygame #gaming module (aka library)
import random
pygame.init() #initializes Pygame
pygame.display.set_caption("flowers!") #sets the window title
screen = pygame.display.set_mode((800, 800)) #creates game screen
screen.fill((0, 0, 0)) #paint background black


def draw_flower(screen, x, y, color1, color2):
    pygame.draw.rect(screen, (GREEN), (190, 220, 20, 100)) #(190, 330) is my top left corner (stem)
    pygame.draw.circle(screen, (RED), (180, 220), 20)#pedal
    pygame.draw.circle(screen, (RED), (180, 180), 20)#pedal
    pygame.draw.circle(screen, (RED), (220, 220), 20)#pedal
    pygame.draw.circle(screen, (RED), (220, 180), 20)#pedal
    pygame.draw.circle(screen, (ORANGE), (200, 200), 20)#center





#set up some colors
RED = (250,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)

draw_flower(screen, 190, 220, (252, 0, 0), (200, 100, 0))
draw_flower(screen, 200, 200, (0, 0, 255), (255, 255, 0))


pygame.display.flip() #this flips all those shapes onto the game screen (needed for every game)


