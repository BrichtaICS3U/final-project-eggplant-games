import pygame
pygame.init()
from hero import Hero, Enemy, Bullet    #import the sprites that Abbey has made
from Door import DOOR                   #import the sprites that Nick has made
from LVLs import LVL                    #FML

# define colours #
WHITE = (255,255,255)       #White
GRAY  = (121,121,121)       #Gray
BLACK = (0,0,0)             #Black
RED   = (255,0,0)           #test Red
GREEN = (0,255,0)           #test Green
BLUE  = (0,0,255)           #test Blue
BC1   = (66,3,61)           #Button colour 1
BC2   = (104,14,75)         #Button coloutr 2
I_TEXT = (255,164,0)        #insztructions text colour (subject to change)
M_TEXT = (130,2,99)         #menu text colour
PG_TEXT = (255,164,0)       #pregame text

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
#pygame.mixer.music.play(-1)                                                 #            
    
# ----------- end of music catagory ------------- #




# ----------- list of global variables ------------- #
shoot = True
b = False
Y = 1
X = 1
# ----------- end of variable list ---------------#




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
    
def Change_SCREEN():
    global Y
    global X
    if player.rect.y < 50:
        player.rect.y = SCREEN_HEIGHT - 46
        print("screen UP.")
        Y += 1
    elif player.rect.y > 750:
        player.rect.y = 6
        print("screen DOWN.")
        Y -= 1
    elif player.rect.x < 50:
        player.rect.x = SCREEN_WIDTH - 36
        print("screen LEFT.")
        X -= 1
    elif player.rect.x > 1150:
        player.rect.x = 6
        print("screen RIGHT.")
        X += 1
            
# --------------------- End of functions list ----------------------- #



# --------------------- this will be the main code for the game -------------------- #
"""
this is where the bulk of the game code will be located. the point of placing it 
in a function is so that we can easily call it when needed form the menu
"""

#sprite list
all_sprites_list = pygame.sprite.Group()        #this is the master sprite list. All of the sprites are located her unpon creation
Hero_sprite_list = pygame.sprite.Group()        #this is the Hero sprite list. Only the hero sprite will be located here
Bullet_sprites_list = pygame.sprite.Group()     #this is the bullet sprite list. all the Bullets taht are fired will be located here
enemy_list = pygame.sprite.Group()              #this is the enemy sprite list

#player character
player = Hero(30,40)
player.rect.x = SCREEN_WIDTH/2
player.rect.y = SCREEN_HEIGHT/2
playerHealth = player.HP

#Initial enemy character
enemy = Enemy(BLACK, 40, 40)        #adds a single enemy to first room
enemy_list.add(enemy)
all_sprites_list.add(enemy)

#Initial bullet
bullet = Bullet(BLACK, 5, 5, player.rect.x, player.rect.y)

#list of lvls
lvls = []
enemies_list = []

#lvl 1-1
lvl1 = LVL(3)
lvls.append(lvl1)

#lvl 1-2
lvl2 = LVL(9)
lvls.append(lvl2)

#lvl 2-1
lvl3 = LVL(5)
lvls.append(lvl3)

#lvl 2-2
lvl4 = LVL(10)
lvls.append(lvl4)


#add all of the sprites into their respected lists 
all_sprites_list.add(player)
Hero_sprite_list.add(player)


def Game():
    global Y
    global SCREEN_WIDTH         #turn the screen width into a global variable for the game
    global SCREEN_HEIGHT        #turn the screen height into a global variable for the game
    global shoot                #adds the shoot variable
    global b                    #adds bullet collision variable
    Game = True                 #while the variable is true the game will run
    
    while Game:
        for event in pygame.event.get():        #
            if event.type == pygame.QUIT:       #if the red box at the top right is clicked
                pygame.quit()                   #quit the etire code
            elif event.type == pygame.KEYDOWN:  #
                if event.key==pygame.K_p:       #if the p key is pressed
                    Game = False
                    #exit the game and return to the main menu
                    
#fill the screen white evertime the code runs
        screen.fill(WHITE)
    
########################################## IMPORTANT DO NOT TOUCH PLZ (@_@)
        if Y == 1 and X == 1:
            lvl1.draw(screen)
            pygame.draw.rect(screen,RED,[50,50,50,50])
            e_screen = 2        #variable to control the number of enemies on screen
                                #2 enemies in red room
            
        if Y == 2 and X == 1:
            lvl2.draw(screen)
            pygame.draw.rect(screen,GREEN,[50,50,50,50])
            e_screen = 3        #3 enemies in green room


        if Y == 1 and X == 2:
            lvl3.draw(screen)
            pygame.draw.rect(screen,BLUE,[50,50,50,50])
            e_screen = 2        #2 enemies in blue room
            
        

        if Y == 2 and X == 2:
            lvl4.draw(screen)
            pygame.draw.rect(screen,BLACK,[50,50,50,50])
            e_screen = 1        #1 enemy in black room
        
            
        for lvl in lvls:
            Door_collision_list = pygame.sprite.spritecollide(player,lvl.doors_list,False)
            for door in Door_collision_list:
                Change_SCREEN()
                
                for enemy in enemy_list:                #this code deletes the previous enemies off the screen
                    enemy.HP = 0
                    all_sprites_list.remove(enemy)
                    enemy_list.remove(enemy)
                    pygame.draw.rect(screen, WHITE, [enemy.rect.x+5, enemy.rect.y-10, 10, 5], 0)

                for i in range(e_screen):                      #this code adds new enemies to next screen
                    enemy = Enemy(BLACK, 40, 40)                #based off of the number of enemies that was
                    enemy_list.add(enemy)                       #set earlier
                    all_sprites_list.add(enemy)
                
#########################################################            

        keys = pygame.key.get_pressed()         #built in pygame function to detect is keys are pressed

        #player movement
        if keys[pygame.K_a]:                    #if the A key is pressed
            player.move()                           #the player will move to the Left at a speed of 2 pixels
        elif keys[pygame.K_s]:                  #if the S key is pressed
            player.move()                           #the player will move Down at a speed of 2 pixels
        elif keys[pygame.K_d]:                  #if the D key is pressed
            player.move()                           #the player will move to the Right at a speed of 2 pixels
        elif keys[pygame.K_w]:                  #if the W key is pressed
            player.move()                           #the player will move Up at a speed of 2 pixels

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

        #Enemy follow player (while living)
        for enemy in enemy_list:
            if enemy.HP > 0:
                enemy.move_to_player(player)
                        
        #player shooting
        if event.type==pygame.MOUSEBUTTONDOWN and shoot == True:                            #if the mouse Button has been pressed and the player is allowed to shoot
                bullet = Bullet(BLACK,5,5,player.rect.x + (30/2),player.rect.y + (40/2))    #shoot a bullet from the center of the player sprite
                shoot = False                                                               #take away he ability to shoot so the game doesn't break
                b = True
                all_sprites_list.add(bullet)                                                #add the bullets to th universal list   
                Bullet_sprites_list.add(bullet)                                             #add the bullets to the respected list
                
        #this allows the player to shoot again when he/she releases the mouse button
        if event.type==pygame.MOUSEBUTTONUP:                                                #when the mouse button is releasd
            shoot = True                                                                    #the player can shoot again
                      
        #update sprite list(s)
        all_sprites_list.update()
        Bullet_sprites_list.update()
        enemy_list.update()

#---------------- collisions--------------------------------------------------------------------------------------
        collision_list = pygame.sprite.spritecollide(player, enemy_list, False)     #collisions between enemy and player
        
        if b == True:                                   #global variable indicating that a bullet is present   
            for enemy in enemy_list:
                bullet_col = pygame.sprite.collide_rect(bullet, enemy)  #collisions between bullets and enemies
                if bullet_col == True:
                    enemy.HP -= 20                      #decrease enemy health by 20   
                    bullet.rect.x = 0                   #teleport bullet to top left of screen, because if not the bullet stays 'colliding'
                    bullet.rect.y = 0                   #with the enemy and it becomes a one shot kill (not what we want!)
                    Bullet_sprites_list.remove(bullet)  #remove bullet from lists 
                    all_sprites_list.remove(bullet)

            
        """insert code for collisions between enemies here"""
        
# -------------------end of collisions --------------------------------------------------------------------------------                   
    

        #Drawing Health Bars
        pygame.draw.rect(screen, GREEN, [20, 30, 15, 25], 0) #player health bars
        pygame.draw.rect(screen, GREEN, [40, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [60, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [80, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [100, 30, 15, 25], 0)
        TEXT("Player Health", 60, 20, 15)
        
        for enemy in enemy_list:
            pygame.draw.rect(screen, RED, [enemy.rect.x+5, enemy.rect.y-10, 30, 5], 0)  #Enemy health bar

        #Updating health bars
        for collision in collision_list:
            player.HP -= 20
            print(player.HP)
            player.rect.x -= 100            #Player bounces back on enemy collision
            player.rect.y -= 50

    

        # This draws white (alternatively other background colour) over
        # original health bars to simulate the bars disappearing
            #Player health bars
        if player.HP <= 80:
            pygame.draw.rect(screen, WHITE, [100, 30, 15, 25], 0)
            if player.HP <= 60:
                pygame.draw.rect(screen, WHITE, [80, 30, 15, 25], 0)
                if player.HP <= 40:
                    pygame.draw.rect(screen, WHITE, [60, 30, 15, 25], 0)
                if player.HP <= 20:
                    pygame.draw.rect(screen, WHITE, [40, 30, 15, 25], 0)
                if player.HP == 0:
                    pygame.draw.rect(screen, WHITE, [20, 30, 15, 25], 0)
                    player.die()
                    carryOn = False
                    pygame.quit()
                    
                #Enemy health bar
        for enemy in enemy_list:
            if enemy.HP <= 80:
                pygame.draw.rect(screen, WHITE, [enemy.rect.x+29, enemy.rect.y-10, 6, 5], 0)
                if enemy.HP <= 60:
                    pygame.draw.rect(screen, WHITE, [enemy.rect.x+23, enemy.rect.y-10, 6, 5], 0)
                    if enemy.HP <= 40:
                        pygame.draw.rect(screen, WHITE, [enemy.rect.x+17, enemy.rect.y-10, 6, 5], 0)
                        if enemy.HP <= 20:
                            pygame.draw.rect(screen, WHITE, [enemy.rect.x+11, enemy.rect.y-10, 6, 5], 0)
                            if enemy.HP <= 0:
                                pygame.draw.rect(screen, WHITE, [enemy.rect.x+5, enemy.rect.y-10, 10, 5], 0)
                                all_sprites_list.remove(enemy)
                                enemy_list.remove(enemy)


        
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


        #Draw all sprites
        all_sprites_list.draw(screen)
        
        
        pygame.display.flip()
        clock.tick(60)
# ------------------- end of main Game code ------------------ #

Game()    
pygame.quit()
