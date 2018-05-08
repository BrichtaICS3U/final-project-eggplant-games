import pygame
pygame.init()
from hero import Hero, Enemy, Bullet


# define colours #
WHITE = (255,255,255)       #White
GRAY  = (121,121,121)       #Gray
BLACK = (0,0,0)             #Black
RED   = (255,0,0)           #test Red
GREEN = (0,255,0)           #test Green
BLUE  = (0,0,255)           #test Blue
BC1   = (66,3,61)           #Button colour 1
BC2   = (104,14,75)         #Button coloutr 2
I_TEXT = (255,164,0)        #instructions text colour (subject to change)
M_TEXT = (130,2,99)         #menu text colour
PG_TEXT = (255,164,0)       #pregame text

#background(s)
T_background = pygame.image.load("Menu_Background.png") #this is the background for the title screen
C_background = pygame.image.load("Controls_back.jpg")   #this is the background for the controls screen
S_bakckground = pygame.image.load("S_B.jpg")            #this is the background for the settings screen
PG_Background = pygame.image.load("Settings_B.jpg")     #this is the background for the pre game screen

# screen dimensions and game clock #
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 800
size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


# ----------- Music ----------- #
Music = True

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load("Menu_Music.mp3")
pygame.mixer.music.play(-1)
    
# ----------- end of music catagory ------------- #



# ---------- this will be catagory of functions to be used in the summative ----------- #

def Button(msg,x,y,w,h,col1,col2,FS,action = None,CT = None):
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
        pygame.draw.rect(screen,col2,(x,y,w,h))                     #redraw the Button but in a diffirent colour 
    elif x < mouse[0] < x+w and y < mouse[1] < y+h and layer == 3:  #this if statement is for only the Buttons located in the "Controls" section of the menu
        pygame.draw.rect(screen,col2,(x,y,w,h))                     #it redraws the button in its second colour. 
        
        CFont = pygame.font.Font("freesansbold.ttf",FS)     #as well as displays a definition of what that Button does in the game
        CText = CFont.render(CT,True,I_TEXT)                #
        CTextrect = CText.get_rect()                        #
        CTextrect.center = (1000, y + (h/2))                #
        screen.blit(CText,CTextrect)                        #
        
    else:                                                           #if nothing is interacting with the Button 
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
    
# --------------------- End of functions list ----------------------- #

# --------------------- this will be the main code for the game -------------------- #
"""this is where the bulk of the game code will be located. the point of placing it 
in a function is so that we can easily call it when needed"""

#sprite list
all_sprites_list = pygame.sprite.Group()
Hero_Sprite_list = pygame.sprite.Group()
Bullet_sprites_list = pygame.sprite.Group()

#player character
player = Hero(30,40)
player.rect.x = SCREEN_WIDTH/2
player.rect.y = SCREEN_HEIGHT/2
playerHealth = player.HP

#add the player to the universal list
all_sprites_list.add(player)

def Game():
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    Game = True
    lvl = GRAY
    shoot = True

    
    while Game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    Game = False

        screen.fill(lvl)

        keys = pygame.key.get_pressed()

        #player movement
        if keys[pygame.K_a]:
            player.move()
        elif keys[pygame.K_s]:
            player.move()
        elif keys[pygame.K_d]:
            player.move()
        elif keys[pygame.K_w]:
            player.move()

        #player sprinting
        if keys[pygame.K_LSHIFT]:
                if keys[pygame.K_a]:
                    player.move()
                elif keys[pygame.K_s]:
                    player.move()
                elif keys[pygame.K_d]:
                    player.move()
                elif keys[pygame.K_w]:
                    player.move()
                    
        #player shooting
        if event.type==pygame.MOUSEBUTTONDOWN and shoot == True:
                bullet = Bullet(BLACK,5,5,player.rect.x + (30/2),player.rect.y + (40/2))
                shoot = False
                all_sprites_list.add(bullet)
                Bullet_sprites_list.add(bullet)
                
        #this allows the player to shoot again when he/she relases the mouse button        
        if event.type==pygame.MOUSEBUTTONUP:
            shoot = True

        #update sprite list(s)
        all_sprites_list.update()
        Bullet_sprites_list.update()

        
        #wall restrictions
        #Right wall
        if player.rect.x + 30 > SCREEN_WIDTH:
            player.rect.x -= 2
            if keys[pygame.K_LSHIFT]:
                player.rect.x -= 2
        #Left wall
        elif player.rect.x < 0:
            player.rect.x += 2
            if keys[pygame.K_LSHIFT]:
                player.rect.x += 2
        #top wall
        elif player.rect.y < 0:
            player.rect.y += 2
            if keys[pygame.K_LSHIFT]:
                player.rect.y += 2
        #Bottom wall
        elif player.rect.y + 40 > SCREEN_HEIGHT:
            player.rect.y -= 2
            if keys[pygame.K_LSHIFT]:
                player.rect.y -= 2


        
        


        all_sprites_list.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
# ------------------- end of main Game code ------------------ #

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
        Button("Continue",SCREEN_WIDTH/2 - 75,650,150,75,BC1,BC2,25,Game)
            


    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()

