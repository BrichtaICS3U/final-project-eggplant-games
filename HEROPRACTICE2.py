import pygame
pygame.init()
from hero import *                          #import the sprites that Abbey has made
from Door import DOOR, KEY
from LVLs import LVL                        #FML
import math
import random

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
Generate = True
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
    global Generate
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
    Generate = True

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
ammo_drops_list = pygame.sprite.Group()         #enemy ammo drops list
health_drops_list = pygame.sprite.Group()       #enemy health drops list
money_drops_list = pygame.sprite.Group()
store_stuff_list = pygame.sprite.Group()

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

#Initial sword
player_sword = Sword(1,1)
all_sprites_list.add(player_sword)

#list of lvls
lvls = []

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
    global Generate             #adds variable to generate levels
    Game = True                 #while the variable is true the game will run
    
    while Game:
        for event in pygame.event.get():        #
            if event.type == pygame.QUIT:       #if the red box at the top right is clicked
                pygame.quit()                   #quit the etire code
            elif event.type == pygame.KEYDOWN:  #
                if event.key==pygame.K_p:       #if the p key is pressed
                    Game = False
                    #exit the game and return to the main menu

        keys = pygame.key.get_pressed()
                    
#fill the screen white evertime the code runs
        screen.fill(WHITE)
    
########################################## IMPORTANT DO NOT TOUCH PLZ (@_@)
        ########################################## IMPORTANT DO NOT TOUCH PLZ <(^_^)<
# this commented blocked portion is the section where the lvls are drawn and the player interacts with the sorrounding

# Forest/outside dungeon ---- Tutorial #

        if Generate == True:

    #lvl store
            if Y == 0 and X == 1:
                lvl0 = LVL(1)
                lvls.append(lvl0)
                e_screen = 0
                store_ammo1 = StorePlate(GRAY, SCREEN_WIDTH/5, SCREEN_HEIGHT-100, 80, 40)
                store_ammo3 = StorePlate(GRAY, SCREEN_WIDTH/5*2, SCREEN_HEIGHT-100, 80, 40)            
                store_health = StorePlate(GRAY, SCREEN_WIDTH/5*3, SCREEN_HEIGHT-100, 80, 40)
                store_speed = StorePlate(GRAY, SCREEN_WIDTH/5*4, SCREEN_HEIGHT-100, 80, 40)

                store_stuff_list.add(store_ammo1)
                store_stuff_list.add(store_ammo3)
                store_stuff_list.add(store_health)
                store_stuff_list.add(store_speed)
                store_stuff_list.draw(screen)
                store_speed.drawExtra(screen)
                

    #lvl 1
            elif Y == 1 and X == 1:
                store_stuff_list.empty()
                lvl1 = LVL(8)
                lvls.append(lvl1)
                e_screen = 0
                        

    #lvl 2
            elif Y == 2 and X == 1:
                lvl3 = LVL(8)
                lvls.append(lvl3)
                lvl3.draw(screen)
                e_screen = 1
                

    #lvl 3
            elif Y == 3 and X == 1:
                lvl5 = LVL(100)
                lvls.append(lvl5)
                
                
    #lvl 5
            elif Y == 3 and X == 0:
                lvl4 = LVL(6)
                lvls.append(lvl4)
                e_screen = 1
               

    #lvl 6
            elif Y == 3 and X == -1:
                lvl6 = LVL(10)
                lvls.append(lvl6)
                e_screen = 1

    #lvl 7
            elif Y == 2 and X == -1:
                lvl7 = LVL(1)
                lvls.append(lvl7)
                e_screen = 1
                
    # Enterance/Sewers ----- lvl 1 #
    #lvl 8
            elif Y == 4 and X == 1:
                lvl8 = LVL(8)
                lvls.append(lvl8)
                e_screen = 0

    #lvl 9
            elif Y == 5 and X == 1:
                lvl9 = LVL(8)
                lvls.append(lvl9)
                e_screen = 0

    #lvl 10 //first floor / hub for floor (reference point)//
            elif Y == 6 and X == 1:
                lvl10 = LVL(100)
                lvls.append(lvl10)
                e_screen = 0

    #lvl 11
            elif Y == 6 and X == 2:
                lvl11 = LVL(6)
                lvls.append(lvl11)
                e_screen = 0

    #lvl 12 //Roundabout entrance//
            elif Y == 6 and X == 3:
                lvl12 = LVL(20)
                lvls.append(lvl12)
                e_screen = 0

    #lvl 13
            elif Y == 7 and X == 3:
                lvl13 = LVL(10)
                lvls.append(lvl13)
                e_screen = 0

    #lvl 14
            elif Y == 7 and X == 4:
                lvl14 = LVL(6)
                lvls.append(lvl14)
                e_screen = 0

    #lvl 15
            elif Y == 7 and X == 5:
                lvl15 = LVL(9)
                lvls.append(lvl15)
                e_screen = 0

    #lvl 16
            elif Y == 6 and X == 5:
                lvl16 = LVL(8)
                lvls.append(lvl16)
                e_screen = 0

    #lvl 17
            elif Y == 5 and X == 5:
                lvl17 = LVL(3)
                lvls.append(lvl17)
                e_screen = 0

    #lvl 18
            elif Y == 5 and X == 4:
                lvl18 = LVL(6)
                lvls.append(lvl18)
                e_screen = 0

    #lvl 19 //end of sewer roundabout//
            elif Y == 5 and X == 3:
                lvl19 = LVL(5)
                lvls.append(lvl19)
                e_screen = 0

        
    #lvl 21 // start of left part of sewers//
            elif Y == 6 and X == 0:
                lvl21 = LVL(6)
                lvls.append(lvl21)
                e_screen = 0

    #lvl 22
            elif Y == 6 and X == -1:
                lvl22 = LVL(30)
                lvls.append(lvl22)
                e_screen = 0

    #lvl 23
            elif Y == 5 and X == -1:
                lvl23 = LVL(1)
                lvls.append(lvl23)
                e_screen = 0

    #lvl 24
            elif Y == 6 and X == -2:
                lvl24 = LVL(40)
                lvls.append(lvl24)
                e_screen = 0            

    #lvl 25
            elif Y == 6 and X == -3:
                lvl25 = LVL(4)
                lvls.append(lvl25)
                e_screen = 0    

    #lvl 26
            elif Y == 7 and X == -2:
                lvl26 = LVL(8)
                lvls.append(lvl26)
                e_screen = 0

    #lvl 27
            elif Y == 8 and X == -2:
                lvl27 = LVL(9)
                lvls.append(lvl27)
                e_screen = 0

    #lvl 28
            elif Y == 8 and X == -3:
                lvl28 = LVL(4)
                lvls.append(lvl28)
                e_screen = 0

            Generate = False

        #hit detection for doors            
        for lvl in lvls:

            if Y == 0 and X == 1:
                lvl0.draw(screen)
                    
            elif Y == 1 and X == 1:#plz dunt dark marks cyuz i t luk bad ;-;
                lvl1.draw(screen)
            elif Y == 2 and X == 1:
                lvl2.draw(screen)
            elif Y == 3 and X == 1:
                lvl3.draw(screen)
            elif Y == 3 and X == 2:
                lvl4.draw(screen)
            elif Y == 3 and X == 0:
                lvl5.draw(screen)
            elif Y == 3 and X == -1:
                lvl6.draw(screen)
            elif Y == 2 and X == -1:
                lvl7.draw(screen)
            elif Y == 4 and X == 1:
                lvl8.draw(screen)
            elif Y == 5 and X == 1:
                lvl10.draw(screen)
            elif Y == 5 and X == 2:
                lvl11.draw(screen)
            elif Y == 5 and X == 3:
                lvl12.draw(screen)
            elif Y == 6 and X == 3:
                lvl13.draw(screen)
            elif Y == 6 and X == 4:
                lvl14.draw(screen)
            elif Y == 6 and X == 5:
                lvl15.draw(screen)
            elif Y == 5 and X == 5:
                lvl16.draw(screen)
            elif Y == 4 and X == 5:
                lvl17.draw(screen)
            elif Y == 4 and X == 4:
                lvl18.draw(screen)
            elif Y == 4 and X == 3:
                lvl19.draw(screen)
            elif Y == 5 and X == 0:
                lvl21.draw(screen)
            elif Y == 5 and X == -1:
                lvl22.draw(screen)
            elif Y == 4 and X == -1:
                lvl23.draw(screen)
            elif Y == 5 and X == -2:
                lvl24.draw(screen)
            elif Y == 5 and X == -3:
                lvl25.draw(screen)
            elif Y == 6 and X == -2:
                lvl26.draw(screen)
            elif Y == 7 and X == -2:
                lvl27.draw(screen)
            elif Y == 7 and X == -3:
                lvl28.draw(screen)
        
            
        for lvl in lvls:
            Door_collision_list = pygame.sprite.spritecollide(player,lvl.doors_list,False)
            for door in Door_collision_list:
                Change_SCREEN()
                
                for enemy in enemy_list:                        #this code deletes the previous enemies off the screen
                    enemy.HP = 0
                    all_sprites_list.remove(enemy)
                    enemy_list.remove(enemy)
                
                for en_drop in ammo_drops_list:
                    ammo_drops_list.remove(en_drop)
                    all_sprites_list.remove(en_drop)

                for en_drop in health_drops_list:
                    health_drops_list.remove(en_drop)
                    all_sprites_list.remove(en_drop)
                
                for i in range(e_screen):                       #this code adds new enemies to next screen
                    enemy = Enemy(BLACK, 40, 40)                #based off of the number of enemies that was
                    enemy_list.add(enemy)                       #set earlier
                    all_sprites_list.add(enemy)


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


#this little bit is for the hit detection between players and keys                    
            Key_collision_list = pygame.sprite.spritecollide(player,lvl.Key_list,False)
            for key in Key_collision_list:
                for Key in lvl.Key_list:
                    pygame.draw.rect(screen,F_C,[Key.rect.x,Key.rect.y,Key.width,Key.height])

                
#########################################################            

        keys = pygame.key.get_pressed()             #built in pygame function to detect is keys are pressed

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
        if keys[pygame.K_LSHIFT]:                   #if left shift is pressed
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
        if event.type==pygame.MOUSEBUTTONDOWN and shoot == True and player.ammo > 0:                            #if the mouse Button has been pressed and the player is allowed to shoot
                bullet = Bullet(BLACK,5,5,player.rect.x + (30/2),player.rect.y + (40/2))    #shoot a bullet from the center of the player sprite
                shoot = False                                                               #take away he ability to shoot so the game doesn't break
                b = True
                all_sprites_list.add(bullet)                                                #add the bullets to th universal list   
                Bullet_sprites_list.add(bullet)                                             #add the bullets to the respected list
                player.ammo -= 1                                                            #removes a 'bullet' from ammo count
                
                
        #this allows the player to shoot again when he/she releases the mouse button
        if event.type==pygame.MOUSEBUTTONUP:                                                #when the mouse button is releasd
            shoot = True                                                                    #the player can shoot again

                      
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
                    player.rect.y -= 50
        
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

        for store_item in store_stuff_list:
            store_col = pygame.sprite.collide_rect(player, store_item)
            if store_col == True:
                if store_item.colour == GRAY and player.money >= 2:
                    player.money -= 2
                    player.rect.y -= 200
                    player.ammo += 1
                else:
                    player.rect.y -= 200
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
                    en_drop = Drops(BROWN, 10, 10, enemy.rect.x, enemy.rect.y)
                    en_drop.rect.x += 50
                    all_sprites_list.add(en_drop)
                    money_drops_list.add(en_drop)
                    
                elif 60 < m_chance < 90:                    #30% chance of silver coin ($2)
                    en_drop = Drops(SILVER, 10, 10, enemy.rect.x, enemy.rect.y)
                    en_drop.rect.x += 50
                    all_sprites_list.add(en_drop)
                    money_drops_list.add(en_drop)
           
                elif m_chance >= 90:                        #10% chance of gold coin ($3)
                    en_drop = Drops(GOLD, 10, 10, enemy.rect.x, enemy.rect.y)
                    en_drop.rect.x += 50
                    all_sprites_list.add(en_drop)
                    money_drops_list.add(en_drop)
                    
                #ammo/health drop (happens 50% of time)
                chance = random.randint(0, 100)             #get a random number from 1-100
                if chance <= 50:                            #numbers 1-50 give a drop (50% chance)
                    chance2 = random.randint(0, 100)        #get another random numner
                    if chance2 <= 75:                       #75% chance the drop is for ammo
                        en_drop = Drops(GRAY, 20, 20, enemy.rect.x, enemy.rect.y)
                        all_sprites_list.add(en_drop)
                        ammo_drops_list.add(en_drop)
                    elif chance2 > 75:                      #25% chance the drop is for health
                        en_drop = Drops(RED, 20, 20, enemy.rect.x, enemy.rect.y)
                        all_sprites_list.add(en_drop)
                        health_drops_list.add(en_drop)
                    
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
