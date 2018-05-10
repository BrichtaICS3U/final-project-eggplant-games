import pygame
from hero import Hero, Enemy, Bullet
from Door import DOOR

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

class LVL():

    def __init__(self, doors = 0):
        
        self.doors_list = pygame.sprite.Group()
        
        if doors == 1:
            top_door = DOOR(100,5)                 
            top_door.rect.x = 625 - 50
            top_door.rect.y = 0
            self.doors_list.add(top_door)

        if doors == 2:
            bot_door = DOOR(100,5)
            bot_door.rect.x = 625 - 50
            bot_door.rect.y = 800 - 5
            self.doors_list.add(bot_door)

    def draw(self,screen):
        self.doors_list.draw(screen)
        
