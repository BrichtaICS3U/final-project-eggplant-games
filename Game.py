import pygame, sys, random
from pygame.locals import *
pygame.init()
from hero import *    #import the sprites that Abbey has made
from LVLs import LVL                    #FML
from Door import DOOR, KEY



# define colours #
WHITE = (255,255,255)       #White
GRAY  = (121,121,121)       #Gray
BLACK = (0,0,0)             #Black
BROWN = (74,67,23)          #Brown
SILVER = (204,201,182)      #Silver
GOLD = (235,207,26)         #Gold
RED   = (255,0,0)           #test Red
GREEN = (0,255,0)           #test Green
BLUE  = (0,0,255)           #test Blue
BC1   = (66,3,61)           #Button colour 1
BC2   = (104,14,75)         #Button coloutr 2
I_TEXT = (255,164,0)        #insztructions text colour (subject to change)
M_TEXT = (130,2,99)         #menu text colour
PG_TEXT = (255,164,0)       #pregame text
D    = (252, 216, 168)

#background(s)
T_background = pygame.image.load("Menu_Background.png") #this is the background for the title screen
C_background = pygame.image.load("Controls_back.jpg")   #this is the background for the controls screen
S_bakckground = pygame.image.load("S_B.jpg")            #this is the background for the settings screen
PG_Background = pygame.image.load("Settings_B.jpg")     #this is the background for the pre game screen

# screen dimensions and game clock #
SCREEN_WIDTH = 1250                     #screen width
SCREEN_HEIGHT = 800                     #screen height
size = (SCREEN_WIDTH,SCREEN_HEIGHT)     #the total dimensions of the screen
screen = pygame.display.set_mode(size)  #create the display area
clock = pygame.time.Clock()             #built in pygame clock


# ----------- Music ----------- #
Music = True

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)   #this is the music for the menu
pygame.mixer.music.load("Menu_Music.mp3")                                   #
pygame.mixer.music.play(-1)                                                 #            
    
# ----------- end of music catagory ------------- #




# ----------- list of global variables ------------- #
shoot = True
LayerP = 1
b = False
Y = 1
X = 1
F_C = D
Generate = True
B_D_L = True
R_D_L = True
Y_D_L = True
UNLOCK_BLUE = True
UNLOCK_RED = True
UNLOCK_YELLOW = True
TILESIZE = 50
MAPWIDTH = 25
MAPHEIGHT = 16
DIRT = 0
GRASS = 1
WATER = 2 
tilemap = []
textures =  {
                DIRT : pygame.image.load('Dirt.png'),
                GRASS : pygame.image.load('grass.png'),
                WATER : pygame.image.load('water.png')
            }
  
# ----------- end of variable list ---------------#




# ---------- this will be catagory of functions to be used in the summative ----------- #

def Button(msg,x,y,w,h,col1,col2,FS,action = None,CT = None):
    global event
    """
        this is a short function that acts as a button class (will likley be changed into a module)
        msg    --- the label that will appear on the button
        x      --- the x coordinate for the button
        y      --- the y coordinate for the button
        w      --- the width od the button
        h      --- the height of the button
        col1   --- the first colour of the button
        col2   --- the second colour of the button
        FS     --- the font size of the buttons text
        action --- the function that the button activates
        CT     --- the controls text (only for layer 3/controls screen Buttons)
    """
    
    global layer                        #adds the layer variable to the Button function
    mouse = pygame.mouse.get_pos()      #gathers the position of the mouse
    click = pygame.mouse.get_pressed()  #finds out if the mouse has been pressed

    if x < mouse[0] <x+w and y < mouse[1] < y+h and click[0] == 1:  #if the cursor is over the button and mouse 1 has been pressed
        pygame.draw.rect(screen,BLACK,(x,y,w,h))                    #redraw the Button but BLACK
        if click[0] == 1 and action != None:                        #if the Button has a function assigned to it
            action()                                                #activate that function
    elif x < mouse[0] < x+w and y < mouse[1] < y+h and layer != 3:  #if the cursor is over the button but mouse 1 hasn't been pressed yet
        pygame.draw.rect(screen,BLACK,(x-5,y-5,w+10,h+10))
        pygame.draw.rect(screen,col2,(x,y,w,h))                     #redraw the Button but in a diffirent colour
    elif x < mouse[0] < x+w and y < mouse[1] < y+h and layer == 3:  #this if statement is for only the Buttons located in the "Controls" section of the menu
        pygame.draw.rect(screen,BLACK,(x-5,y-5,w+10,h+10))
        pygame.draw.rect(screen,col2,(x,y,w,h))                     #it redraws the button in its second colour. 
        
        CFont = pygame.font.Font("freesansbold.ttf",FS)     #as well as displays a definition of what that Button does in the game
        CText = CFont.render(CT,True,I_TEXT)                #
        CTextrect = CText.get_rect()                        #
        CTextrect.center = (1000, y + (h/2))                #
        screen.blit(CText,CTextrect)                        #
        
    else:                                                           #if nothing is interacting with the Button
        pygame.draw.rect(screen,BLACK,(x-5,y-5,w+10,h+10))
        pygame.draw.rect(screen,col1,(x,y,w,h))                     #simply draw it with its orginal perameters

    Bfont = pygame.font.Font("freesansbold.ttf",FS)                 #these few lines are the Button labels 
    Btext = Bfont.render(msg,True,BLACK)                            #
    Btextrect = Btext.get_rect()                                    #
    Btextrect.center = (x + (w/2), y + (h/2))                       #
    screen.blit(Btext,Btextrect)                                    #
    
def TEXT(TXT,x,y,TF,TC = (130,2,99)):
    """
        this function exists to create headings for each menu screens
        TXT   --- the text that the the function will create
        x     --- the x position of the text
        y     --- the y position of the text
        TF    --- the font of the text
        TC    --- the colour of the text
    """

    fontTitle = pygame.font.Font('freesansbold.ttf', TF)
    textSurfaceTitle = fontTitle.render(TXT, True,TC)
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (x,y)
    screen.blit(textSurfaceTitle,textRectTitle)
    
def M_Menu():
    """this function will bring the user back to the menu"""
    global layer
    layer = 1

def Settings():
    """this function will bring the user to the settings menu"""
    global layer
    layer = 2

def Controls():
    """this function will lead to the instructions menu"""
    global layer
    layer = 3

def Game_intro():
    """ this will bring the player to the game's introduction"""
    global layer
    layer = 4

def MENU_Music_ON():
    """this function will turn on the music if the On button is pressed for the music"""
    pygame.mixer.music.unpause()

def MENU_Music_OFF():
    """this function will turn the music off when the off Buton is pressed"""
    pygame.mixer.music.pause()
    
def Quit():
    """this function will cause the game to end and close the program"""
    global Menu
    Menu = False
    

def P_settings():
    global LayerP
    LayerP += 1

def P_menu():
    global LayerP
    LayerP -= 1

  
def Change_SCREEN():
    """ the point of this function is to change the lvls that the player are in, it also delets the pas objects so the player has no way to glitch the game"""
    global Y
    global X
    global lvls
    global Generate
    global tilemap
    
    lvls = []
    tilemap = []
    Generate = True
    
    if player.rect.y < 50:
        player.rect.y = SCREEN_HEIGHT - 46
        #print("screen UP.")
        Y += 1
    elif player.rect.y > 750:
        player.rect.y = 6
        #print("screen DOWN.")
        Y -= 1
    elif player.rect.x < 50:
        player.rect.x = SCREEN_WIDTH - 36
        #print("screen LEFT.")
        X -= 1
    elif player.rect.x > 1150:
        player.rect.x = 6
        #print("screen RIGHT.")
        X += 1
    

def Hit_Wall_R():
    keys = pygame.key.get_pressed()
    player.rect.x -= 5
    if keys[pygame.K_LSHIFT]:
        player.rect.x -= 3
    
    

def Hit_Wall_L():
    keys = pygame.key.get_pressed()
    player.rect.x += 4
    if keys[pygame.K_LSHIFT]:
        player.rect.x += 3
    
    
        
def Hit_Wall_U():
    keys = pygame.key.get_pressed()
    player.rect.y -= 4
    if keys[pygame.K_LSHIFT]:
        player.rect.y -= 3
    
    
        
def Hit_Wall_D():
    keys = pygame.key.get_pressed()
    player.rect.y += 4
    if keys[pygame.K_LSHIFT]:
        player.rect.y += 3
    

def Unlock_B_D():
    global B_D_L 
    B_D_L = False

def Unlock_R_D():
    global R_D_L
    R_D_L = False

def Unlock_Y_D():
    global Y_D_L
    Y_D_L = False

def draw_MAP():
    global MAPHEIGHT
    global MAPWIDTH
    global tilemap
    global textures
    global GRASS
    global DIRT
    global WATER
    global tilemap
    global Y
    global X
    if tilemap != []:
        for row in range (MAPHEIGHT):
            for column in range(MAPWIDTH):
                screen.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))

    
    
        

                

            
# --------------------- End of functions list ----------------------- #



# --------------------- this will be the main code for the game -------------------- #
"""
this is where the bulk of the game code will be located. the point of placing it 
in a function is so that we can easily call it when needed form the menu
"""

#sprite list(s)
all_sprites_list = pygame.sprite.Group()        #this is the master sprite list. All of the sprites are located her unpon creation
Hero_sprite_list = pygame.sprite.Group()        #this is the Hero sprite list. Only the hero sprite will be located here
Bullet_sprites_list = pygame.sprite.Group()     #this is the bullet sprite list. all the Bullets taht are fired will be located here
enemy_list = pygame.sprite.Group()              #this is the enemy sprite list
ammo_drops_list = pygame.sprite.Group()         #enemy ammo drops list
health_drops_list = pygame.sprite.Group()       #enemy health drops list
money_drops_list = pygame.sprite.Group()

#player character)
player = Hero(30,40)
player.rect.x = SCREEN_WIDTH/2
player.rect.y = SCREEN_HEIGHT/2
playerHealth = player.HP

#Initial sword
player_sword = Sword(1,1)
all_sprites_list.add(player_sword)

#Initial enemy character
enemy = Enemy(BLACK, 40, 40)        #adds a single enemy to first room
enemy_list.add(enemy)
all_sprites_list.add(enemy)

#Initial bullet
bullet = Bullet(BLACK, 5, 5, player.rect.x, player.rect.y)

#list of lvls
lvls = []

#add all of the sprites into their respected lists 
all_sprites_list.add(player)
Hero_sprite_list.add(player)


def Game():
            
        
    
    
    global Y
    global event
    global SCREEN_WIDTH         #turn the screen width into a global variable for the game
    global SCREEN_HEIGHT        #turn the screen height into a global variable for the game
    global shoot                #adds the shoot variable
    global b
    global F_C
    global Generate
    global B_D_L
    global UNLOCK_BLUE
    global UNLOCK_RED
    global UNLOCK_YELLOW
    global MAPHEIGHT
    global MAPWIDTH
    global TILESIZE
    global GRASS
    global DIRT
    global WATER
    global tilemap
    Game = True                 #while the variable is true the game will run
       
    while Game:
        for event in pygame.event.get():        #
            if event.type == pygame.QUIT:       #if the red box at the top right is clicked
                pygame.quit()                   #quit the etire code
            elif event.type == pygame.KEYDOWN:  #
                if event.key==pygame.K_ESCAPE:
                    Pause_Menu()
                    Game = False                #exit the game and return to the main menu

        keys = pygame.key.get_pressed()

        

        screen.fill(F_C)

        if Y < 4:
            F_C = D
        if Y >= 4:
            F_C = GRAY

        
#                                                                       ___
########################################## IMPORTANT DO NOT TOUCH PLZ <(^_^)<
# this commented blocked portion is the section where the lvls are drawn and the player interacts with the sorrounding


        

        if Generate == True:
            #                                                                       ___
            ########################################## IMPORTANT DO NOT TOUCH PLZ <(^_^)<
            # this commented blocked portion is the section where the lvls are drawn and the player interacts with the sorrounding

            # Forest/outside dungeon ---- Tutorial #
            #lvl 1
            if Y == 1 and X == 1:
                lvl1 = LVL(1)
                lvls.append(lvl1)
                e_screen = 1
                print("lvl1")
                    
            #lvl 2
            elif Y == 2 and X == 1:
                lvl2 = LVL(8)
                lvls.append(lvl2)
                e_screen = 1
                print("lvl2")

            #lvl 3
            elif Y == 3 and X == 1:
                lvl3 = LVL(100,0,1)
                lvls.append(lvl3)
                e_screen = 1
                print("lvl3")#this is the lvl where i need to  return the locked door into position

            

            #lvl 4            
            elif Y == 3 and X == 2:
                lvl4 = LVL(2)
                lvls.append(lvl4)
                e_screen = 1
                print("lvl4")
            
            
            #lvl 5
            elif Y == 3 and X == 0:
                lvl5 = LVL(6)
                lvls.append(lvl5)
                e_screen = 1
                print("lvl5")
                
           
            #lvl 6
            elif Y == 3 and X == -1:
                lvl6 = LVL(10)
                lvls.append(lvl6)
                e_screen = 1
                print("lvl6")

            #lvl 7
            elif Y == 2 and X == -1:
                lvl7 = LVL(1,0,0,1)
                lvls.append(lvl7)
                e_screen = 1
                print("lvl7")
            
            # Enterance/Sewers ----- lvl 1 #
            #lvl 8
            elif Y == 4 and X == 1:
                lvl8 = LVL(8)
                lvls.append(lvl8)
                e_screen = 0
                print("lvl8")

        
            #lvl 10 //first floor / hub for floor (reference point)//
            elif Y == 5 and X == 1:
                lvl10 = LVL(100,0,2)
                lvls.append(lvl10)
                e_screen = 0
                print("lvl10")

            #lvl 11
            elif Y == 5 and X == 2:
                lvl11 = LVL(6)
                lvls.append(lvl11)
                e_screen = 0
                print("lvl11")

            #lvl 12 //Roundabout entrance//
            elif Y == 5 and X == 3:
                lvl12 = LVL(20)
                lvls.append(lvl12)
                e_screen = 0
                print("lvl12")

            #lvl 13
            elif Y == 6 and X == 3:
                lvl13 = LVL(10)
                lvls.append(lvl13)
                e_screen = 0
                print("lvl13")

            #lvl 14
            elif Y == 6 and X == 4:
                lvl14 = LVL(6)
                lvls.append(lvl14)
                e_screen = 0
                print("lvl14")

           #lvl 15
            elif Y == 6 and X == 5:
                lvl15 = LVL(9)
                lvls.append(lvl15)
                e_screen = 0
                print("lvl15")

            #lvl 16
            elif Y == 5 and X == 5:
                lvl16 = LVL(8,0,0,3)
                lvls.append(lvl16)
                e_screen = 0
                print("lvl16")

            #lvl 17
            elif Y == 4 and X == 5:
                lvl17 = LVL(3)
                lvls.append(lvl17)
                e_screen = 0
                print("lvl17")

            #lvl 18
            elif Y == 4 and X == 4:
                lvl18 = LVL(6)
                lvls.append(lvl18)
                e_screen = 0
                print("lvl18")

            #lvl 19 //end of sewer roundabout//
            elif Y == 4 and X == 3:
                lvl19 = LVL(5)
                lvls.append(lvl19)
                e_screen = 0
                print("lvl19")
    
    
            #lvl 21 // start of left part of sewers//
            elif Y == 5 and X == 0:
                lvl21 = LVL(6)
                lvls.append(lvl21)
                e_screen = 0
                print("lvl21")

            #lvl 22
            elif Y == 5 and X == -1:
                lvl22 = LVL(30)
                lvls.append(lvl22)
                e_screen = 0
                print("lvl22")

            #lvl 23
            elif Y == 4 and X == -1:
                lvl23 = LVL(1)
                lvls.append(lvl23)
                e_screen = 0
                print("lvl23")

            #lvl 24
            elif Y == 5 and X == -2:
                lvl24 = LVL(40)
                lvls.append(lvl24)
                e_screen = 0
                print("lvl24")

            #lvl 25
            elif Y == 5 and X == -3:
                lvl25 = LVL(4)
                lvls.append(lvl25)
                e_screen = 0
                print("lvl25")

            #lvl 26
            elif Y == 6 and X == -2:
                lvl26 = LVL(8)
                lvls.append(lvl26)
                e_screen = 0
                print("lvl26")

            #lvl 27
            elif Y == 7 and X == -2:
                lvl27 = LVL(9)
                lvls.append(lvl27)
                e_screen = 0
                print("lvl27")

            #lvl 28
            elif Y == 7 and X == -3:
                lvl28 = LVL(4,0,0,2)
                lvls.append(lvl28)
                e_screen = 0
                print("lvl28")
            
            


        
            if Y == 1 and X == 1:
                tilemap = [
                            [2,2,2,2,2,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]                                       
                        ]

            if Y == 2 and X == 1:
                tilemap = [
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2],
                            [2,2,2,2,2,2,2,2,1,1,1,1,0,0,1,1,1,1,2,2,2,2,2,2,2]                                        
                        ]

            if Y == 3 and X == 1:
                tilemap = [
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1]                                        
                        ]

            if Y == 3 and X == 2:
                tilemap = [
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                            [0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
                            [0,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]                                        
                        ]

            if Y == 3 and X == 0:
                tilemap = [
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]                                        
                        ]


            if Y == 3 and X == -1:
                tilemap = [
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1]                                        
                        ]

            if Y == 2 and X == -1:
                tilemap = [
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]                                        
                        ]
                
            Generate = False            
                   
    
#hit detection for doors            
        for lvl in lvls:

            if Y == 1 and X == 1:#plz dunt dark marks cyuz i t luk bad ;-;
                draw_MAP()
                lvl1.draw(screen)
            elif Y == 2 and X == 1:
                draw_MAP()
                lvl2.draw(screen)
            elif Y == 3 and X == 1:
                draw_MAP()
                lvl3.draw(screen)
            elif Y == 3 and X == 2:
                draw_MAP()
                lvl4.draw(screen)
            elif Y == 3 and X == 0:
                draw_MAP()
                lvl5.draw(screen)
            elif Y == 3 and X == -1:
                draw_MAP()
                lvl6.draw(screen)
            elif Y == 2 and X == -1:
                draw_MAP()
                lvl7.draw(screen)
            elif Y == 4 and X == 1:
                draw_MAP()
                lvl8.draw(screen)
            elif Y == 5 and X == 1:
                draw_MAP()
                lvl10.draw(screen)
            elif Y == 5 and X == 2:
                draw_MAP()
                lvl11.draw(screen)
            elif Y == 5 and X == 3:
                draw_MAP()
                lvl12.draw(screen)
            elif Y == 6 and X == 3:
                draw_MAP()
                lvl13.draw(screen)
            elif Y == 6 and X == 4:
                draw_MAP()
                lvl14.draw(screen)
            elif Y == 6 and X == 5:
                draw_MAP()
                lvl15.draw(screen)
            elif Y == 5 and X == 5:
                draw_MAP()
                lvl16.draw(screen)
            elif Y == 4 and X == 5:
                lvl17.draw(screen)
            elif Y == 4 and X == 4:
                draw_MAP()
                lvl18.draw(screen)
            elif Y == 4 and X == 3:
                draw_MAP()
                lvl19.draw(screen)
            elif Y == 5 and X == 0:
                draw_MAP()
                lvl21.draw(screen)
            elif Y == 5 and X == -1:
                draw_MAP()
                lvl22.draw(screen)
            elif Y == 4 and X == -1:
                draw_MAP()
                lvl23.draw(screen)
            elif Y == 5 and X == -2:
                draw_MAP()
                lvl24.draw(screen)
            elif Y == 5 and X == -3:
                draw_MAP()
                lvl25.draw(screen)
            elif Y == 6 and X == -2:
                draw_MAP()
                lvl26.draw(screen)
            elif Y == 7 and X == -2:
                draw_MAP()
                lvl27.draw(screen)
            elif Y == 7 and X == -3:
                draw_MAP()
                lvl28.draw(screen)
          
            
            


            
            Door_collision_list = pygame.sprite.spritecollide(player,lvl.doors_list,False)
            key_collision_list  = pygame.sprite.spritecollide(player,lvl.Key_list,False)
            
            for door in Door_collision_list:
                
                
                        
                
                if door.LOCK == 0:
                    door.IS_LOCKED()

                elif door.LOCK == 1:
                    if B_D_L == False:
                        door.IS_LOCKED()

                elif door.LOCK == 2:
                    if R_D_L == False:
                        door.IS_LOCKED()

                elif door.LOCK == 3:
                    if Y_D_L == False:
                        door.IS_LOCKED()

                if door.OPEN == True:
                    Change_SCREEN()
                

                    for enemy in enemy_list:                #this code deletes the previous enemies off the screen
                        enemy.HP = 0
                        all_sprites_list.remove(enemy)
                        enemy_list.remove(enemy)
                
                    for en_drop in ammo_drops_list:
                        ammo_drops_list.remove(en_drop)
                        all_sprites_list.remove(en_drop)

                    for en_drop in health_drops_list:
                        health_drops_list.remove(en_drop)
                        all_sprites_list.remove(en_drop)
                
                    for i in range(e_screen):                      #this code adds new enemies to next screen
                        enemy = Enemy(BLACK, 40, 40)                #based off of the number of enemies that was
                        enemy_list.add(enemy)                       #set earlier
                        all_sprites_list.add(enemy)
    
            for key in key_collision_list:

                if key.D_N == 1:
                    if UNLOCK_BLUE == True:
                        Unlock_B_D()
                        print("the blue door has been unlocked")
                        UNLOCK_BLUE = False
                    
                if key.D_N == 2:    
                    if UNLOCK_RED == True:
                        Unlock_R_D()
                        print("the red door has been unlocked")
                        UNLOCK_RED = False

                if key.D_N == 3:
                    if UNLOCK_YELLOW == True:
                        Unlock_Y_D()
                        print("the yellow door has been unlocked")
                        UNLOCK_YELLOW = False
                    
                        
                
                

#hit detection for objects or "HOLE"(s) or "WALLS" in the game                
            Hole_collision_list = pygame.sprite.spritecollide(player,lvl.hole_list,False)
            for hole in Hole_collision_list:
                
                for HOLE in lvl.hole_list: 
                    if player.rect.x + 30 >= HOLE.rect.x -2 and player.rect.x < HOLE.rect.x - 26:#Left
                        Hit_Wall_R()
                    elif player.rect.x <= HOLE.rect.x + HOLE.width and player.rect.x + 30 > HOLE.rect.x + HOLE.width + 26:#Right
                        Hit_Wall_L()
                    elif player.rect.y + 40 > HOLE.rect.y and player.rect.y < HOLE.rect.y - 36:#Top
                        Hit_Wall_U()
                    elif player.rect.y < HOLE.rect.y + HOLE.height and player.rect.y + 40 > HOLE.rect.y + HOLE.height + 36:#Bottom
                        Hit_Wall_D()

                    
       
#########################################################            

        keys = pygame.key.get_pressed()         #built in pygame function to detect is keys are pressed

         #player movement / melee
        if keys[pygame.K_a]:                        #if the A key is pressed
            player.move()                           #the player will move to the Left at a speed of 2 pixels
            if keys[pygame.K_e]:
                player_sword.left(player, screen)   #player melee attacks to the left            
        elif keys[pygame.K_s]:                      #if the S key is pressed
            player.move()                           #the player will move Down at a speed of 2 pixels
            if keys[pygame.K_e]:
                player_sword.down(player, screen)   #player melee attacks downward
        elif keys[pygame.K_d]:                      #if the D key is pressed
            player.move()                           #the player will move to the Right at a speed of 2 pixels
            if keys[pygame.K_e]:
                player_sword.right(player, screen)  #player melee attacks to the right
        elif keys[pygame.K_w]:                      #if the W key is pressed
            player.move()                           #the player will move Up at a speed of 2 pixels
            if keys[pygame.K_e]:
                player_sword.up(player, screen)     #player melee attacks upwards
                
        #player sprinting
        if keys[pygame.K_LSHIFT]:               #if left shift is pressed
                if keys[pygame.K_a]:                #and if A is pressed
                    player.move()                       #double the movement speed Left
                elif keys[pygame.K_s]:              #and if S is pressed
                    player.move()                       #double the movement speed Down
                elif keys[pygame.K_d]:              #and if D is pressed
                    player.move()                       #double the movement speed Right
                elif keys[pygame.K_w]:              #and if W is pressed
                    player.move()                       #double the movement speed up


                        
        #player shooting
        if event.type==pygame.MOUSEBUTTONDOWN and shoot == True and player.ammo > 0:                            #if the mouse Button has been pressed and the player is allowed to shoot
                bullet = Bullet(BLACK,5,5,player.rect.x + (30/2),player.rect.y + (40/2))    #shoot a bullet from the center of the player sprite
                shoot = False                                                               #take away he ability to shoot so the game doesn't break
                all_sprites_list.add(bullet)                                                #add the bullets to th universal list
                b = True
                Bullet_sprites_list.add(bullet)
                player.ammo -= 1
                
        #this allows the player to shoot again when he/she relases the mouse button
        
        if event.type==pygame.MOUSEBUTTONUP:                                                #when the mouse button is releasd
            shoot = True                                                                    #the player can shoot again

        #Enemy follow player (while living)
        for enemy in enemy_list:
            if enemy.HP > 0:
                enemy.move_to_player(player)  
        
        #update sprite list(s)
        all_sprites_list.update()
        Bullet_sprites_list.update()
        enemy_list.update()




#---------------- collisions--------------------------------------------------------------------------------------
        for enemy in enemy_list:    
            main_col = pygame.sprite.collide_rect(player, enemy)    #collisions between player and enemies
            if main_col == True:
                if keys[pygame.K_e]:            #if the player is holding E, cue melee attack
                    enemy.HP -= 25              #decrease enemy health by 10
                    enemy.rect.x -= 100         #enemy bounces back on collision with 'sword' 
                    enemy.rect.y -= 100         #aka player who is holding 'sword'
                else:
                    player.HP -= 20
                    player.rect.x -= 100        #Player bounces back on enemy collision
                    player.rect.y -= 50         #collisions between enemy and player
        
        if b == True:                                   #global variable indicating that a bullet is present   
            for enemy in enemy_list:
                bullet_col = pygame.sprite.collide_rect(bullet, enemy)  #collisions between bullets and enemies
                if bullet_col == True:
                    enemy.HP -= 50                      #decrease enemy health by 20   
                    bullet.rect.x = 0                   #teleport bullet to top left of screen, because if not the bullet stays 'colliding'
                    bullet.rect.y = 0                   #with the enemy and it becomes a one shot kill (not what we want!)
                    Bullet_sprites_list.remove(bullet)  #remove bullet from lists 
                    all_sprites_list.remove(bullet)

        for en_drop in ammo_drops_list:                                  
            ammo_drop_col = pygame.sprite.collide_rect(player, en_drop)
            if ammo_drop_col == True:                        #if player collides with dropped item
                ammo_drops_list.remove(en_drop)              #drop is removed from lists
                all_sprites_list.remove(en_drop)            #and subsequently, screen
                if player.ammo <5:                          #if player has less than 5 bullets,
                    player.ammo += 1                        #player gets +1 ammo

        for en_drop in health_drops_list:                                  
            health_drop_col = pygame.sprite.collide_rect(player, en_drop)
            if health_drop_col == True:                        
                health_drops_list.remove(en_drop)               
                all_sprites_list.remove(en_drop)                
                if player.HP < 100:                             #if player has less than 100 health,
                    player.HP += 20                             #player gets +20 health

        for en_drop in money_drops_list:
            money_drop_col = pygame.sprite.collide_rect(player, en_drop)
            if money_drop_col == True:
                if en_drop.colour == BROWN:
                    money_drops_list.remove(en_drop)               
                    all_sprites_list.remove(en_drop)
                    player.money += 1
                elif en_drop.colour == SILVER:
                    money_drops_list.remove(en_drop)               
                    all_sprites_list.remove(en_drop)
                    player.money += 2
                elif en_drop.colour == GOLD:
                    money_drops_list.remove(en_drop)               
                    all_sprites_list.remove(en_drop)
                    player.money += 3
            
        """insert code for collisions between enemies here"""

        
# -------------------end of collisions --------------------------------------------------------------------------------                   
    
        HealthBar(screen, player)           #this draws and updates the player health bar(s)
        TEXT("Player Health", 60, 20, 15)   #add text to explain what the bars are
        AmmoBar(screen, player)             #draws and updates the player ammo bar
        TEXT("Player Ammo", 60, 80, 15)
        TEXT("Money", 40, 140, 15)
        money_string = "$ {}".format(player.money)
        TEXT(money_string, 40, 160, 15)
                
        for enemy in enemy_list:    #enemy health bar drawing/updates
            enemy.health(screen)
            #------enemy drops-------------------------------------------------------------------
            if enemy.HP <= 0:                               #if enemy dies
                #money drop (always happens)
                m_chance = random.randint(0, 100)
                if m_chance <= 60:                          #60% chance of brown coin (1$)
                    en_drop = Drops(BROWN, 10, 10, enemy)
                    en_drop.rect.x += 50
                    all_sprites_list.add(en_drop)
                    money_drops_list.add(en_drop)
                    
                elif 60 < m_chance < 90:                    #30% chance of silver coin ($2)
                    en_drop = Drops(SILVER, 10, 10, enemy)
                    en_drop.rect.x += 50
                    all_sprites_list.add(en_drop)
                    money_drops_list.add(en_drop)
           
                elif m_chance >= 90:                        #10% chance of gold coin ($3)
                    en_drop = Drops(GOLD, 10, 10, enemy)
                    en_drop.rect.x += 50
                    all_sprites_list.add(en_drop)
                    money_drops_list.add(en_drop)
                    
                #ammo/health drop (happens 50% of time)
                chance = random.randint(0, 100)             #get a random number from 1-100
                if chance <= 50:                            #numbers 1-50 give a drop (50% chance)
                    chance2 = random.randint(0, 100)        #get another random numner
                    if chance2 <= 75:                       #75% chance the drop is for ammo
                        en_drop = Drops(GRAY, 20, 20, enemy)
                        all_sprites_list.add(en_drop)
                        ammo_drops_list.add(en_drop)
                    elif chance2 > 75:                      #25% chance the drop is for health
                        en_drop = Drops(RED, 20, 20, enemy)
                        all_sprites_list.add(en_drop)
                        health_drops_list.add(en_drop)
                    
                all_sprites_list.remove(enemy)
                enemy_list.remove(enemy)
                


        
        #wall restrictions
        #Right wall
        if player.rect.x + 28 > SCREEN_WIDTH:
            player.rect.x -= 4
            if keys[pygame.K_LSHIFT]:
                player.rect.x -= 4
        #Left wall
        elif player.rect.x < -2:
            player.rect.x += 4
            if keys[pygame.K_LSHIFT]:
                player.rect.x += 4
        #top wall
        elif player.rect.y < -2:
            player.rect.y += 4
            if keys[pygame.K_LSHIFT]:
                player.rect.y += 4
        #Bottom wall
        elif player.rect.y + 38 > SCREEN_HEIGHT:
            player.rect.y -= 4
            if keys[pygame.K_LSHIFT]:
                player.rect.y -= 4


    
        #Draw all sprites
        all_sprites_list.draw(screen)
        
        
        pygame.display.flip()
        clock.tick(30)
# ------------------- end of main Game code ------------------ #

# ------------------- this section will house the pause menu code --------------- !!!!DONE!!!!

def Pause_Menu():
    global LayerP
    Pause = True
    while Pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game()

        screen.fill(WHITE)

        if LayerP == 1:
            screen.blit(S_bakckground,(0,0))
            pygame.draw.rect(screen,BC1,[SCREEN_WIDTH/6 * 2 + 88,188,224,324])
            pygame.draw.rect(screen,BLACK,[SCREEN_WIDTH/6 * 2 + 100,200,200,300])
            
            Button("Settings",SCREEN_WIDTH/2 - 85,240,150,50,BC1,BC2,35,P_settings)
            Button("Resume",SCREEN_WIDTH/2 - 85,320,150,50,BC1,BC2,35,Game)
            Button("Quit",SCREEN_WIDTH/2 - 85,400,150,50,BC1,BC2,35,pygame.quit)
        

        elif LayerP == 2:
            screen.blit(S_bakckground,(0,0))
            TEXT("Settings",180,50,70)                                          #settings Heading
            TEXT("Music",SCREEN_WIDTH/2,175,50)                                 #Music Sub-Heading
            TEXT("Difficulty",SCREEN_WIDTH/2,450,50)                            #Difficulty Sub-Heading

            Button("ON",SCREEN_WIDTH/3,250,100,65,BC1,BC2,35,MENU_Music_ON)            #this Button toggles the music on 
            Button("OFF",SCREEN_WIDTH/1.75 + 20 ,250,100,65,BC1,BC2,35,MENU_Music_OFF) #this Button toggles the music off

            Button("Baby",SCREEN_WIDTH/6 ,525,220,65,BC1,BC2,35)         #this Button is used to toggle the easiest difficulty    
            Button("Boring",525,525,220,65,BC1,BC2,35)                   #this Button is used to toggle the medium difficulty 
            Button("Thrilling",842 ,525,220,65,BC1,BC2,35)               #this Button is used to toggle the hardest difficulty
           
            Button("Back",20,700,80,50,BC1,BC2,25,P_menu)







        pygame.display.flip()
        clock.tick(60)
# ------------------- this is the end of the pause menu code -------------------- # !!!!DONE!!!!

# ------------------- this will be the code that operates the beggining of the game ------------------- # !!!!DONE!!!!
layer = 1
Menu = True  
while Menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Menu = False
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_x:
                Menu = False
            elif event.key==pygame.K_ESCAPE:
                layer == 1
        
# code for the main menu will be located here # 
    screen.fill(WHITE)
   
    if layer == 1:
        #title
        screen.blit(T_background,(0,0))                           #Main menu background
        TEXT("Ctrl and Destroy",300,50,70)                        #Game title

        Button("Start", 20,200,210,80,BC1,BC2,35,Game_intro)      #this Button leads to the game intro, and then into the game
        Button("Controls",20,340,210,80,BC1,BC2,35,Controls)      #this Button leads to the Controls menu, which quickly teaches the player the controls
        Button("Settings",20,480,210,80,BC1,BC2,35,Settings)      #this Button leads to the Settings menu, which allows the player to either turn off the music or select a specific game difficulty 
        Button("Quit",20,620,210,80,BC1,BC2,35,Quit)              #this Button simply quits the game
        
    elif layer == 2:
        #Settings
        screen.blit(S_bakckground,(0,0))
        TEXT("Settings",180,50,70)                                          #settings Heading
        TEXT("Music",SCREEN_WIDTH/2,175,50)                                 #Music Sub-Heading
        TEXT("Difficulty",SCREEN_WIDTH/2,450,50)                            #Difficulty Sub-Heading

        Button("ON",SCREEN_WIDTH/3,250,100,65,BC1,BC2,35,MENU_Music_ON)            #this Button toggles the music on 
        Button("OFF",SCREEN_WIDTH/1.75 + 20 ,250,100,65,BC1,BC2,35,MENU_Music_OFF) #this Button toggles the music off

        Button("Baby",SCREEN_WIDTH/6 ,525,220,65,BC1,BC2,35,None)         #this Button is used to toggle the easiest difficulty    
        Button("Boring",525,525,220,65,BC1,BC2,35,None)                   #this Button is used to toggle the medium difficulty 
        Button("Thrilling",842 ,525,220,65,BC1,BC2,35,None)               #this Button is used to toggle the hardest difficulty
        
        Button("Back",20,700,80,50,BC1,BC2,25,M_Menu)                     #this Button will return the user to the main menu

    elif layer == 3:
        #Controls
        screen.blit(C_background,(0,0))                           #Controls Background
        TEXT("Game Controls",300,50,70)                           #Controls Heading
        
        #move controls
        Button("W",120,100,50,50,BC1,BC2,35,None,"Move UP")       #hovering over this button will tell the player how to move up
        Button("S",120,170,50,50,BC1,BC2,35,None,"Move DOWN")     #hovering over this button will tell the player how to move down
        Button("A",50,170,50,50,BC1,BC2,35,None,"Move LEFT")      #hovering over this button will tell the player how to move left
        Button("D",190,170,50,50,BC1,BC2,35,None,"Move RIGHT")    #hovering over this button will tell the player how to move Right

        #melee atk control
        Button("E",120,300,50,50,BC1,BC2,35,None,"Melee Atk")     #hovering over this button will tell the player how to Attack 

        #shoot controls
        #have to manualy create arrows using a sprite engine
        Button("",120,430,50,50,BC1,BC2,35,None,"Shoot UP")       #hovering over this button will tell the player how to shoot up  
        Button("",120,500,50,50,BC1,BC2,35,None,"Shoot DOWN")     #hovering over this button will tell the player how to shoot down
        Button("",50,500,50,50,BC1,BC2,35,None,"Shoot LEFT")      #hovering over this button will tell the player how to shoot left
        Button("",190,500,50,50,BC1,BC2,35,None,"Shoot RIGHT")    #hovering over this button will tell the player how to shoot right

        #pause menu bind
        Button("ESC",100,630,90,50,BC1,BC2,35,None,"Toggle Menu") #hovering over this button will tell the player how to toggle the main menu
        
        Button("Back",20,700,80,50,BC1,BC2,25,M_Menu,None)        #this Button will return the user to the main menu

    elif layer == 4:
        #game intro

               
        screen.blit(PG_Background ,(0,0))
        TEXT("Transcript #423-27b",SCREEN_WIDTH/2,50,70)
        TEXT("June 12, 18927",100,200,25,PG_TEXT)
        TEXT("Since the catastrophe caused by the Xepher plant in 18905, the planet has undergone transformations rendering it into a wasteland.", SCREEN_WIDTH/2,240,18,PG_TEXT)
        TEXT("The catastrophe caused a  massive increase in radiation levels on the surface. As well as deadly natural phenomenons.", SCREEN_WIDTH/2,280,18,PG_TEXT)
        TEXT("Trillions were killed in a matter of hours.", SCREEN_WIDTH/2,320,18,PG_TEXT)
        
        TEXT('Those who survived have migrated into the hollows of the earths crust and have taken to the name "Nesters"',SCREEN_WIDTH/2,380,18,PG_TEXT)
        TEXT("Due to extensive exposure to radiation most Nesters are far too frail to fight the monsters that lurk under the crust.",SCREEN_WIDTH/2,420,18,PG_TEXT)
        

        Button("Back",20,700,80,50,BC1,BC2,25,M_Menu)#temporary, for test and faster performence purposes
        Button("Continue",SCREEN_WIDTH/2 - 75,700,150,50,BC1,BC2,25,Game)
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game()

    
    pygame.display.flip()
    clock.tick(60)
# -------------------------------- this is the end of the main menu code -------------------------- # !!!!DONE!!!!
 
pygame.quit()




