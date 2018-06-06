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
                top_door = DOOR(100,6,BLUE,1)
            elif Lock == 2:
                top_door = DOOR(100,6,RED,2)
            else:

                top_door = DOOR(100,6,WHITE)
            top_door.rect.x = 650 - 50
            top_door.rect.y = 0
            self.doors_list.add(top_door)
           

        if S == True:

            bot_door = DOOR(100,6,WHITE)

            bot_door.rect.x = 650 - 50
            bot_door.rect.y = 800 - 5
            self.doors_list.add(bot_door)

        if W == True:
            if Lock == 2:
                lt_door = DOOR(6,100,YELLOW,3)
            else:
                lt_door = DOOR(6,100,WHITE)
            lt_door.rect.x = 0
            lt_door.rect.y = 400 - 50
            self.doors_list.add(lt_door)

        if E == True:
            rt_door = DOOR(6,100,WHITE)
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
            B_Key.rect.y = 730
            self.Key_list.add(B_Key)

        if Key == 2:
            R_Key = KEY(50,50,RED,2)
            R_Key.rect.x = 550
            R_Key.rect.y = 375
            self.Key_list.add(R_Key)


        if Key == 3:
            Y_Key = KEY(50,50,YELLOW,3)
            Y_Key.rect.x = 1175
            Y_Key.rect.y = 425
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
            

        if Holes == 7:

            h7_1 = HOLE(50,700,WHITE)
            h7_1.rect.x = 150
            h7_1.rect.y = 0
            self.hole_list.add(h7_1)

            h7_3 = HOLE(50,50,WHITE)
            h7_3.rect.x = 200
            h7_3.rect.y = 700
            self.hole_list.add(h7_3)

            h7_4 = HOLE(50,50,WHITE)
            h7_4.rect.x = 250
            h7_4.rect.y = 750
            self.hole_list.add(h7_4)


            h7_2 = HOLE(50,650,WHITE)
            h7_2.rect.x = 1100
            h7_2.rect.y = 0
            self.hole_list.add(h7_2)

            h7_5 = HOLE(50,50,WHITE)
            h7_5.rect.x = 1050
            h7_5.rect.y = 650
            self.hole_list.add(h7_5)

            h7_6 = HOLE(50,50,WHITE)
            h7_6.rect.x = 1000
            h7_6.rect.y = 700
            self.hole_list.add(h7_6)

            h7_7 = HOLE(50,50,WHITE)
            h7_7.rect.x = 950
            h7_7.rect.y = 750
            self.hole_list.add(h7_7)

            h7_8 = HOLE(200,50,WHITE)
            h7_8.rect.x = 550
            h7_8.rect.y = 250
            self.hole_list.add(h7_8)

            h7_9 = HOLE(200,50,WHITE)
            h7_9.rect.x = 550
            h7_9.rect.y = 500
            self.hole_list.add(h7_9)

            h7_10 = HOLE(50,200,WHITE)
            h7_10.rect.x = 500
            h7_10.rect.y = 300
            self.hole_list.add(h7_10)

            h7_11 = HOLE(50,200,WHITE)
            h7_11.rect.x = 750
            h7_11.rect.y = 300
            self.hole_list.add(h7_11)

            

            
            


            
            
        if Holes == 8:

            h8_1 = HOLE(50,800,WHITE)
            h8_1.rect.x = 500
            h8_1.rect.y = 0
            self.hole_list.add(h8_1)

            h8_2 = HOLE(50,800,WHITE)
            h8_2.rect.x = 750
            h8_2.rect.y = 0
            self.hole_list.add(h8_2)
            

        if Holes == 10:
            h9_1 = HOLE(50,50,WHITE)
            h9_1.rect.x = 0
            h9_1.rect.y = 550
            self.hole_list.add(h9_1)

            h9_2 = HOLE(50,50,WHITE)
            h9_2.rect.x = 50
            h9_2.rect.y = 600
            self.hole_list.add(h9_2)

            h9_3 = HOLE(50,50,WHITE)
            h9_3.rect.x = 100
            h9_3.rect.y = 650
            self.hole_list.add(h9_3)

            h9_4 = HOLE(50,50,WHITE)
            h9_4.rect.x = 150
            h9_4.rect.y = 700
            self.hole_list.add(h9_4)

            h9_5 = HOLE(50,50,WHITE)
            h9_5.rect.x = 200
            h9_5.rect.y = 750
            self.hole_list.add(h9_5)

            h9_6 = HOLE(50,50,WHITE)
            h9_6.rect.x = 1000
            h9_6.rect.y = 750
            self.hole_list.add(h9_6)

            h9_7 = HOLE(50,50,WHITE)
            h9_7.rect.x = 1050
            h9_7.rect.y = 700
            self.hole_list.add(h9_7)

            h9_8 = HOLE(50,50,WHITE)
            h9_8.rect.x = 1100
            h9_8.rect.y = 650
            self.hole_list.add(h9_8)

            h9_9 = HOLE(50,50,WHITE)
            h9_9.rect.x = 1150
            h9_9.rect.y = 600
            self.hole_list.add(h9_9)
            
            h9_10 = HOLE(50,50,WHITE)
            h9_10.rect.x = 1200
            h9_10.rect.y = 550
            self.hole_list.add(h9_10)

            h9_11 = HOLE(50,50,WHITE)
            h9_11.rect.x = 0
            h9_11.rect.y = 200
            self.hole_list.add(h9_11)

            h9_12 = HOLE(50,50,WHITE)
            h9_12.rect.x = 50
            h9_12.rect.y = 150
            self.hole_list.add(h9_12)

            h9_13 = HOLE(50,50,WHITE)
            h9_13.rect.x = 100
            h9_13.rect.y = 100
            self.hole_list.add(h9_13)

            h9_14 = HOLE(50,50,WHITE)
            h9_14.rect.x = 150
            h9_14.rect.y = 50
            self.hole_list.add(h9_14)

            h9_15 = HOLE(50,50,WHITE)
            h9_15.rect.x = 200
            h9_15.rect.y = 0
            self.hole_list.add(h9_15)

            h9_16 = HOLE(50,50,WHITE)
            h9_16.rect.x = 1000
            h9_16.rect.y = 0
            self.hole_list.add(h9_16)

            h9_17 = HOLE(50,50,WHITE)
            h9_17.rect.x = 1050
            h9_17.rect.y = 50
            self.hole_list.add(h9_17)

            h9_18 = HOLE(50,50,WHITE)
            h9_18.rect.x = 1100
            h9_18.rect.y = 100
            self.hole_list.add(h9_18)

            h9_19 = HOLE(50,50,WHITE)
            h9_19.rect.x = 1150
            h9_19.rect.y = 150
            self.hole_list.add(h9_19)
            
            h9_20 = HOLE(50,50,WHITE)
            h9_20.rect.x = 1200
            h9_20.rect.y = 200
            self.hole_list.add(h9_20)

        if Holes == 11:
            
            h11_1 = HOLE(50,250,WHITE)
            h11_1.rect.x = 0
            h11_1.rect.y = 550
            self.hole_list.add(h11_1)

            h11_2 = HOLE(50,250,WHITE)
            h11_2.rect.x = 0
            h11_2.rect.y = 0
            self.hole_list.add(h11_2)

            h11_3 = HOLE(50,300,WHITE)
            h11_3.rect.x = 550
            h11_3.rect.y = 0
            self.hole_list.add(h11_3)

            h11_4 = HOLE(350,50,WHITE)
            h11_4.rect.x = 600
            h11_4.rect.y = 300
            self.hole_list.add(h11_4)

            h11_5 = HOLE(350,50,WHITE)
            h11_5.rect.x = 600
            h11_5.rect.y = 450
            self.hole_list.add(h11_5)

            h11_6 = HOLE(50,300,WHITE)
            h11_6.rect.x = 550
            h11_6.rect.y = 500
            self.hole_list.add(h11_6)

            h11_7 = HOLE(300,50,WHITE)
            h11_7.rect.x = 950
            h11_7.rect.y = 250
            self.hole_list.add(h11_7)

            h11_8 = HOLE(300,50,WHITE)
            h11_8.rect.x = 950
            h11_8.rect.y = 500
            self.hole_list.add(h11_8)

            h11_9 = HOLE(100,50,WHITE)
            h11_9.rect.x = 750
            h11_9.rect.y = 350
            self.hole_list.add(h11_9)

        if Holes == 12:
            h12_1 = HOLE(150,50,WHITE)
            h12_1.rect.x = 0
            h12_1.rect.y = 250
            self.hole_list.add(h12_1)

            h12_2 = HOLE(150,50,WHITE)
            h12_2.rect.x = 0
            h12_2.rect.y = 500
            self.hole_list.add(h12_2)

            h12_3 = HOLE(100,100,WHITE)
            h12_3.rect.x = 150
            h12_3.rect.y = 450
            self.hole_list.add(h12_3)

            h12_4 = HOLE(50,100,WHITE)
            h12_4.rect.x = 0
            h12_4.rect.y = 550
            self.hole_list.add(h12_4)

            h12_5 = HOLE(300,100,WHITE)
            h12_5.rect.x = 0
            h12_5.rect.y = 650
            self.hole_list.add(h12_5)

            h12_6 = HOLE(100,50,WHITE)
            h12_6.rect.x = 300
            h12_6.rect.y = 750
            self.hole_list.add(h12_6)

            h12_7 = HOLE(450,250,WHITE)
            h12_7.rect.x = 500
            h12_7.rect.y = 450
            self.hole_list.add(h12_7)

            h12_8 = HOLE(50,100,WHITE)
            h12_8.rect.x = 350
            h12_8.rect.y = 450
            self.hole_list.add(h12_8)
            
            h12_9 = HOLE(100,200,WHITE)
            h12_9.rect.x = 400
            h12_9.rect.y = 450
            self.hole_list.add(h12_9)

            h12_10 = HOLE(50,100,WHITE)
            h12_10.rect.x = 950
            h12_10.rect.y = 600
            self.hole_list.add(h12_10)

            h12_11 = HOLE(50,100,WHITE)
            h12_11.rect.x = 500
            h12_11.rect.y = 700
            self.hole_list.add(h12_11)

            h12_12 = HOLE(300,50,WHITE)
            h12_12.rect.x = 750
            h12_12.rect.y = 750
            self.hole_list.add(h12_12)

            h12_13 = HOLE(50,200,WHITE)
            h12_13.rect.x = 1050
            h12_13.rect.y = 550
            self.hole_list.add(h12_13)

            h12_14 = HOLE(50,150,WHITE)
            h12_14.rect.x = 1000
            h12_14.rect.y = 400
            self.hole_list.add(h12_14)

            h12_15 = HOLE(450,100,WHITE)
            h12_15.rect.x = 150
            h12_15.rect.y = 250
            self.hole_list.add(h12_15)

            h12_16 = HOLE(100,50,WHITE)
            h12_16.rect.x = 450
            h12_16.rect.y = 350
            self.hole_list.add(h12_16)

            h12_17 = HOLE(50,150,WHITE)
            h12_17.rect.x = 700
            h12_17.rect.y = 250
            self.hole_list.add(h12_17)

            h12_18 = HOLE(150,100,WHITE)
            h12_18.rect.x = 750
            h12_18.rect.y = 250
            self.hole_list.add(h12_18)

            h12_19 = HOLE(50,50,WHITE)
            h12_19.rect.x = 800
            h12_19.rect.y = 400
            self.hole_list.add(h12_19)

            h12_20 = HOLE(100,50,WHITE)
            h12_20.rect.x = 900
            h12_20.rect.y = 350
            self.hole_list.add(h12_20)

            h12_21 = HOLE(50,250,WHITE)
            h12_21.rect.x = 350
            h12_21.rect.y = 0
            self.hole_list.add(h12_21)

            h12_22 = HOLE(50,100,WHITE)
            h12_22.rect.x = 750
            h12_22.rect.y = 0
            self.hole_list.add(h12_22)

            h12_23 = HOLE(350,50,WHITE)
            h12_23.rect.x = 450
            h12_23.rect.y = 100
            self.hole_list.add(h12_23)
            

        if Holes == 13:
            
            h13_1 = HOLE(150,50,WHITE)
            h13_1.rect.x = 0
            h13_1.rect.y = 300
            self.hole_list.add(h13_1)

            h13_2 = HOLE(150,50,WHITE)
            h13_2.rect.x = 0
            h13_2.rect.y = 550
            self.hole_list.add(h13_2)

            h13_3 = HOLE(50,100,WHITE)
            h13_3.rect.x = 250
            h13_3.rect.y = 400
            self.hole_list.add(h13_3)

            h13_4 = HOLE(50,50,WHITE)
            h13_4.rect.x = 450
            h13_4.rect.y = 400
            self.hole_list.add(h13_4)

            h13_5 = HOLE(1100,50,WHITE)
            h13_5.rect.x = 0
            h13_5.rect.y = 350
            self.hole_list.add(h13_5)

            h13_6 = HOLE(400,50,WHITE)
            h13_6.rect.x = 150
            h13_6.rect.y = 500
            self.hole_list.add(h13_6)

            h13_7 = HOLE(350,50,WHITE)
            h13_7.rect.x = 750
            h13_7.rect.y = 500
            self.hole_list.add(h13_7)

            h13_8 = HOLE(50,250,WHITE)
            h13_8.rect.x = 500
            h13_8.rect.y = 550
            self.hole_list.add(h13_8)

            h13_9 = HOLE(50,250,WHITE)
            h13_9.rect.x = 750
            h13_9.rect.y = 550
            self.hole_list.add(h13_9)

            h13_10 = HOLE(150,50,WHITE)
            h13_10.rect.x = 1100
            h13_10.rect.y = 550
            self.hole_list.add(h13_10)

            h13_11 = HOLE(150,50,WHITE)
            h13_11.rect.x = 1100
            h13_11.rect.y = 300
            self.hole_list.add(h13_11)

        if Holes == 14:
            h14_1 = HOLE(600,300,WHITE)
            h14_1.rect.x = 400
            h14_1.rect.y = 250
            self.hole_list.add(h14_1)

            h14_2 = HOLE(500,50,WHITE)
            h14_2.rect.x = 450
            h14_2.rect.y = 200
            self.hole_list.add(h14_2)

            h14_3 = HOLE(500,50,WHITE)
            h14_3.rect.x = 450
            h14_3.rect.y = 550
            self.hole_list.add(h14_3)

            h14_4 = HOLE(50,100,WHITE)
            h14_4.rect.x = 350
            h14_4.rect.y = 350
            self.hole_list.add(h14_4)

            h14_5 = HOLE(50,200,WHITE)
            h14_5.rect.x = 1000
            h14_5.rect.y = 300
            self.hole_list.add(h14_5)

            h14_6 = HOLE(50,50,WHITE)
            h14_6.rect.x = 550
            h14_6.rect.y = 150
            self.hole_list.add(h14_6)

            h14_7 = HOLE(50,50,WHITE)
            h14_7.rect.x = 750
            h14_7.rect.y = 600
            self.hole_list.add(h14_7)

            h14_8 = HOLE(50,50,WHITE)
            h14_8.rect.x = 650
            h14_8.rect.y = 650
            self.hole_list.add(h14_8)

            h14_9 = HOLE(100,50,WHITE)
            h14_9.rect.x = 450
            h14_9.rect.y = 600
            self.hole_list.add(h14_9)

            h14_10 = HOLE(150,50,WHITE)
            h14_10.rect.x = 0
            h14_10.rect.y = 250
            self.hole_list.add(h14_10)

            h14_11 = HOLE(150,50,WHITE)
            h14_11.rect.x = 0
            h14_11.rect.y = 500
            self.hole_list.add(h14_11)

            h14_12 = HOLE(150,50,WHITE)
            h14_12.rect.x = 1100
            h14_12.rect.y = 250
            self.hole_list.add(h14_12)

            h14_13 = HOLE(150,50,WHITE)
            h14_13.rect.x = 1100
            h14_13.rect.y = 500
            self.hole_list.add(h14_13)

            h14_14 = HOLE(100,50,WHITE)
            h14_14.rect.x = 150
            h14_14.rect.y = 300
            self.hole_list.add(h14_14)

            h14_15 = HOLE(100,50,WHITE)
            h14_15.rect.x = 150
            h14_15.rect.y = 450
            self.hole_list.add(h14_15)

            h14_16 = HOLE(50,50,WHITE)
            h14_16.rect.x = 250
            h14_16.rect.y = 250
            self.hole_list.add(h14_16)

            h14_17 = HOLE(50,50,WHITE)
            h14_17.rect.x = 250
            h14_17.rect.y = 500
            self.hole_list.add(h14_17)

            h14_18 = HOLE(50,150,WHITE)
            h14_18.rect.x = 300
            h14_18.rect.y = 100
            self.hole_list.add(h14_18)

            h14_19 = HOLE(50,150,WHITE)
            h14_19.rect.x = 300
            h14_19.rect.y = 550
            self.hole_list.add(h14_19)

            h14_20 = HOLE(700,50,WHITE)
            h14_20.rect.x = 350
            h14_20.rect.y = 700
            self.hole_list.add(h14_20)

            h14_21 = HOLE(700,50,WHITE)
            h14_21.rect.x = 350
            h14_21.rect.y = 50
            self.hole_list.add(h14_21)

            h14_22 = HOLE(50,100,WHITE)
            h14_22.rect.x = 1050
            h14_22.rect.y = 100
            self.hole_list.add(h14_22)

            h14_23 = HOLE(50,100,WHITE)
            h14_23.rect.x = 1050
            h14_23.rect.y = 600
            self.hole_list.add(h14_23)

            h14_24 = HOLE(50,50,WHITE)
            h14_24.rect.x = 1100
            h14_24.rect.y = 200
            self.hole_list.add(h14_24)

            h14_25 = HOLE(50,50,WHITE)
            h14_25.rect.x = 1100
            h14_25.rect.y = 550
            self.hole_list.add(h14_25)

            



            

            
                                    

            

        if Holes == 15:

            h15_1 = HOLE(100,50,WHITE)
            h15_1.rect.x = 0
            h15_1.rect.y = 250
            self.hole_list.add(h15_1)

            h15_2 = HOLE(100,50,WHITE)
            h15_2.rect.x = 0
            h15_2.rect.y = 550
            self.hole_list.add(h15_2)

            h15_3 = HOLE(500,50,WHITE)
            h15_3.rect.x = 100
            h15_3.rect.y = 450
            self.hole_list.add(h15_3)

            h15_4 = HOLE(700,50,WHITE)
            h15_4.rect.x = 100
            h15_4.rect.y = 300
            self.hole_list.add(h15_4)

            h15_5 = HOLE(100,50,WHITE)
            h15_5.rect.x = 450
            h15_5.rect.y = 350
            self.hole_list.add(h15_5)

            h15_6 = HOLE(50,400,WHITE)
            h15_6.rect.x = 700
            h15_6.rect.y = 300
            self.hole_list.add(h15_6)

            h15_7 = HOLE(50,200,WHITE)
            h15_7.rect.x = 550
            h15_7.rect.y = 500
            self.hole_list.add(h15_7)

            h15_8 = HOLE(50,100,WHITE)
            h15_8.rect.x = 500
            h15_8.rect.y = 700
            self.hole_list.add(h15_8)

            h15_9 = HOLE(50,100,WHITE)
            h15_9.rect.x = 750
            h15_9.rect.y = 700
            self.hole_list.add(h15_9)

        if Holes == 17:

            h17_1 = HOLE(50,250,WHITE)
            h17_1.rect.x = 500
            h17_1.rect.y = 0
            self.hole_list.add(h17_1)

            
            h17_2 = HOLE(50,50,WHITE)
            h17_2.rect.x = 750
            h17_2.rect.y = 0
            self.hole_list.add(h17_2)

            h17_3 = HOLE(200,50,WHITE)
            h17_3.rect.x = 750
            h17_3.rect.y = 50
            self.hole_list.add(h17_3)

            h17_4 = HOLE(50,450,WHITE)
            h17_4.rect.x = 950
            h17_4.rect.y = 100
            self.hole_list.add(h17_4)

            h17_5 = HOLE(400,50,WHITE)
            h17_5.rect.x = 550
            h17_5.rect.y = 550
            self.hole_list.add(h17_5)

            h17_6 = HOLE(200,50,WHITE)
            h17_6.rect.x = 650
            h17_6.rect.y = 400
            self.hole_list.add(h17_6)

            h17_7 = HOLE(50,200,WHITE)
            h17_7.rect.x = 800
            h17_7.rect.y = 200
            self.hole_list.add(h17_7)

            h17_8 = HOLE(250,50,WHITE)
            h17_8.rect.x = 550
            h17_8.rect.y = 200
            self.hole_list.add(h17_8)

            h17_9 = HOLE(50,150,WHITE)
            h17_9.rect.x = 650
            h17_9.rect.y = 250
            self.hole_list.add(h17_9)

            h17_10 = HOLE(50,250,WHITE)
            h17_10.rect.x = 500
            h17_10.rect.y = 350
            self.hole_list.add(h17_10)

            h17_11 = HOLE(100,50,WHITE)
            h17_11.rect.x = 400
            h17_11.rect.y = 200
            self.hole_list.add(h17_11)

            h17_12 = HOLE(50,300,WHITE)
            h17_12.rect.x = 350
            h17_12.rect.y = 200
            self.hole_list.add(h17_12)

            h17_13 = HOLE(50,300,WHITE)
            h17_13.rect.x = 300
            h17_13.rect.y = 200
            self.hole_list.add(h17_13)

            h17_14 = HOLE(200,50,WHITE)
            h17_14.rect.x = 100
            h17_14.rect.y = 300
            self.hole_list.add(h17_14)

            h17_15 = HOLE(100,50,WHITE)
            h17_15.rect.x = 100
            h17_15.rect.y = 450
            self.hole_list.add(h17_15)

            h17_16 = HOLE(300,50,WHITE)
            h17_16.rect.x = 200
            h17_16.rect.y = 600
            self.hole_list.add(h17_16)

            h17_17 = HOLE(50,100,WHITE)
            h17_17.rect.x = 150
            h17_17.rect.y = 500
            self.hole_list.add(h17_17)

            h17_18 = HOLE(100,50,WHITE)
            h17_18.rect.x = 0
            h17_18.rect.y = 250
            self.hole_list.add(h17_18)

            h17_19 = HOLE(100,50,WHITE)
            h17_19.rect.x = 0
            h17_19.rect.y = 500
            self.hole_list.add(h17_19)

        if Holes == 18:
            h18_1 = HOLE(100,50,WHITE)
            h18_1.rect.x = 0
            h18_1.rect.y = 250
            self.hole_list.add(h18_1)

            h18_2 = HOLE(100,50,WHITE)
            h18_2.rect.x = 0
            h18_2.rect.y = 500
            self.hole_list.add(h18_2)

            h18_3 = HOLE(100,50,WHITE)
            h18_3.rect.x = 1150
            h18_3.rect.y = 500
            self.hole_list.add(h18_3)

            h18_4 = HOLE(100,50,WHITE)
            h18_4.rect.x = 1150
            h18_4.rect.y = 250
            self.hole_list.add(h18_4)

            h18_5 = HOLE(250,200,WHITE)
            h18_5.rect.x = 500
            h18_5.rect.y = 300
            self.hole_list.add(h18_5)

            h18_6 = HOLE(50,50,WHITE)
            h18_6.rect.x = 700
            h18_6.rect.y = 150
            self.hole_list.add(h18_6)

            h18_7 = HOLE(50,50,WHITE)
            h18_7.rect.x = 450
            h18_7.rect.y = 200
            self.hole_list.add(h18_7)

            h18_8 = HOLE(50,50,WHITE)
            h18_8.rect.x = 300
            h18_8.rect.y = 300
            self.hole_list.add(h18_8)

            h18_9 = HOLE(50,50,WHITE)
            h18_9.rect.x = 350
            h18_9.rect.y = 500
            self.hole_list.add(h18_9)

            h18_10 = HOLE(50,50,WHITE)
            h18_10.rect.x = 700
            h18_10.rect.y = 550
            self.hole_list.add(h18_10)

            h18_11 = HOLE(50,50,WHITE)
            h18_11.rect.x = 850
            h18_11.rect.y = 300
            self.hole_list.add(h18_11)

            h18_12 = HOLE(100,50,WHITE)
            h18_12.rect.x = 100
            h18_12.rect.y = 300
            self.hole_list.add(h18_12)

            h18_13 = HOLE(100,50,WHITE)
            h18_13.rect.x = 100
            h18_13.rect.y = 450
            self.hole_list.add(h18_13)

            h18_14 = HOLE(100,50,WHITE)
            h18_14.rect.x = 1050
            h18_14.rect.y = 300
            self.hole_list.add(h18_14)

            h18_15 = HOLE(100,50,WHITE)
            h18_15.rect.x = 1050
            h18_15.rect.y = 450
            self.hole_list.add(h18_15)

            h18_16 = HOLE(50,50,WHITE)
            h18_16.rect.x = 200
            h18_16.rect.y = 100
            self.hole_list.add(h18_16)

            h18_17 = HOLE(50,50,WHITE)
            h18_17.rect.x = 200
            h18_17.rect.y = 650
            self.hole_list.add(h18_17)

            h18_18 = HOLE(50,50,WHITE)
            h18_18.rect.x = 1000
            h18_18.rect.y = 100
            self.hole_list.add(h18_18)

            h18_19 = HOLE(50,50,WHITE)
            h18_19.rect.x = 1000
            h18_19.rect.y = 650
            self.hole_list.add(h18_19)

            h18_20 = HOLE(750,50,WHITE)
            h18_20.rect.x = 250
            h18_20.rect.y = 50
            self.hole_list.add(h18_20)

            h18_21 = HOLE(750,50,WHITE)
            h18_21.rect.x = 250
            h18_21.rect.y = 700
            self.hole_list.add(h18_21)

            h18_22 = HOLE(50,150,WHITE)
            h18_22.rect.x = 150
            h18_22.rect.y = 150
            self.hole_list.add(h18_22)

            h18_23 = HOLE(50,150,WHITE)
            h18_23.rect.x = 150
            h18_23.rect.y = 500
            self.hole_list.add(h18_23)

            h18_24 = HOLE(50,150,WHITE)
            h18_24.rect.x = 1050
            h18_24.rect.y = 150
            self.hole_list.add(h18_24)

            h18_25 = HOLE(50,150,WHITE)
            h18_25.rect.x = 1050
            h18_25.rect.y = 500
            self.hole_list.add(h18_25)


        if Holes == 19:

            h19_1 = HOLE(100,100,WHITE)
            h19_1.rect.x = 450
            h19_1.rect.y = 0
            self.hole_list.add(h19_1)

            h19_2 = HOLE(50,250,WHITE)
            h19_2.rect.x = 850
            h19_2.rect.y = 0
            self.hole_list.add(h19_2)

            h19_3 = HOLE(300,50,WHITE)
            h19_3.rect.x = 550
            h19_3.rect.y = 250
            self.hole_list.add(h19_3)

            h19_4 = HOLE(100,50,WHITE)
            h19_4.rect.x = 450
            h19_4.rect.y = 200
            self.hole_list.add(h19_4)

            h19_5 = HOLE(50,250,WHITE)
            h19_5.rect.x = 200
            h19_5.rect.y = 0
            self.hole_list.add(h19_5)

            h19_6 = HOLE(50,250,WHITE)
            h19_6.rect.x = 250
            h19_6.rect.y = 250
            self.hole_list.add(h19_6)

            h19_7 = HOLE(50,250,WHITE)
            h19_7.rect.x = 400
            h19_7.rect.y = 250
            self.hole_list.add(h19_7)

            h19_8 = HOLE(50,200,WHITE)
            h19_8.rect.x = 200
            h19_8.rect.y = 500
            self.hole_list.add(h19_8)

            h19_9 = HOLE(200,50,WHITE)
            h19_9.rect.x = 450
            h19_9.rect.y = 450
            self.hole_list.add(h19_9)

            h19_10 = HOLE(400,50,WHITE)
            h19_10.rect.x = 250
            h19_10.rect.y = 700
            self.hole_list.add(h19_10)

            h19_11 = HOLE(250,50,WHITE)
            h19_11.rect.x = 650
            h19_11.rect.y = 500
            self.hole_list.add(h19_11)

            h19_12 = HOLE(250,50,WHITE)
            h19_12.rect.x = 650
            h19_12.rect.y = 650
            self.hole_list.add(h19_12)

            h19_13 = HOLE(250,50,WHITE)
            h19_13.rect.x = 900
            h19_13.rect.y = 700
            self.hole_list.add(h19_13)

            h19_14 = HOLE(100,200,WHITE)
            h19_14.rect.x = 1150
            h19_14.rect.y = 500
            self.hole_list.add(h19_14)

            h19_15 = HOLE(150,200,WHITE)
            h19_15.rect.x = 900
            h19_15.rect.y = 300
            self.hole_list.add(h19_15)

            h19_16 = HOLE(200,50,WHITE)
            h19_16.rect.x = 1050
            h19_16.rect.y = 250
            self.hole_list.add(h19_16)

        if Holes == 16:
            
            h16_1 = HOLE(50,200,WHITE)
            h16_1.rect.x = 200
            h16_1.rect.y = 350
            self.hole_list.add(h16_1)

            h16_2 = HOLE(50,50,WHITE)
            h16_2.rect.x = 250
            h16_2.rect.y = 300
            self.hole_list.add(h16_2)

            h16_3 = HOLE(50,50,WHITE)
            h16_3.rect.x = 300
            h16_3.rect.y = 250
            self.hole_list.add(h16_3)

            h16_4 = HOLE(50,50,WHITE)
            h16_4.rect.x = 350
            h16_4.rect.y = 200
            self.hole_list.add(h16_4)

            h16_5 = HOLE(50,50,WHITE)
            h16_5.rect.x = 400
            h16_5.rect.y = 150
            self.hole_list.add(h16_5)

            h16_6 = HOLE(50,100,WHITE)
            h16_6.rect.x = 450
            h16_6.rect.y = 50
            self.hole_list.add(h16_6)

            h16_7 = HOLE(50,50,WHITE)
            h16_7.rect.x = 500
            h16_7.rect.y = 0
            self.hole_list.add(h16_7)


            h16_8 = HOLE(50,50,WHITE)
            h16_8.rect.x = 250
            h16_8.rect.y = 550
            self.hole_list.add(h16_8)

            h16_9 = HOLE(50,50,WHITE)
            h16_9.rect.x = 300
            h16_9.rect.y = 600
            self.hole_list.add(h16_9)

            h16_10 = HOLE(50,50,WHITE)
            h16_10.rect.x = 350
            h16_10.rect.y = 650
            self.hole_list.add(h16_10)

            h16_11 = HOLE(100,50,WHITE)
            h16_11.rect.x = 400
            h16_11.rect.y = 700
            self.hole_list.add(h16_11)

            h16_12 = HOLE(50,50,WHITE)
            h16_12.rect.x = 500
            h16_12.rect.y = 750
            self.hole_list.add(h16_12)

            h16_13 = HOLE(50,50,WHITE)
            h16_13.rect.x = 750
            h16_13.rect.y = 750
            self.hole_list.add(h16_13)

            h16_14 = HOLE(100,50,WHITE)
            h16_14.rect.x = 800
            h16_14.rect.y = 700
            self.hole_list.add(h16_14)

            h16_15 = HOLE(50,50,WHITE)
            h16_15.rect.x = 900
            h16_15.rect.y = 650
            self.hole_list.add(h16_15)

            h16_16 = HOLE(50,50,WHITE)
            h16_16.rect.x = 950
            h16_16.rect.y = 600
            self.hole_list.add(h16_16)

            h16_17 = HOLE(200,50,WHITE)
            h16_17.rect.x = 1000
            h16_17.rect.y = 550
            self.hole_list.add(h16_17)

            h16_18 = HOLE(50,50,WHITE)
            h16_18.rect.x = 1200
            h16_18.rect.y = 600
            self.hole_list.add(h16_18)

            h16_19 = HOLE(200,50,WHITE)
            h16_19.rect.x = 1000
            h16_19.rect.y = 300
            self.hole_list.add(h16_19)

            h16_20 = HOLE(50,50,WHITE)
            h16_20.rect.x = 1200
            h16_20.rect.y = 250
            self.hole_list.add(h16_20)

            h16_25 = HOLE(50,50,WHITE)
            h16_25.rect.x = 950
            h16_25.rect.y = 250
            self.hole_list.add(h16_25)

            h16_21 = HOLE(50,50,WHITE)
            h16_21.rect.x = 900
            h16_21.rect.y = 200
            self.hole_list.add(h16_21)

            h16_22 = HOLE(50,50,WHITE)
            h16_22.rect.x = 850
            h16_22.rect.y = 150
            self.hole_list.add(h16_22)

            h16_23 = HOLE(50,100,WHITE)
            h16_23.rect.x = 800
            h16_23.rect.y = 50
            self.hole_list.add(h16_23)

            h16_24 = HOLE(50,50,WHITE)
            h16_24.rect.x = 750
            h16_24.rect.y = 0
            self.hole_list.add(h16_24)

            

        elif Holes == 21:
            h21_1 = HOLE(1100,50,WHITE)
            h21_1.rect.x = 150
            h21_1.rect.y = 300
            self.hole_list.add(h21_1)

            h21_2 = HOLE(1100,50,WHITE)
            h21_2.rect.x = 150
            h21_2.rect.y = 450
            self.hole_list.add(h21_2)

            h21_3 = HOLE(150,50,WHITE)
            h21_3.rect.x = 0
            h21_3.rect.y = 250
            self.hole_list.add(h21_3)

            h21_4 = HOLE(150,50,WHITE)
            h21_4.rect.x = 0
            h21_4.rect.y = 500
            self.hole_list.add(h21_4)

        elif Holes == 22:

            h22_1 = HOLE(50,50,WHITE)
            h22_1.rect.x = 0
            h22_1.rect.y = 300
            self.hole_list.add(h22_1)

            h22_2 = HOLE(50,50,WHITE)
            h22_2.rect.x = 0
            h22_2.rect.y = 450
            self.hole_list.add(h22_2)

            h22_3 = HOLE(100,200,WHITE)
            h22_3.rect.x = 50
            h22_3.rect.y = 100
            self.hole_list.add(h22_3)

            h22_4 = HOLE(100,200,WHITE)
            h22_4.rect.x = 50
            h22_4.rect.y = 500
            self.hole_list.add(h22_4)

            h22_5 = HOLE(1250,50,WHITE)
            h22_5.rect.x = 0
            h22_5.rect.y = 50
            self.hole_list.add(h22_5)

            h22_6 = HOLE(1250,50,WHITE)
            h22_6.rect.x = 0
            h22_6.rect.y = 700
            self.hole_list.add(h22_6)

            h22_7 = HOLE(200,200,WHITE)
            h22_7.rect.x = 1050
            h22_7.rect.y = 100
            self.hole_list.add(h22_7)

            h22_8 = HOLE(200,200,WHITE)
            h22_8.rect.x = 1050
            h22_8.rect.y = 500
            self.hole_list.add(h22_8)

            h22_9 = HOLE(100,500,WHITE)
            h22_9.rect.x = 850
            h22_9.rect.y = 100
            self.hole_list.add(h22_9)

            h22_10 = HOLE(100,500,WHITE)
            h22_10.rect.x = 650
            h22_10.rect.y = 200
            self.hole_list.add(h22_10)

            h22_11 = HOLE(100,150,WHITE)
            h22_11.rect.x = 450
            h22_11.rect.y = 100
            self.hole_list.add(h22_11)

            h22_12 = HOLE(100,350,WHITE)
            h22_12.rect.x = 450
            h22_12.rect.y = 350
            self.hole_list.add(h22_12)

            h23_13 = HOLE(100,200,WHITE)
            h23_13.rect.x = 250
            h23_13.rect.y = 100
            self.hole_list.add(h23_13)

            h23_14 = HOLE(100,250,WHITE)
            h23_14.rect.x = 250
            h23_14.rect.y = 450
            self.hole_list.add(h23_14)

        if Holes == 24:

            h24_1 = HOLE(1000,100,WHITE)
            h24_1.rect.x = 250
            h24_1.rect.y = 250
            self.hole_list.add(h24_1)

            h24_2 = HOLE(150,350,WHITE)
            h24_2.rect.x = 0
            h24_2.rect.y = 0
            self.hole_list.add(h24_2)

            h24_3 = HOLE(150,350,WHITE)
            h24_3.rect.x = 0
            h24_3.rect.y = 450
            self.hole_list.add(h24_3)

            h24_4 = HOLE(450,150,WHITE)
            h24_4.rect.x = 150
            h24_4.rect.y = 0
            self.hole_list.add(h24_4)

            h24_5 = HOLE(550,250,WHITE)
            h24_5.rect.x = 700
            h24_5.rect.y = 0
            self.hole_list.add(h24_5)

            h24_6 = HOLE(650,300,WHITE)
            h24_6.rect.x = 250
            h24_6.rect.y = 350
            self.hole_list.add(h24_6)

            h24_7 = HOLE(550,450,WHITE)
            h24_7.rect.x = 1000
            h24_7.rect.y = 450
            self.hole_list.add(h24_7)

            h24_8 = HOLE(1250,50,WHITE)
            h24_8.rect.x = 0
            h24_8.rect.y = 750
            self.hole_list.add(h24_8)
            
        if Holes == 26:

            h26_1 = HOLE(50,100,WHITE)
            h26_1.rect.x = 550
            h26_1.rect.y = 700
            self.hole_list.add(h26_1)

            h26_2 = HOLE(50,100,WHITE)
            h26_2.rect.x = 700
            h26_2.rect.y = 700
            self.hole_list.add(h26_2)

            h26_3 = HOLE(50,50,WHITE)
            h26_3.rect.x = 500
            h26_3.rect.y = 650
            self.hole_list.add(h26_3)

            h26_4 = HOLE(50,50,WHITE)
            h26_4.rect.x = 450
            h26_4.rect.y = 600
            self.hole_list.add(h26_4)

            h26_5 = HOLE(50,50,WHITE)
            h26_5.rect.x = 400
            h26_5.rect.y = 550
            self.hole_list.add(h26_5)

            h26_6 = HOLE(50,50,WHITE)
            h26_6.rect.x = 350
            h26_6.rect.y = 500
            self.hole_list.add(h26_6)

            h26_7 = HOLE(50,50,WHITE)
            h26_7.rect.x = 300
            h26_7.rect.y = 450
            self.hole_list.add(h26_7)

            h26_8 = HOLE(50,100,WHITE)
            h26_8.rect.x = 250
            h26_8.rect.y = 350
            self.hole_list.add(h26_8)

            h26_9 = HOLE(50,50,WHITE)
            h26_9.rect.x = 300
            h26_9.rect.y = 300
            self.hole_list.add(h26_9)

            h26_10 = HOLE(50,50,WHITE)
            h26_10.rect.x = 350
            h26_10.rect.y = 250
            self.hole_list.add(h26_10)

            h26_11 = HOLE(50,50,WHITE)
            h26_11.rect.x = 400
            h26_11.rect.y = 200
            self.hole_list.add(h26_11)

            h26_12 = HOLE(50,50,WHITE)
            h26_12.rect.x = 450
            h26_12.rect.y = 150
            self.hole_list.add(h26_12)

            h26_13 = HOLE(50,50,WHITE)
            h26_13.rect.x = 500
            h26_13.rect.y = 100
            self.hole_list.add(h26_13)

            h26_14 = HOLE(50,100,WHITE)
            h26_14.rect.x = 550
            h26_14.rect.y = 0
            self.hole_list.add(h26_14)

            h26_15 = HOLE(50,50,WHITE)
            h26_15.rect.x = 750
            h26_15.rect.y = 650
            self.hole_list.add(h26_15)

            h26_16 = HOLE(50,50,WHITE)
            h26_16.rect.x = 800
            h26_16.rect.y = 600
            self.hole_list.add(h26_16)

            h26_17 = HOLE(50,50,WHITE)
            h26_17.rect.x = 850
            h26_17.rect.y = 550
            self.hole_list.add(h26_17)

            h26_18 = HOLE(50,50,WHITE)
            h26_18.rect.x = 900
            h26_18.rect.y = 500
            self.hole_list.add(h26_18)

            h26_19 = HOLE(50,50,WHITE)
            h26_19.rect.x = 950
            h26_19.rect.y = 450
            self.hole_list.add(h26_19)

            h26_20 = HOLE(50,100,WHITE)
            h26_20.rect.x = 1000
            h26_20.rect.y = 350
            self.hole_list.add(h26_20)

            h26_21 = HOLE(50,50,WHITE)
            h26_21.rect.x = 950
            h26_21.rect.y = 300
            self.hole_list.add(h26_21)

            h26_22 = HOLE(50,50,WHITE)
            h26_22.rect.x = 900
            h26_22.rect.y = 250
            self.hole_list.add(h26_22)

            h26_23 = HOLE(50,50,WHITE)
            h26_23.rect.x = 850
            h26_23.rect.y = 200
            self.hole_list.add(h26_23)

            h26_24 = HOLE(50,50,WHITE)
            h26_24.rect.x = 800
            h26_24.rect.y = 150
            self.hole_list.add(h26_24)

            h26_25 = HOLE(50,50,WHITE)
            h26_25.rect.x = 750
            h26_25.rect.y = 100
            self.hole_list.add(h26_25)

            h26_26 = HOLE(50,100,WHITE)
            h26_26.rect.x = 700
            h26_26.rect.y = 0
            self.hole_list.add(h26_26)

        if Holes == 27:
            h27_1 = HOLE(600,350,WHITE)
            h27_1.rect.x = 0
            h27_1.rect.y = 450
            self.hole_list.add(h27_1)

            h27_2 = HOLE(1000,50,WHITE)
            h27_2.rect.x = 0
            h27_2.rect.y = 300
            self.hole_list.add(h27_2)

            h27_3 = HOLE(50,800,WHITE)
            h27_3.rect.x = 700
            h27_3.rect.y = 0
            self.hole_list.add(h27_3)

        if Holes == 28:
            h28_1 = HOLE(600,100,WHITE)
            h28_1.rect.x = 650
            h28_1.rect.y = 250
            self.hole_list.add(h28_1)

            h28_2 = HOLE(600,100,WHITE)
            h28_2.rect.x = 650
            h28_2.rect.y = 450
            self.hole_list.add(h28_2)

            h28_3 = HOLE(150,50,WHITE)
            h28_3.rect.x = 500
            h28_3.rect.y = 200
            self.hole_list.add(h28_3)

            h28_4 = HOLE(150,50,WHITE)
            h28_4.rect.x = 500
            h28_4.rect.y = 550
            self.hole_list.add(h28_4)

            h28_5 = HOLE(50,350,WHITE)
            h28_5.rect.x = 450
            h28_5.rect.y = 200
            self.hole_list.add(h28_5)

            
            

            

            

            

            

            
            

            
            
        
            
            

         
            
            
            
        
            


    def draw(self,screen):
        """this is the function that will draw everything once i tell it to in the code"""
        self.doors_list.draw(screen)
        self.hole_list.draw(screen)
        self.Key_list.draw(screen)
