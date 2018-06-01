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
            B_Key.rect.y = 700
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

        if Holes == 3:
            
            h3_1 = HOLE(50,250,WHITE)
            h3_1.rect.x = 450
            h3_1.rect.y = 0
            self.hole_list.add(h3_1)

            h3_2 = HOLE(50,250,WHITE)
            h3_2.rect.x = 800
            h3_2.rect.y = 0
            self.hole_list.add(h3_2)

            h3_3 = HOLE(50,250,WHITE)
            h3_3.rect.x = 450
            h3_3.rect.y = 550
            self.hole_list.add(h3_3)

            h3_5 = HOLE(50,250,WHITE)
            h3_5.rect.x = 800
            h3_5.rect.y = 550
            self.hole_list.add(h3_5)

            h3_6 = HOLE(400,50,WHITE)
            h3_6.rect.x = 850
            h3_6.rect.y = 500
            self.hole_list.add(h3_6)

            h3_7 = HOLE(450,50,WHITE)
            h3_7.rect.x = 0
            h3_7.rect.y = 500
            self.hole_list.add(h3_7)

            h3_8 = HOLE(450,50,WHITE)
            h3_8.rect.x = 0
            h3_8.rect.y = 250
            self.hole_list.add(h3_8)

            h3_4 = HOLE(450,50,WHITE)
            h3_4.rect.x = 850
            h3_4.rect.y = 250
            self.hole_list.add(h3_4)

            h3_5 = HOLE(100,100,WHITE)
            h3_5.rect.x = 600
            h3_5.rect.y = 350
            self.hole_list.add(h3_5)

        if Holes == 5:
    #top part

            h5_1 = HOLE(50,50,WHITE)
            h5_1.rect.x = 0
            h5_1.rect.y = 200
            self.hole_list.add(h5_1)

            h5_2 = HOLE(300,50,WHITE)
            h5_2.rect.x = 50
            h5_2.rect.y = 150
            self.hole_list.add(h5_2)

            h5_3 = HOLE(100,50,WHITE)
            h5_3.rect.x = 350
            h5_3.rect.y = 200
            self.hole_list.add(h5_3)

            h5_4 = HOLE(100,50,WHITE)
            h5_4.rect.x = 450
            h5_4.rect.y = 150
            self.hole_list.add(h5_4)

            h5_5 = HOLE(100,50,WHITE)
            h5_5.rect.x = 500
            h5_5.rect.y = 200
            self.hole_list.add(h5_5)

            h5_6 = HOLE(250,50,WHITE)
            h5_6.rect.x = 600
            h5_6.rect.y = 150
            self.hole_list.add(h5_6)

            h5_7 = HOLE(100,50,WHITE)
            h5_7.rect.x = 850
            h5_7.rect.y = 200
            self.hole_list.add(h5_7)

            h5_8 = HOLE(100,50,WHITE)
            h5_8.rect.x = 950
            h5_8.rect.y = 150
            self.hole_list.add(h5_8)

            h5_9 = HOLE(150,50,WHITE)
            h5_9.rect.x = 1050
            h5_9.rect.y = 200
            self.hole_list.add(h5_9)

            h5_10 = HOLE(50,50,WHITE)
            h5_10.rect.x = 1200
            h5_10.rect.y = 150
            self.hole_list.add(h5_10)

    #bottom part

            h5_11 = HOLE(350,50,WHITE)
            h5_11.rect.x = 0
            h5_11.rect.y = 600
            self.hole_list.add(h5_11)

            h5_12 = HOLE(50,50,WHITE)
            h5_12.rect.x = 350
            h5_12.rect.y = 650
            self.hole_list.add(h5_12)

            h5_13 = HOLE(100,50,WHITE)
            h5_13.rect.x = 400
            h5_13.rect.y = 600
            self.hole_list.add(h5_13)

            h5_14 = HOLE(100,50,WHITE)
            h5_14.rect.x = 500
            h5_14.rect.y = 650
            self.hole_list.add(h5_14)

            h5_15 = HOLE(150,50,WHITE)
            h5_15.rect.x = 600
            h5_15.rect.y = 600
            self.hole_list.add(h5_15)

            h5_16 = HOLE(150,50,WHITE)
            h5_16.rect.x = 750
            h5_16.rect.y = 650
            self.hole_list.add(h5_16)

            h5_17 = HOLE(250,50,WHITE)
            h5_17.rect.x = 900
            h5_17.rect.y = 600
            self.hole_list.add(h5_17)
            
            h5_18 = HOLE(100,50,WHITE)
            h5_18.rect.x = 1150
            h5_18.rect.y = 650
            self.hole_list.add(h5_18)

            


        if Holes == 6:

            h6_1 = HOLE(50,650,WHITE)
            h6_1.rect.x = 350
            h6_1.rect.y = 150
            self.hole_list.add(h6_1)

            h6_2 = HOLE(50,250,WHITE)
            h6_2.rect.x = 800
            h6_2.rect.y = 550
            self.hole_list.add(h6_2)

            h6_3 = HOLE(850,50,WHITE)
            h6_3.rect.x = 400
            h6_3.rect.y = 150
            self.hole_list.add(h6_3)

            h6_4 = HOLE(400,50,WHITE)
            h6_4.rect.x = 850
            h6_4.rect.y = 550
            self.hole_list.add(h6_4)


            
            
        if Holes == 8:

            h8_1 = HOLE(50,800,WHITE)
            h8_1.rect.x = 550
            h8_1.rect.y = 0
            self.hole_list.add(h8_1)

            h8_2 = HOLE(50,800,WHITE)
            h8_2.rect.x = 700
            h8_2.rect.y = 0
            self.hole_list.add(h8_2)
        
            
            

         
            
            
            
        
            


    def draw(self,screen):
        """this is the function that will draw everything once i tell it to in the code"""
        self.doors_list.draw(screen)
        self.hole_list.draw(screen)
        self.Key_list.draw(screen)

        
