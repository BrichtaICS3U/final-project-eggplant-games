import pygame
pygame.init()

# define colours #
WHITE = (255,255,255)
GRAY  = (121,121,121)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
M_TEXT = (164,44,214)

#background(s)
background = pygame.image.load("Menu_Background.png")

# screen dimensions and game clock #
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 800
size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


# ---------- this will be catagory of functions to be used in the summative ----------- #

def Button(msg,x,y,w,h,col1,col2,FS,action = None,CT = None):
    """
        this is a short function that acts as a button class (will likley be changed into a module)
        msg    --- the text that will appear on the button
        x      --- the x coordinate for the button
        y      --- the y coordinate for the button
        w      --- the width od the button
        h      --- the height of the button
        col1   --- the first colour of the button
        col2   --- the second colour of the button
        FS     --- the font size of the buttons text
        action --- the function that the button activates
        CT     --- the controls text (only for layer 3/controls screen)
    """
    
    global layer
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] <x+w and y < mouse[1] < y+h and click[0] == 1:
        pygame.draw.rect(screen,BLACK,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    elif x < mouse[0] < x+w and y < mouse[1] < y+h and layer != 3:
        pygame.draw.rect(screen,col2,(x,y,w,h))
    elif x < mouse[0] < x+w and y < mouse[1] < y+h and layer == 3:
        pygame.draw.rect(screen,col2,(x,y,w,h))
        
        CFont = pygame.font.Font("freesansbold.ttf",FS)
        CText = CFont.render(CT,True,WHITE)
        CTextrect = CText.get_rect()
        CTextrect.center = (1000, y + (h/2))
        screen.blit(CText,CTextrect)
        
    else:
        pygame.draw.rect(screen,col1,(x,y,w,h))

    Bfont = pygame.font.Font("freesansbold.ttf",FS)
    Btext = Bfont.render(msg,True,BLACK)
    Btextrect = Btext.get_rect()
    Btextrect.center = (x + (w/2), y + (h/2))
    screen.blit(Btext,Btextrect)
    
def TEXT(TXT,x,y,TF):
    """this function exists to create headings for each menu screens"""

    fontTitle = pygame.font.Font('freesansbold.ttf', TF)
    textSurfaceTitle = fontTitle.render(TXT, True,M_TEXT)
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (x,y)
    screen.blit(textSurfaceTitle,textRectTitle)
    
def Menu():
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
    
def Quit():
    global Game
    Game = False
    
# --------------------- End of functions list ----------------------- #    



# this will be the main code for the game #
layer = 1
Game = True
while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_x:
                Game = False
            elif event.key==pygame.K_ESCAPE:
                layer == 1
# code for the main menu will be located here # 
    screen.fill(WHITE)
    screen.blit(background,(0,0))

    if layer == 1:
        #title 
        TEXT("Ctrl and Destroy",300,50,70)

        Button("Start", 20,200,210,80,RED,GREEN,35,Game_intro)
        Button("Controls",20,340,210,80,RED,GREEN,35,Controls)
        Button("Settings",20,480,210,80,RED,GREEN,35,Settings)
        Button("Quit",20,620,210,80,RED,GREEN,35,Quit)
        
    elif layer == 2:
        #Settings
        TEXT("Settings",180,50,70)
        TEXT("Music",SCREEN_WIDTH/2,175,50)
        TEXT("Difficulty",SCREEN_WIDTH/2,450,50)

        Button("ON",SCREEN_WIDTH/3,250,100,65,RED,GREEN,35,None)
        Button("OFF",SCREEN_WIDTH/1.75 + 20 ,250,100,65,RED,GREEN,35,None)

        Button("Baby",SCREEN_WIDTH/6 ,525,220,65,RED,GREEN,35,None)
        Button("Boring",525,525,220,65,RED,GREEN,35,None)
        Button("Thrilling",842 ,525,220,65,RED,GREEN,35,None)
        
        Button("Back",20,700,80,50,RED,GREEN,25,Menu)

    elif layer == 3:
        #Controls
        TEXT("Game Controls",300,50,70)
        
        #move controls
        Button("W",120,100,50,50,RED,GREEN,35,None,"Move UP")
        Button("S",120,170,50,50,RED,GREEN,35,None,"Move DOWN")
        Button("A",50,170,50,50,RED,GREEN,35,None,"Move RIGHT")
        Button("D",190,170,50,50,RED,GREEN,35,None,"Move LEFT")

        #melee atk control
        Button("E",120,300,50,50,RED,GREEN,35,None,"Melee Atk")

        #shoot controls
        Button("",120,430,50,50,RED,GREEN,35,None,"Shoot UP")
        Button("",120,500,50,50,RED,GREEN,35,None,"Shoot DOWN")
        Button("",50,500,50,50,RED,GREEN,35,None,"Shoot LEFT")
        Button("",190,500,50,50,RED,GREEN,35,None,"Shoot RIGHT")

        #pause menu bind
        Button("ESC",100,630,90,50,RED,GREEN,35,None,"Toggle Menu")
        
        Button("Back",20,700,80,50,RED,GREEN,25,Menu,None)

    elif layer == 4:
        #game intro
        TEXT("sample_txt.mp4",SCREEN_WIDTH/2,50,70)

        Button("Back",20,700,80,50,RED,GREEN,25,Menu)#temporary, for test purposes 
            


    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()

