import pygame
from hero import Hero, Enemy, Bullet
from Door import DOOR

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

class LVL_1():

    def __init__(self,width = 1250,height = 800, doors = 0):
        
        self.doors_list = pygame.sprite.Group()
        
        if doors == 1:
            top_door = DOOR(100,5)                 
            top_door.rect.x = SCREEN_WIDTH/2 - 50
            top_door.rect.y = 0
            self.doors_list.add(top_door)

        
