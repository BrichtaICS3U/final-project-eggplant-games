import pygame, random

#Import classes
from hero import Hero, Enemy, Bullet
from Door import DOOR
from LVLs import LVL

pygame.init()

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (81, 222, 232)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
M_TEXT = (164,44,214)
        
SCREEN_WIDTH=1250
SCREEN_HEIGHT=800

Y = 1
X = 1

def TEXT(TXT,x,y,TF):
    """this function exists to create headings for each menu screens"""

    fontTitle = pygame.font.Font('freesansbold.ttf', TF)
    textSurfaceTitle = fontTitle.render(TXT, True,M_TEXT)
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (x,y)
    screen.blit(textSurfaceTitle,textRectTitle)

def NEXT_SCREEN_UP():
    """this function will transfer the player to a new screen UP and reset their position in the correct area"""
    player.rect.y = SCREEN_HEIGHT - 46

def NEXT_SCREEN_RIGHT():
    """this function will transfer the player to a new screen RIGHT and reset their position in the correct area"""
    player.rect.x = 6

def NEXT_SCREEN_LEFT():
    """this function will transfer the player to a new screen LEFT and reset their position in the correct area"""
    player.rect.x = SCREEN_WIDTH - 36

def NEXT_SCREEN_DOWN():
    """this function will transfer the player to a new screen UP and reset their position in the correct area"""
    player.rect.y = 6

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
 
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Irrelevant")
shoot = True

#List containing all sprites 
all_sprites_list = pygame.sprite.Group()

#Other sprite lists
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
door_sprites_list = pygame.sprite.Group()

#Create Hero, enemy, bullet
player = Hero(30, 50)
player.rect.x = 200
player.rect.y = 300
playerHealth = player.HP

enemy = Enemy(BLACK, 40, 40)
enemy_list.add(enemy)

bullet = Bullet(BLACK, 5, 5, player.rect.x, player.rect.y)

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


#this is where all the "door" objects are created
#top door
top_door = DOOR(100,5)                 
top_door.rect.x = SCREEN_WIDTH/2 - 50
top_door.rect.y = 0

#bottom door
bot_door = DOOR(100,5)
bot_door.rect.x = SCREEN_WIDTH/2 - 50
bot_door.rect.y = SCREEN_HEIGHT - 5

#right door
rt_door = DOOR(5,100)
rt_door.rect.x = SCREEN_WIDTH - 5
rt_door.rect.y = SCREEN_HEIGHT/2 - 50

#left door
lt_door = DOOR(5,100)
lt_door.rect.x = 0
lt_door.rect.y = SCREEN_HEIGHT/2 - 50

# Add sprites to list of sprites
all_sprites_list.add(player)
all_sprites_list.add(enemy)
door_sprites_list.add(bot_door)
door_sprites_list.add(top_door)
door_sprites_list.add(rt_door)
door_sprites_list.add(lt_door)



#Set shoot = False for later
shoot = False

#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
 
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False

        if Y == 1 and X == 1:
            lvl1.draw(screen)
            pygame.draw.rect(screen,RED,[50,50,50,50])
            
        if Y == 2 and X == 1:
            lvl2.draw(screen)
            pygame.draw.rect(screen,GREEN,[50,50,50,50])

        if Y == 1 and X == 2:
            lvl3.draw(screen)
            pygame.draw.rect(screen,BLUE,[50,50,50,50])

        if Y == 2 and X == 2:
            lvl4.draw(screen)
            pygame.draw.rect(screen,BLACK,[50,50,50,50])
            
        for lvl in lvls:
            Door_collision_list = pygame.sprite.spritecollide(player,lvl.doors_list,False)       
            for door in Door_collision_list:
                Change_SCREEN()
         
        keys = pygame.key.get_pressed()

        #Player Move
        if keys[pygame.K_a]:
            player.move()
        if keys[pygame.K_d]:
            player.move()
        if keys[pygame.K_w]:
            player.move()
        if keys[pygame.K_s]:
           player.move()

        #Player Sprint
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_a]:
                player.sprint()
            elif keys[pygame.K_d]:
                player.sprint()
            elif keys[pygame.K_w]:
                player.sprint()
            elif keys[pygame.K_s]:
                player.sprint()
                    
        #Enemy follow player (while living)
        if enemy.HP > 0:
            enemy.move_to_player(player)
                
        #Player shooting
        if event.type==pygame.MOUSEBUTTONDOWN and shoot == True:
                bullet = Bullet(BLACK,5,5,player.rect.x ,player.rect.y)
                shoot = False
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                
        #this allows the player to shoot again when he/she releases the mouse button        
        if event.type==pygame.MOUSEBUTTONUP:
            shoot = True
                        
        #Game Logic
        all_sprites_list.update()
        collision_list = pygame.sprite.spritecollide(player, enemy_list, False)
        bullet_collision = pygame.sprite.spritecollide(bullet, enemy_list, False)
        
        #Drawing on Screen
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [20, 30, 15, 25], 0) #Draw player health bars
        pygame.draw.rect(screen, GREEN, [40, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [60, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [80, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [100, 30, 15, 25], 0)
        TEXT("Player Health", 60, 20, 15)
        pygame.draw.rect(screen, RED, [enemy.rect.x+5, enemy.rect.y-10, 30, 5], 0)  #Enemy health bar

        #Updating health bars
        for collision in collision_list:
            player.HP -= 20
            print(player.HP)
            player.rect.x -= 100  ###### Adjust later
            player.rect.y -= 50

        for collision in bullet_collision:
            enemy.HP -= 5
            print(enemy.HP)

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
                #Enemy health bar
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

        #collision with the door(s)
        if player.rect.y < top_door.rect.y + 5 and player.rect.x > top_door.rect.x and player.rect.x + 30 < top_door.rect.x + 100: #top door
            NEXT_SCREEN_UP()

        if player.rect.y + 40 > bot_door.rect.y and player.rect.x > bot_door.rect.x and player.rect.x + 30 < top_door.rect.x + 100: #bottom door
            NEXT_SCREEN_DOWN()

        if player.rect.x + 30 > rt_door.rect.x and player.rect.y > rt_door.rect.y and player.rect.y + 40 < rt_door.rect.y + 100:#right door 
            NEXT_SCREEN_RIGHT()

        if player.rect.x < lt_door.rect.x and player.rect.y > rt_door.rect.y and player.rect.y + 40 < rt_door.rect.y + 100:#left door
            NEXT_SCREEN_LEFT()
        
        #Draw all the sprites
        all_sprites_list.draw(screen)
        door_sprites_list.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
