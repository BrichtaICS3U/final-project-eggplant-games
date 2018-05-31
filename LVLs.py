import pygame
from hero import Enemy, Bullet
from Door import DOOR,  KEY
from Hole import HOLE

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
YELLOW = (255,255,0)

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
                top_door = DOOR(100,5,BLUE,1)
            elif Lock == 2:
                top_door = DOOR(100,5,RED,2)
            else:
                top_door = DOOR(100,5,WHITE)
            top_door.rect.x = 650 - 50
            top_door.rect.y = 0
            self.doors_list.add(top_door)
           

        if S == True:
            bot_door = DOOR(100,5,WHITE)
            bot_door.rect.x = 650 - 50
            bot_door.rect.y = 800 - 5
            self.doors_list.add(bot_door)

        if W == True:
            if Lock == 2:
                lt_door = DOOR(5,100,YELLOW,3)
            else:
                lt_door = DOOR(5,100,WHITE)
            lt_door.rect.x = 0
            lt_door.rect.y = 400 - 50
            self.doors_list.add(lt_door)

        if E == True:
            rt_door = DOOR(5,100,WHITE)
            rt_door.rect.x = 1250 - 5
            rt_door.rect.y = 400 - 50
            self.doors_list.add(rt_door)

        if END == True:
            E_door = DOOR(50,50,WHITE)
            E_door.rect.x = 600
            E_door.rect.y = 400
            self.doors_list.add(E_door)

# ----------------------------- this is the end of the code that will add the doors ------------------------------ #

# ----------------------------- this section of code will be for the keys that will unlock the locked doors -------------------#

        self.Key_list = pygame.sprite.Group()


        if Key == 1:
            B_Key = KEY(50,50,BLUE,1)
            B_Key.rect.x = 625
            B_Key.rect.y = 750
            self.Key_list.add(B_Key)

        if Key == 2:
            R_Key = KEY(50,50,RED,2)
            R_Key.rect.x = 600
            R_Key.rect.y = 600
            self.Key_list.add(R_Key)

        if Key == 3:
            Y_Key = KEY(50,50,YELLOW,3)
            Y_Key.rect.x = 600
            Y_Key.rect.y = 600
            self.Key_list.add(Y_Key)
            


















# ----------------------------- this dense area of code is used to create holes ---------------------------------- #

        self.hole_list = pygame.sprite.Group()
        
        if Holes == 1:
            
            h1_1 = HOLE(250,800,WHITE)
            h1_1.rect.x = 0
            h1_1.rect.y = 0
            self.hole_list.add(h1_1)

            h1_2 = HOLE(250,800,WHITE)
            h1_2.rect.x = 1000
            h1_2.rect.y = 0
            self.hole_list.add(h1_2)
            
            h1_3 = HOLE(750,150,WHITE)
            h1_3.rect.x = 250
            h1_3.rect.y = 650
            self.hole_list.add(h1_3)

            h1_4 = HOLE(50,50,WHITE)
            h1_4.rect.x = 300
            h1_4.rect.y = 50
            self.hole_list.add(h1_4)

            h1_5 = HOLE(100,100,WHITE)
            h1_5.rect.x = 350
            h1_5.rect.y = 150
            self.hole_list.add(h1_5)

        if Holes == 2:
            h2_1 = HOLE(50,800,WHITE)
            h2_1.rect.x = 400
            h2_1.rect.y = 0
            self.hole_list.add(h2_1)

            h2_2 = HOLE(50,800,WHITE)
            h2_2.rect.x = 850
            h2_2.rect.y = 0
            self.hole_list.add(h2_2)
            
        
            
            

         
            
            
            
        
            


    def draw(self,screen):
        """this is the function that will draw everything once i tell it to in the code"""
        self.doors_list.draw(screen)
        self.hole_list.draw(screen)
        self.Key_list.draw(screen)

        
