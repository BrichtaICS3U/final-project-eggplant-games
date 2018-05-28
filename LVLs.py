import pygame
from hero import Enemy, Bullet
from Door import DOOR,  KEY
from Hole import HOLE

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

draw = True

class LVL():

    def __init__(self, doors = 0, Holes = 0, Lock = 0, Key = 0):
        global draw


# --------------------- this dense area of code is used to create and add the doors to the object -------------------- #        
        self.doors_list = pygame.sprite.Group()

        N = False
        S = False
        E = False
        W = False
        END = False
        
        if doors == 1:
            N = True
        elif doors == 2:
            W = True
        elif doors == 3:
            N = True
            W = True
        elif doors == 4:
            E = True
        elif doors == 5:
            N = True
            E = True
        elif doors == 6:
            E = True
            W = True
        elif doors == 7:
            S = True
        elif doors == 8:
            N = True
            S = True
        elif doors == 9:
            S = True
            W = True
        elif doors == 10:
            S = True
            E = True
        elif doors == 20:
            W = True
            S = True
            N = True
        elif doors == 30:
            W = True
            S = True
            E = True
        elif doors == 40:
            W = True
            E = True
            N = True
        elif doors == 100:
            N = True
            S = True
            W = True
            E = True
        elif doors == 2571:
            END = True
                    
        if N == True:
            if Lock == 1:
                top_door = DOOR(100,5,BLUE)
            else:
                top_door = DOOR(100,5)
            top_door.rect.x = 625 - 50
            top_door.rect.y = 0
            self.doors_list.add(top_door)
           

        if S == True:
            bot_door = DOOR(100,5)
            bot_door.rect.x = 625 - 50
            bot_door.rect.y = 800 - 5
            self.doors_list.add(bot_door)

        if W == True:
            lt_door = DOOR(5,100)
            lt_door.rect.x = 0
            lt_door.rect.y = 400 - 50
            self.doors_list.add(lt_door)

        if E == True:
            rt_door = DOOR(5,100)
            rt_door.rect.x = 1250 - 5
            rt_door.rect.y = 400 - 50
            self.doors_list.add(rt_door)

        if END == True:
            E_door = DOOR(50,50)
            E_door.rect.x = 600
            E_door.rect.y = 400
            self.doors_list.add(E_door)

# ----------------------------- this is the end of the code that will add the doors ------------------------------ #

# ----------------------------- this section of code will be for the keys that will unlock the locked doors -------------------#

        self.Key_list = pygame.sprite.Group()


        if Key == 1:
            B_Key = KEY(5,7,BLUE)
            B_Key.rect.x = 600
            B_Key.rect.y = 600
            self.Key_list.add(B_Key)
            


















# ----------------------------- this dense area of code is used to create holes ---------------------------------- #

        self.hole_list = pygame.sprite.Group()
        

            
            

         
            
            
            
        
            


    def draw(self,screen):
        """this is the function that will draw everything once i tell it to in the code"""
        self.doors_list.draw(screen)
        self.hole_list.draw(screen)
        self.Key_list.draw(screen)

        
